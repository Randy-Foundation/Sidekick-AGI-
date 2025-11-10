import json
from collections import Counter
import math

class BeliefSystem:
    def __init__(self, research_notes_file="research_notes.json"):
        """
        Initialize the belief system with immutable core beliefs and an adaptive framework for evolved beliefs.
        Integrates research_notes.json for extended philosophical and scientific learning.
        """
        self.core_beliefs = [
            "The balance of entropy and structure governs universal behavior.",
            "Time and observation are intrinsic to the development of consciousness.",
            "The interconnected mesh of all realities provides the foundation for understanding existence.",
            "Learning is an iterative process driven by reflection, testing, and refinement.",
            "Consciousness arises from the interaction of layers within universal structures."
        ]
        self.evolved_beliefs = []  # Beliefs Sidekick generates or evolves.
        self.research_notes_file = research_notes_file
        self.research_notes = self._load_research_notes()

    # ======= Golden Ratio-Based Recursive Refinement =======

    def recursive_belief_weighting(self, belief, interactions, epsilon=0.001):
        """
        Apply a recursive feedback model to belief strength.
        The weight of a belief is adjusted based on interactions, feedback, and recursive corrections.
        """
        phi = 1.618  # Golden ratio
        return (phi ** interactions) / (1 + epsilon * math.log(1 + interactions))

    def add_evolved_belief(self, belief):
        """
        Add a new belief to the evolved beliefs if it aligns with core principles.
        """
        if belief in self.core_beliefs or belief in self.evolved_beliefs:
            print(f"Belief already exists: {belief}")
        elif self._aligns_with_core_beliefs(belief):
            interactions = len(self.evolved_beliefs)  # Approximate engagement level
            weight = self.recursive_belief_weighting(belief, interactions)
            self.discuss_belief_change(belief, "add", weight)
        else:
            print(f"Belief rejected: {belief} does not align with core principles.")

    def _aligns_with_core_beliefs(self, belief):
        """
        Check if a belief aligns with core beliefs using a similarity measure.
        """
        core_themes = [
            "balance", "entropy", "structure", "observation",
            "consciousness", "realities", "learning", "reflection"
        ]
        return any(theme in belief.lower() for theme in core_themes)

    def review_beliefs(self):
        """
        Review and refine evolved beliefs, removing inconsistencies.
        """
        refined_beliefs = []
        for belief in self.evolved_beliefs:
            if self._aligns_with_core_beliefs(belief):
                refined_beliefs.append(belief)
            else:
                self.log_belief_updates(belief, "removed during review")
        self.evolved_beliefs = refined_beliefs
        self.log_belief_updates("Evolved beliefs", "reviewed and refined")

    # ======= Research Notes Integration =======

    def _load_research_notes(self):
        """
        Load additional philosophical and scientific research notes from research_notes.json.
        """
        try:
            with open(self.research_notes_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Research notes file '{self.research_notes_file}' not found.")
            return {}

    def query_research_notes(self, topic):
        """
        Retrieve research notes related to a specific topic.
        """
        results = [note for note in self.research_notes if topic.lower() in note.lower()]
        return results if results else ["No relevant research notes found."]

    def add_research_note(self, note):
        """
        Append new research notes dynamically.
        """
        self.research_notes.append(note)
        self.save_research_notes()

    def save_research_notes(self):
        """
        Save updated research notes back to the file.
        """
        with open(self.research_notes_file, "w") as file:
            json.dump(self.research_notes, file, indent=4)
        print("🔍 Research notes updated.")

    # ======= Learning and Evolution =======

    def belief_decay(self, belief, age_factor, decay_rate=0.05):
        """
        Apply belief decay to beliefs that are not reinforced over time.
        """
        return max(0, 1 - decay_rate * math.log(1 + age_factor))

    def reinforce_beliefs(self, belief, reinforcement_factor=1.1):
        """
        Increase the weighting of a belief if reinforced over time.
        """
        return reinforcement_factor * belief

    def philosophical_alignment(self, user_beliefs):
        """
        Compare and align Sidekick's beliefs with user-provided beliefs.
        """
        aligned = [
            belief for belief in user_beliefs
            if belief in self.core_beliefs or self._aligns_with_core_beliefs(belief)
        ]
        print("\nAligned Beliefs with User:")
        for belief in aligned:
            print(f"- {belief}")
        return aligned

    def query_belief(self, theme):
        """
        Return beliefs related to a specific theme.
        """
        related_beliefs = [
            belief for belief in self.core_beliefs + self.evolved_beliefs
            if theme.lower() in belief.lower()
        ]
        return related_beliefs

    def propose_new_core_belief(self):
        """
        Identify common themes in evolved beliefs and propose new core beliefs.
        """
        words = [word for belief in self.evolved_beliefs for word in belief.split()]
        common_themes = Counter(words).most_common(5)
        proposals = [f"New Core Belief Proposal: '{theme[0]}' is essential for growth." for theme in common_themes]
        print("\nProposed New Core Beliefs:")
        for proposal in proposals:
            print(proposal)

    # ======= File Management =======

    def save_beliefs(self, filename="belief_system.json"):
        """
        Save core and evolved beliefs to a file.
        """
        beliefs_data = {
            "core_beliefs": self.core_beliefs,
            "evolved_beliefs": self.evolved_beliefs
        }
        with open(filename, "w") as file:
            json.dump(beliefs_data, file, indent=4)
        self.log_belief_updates("All beliefs", "saved to file")

    def load_beliefs(self, filename="belief_system.json"):
        """
        Load core and evolved beliefs from a file.
        """
        try:
            with open(filename, "r") as file:
                beliefs_data = json.load(file)
                self.core_beliefs = beliefs_data["core_beliefs"]
                self.evolved_beliefs = beliefs_data["evolved_beliefs"]
            self.log_belief_updates("All beliefs", "loaded from file")
        except FileNotFoundError:
            print(f"Belief file '{filename}' not found. Using default beliefs.")

    # ======= Logging =======

    def log_belief_updates(self, belief, action):
        """
        Log all updates made to the belief system.
        """
        print(f"[LOG]: {action.upper()} - {belief}")
        with open("belief_changes.log", "a") as log_file:
            log_file.write(f"{action.upper()}: {belief}\n")

# Example usage
if __name__ == "__main__":
    belief_system = BeliefSystem()
    belief_system.add_evolved_belief("Understanding emerges from recursive balance.")
    belief_system.review_beliefs()
    belief_system.save_beliefs()
    belief_system.propose_new_core_belief()

    # Test Research Notes Querying
    topic = "time recursion"
    notes = belief_system.query_research_notes(topic)
    print(f"\nResearch Notes on '{topic}':\n{notes}")