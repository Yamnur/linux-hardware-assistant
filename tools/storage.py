
import subprocess
import shutil
import json


def get_storage_info():

    if not shutil.which("lsblk"):
        return {"error": "lsblk command not available"}

    try:
        result = subprocess.run(
            ["lsblk", "-J", "-b", "-o",
             "NAME,SIZE,TYPE,MODEL,TRAN,FSTYPE,MOUNTPOINT"],
            capture_output=True,
            text=True,
            timeout=5,
            check=True
        )

        return json.loads(result.stdout)

    except subprocess.TimeoutExpired:
        return {"error": "Storage inspection timed out"}

    except (subprocess.CalledProcessError, json.JSONDecodeError):
        return {"error": "Storage inspection failed"}


if __name__ == "__main__":
    print(json.dumps(get_storage_info(), indent=4))

