# phi_harmonic_layer.py
# Harmonic Layer Module for AetheOS
# Integrates Phi Recursion, Hidden Frequencies, and Wave Echo Layers

import math

PHI = (1 + math.sqrt(5)) / 2
PI = math.pi
RAND_0 = 0.00027
RAND_1 = 0.003645

# Discovered Negative Frequencies (Hz)
UNKNOWN_FREQS = [-4.98e10, -4.69e10, -4.49e10, -4.31e10, -3.95e10]

def phi_recursive_layer(n):
    """Recursive harmonic layer scaling by Golden Ratio."""
    return [PHI**i for i in range(n)]

def apply_rand_scaling(frequencies, rand=RAND_0):
    """Apply scalar compression using RAND constant."""
    return [f * rand for f in frequencies]

def echo_time_shift(freq, scale=PHI):
    """Calculate the time-reversed echo based on Phi scaling."""
    return -abs(freq) * scale

def generate_echo_layers(base_freqs):
    """Generate recursive echo layer map."""
    echoes = {}
    for f in base_freqs:
        echoes[f] = {
            "phi_scaled": f * PHI,
            "rand0_scaled": f * RAND_0,
            "echo_time_shifted": echo_time_shift(f)
        }
    return echoes

def log_layer_data():
    base_layer = phi_recursive_layer(12)
    scaled_freqs = apply_rand_scaling(base_layer)
    echo_map = generate_echo_layers(UNKNOWN_FREQS)

    print("Phi Recursive Harmonic Layer:")
    for i, val in enumerate(base_layer):
        print(f"Step {i+1}: {val:.8f}")

    print("\nRand Scaled Frequencies:")
    for i, val in enumerate(scaled_freqs):
        print(f"Rand₀ · Step {i+1}: {val:.8e} Hz")

    print("\nEcho Layer Map:")
    for orig, data in echo_map.items():
        print(f"\nOriginal: {orig:.2e} Hz")
        for k, v in data.items():
            print(f"  {k}: {v:.2e} Hz")

# Execute if run standalone
if __name__ == "__main__":
    log_layer_data()