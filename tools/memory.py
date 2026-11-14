
import subprocess
import shutil


def get_memory_info():

    if not shutil.which("free"):
        return {"error": "free command not available"}

    try:
        result = subprocess.run(
            ["free", "-b"],
            capture_output=True,
            text=True,
            timeout=5,
            check=True
        )

        lines = result.stdout.splitlines()

        for line in lines:
            if line.startswith("Mem:"):
                values = line.split()

                return {
                    "total_bytes": int(values[1]),
                    "used_bytes": int(values[2]),
                    "free_bytes": int(values[3]),
                    "available_bytes": int(values[6])
                }

        return {"error": "Memory information unavailable"}

    except subprocess.TimeoutExpired:
        return {"error": "Memory inspection timed out"}

    except (subprocess.CalledProcessError, ValueError, IndexError):
        return {"error": "Memory inspection failed"}


if __name__ == "__main__":
    print(get_memory_info())

