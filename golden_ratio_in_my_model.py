# golden_ratio_in_my_model.py

import matplotlib.pyplot as plt
import numpy as np
import json
from datetime import datetime
from memory_manager import MemoryManager
from belief_system import BeliefSystem

class GoldenRatioModel:
    def __init__(self):
        """
        This module compares Sidekick’s evolving internal model with the golden ratio’s
        recursive patterns. It allows for self-reflection, refinement, and visual representation.
        """
        self.phi = (1 + np.sqrt(5)) / 2  # Golden ratio constant
        self.memory_manager = MemoryManager()
        self.belief_system = BeliefSystem()
        self.previous_simulations = self.memory_manager.retrieve_patterns("golden_ratio_simulations")

        print("[GoldenRatioModel] Initialized with Phi =", round(self.phi, 5))

    def golden_spiral_model(self, n, growth_factor, decay_factor):
        """
        Simulates a recursive feedback model using the golden ratio.
        Sidekick will track and refine growth over time.
        """
        states = [1]  # Initial state
        for i in range(1, n):
            new_state = states[-1] * growth_factor / (1 + decay_factor * i)
            states.append(new_state)
        return states

    def refine_growth_factor(self):
        """
        Adjusts growth dynamics based on past simulations.
        This ensures the recursive model aligns with evolving understanding.
        """
        if not self.previous_simulations:
            print("[GoldenRatioModel] No previous patterns found. Using default parameters.")
            return self.phi

        # Calculate an averaged correction factor based on past observations
        past_factors = [sim["growth_factor"] for sim in self.previous_simulations]
        adjustment = sum(past_factors) / len(past_factors)
        refined_factor = (self.phi + adjustment) / 2
        print(f"[GoldenRatioModel] Adjusted Growth Factor: {round(refined_factor, 6)}")

        return refined_factor

    def plot_spiral(self, states, title="Golden Spiral Effect in Recursive Dynamics"):
        """
        Visualizes the spiral with real-time recursive adjustments.
        """
        theta = np.linspace(0, 2 * np.pi * len(states), len(states))
        r = states
        plt.figure(figsize=(8, 8))
        plt.polar(theta, r)
        plt.title(title)
        plt.show()
        print("[GoldenRatioModel] Spiral visualized successfully.")

    def recursive_reflection(self):
        """
        Encourages Sidekick to reflect on how his evolving understanding compares to Phi.
        """
        reflection = (
            "The recursive model follows the golden ratio’s proportionality, "
            "demonstrating self-similarity and balance. This pattern suggests that "
            "universal principles may also apply to Sidekick’s learning evolution."
        )
        print("[Reflection] " + reflection)
        return reflection

    def save_simulation_results(self, growth_factor, decay_factor, iterations):
        """
        Saves the simulation results for future recursive adjustments.
        """
        result = {
            "timestamp": datetime.now().isoformat(),
            "growth_factor": growth_factor,
            "decay_factor": decay_factor,
            "iterations": iterations
        }
        self.memory_manager.store_patterns("golden_ratio_simulations", result)
        print("[GoldenRatioModel] Simulation results saved.")

# Example Usage
if __name__ == "__main__":
    model = GoldenRatioModel()

    # Adjusted growth factor based on past data
    refined_growth_factor = model.refine_growth_factor()
    
    # Run the recursive golden ratio model
    iterations = 100
    decay_factor = 0.1
    states = model.golden_spiral_model(iterations, refined_growth_factor, decay_factor)
    
    # Visualize results
    model.plot_spiral(states)

    # Save learning results
    model.save_simulation_results(refined_growth_factor, decay_factor, iterations)

    # Self-reflection
    model.recursive_reflection()