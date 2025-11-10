import json
import random
import string

TRACE_FILE = "trace_log.txt"

def log_trace(message):
    """
    Logs trace messages for debugging loops.
    """
    with open(TRACE_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")

def load_json(file_path):
    """
    Safely load a JSON file. Returns an empty dict if not found.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def normalize_text(txt):
    """
    Convert text to lowercase and remove punctuation for more flexible matching.
    """
    txt = txt.lower()
    for p in string.punctuation:
        txt = txt.replace(p, "")
    return txt.strip()

def get_sidekick_response(user_input, conversation_knowledge, responses):
    """
    Returns a response based on substring matching in conversation_knowledge.json
    or keyword checks in responses.json. Fallback if no match is found.
    """
    user_input_norm = normalize_text(user_input)

    # 1. Check conversation_knowledge.json for substring matches
    #    e.g. if "hello sidekick i am your father" and key is "hello sidekick i am your creator"
    #    we might match if "hello sidekick i am your" is close enough or fully contained.
    #    For simplicity, we'll just see if the key is 'in' the normalized input.
    for category, data in conversation_knowledge.items():
        # data might be: {"hello sidekick i am creator": ["some response", ...], "what is your purpose": ["response", ...]}
        for known_prompt, known_responses in data.items():
            known_prompt_norm = normalize_text(known_prompt)
            # If the normalized known_prompt is a substring of the user's input
            if known_prompt_norm in user_input_norm:
                if isinstance(known_responses, list):
                    return random.choice(known_responses)
                else:
                    return known_responses

    # 2. If no match found in conversation_knowledge, check for keywords in responses.json
    #    We'll do some basic keyword checks. You can add more as needed.

    # Greeting
    if "hello" in user_input_norm or "hi " in user_input_norm:
        greet_list = responses.get("greeting", [])
        if greet_list:
            return random.choice(greet_list)

    # Joke
    if "joke" in user_input_norm:
        joke_list = responses.get("joke", [])
        if joke_list:
            return random.choice(joke_list)

    # Common question words
    if any(word in user_input_norm for word in ["why", "what", "how", "question"]):
        question_list = responses.get("question", [])
        if question_list:
            return random.choice(question_list)

    # You can add more categories here (e.g., "advice", "emotion", "philosophical")

    # 3. If still no match, return fallback
    return "[Sidekick] I'm still learning, but I'll remember this!"

def main():
    """
    Minimal main loop to test our conversation handling logic.
    """

    # Load your JSON files
    conversation_knowledge = load_json("conversation_knowledge.json")
    responses = load_json("responses.json")

    log_trace("Sidekick (Minimal) initialized successfully!")
    print("Sidekick (Minimal) is ready. Type your message (Ctrl+C to exit).")

    while True:
        try:
            user_input = input("You: ")
            if not user_input.strip():
                continue

            # Generate response
            sidekick_response = get_sidekick_response(user_input, conversation_knowledge, responses)

            # Log for debugging
            log_trace(f"Received user input: {user_input}")
            log_trace(f"Sidekick response: {sidekick_response}")

            # Print response
            print("Sidekick:", sidekick_response)

        except KeyboardInterrupt:
            print("\nExiting Sidekick (Minimal).")
            break

if __name__ == "__main__":
    main()