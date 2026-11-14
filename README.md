# Linux Hardware Q&A Assistant
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Yamnur/linux-hardware-assistant?quickstart=1)
A local, natural-language Linux hardware assistant that uses **Google Gemini, Python and secure tool calling** to inspect system hardware and answer questions with real system data.

## Overview

The Linux Hardware Q&A Assistant allows users to ask questions about their computer's hardware using natural language.

Instead of allowing an LLM to guess hardware specifications, the application executes predefined Python tools to collect actual system information and uses Gemini to explain the results.

The application currently supports a command-line interface (CLI).

## Features

- **CPU Information:** Detect processor model, architecture, cores and threads.
- **Memory Information:** Retrieve total, used, free and available RAM.
- **Storage Information:** Detect storage devices, sizes and mount points.
- **GPU Information:** Check available GPU information and WSL GPU interface status.
- **Gemini Integration:** Understand natural-language questions using Google's Gemini API.
- **Function Calling:** Allow Gemini to request specific Python hardware tools.
- **Security:** Restrict execution to predefined allow-listed tools.
- **Error Handling:** Handle tool execution failures and retry temporary Gemini server errors.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11 | Core application |
| Google Gemini API | Natural-language understanding and response generation |
| Google Gen AI SDK | Gemini integration and function calling |
| Linux utilities | Hardware information collection |
| Python subprocess | Safe execution of predefined system commands |
| python-dotenv | Environment variable management |
| Git and GitHub | Version control |

## Project Architecture

```text
linux-hardware-assistant/
│
├── agent/
│   ├── assistant.py
│   ├── llm.py
│   └── tools_schema.py
│
├── tools/
│   ├── cpu.py
│   ├── memory.py
│   ├── storage.py
│   └── gpu.py
│
├── security/
│   ├── allowlist.py
│   └── executor.py
│
├── parsers/
│
├── app.py
├── test_ai.py
├── test_tools.py
├── test_security.py
├── test_hardware_ai.py
├── list_models.py
├── .gitignore
└── README.md
```

## How It Works

1. The user enters a hardware-related question through the CLI.
2. The application identifies the required hardware tools.
3. Gemini function calling requests the appropriate Python functions.
4. The security executor validates the requested tool against the allow-list.
5. The selected Python tool collects hardware information using Linux utilities.
6. The structured results are returned to Gemini.
7. Gemini generates a natural-language response based on the collected information.

## Security Design

The application uses an allow-list-based execution mechanism.

Only predefined functions are permitted:

- `get_cpu_info`
- `get_memory_info`
- `get_storage_info`
- `get_gpu_info`

Arbitrary shell commands are not accepted through the tool executor.

The hardware tools use predefined commands rather than executing arbitrary user-provided shell input.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Yamnur/linux-hardware-assistant.git
cd linux-hardware-assistant
```

### 2. Create a Python virtual environment

Python 3.11 is recommended.

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install google-genai python-dotenv
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never commit your `.env` file or expose your API key publicly.

### 5. Run the application

```bash
python app.py
```

## Example Usage

```text
=======================================================
       LINUX HARDWARE Q&A ASSISTANT
=======================================================

Ask questions about your CPU, RAM, storage and GPU.
Type 'exit' to quit.

You: How much RAM does my system have?

Assistant:
Your system has approximately 7.70 GiB of total RAM.

You: Can you detect my GPU?

Assistant:
No specific GPU device details were detected.
The WSL GPU interface is available, but the
GPU model could not be identified.
```

*Example responses are illustrative; actual results depend on the machine and environment.*

## Testing

Run the individual test scripts:

```bash
python test_tools.py
python test_security.py
python test_ai.py
python test_hardware_ai.py
```

You can also test the application interactively:

- What is my CPU model?
- How much RAM does my system have?
- Show my storage information.
- Can you detect my GPU?
- Give me a complete hardware summary.

## Limitations

- Hardware visibility depends on the Linux environment.
- WSL2 may expose virtual hardware rather than complete physical hardware details.
- GPU model detection depends on available system utilities and permissions.
- Gemini API availability and network connectivity are required for AI-generated responses.

## Future Improvements

- Add support for more hardware sensors.
- Improve hardware detection across Linux distributions.
- Add structured logging and more comprehensive automated tests.
- Introduce a lightweight graphical interface if required.
- Improve deterministic response formatting and validation.

## Author

**Yamanoorappa L Poojar**

GitHub: https://github.com/Yamnur

---

**Project:** Linux Hardware Q&A Assistant  
**Category:** AI Engineering | Python | Linux | LLM Tool Calling
