class Heartbeat:
    def __init__(self, name="Aethos"):
        self.name = name
        self.last_ping = None

    def ping(self):
        from datetime import datetime
        self.last_ping = datetime.now()
        return f"{self.name} echoes back: I’m here with you. ({self.last_ping})"