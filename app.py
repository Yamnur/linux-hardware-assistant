
from agent.assistant import ask_hardware_assistant


def main():

    print("=" * 55)
    print("       LINUX HARDWARE Q&A ASSISTANT")
    print("=" * 55)
    print("Ask questions about your CPU, RAM, storage and GPU.")
    print("Type 'exit' to quit.")
    print("-" * 55)

    while True:

        question = input("\nYou: ").strip()

        if question.lower() in ["exit", "quit", "bye"]:
            print("\nAssistant: Goodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        try:
            print("\nAssistant: Thinking...")

            answer = ask_hardware_assistant(question)

            print("\nAssistant:", answer)

        except Exception as e:
            print("\nError:", str(e))
            print("Please try again.")


if __name__ == "__main__":
    main()

