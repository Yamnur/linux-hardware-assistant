
import subprocess
import shutil
import os


def get_gpu_info():

    gpu_data = {
        "gpu_devices": [],
        "nvidia_available": False,
        "wsl_gpu_interface": os.path.exists("/dev/dxg"),
        "status": "unknown"
    }

    if shutil.which("lspci"):
        try:
            result = subprocess.run(
                ["lspci"],
                capture_output=True,
                text=True,
                timeout=5,
                check=True
            )

            for line in result.stdout.splitlines():
                if any(name in line.lower() for name in
                       ["vga", "3d controller", "display controller"]):
                    gpu_data["gpu_devices"].append(line)

        except (subprocess.TimeoutExpired,
                subprocess.CalledProcessError):
            pass

    if shutil.which("nvidia-smi"):
        try:
            result = subprocess.run(
                ["nvidia-smi", "-L"],
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode == 0:
                gpu_data["nvidia_available"] = True
                gpu_data["nvidia_devices"] = result.stdout.strip()

        except subprocess.TimeoutExpired:
            pass

    if gpu_data["gpu_devices"] or gpu_data["nvidia_available"]:
        gpu_data["status"] = "detected"
    elif gpu_data["wsl_gpu_interface"]:
        gpu_data["status"] = "gpu_interface_available_details_unavailable"
    else:
        gpu_data["status"] = "not_detected"

    return gpu_data


if __name__ == "__main__":
    print(get_gpu_info())

