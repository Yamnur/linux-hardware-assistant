
import subprocess
import shutil


def get_cpu_info():

    if not shutil.which("lscpu"):
        return {"error": "lscpu command not available"}

    try:
        result = subprocess.run(
            ["lscpu"],
            capture_output=True,
            text=True,
            timeout=5,
            check=True
        )

        cpu_data = {}

        for line in result.stdout.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                cpu_data[key.strip()] = value.strip()

        return cpu_data

    except subprocess.TimeoutExpired:
        return {"error": "CPU inspection timed out"}

    except subprocess.CalledProcessError:
        return {"error": "CPU inspection failed"}


if __name__ == "__main__":
    print(get_cpu_info())

