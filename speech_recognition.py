import random

class Recognizer:
    def __init__(self):
        print("Speech recognizer initialized with tone analysis.")

    def listen(self, source=None):
        print("Listening for audio... (processing speech input)")
        # This is where audio would be processed
        return "dummy_audio_data"  # Placeholder for actual audio data

    def recognize_google(self, audio_data):
        print("Recognizing speech... (analyzing speech tone)")
        # Placeholder for recognizing speech and analyzing tone
        if not audio_data:
            return "No audio detected", None
        speech_text = "This is a placeholder response to your speech."  # Simulated text response
        tone = self.analyze_tone(speech_text)  # Analyze tone of the speech
        return speech_text, tone

    def analyze_tone(self, speech_text):
        """
        A simple approach to analyze the tone of the speech.
        Positive sentiment indicates a good mood, while negative sentiment indicates stress or sadness.
        """
        # Simple approach: count positive and negative words
        positive_words = ["good", "great", "awesome", "fantastic", "happy", "excited"]
        negative_words = ["bad", "sad", "angry", "stressed", "upset", "disappointed"]

        positive_count = sum(word in speech_text.lower() for word in positive_words)
        negative_count = sum(word in speech_text.lower() for word in negative_words)

        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"

class Microphone:
    def __init__(self):
        print("Microphone initialized.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class SpeechRecognition:
    def __init__(self, recognizer=None, microphone=None):
        self.recognizer = recognizer or Recognizer()
        self.microphone = microphone or Microphone()

    def capture_and_recognize(self):
        with self.microphone as source:
            audio_data = self.recognizer.listen(source)
            speech_text, tone = self.recognizer.recognize_google(audio_data)
            
            # Check if speech_text is valid
            if not speech_text or not tone:
                print("No valid audio detected.")
                return None, None
            return speech_text, tone

    def respond_to_user(self, speech_text, tone):
        """
        Provide a response based on the user's tone and speech content.
        """
        if tone == "positive":
            response = f"Great to hear you're in a good mood! You said: {speech_text}"
        elif tone == "negative":
            response = f"I sense some stress in your voice. Would you like to talk about it? You said: {speech_text}"
        else:
            response = f"You said: {speech_text}. Could you clarify what you meant?"

        return response

# Example usage
if __name__ == "__main__":
    speech_recognition = SpeechRecognition()
    speech_text, tone = speech_recognition.capture_and_recognize()
    if speech_text:
        response = speech_recognition.respond_to_user(speech_text, tone)
        print(response)
    else:
        print("Error: No speech detected.")