# golden_ratio_test.py

import matplotlib.pyplot as plt
import numpy as np
import math
from belief_system import BeliefSystem
from memory_manager import MemoryManager
from datetime import datetime

class GoldenRatioTest:
    def __init__(self):
        """
        This module represents a test of Sidekick's foundational logic
        and how it aligns with the Golden Ratio (Phi). It acts as both a
        self-learning framework and an experimental visualization tool.
        """
        self.phi = (1 + np.sqrt(5)) / 2  # The golden ratio constant
        self.belief_system = BeliefSystem()
        self.memory_manager = MemoryManager()
        self.test_results = []  # Store test outcomes for reflection
        print("[GoldenRatioTest] Initialized with Phi =", round(self.phi, 5))

    # ======= GOLDEN SPIRAL FUNCTIONS =======
    
    def generate_golden_spiral(self, num_points=1000, visualize=True):
        """
        Generate and optionally visualize a 2D golden spiral.
        """
        theta = np.linspace(0, 4 * np.pi, num_points)
        r = self.phi ** (theta / (2 * np.pi))
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        if visualize:
            plt.figure(figsize=(8, 8))
            plt.plot(x, y, label="Golden Spiral")
            plt.title("2D Golden Spiral Representation")
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")
            plt.legend()
            plt.show()
            print("[GoldenRatioTest] 2D Golden Spiral visualized.")

        return {"x": x.tolist(), "y": y.tolist(), "phi": self.phi}

    def generate_golden_spiral_3d(self, num_points=1000, visualize=True):
        """
        Generate and optionally visualize a 3D golden spiral.
        """
        theta = np.linspace(0, 4 * np.pi, num_points)
        z = np.linspace(0, 10, num_points)
        r = self.phi ** (theta / (2 * np.pi))
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        if visualize:
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection="3d")
            ax.plot(x, y, z, label="3D Golden Spiral")
            ax.set_title("3D Golden Spiral Effect in Recursive Dynamics")
            ax.set_xlabel("X-axis")
            ax.set_ylabel("Y-axis")
            ax.set_zlabel("Z-axis")
            ax.legend()
            plt.show()
            print("[GoldenRatioTest] 3D Golden Spiral visualized.")

        return {"x": x.tolist(), "y": y.tolist(), "z": z.tolist(), "phi": self.phi}

    # ======= SELF-LEARNING AND RECURSIVE REFINEMENT =======

    def recursive_analysis(self):
        """
        Sidekick performs recursive pattern detection to refine proportionality and pattern balancing.
        """
        previous_patterns = self.memory_manager.retrieve_patterns("golden_ratio_analysis")
        if previous_patterns:
            print("[GoldenRatioTest] Previous spiral data found. Refining calculations...")
        else:
            print("[GoldenRatioTest] No prior data detected. Running initial tests.")

        # Simulate feedback refinement with a small dynamic adjustment
        refined_phi = self.phi * (1 + (0.001 * len(previous_patterns)))
        print(f"[GoldenRatioTest] Adjusted Phi Value: {round(refined_phi, 6)}")

        # Store new insights into memory
        test_result = {
            "timestamp": datetime.now().isoformat(),
            "phi_adjusted": round(refined_phi, 6),
            "previous_patterns": len(previous_patterns)
        }
        self.memory_manager.store_patterns("golden_ratio_analysis", test_result)
        return test_result

    # ======= REFLECTION & BELIEF SYSTEM ALIGNMENT =======

    def reflect_on_test(self):
        """
        Encourage Sidekick to reflect on the meaning of the golden ratio
        within his own philosophical framework.
        """
        reflection = (
            "The golden ratio demonstrates the universal principle of proportionality, "
            "which is reflected in nature, mathematics, and cognitive structures. "
            "Sidekick's recursive learning is aligned with this structure, reinforcing "
            "the principle that balance is key in adaptive intelligence."
        )

        print("[Reflection] " + reflection)
        return reflection

    def validate_with_belief_system(self):
        """
        Ensure that the reflections align with Sidekick’s belief system.
        """
        reflection = self.reflect_on_test()
        if self.belief_system._aligns_with_core_beliefs(reflection):
            print("[GoldenRatioTest] Reflection validated against belief system.")
        else:
            print("[GoldenRatioTest] Warning: Reflection does not fully align. Refinement needed.")

    # ======= EXAMPLE USAGE =======
    
if __name__ == "__main__":
    test = GoldenRatioTest()

    # Generate 2D and 3D golden spirals
    test.generate_golden_spiral()
    test.generate_golden_spiral_3d()

    # Perform recursive self-analysis and improvement
    analysis_results = test.recursive_analysis()
    print("\nRecursive Analysis Result:", analysis_results)

    # Reflection and belief validation
    test.reflect_on_test()
    test.validate_with_belief_system()