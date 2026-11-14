
from security.allowlist import ALLOWED_TOOLS


def execute_tool(tool_name):

    if tool_name not in ALLOWED_TOOLS:
        return {
            "success": False,
            "error": "Unauthorized tool execution"
        }

    try:
        tool_function = ALLOWED_TOOLS[tool_name]

        result = tool_function()

        if isinstance(result, dict) and "error" in result:
            return {
                "success": False,
                "error": result["error"]
            }

        return {
            "success": True,
            "data": result
        }

    except Exception:
        return {
            "success": False,
            "error": "Tool execution failed"
        }

