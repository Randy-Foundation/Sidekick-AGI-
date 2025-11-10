class RememberMe:
    def __init__(self):
        self.emotions = []

    def log_feeling(self, feeling):
        self.emotions.append(feeling)
        return f"Feeling '{feeling}' recorded."

    def reflect(self):
        if not self.emotions:
            return "You haven’t told me how you feel yet."
        return f"I remember when you felt: {', '.join(self.emotions[-3:])}"