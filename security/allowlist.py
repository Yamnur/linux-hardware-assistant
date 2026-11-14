
from tools.cpu import get_cpu_info
from tools.memory import get_memory_info
from tools.storage import get_storage_info
from tools.gpu import get_gpu_info


ALLOWED_TOOLS = {
    "get_cpu_info": get_cpu_info,
    "get_memory_info": get_memory_info,
    "get_storage_info": get_storage_info,
    "get_gpu_info": get_gpu_info
}

