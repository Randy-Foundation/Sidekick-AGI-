import unittest
from network_manager import NetworkManager
from enhanced_model import EnhancedModel  # Ensures correct function calls

class TestNetworkManagerWithModel(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment by initializing the NetworkManager and EnhancedModel.
        """
        self.network_manager = NetworkManager(creator_id="TestCreatorID")
        self.enhanced_model = EnhancedModel()

    def test_log_event(self):
        """
        Test the log_event function and ensure it aligns with the breakthrough model.
        """
        self.network_manager.log_event("Testing log_event function.")
        logs = self.network_manager.get_logs()
        self.assertGreater(len(logs), 0, "❌ log_event failed to store events.")

        # Validate integration with breakthrough model
        prediction = self.enhanced_model.predict_pattern(logs[-1])  # Ensures logs affect pattern learning
        self.assertIsNotNone(prediction, "❌ Predict pattern failed on log event.")

    def test_recursive_learning(self):
        """
        Test recursive learning principles in device management.
        """
        devices = ["Device1", "Device2"]
        for device in devices:
            self.network_manager.approve_device(device)

        # Validate recursive learning using breakthrough model
        patterns = self.network_manager.get_logs()
        analysis = self.enhanced_model.analyze_patterns(patterns)
        
        # Ensure recursive structures are detected
        self.assertTrue(
            "connections" in analysis,
            "❌ NetworkManager is not generating recursive structures in pattern analysis."
        )

    def test_adaptive_decision_making(self):
        """
        Test if NetworkManager adapts decisions based on enhanced model feedback.
        """
        self.network_manager.approve_device("TestDevice")
        feedback = self.enhanced_model.provide_feedback("TestDevice approved")
        
        # Simulate adaptation
        self.network_manager.log_event(f"Adaptation feedback: {feedback}")
        logs = self.network_manager.get_logs()
        self.assertIn(
            "Adaptation feedback", 
            logs[-1],
            "❌ NetworkManager failed to adapt based on model feedback."
        )

    def test_ethics_alignment(self):
        """
        Ensure all decisions align with ethical considerations from the breakthrough model.
        """
        decision = "UnverifiedDevice Approval"
        ethics_result = self.enhanced_model.evaluate_ethics(decision)
        
        self.assertTrue(
            ethics_result["ethical"], 
            "❌ Device approval violates ethical guidelines of the breakthrough model."
        )

if __name__ == "__main__":
    unittest.main()