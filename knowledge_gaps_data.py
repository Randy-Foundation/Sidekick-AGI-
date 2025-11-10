import json
import datetime

class KnowledgeGapHandler:
    def __init__(self, file_name="knowledge_gaps.json", research_notes_file="research_notes.json"):
        """
        Initialize the knowledge gap handler with a reference to knowledge gaps and research notes.
        """
        self.file_name = file_name
        self.research_notes_file = research_notes_file
        self.knowledge_data = self._load_knowledge_gaps()
        self.research_notes = self._load_research_notes()

    def _load_knowledge_gaps(self):
        """
        Load knowledge gaps from a JSON file.
        """
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"gaps": [], "resolved_gaps": []}

    def _load_research_notes(self):
        """
        Load research notes from research_notes.json.
        """
        try:
            with open(self.research_notes_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"⚠️ Research notes file '{self.research_notes_file}' not found.")
            return []

    def save_knowledge_gaps(self):
        """
        Save the updated knowledge gaps back to the JSON file.
        """
        with open(self.file_name, "w") as file:
            json.dump(self.knowledge_data, file, indent=4)

    def query_research_notes(self, topic):
        """
        Retrieve research notes related to a specific topic before logging it as a knowledge gap.
        """
        results = [note for note in self.research_notes if topic.lower() in note.lower()]
        return results if results else None

    def log_knowledge_gap(self, topic, suggested_fix=None):
        """
        Log a new knowledge gap if it is not already recorded, ensuring it isn't covered in research_notes.json.
        """
        # Check if the knowledge already exists in research notes before logging a gap
        existing_research = self.query_research_notes(topic)
        if existing_research:
            print(f"✅ Existing research found for '{topic}'. Logging not required.")
            return

        # Check if the topic is already a known gap
        existing_gap = next((gap for gap in self.knowledge_data["gaps"] if gap["topic"] == topic), None)

        if existing_gap:
            existing_gap["occurrences"] += 1
            existing_gap["last_attempt"] = datetime.datetime.now().isoformat()
        else:
            new_gap = {
                "topic": topic,
                "occurrences": 1,
                "last_attempt": datetime.datetime.now().isoformat(),
                "suggested_fix": suggested_fix or "No suggested fix yet.",
                "status": "unresolved"
            }
            self.knowledge_data["gaps"].append(new_gap)

        self.save_knowledge_gaps()
        print(f"🔍 Logged new knowledge gap: {topic}")

    def review_knowledge_gaps(self):
        """
        Display all unresolved knowledge gaps.
        """
        if not self.knowledge_data["gaps"]:
            print("[INFO] No unresolved knowledge gaps.")
            return

        print("\n🔍 Unresolved Knowledge Gaps:")
        for gap in self.knowledge_data["gaps"]:
            print(f"- {gap['topic']} (Attempts: {gap['occurrences']})")
            print(f"  Last Attempt: {gap['last_attempt']}")
            print(f"  Suggested Fix: {gap['suggested_fix']}")
            print(f"  Status: {gap['status']}\n")

    def resolve_knowledge_gap(self, topic, fix_description):
        """
        Mark a knowledge gap as resolved and store it for future reference.
        """
        gap = next((gap for gap in self.knowledge_data["gaps"] if gap["topic"] == topic), None)

        if gap:
            resolved_entry = {
                "topic": topic,
                "resolved_on": datetime.datetime.now().isoformat(),
                "fix": fix_description
            }
            self.knowledge_data["resolved_gaps"].append(resolved_entry)
            self.knowledge_data["gaps"].remove(gap)
            self.save_knowledge_gaps()
            print(f"✅ Marked '{topic}' as resolved and added to research notes.")
            
            # Store resolution in research_notes.json for future reference
            self.add_research_notes(f"Resolved knowledge gap: {topic} - Fix: {fix_description}")
        else:
            print(f"⚠️ Knowledge gap '{topic}' not found.")

    def add_research_notes(self, new_note):
        """
        Append new research notes dynamically when a knowledge gap is resolved.
        """
        self.research_notes.append(new_note)
        self.save_research_notes()

    def save_research_notes(self):
        """
        Save updated research notes back to the file.
        """
        with open(self.research_notes_file, "w") as file:
            json.dump(self.research_notes, file, indent=4)
        print("📚 Research notes updated.")

    def auto_review_and_fix(self):
        """
        Auto-review gaps and attempt to resolve some based on existing knowledge.
        """
        for gap in self.knowledge_data["gaps"]:
            if "ethics" in gap["topic"].lower():
                suggested_fix = "Cross-reference ethical AI principles with Sidekick's core beliefs."
            elif "quantum" in gap["topic"].lower():
                suggested_fix = "Compare quantum mechanics fundamentals with neural network dynamics."
            elif self.query_research_notes(gap["topic"]):
                suggested_fix = "Relevant research exists in research_notes.json."
                gap["status"] = "resolved via research notes"
            else:
                suggested_fix = "Research topic in memory database and external references."

            gap["suggested_fix"] = suggested_fix
            gap["status"] = "pending review"

        self.save_knowledge_gaps()
        print("🔄 Knowledge gaps auto-reviewed with suggested fixes.")

# =====================
# 🔬 Example Usage
# =====================
if __name__ == "__main__":
    handler = KnowledgeGapHandler()
    
    # Example: Logging a gap that already has research
    handler.log_knowledge_gap("Golden Ratio and Time Perception")
    
    # Example: Logging a completely new knowledge gap
    handler.log_knowledge_gap("AI and emotional intelligence", "Explore psychology-based learning models.")
    
    # Reviewing existing gaps
    handler.review_knowledge_gaps()
    
    # Auto-reviewing knowledge gaps
    handler.auto_review_and_fix()
    
    # Resolving a knowledge gap
    handler.resolve_knowledge_gap("AI and emotional intelligence", "Implemented a new emotion recognition system.")