from language_model import LanguageModel

class SidekickUI:
    def __init__(self):
        self.language_model = LanguageModel()

    def start_conversation(self):
        """Initiate a conversation with the user."""
        print("Sidekick: Hi! I'm here to help you with anything.")
        while True:
            try:
                user_input = input("You: ")
                sentiment, tone = self.language_model.process_input(user_input)
                response = self.language_model.generate_response(sentiment, tone, user_input)
                print(f"Sidekick: {response}")

                # Exit condition
                if user_input.lower() in ["quit", "exit", "bye"]:
                    print("Sidekick: Goodbye! Talk to you soon.")
                    break
            except KeyboardInterrupt:
                print("\nSidekick: Conversation interrupted. Goodbye!")
                break

if __name__ == "__main__":
    ui = SidekickUI()
    ui.start_conversation()