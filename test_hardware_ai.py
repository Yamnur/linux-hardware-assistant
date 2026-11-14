from agent.assistant import ask_hardware_assistant

question = input("Ask about your hardware: ")

answer = ask_hardware_assistant(question)

print("\nAssistant:", answer)
