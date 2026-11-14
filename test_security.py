
from security.executor import execute_tool

print("CPU TEST:")
print(execute_tool("get_cpu_info"))

print("\nRAM TEST:")
print(execute_tool("get_memory_info"))

print("\nUNAUTHORIZED TEST:")
print(execute_tool("rm -rf /"))


