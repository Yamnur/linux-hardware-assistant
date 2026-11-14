
import os
import time

from google import genai
from google.genai import types
from google.genai import errors
from dotenv import load_dotenv

from agent.tools_schema import TOOLS
from security.executor import execute_tool

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-3.5-flash-lite"

ALL_TOOLS = [
    "get_cpu_info",
    "get_memory_info",
    "get_storage_info",
    "get_gpu_info"
]


def get_required_tools(question):

    q = question.lower()
    required = []

    if any(word in q for word in [
        "summary",
        "all hardware",
        "system specifications",
        "complete hardware"
    ]):
        return ALL_TOOLS.copy()

    if any(word in q for word in [
        "cpu", "processor", "core", "thread"
    ]):
        required.append("get_cpu_info")

    if any(word in q for word in [
        "ram", "memory"
    ]):
        required.append("get_memory_info")

    if any(word in q for word in [
        "storage", "disk", "drive"
    ]):
        required.append("get_storage_info")

    if any(word in q for word in [
        "gpu", "graphics", "nvidia", "display"
    ]):
        required.append("get_gpu_info")

    return required if required else ALL_TOOLS.copy()


def generate_with_retry(history, config=None):

    for attempt in range(3):

        try:
            return client.models.generate_content(
                model=MODEL,
                contents=history,
                config=config
            )

        except errors.ServerError:

            if attempt == 2:
                raise

            time.sleep(2 ** (attempt + 1))


def ask_hardware_assistant(question):

    history = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=question)
            ]
        )
    ]

    remaining_tools = get_required_tools(question)

    system_instruction = """
    You are a Linux Hardware Assistant.

    Rules:
    1. Use the supplied hardware function results.
    2. Never invent hardware specifications.
    3. Report only facts supported by tool results.
    4. Clearly mention when information is unavailable.
    5. Distinguish WSL virtual hardware from physical hardware.
    6. Do not assume a GPU is absent just because it cannot be detected.
    7. Never invent CPU boost frequency.
    8. Never assume a disk is the primary disk.
    9. Convert bytes into GiB using 1024 ** 3.
    10. Explain results clearly.
    11. Do not give generic troubleshooting instead of
        reporting the requested hardware tool results.
    """

    # Execute all required hardware tools
    while remaining_tools:

        config = types.GenerateContentConfig(
            tools=TOOLS,
            tool_config=types.ToolConfig(
                function_calling_config=types.FunctionCallingConfig(
                    mode="ANY",
                    allowed_function_names=remaining_tools
                )
            ),
            system_instruction=system_instruction
        )

        response = generate_with_retry(history, config)

        if not response.candidates:
            return "Gemini did not return a response."

        model_content = response.candidates[0].content

        history.append(model_content)

        function_responses = []

        for part in model_content.parts:

            if part.function_call:

                tool_name = part.function_call.name

                if tool_name not in remaining_tools:
                    continue

                print(f"\nExecuting tool: {tool_name}")

                result = execute_tool(tool_name)

                print("Tool result:", result)

                function_responses.append(
                    types.Part.from_function_response(
                        name=tool_name,
                        response={
                            "result": result
                        }
                    )
                )

                remaining_tools.remove(tool_name)

        if not function_responses:
            return "Gemini did not request the required hardware tools."

        history.append(
            types.Content(
                role="user",
                parts=function_responses
            )
        )

    # Generate final answer after all tools finish
    final_config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0
    )

    final_response = generate_with_retry(
        history,
        final_config
    )

    return (
        final_response.text
        or "Unable to generate hardware summary."
    )

