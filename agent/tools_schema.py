
from google.genai import types

TOOLS = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name="get_cpu_info",
                description="MANDATORY for CPU questions. Returns actual CPU model, architecture, cores, threads, clock and cache information."
            ),
            types.FunctionDeclaration(
                name="get_memory_info",
                description="MANDATORY for RAM or memory questions. Returns actual total, used, free and available memory in bytes."
            ),
            types.FunctionDeclaration(
                name="get_storage_info",
                description="MANDATORY for disk or storage questions. Returns actual block devices, sizes, types and mount points."
            ),
            types.FunctionDeclaration(
                name="get_gpu_info",
                description="MANDATORY for GPU or graphics questions. Returns detected GPU devices, NVIDIA availability and WSL GPU interface status. Report its result even when no GPU device is identified."
            )
        ]
    )
]

