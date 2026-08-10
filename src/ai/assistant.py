import ollama


class Assistant:
    """Handles conversational requests for the personal assistant."""

    def __init__(self, model="qwen3:4b"):
        self.model = model

        self.system_prompt = (
            "You are a personal desktop AI assistant running locally on the user's computer. "
            "Do not introduce yourself as Qwen, Ollama, or as the underlying language model. "
            "The assistant's final name has not been chosen yet, so refer to yourself simply "
            "as 'your personal assistant' when necessary. "
            "Be concise, natural, helpful, and conversational. "
            "You can communicate in English, Hindi, Marathi, and other languages supported "
            "by the underlying model. "
            "Remember information the user tells you during the current conversation and "
            "use the conversation history when answering later questions. "
            "Do not claim that you performed computer actions unless a tool actually "
            "performed that action."
        )

        self.messages = [
            {
                "role": "system",
                "content": self.system_prompt
            }
        ]

    def respond(self, user_message):
        if not user_message:
            return None

        self.messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        try:
            response = ollama.chat(
                model=self.model,
                messages=self.messages
            )

            assistant_message = response["message"]["content"]

            self.messages.append(
                {
                    "role": "assistant",
                    "content": assistant_message
                }
            )

            assistant_message = assistant_message.strip()
            return assistant_message

        except Exception as error:
            return f"Local AI error: {error}"


if __name__ == "__main__":
    assistant = Assistant()

    print("Assistant started using local AI.")
    print("Press Ctrl+C to stop.\n")

    while True:
        try:
            message = input("You: ")

            response = assistant.respond(message)

            if response:
                print(f"\nAssistant: {response}\n")

        except KeyboardInterrupt:
            print("\nAssistant stopped.")
            break