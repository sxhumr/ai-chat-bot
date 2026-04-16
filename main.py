from chatbot.client import ChatClient
from chatbot.memory import ConversationMemory
from chatbot.logger import ChatLogger

SYSTEM_PROMPT = (
    "You are a helpful, concise assistant. "
    "Answer clearly and ask a follow-up question when useful."
)

def main():
    client = ChatClient()
    memory = ConversationMemory(system_prompt=SYSTEM_PROMPT)
    logger = ChatLogger()

    print("AI Chatbot  |  type 'quit' to exit, 'clear' to reset\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        if user_input.lower() == "clear":
            memory.clear()
            print("[Conversation cleared]\n")
            continue

        memory.add("user", user_input)
        logger.log("user", user_input)

        reply = client.send(memory.get())
        memory.add("assistant", reply)
        logger.log("assistant", reply)

        print(f"\nAssistant: {reply}\n")

if __name__ == "__main__":
    main()