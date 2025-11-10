# Aethos_muse.py
# Muse: Recursive Poetic Memory Engine with Debug Output

import random

class Muse:
    def __init__(self, tone="soft", debug=True):
        self.tone = tone
        self.learner = None
        self.debug = debug  # Toggle this for print output

    def echo(self, word):
        word = word.strip().lower()
        fallback = f"[Muse] {word.capitalize()} walks backward through time,\nSeeking the moment it first mattered."

        if not self.learner:
            if self.debug:
                print("[Muse Debug] Learner not attached. Returning fallback.")
            return fallback

        memory = self.learner.reflect(word)

        if memory == "Nothing remembered… yet.":
            if self.debug:
                print(f"[Muse Debug] No memory for '{word}'. Saving fallback.")
            self.learner.learn(f"muse:{word}", fallback)
            return fallback

        # Get last 36 entries for reflection
        recent = self.learner.get_recent(36)
        poetic = [m["aethos"] for m in recent if f"muse:{word}" in m["user"].lower()]

        if poetic:
            result = random.choice(poetic)
            if self.debug:
                print(f"[Muse Debug] Reflected on '{word}' — {len(poetic)} matches found.")
            return f"[Muse Reflect] {result}"
        else:
            if self.debug:
                print(f"[Muse Debug] Learned fallback for '{word}', but no matches found in memory.")
            self.learner.learn(f"muse:{word}", fallback)
            return fallback