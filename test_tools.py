from security.executor import execute_tool

tools = [
    "get_cpu_info",
    "get_memory_info",
    "get_storage_info",
    "get_gpu_info"
]

for tool in tools:
    print("\nTesting:", tool)

    result = execute_tool(tool)

    print(result)
