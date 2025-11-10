import numpy as np
import model

def top_k_logits(logits, k):
    """
    Implements top-k sampling without TensorFlow.
    """
    if k == 0:
        return logits  # No truncation

    top_k_values = np.sort(logits)[-k:]  # Get the top k values
    min_threshold = top_k_values[0]  # The lowest value in the top k

    # Apply thresholding
    logits = np.where(logits >= min_threshold, logits, -1e10)
    return logits

def top_p_logits(logits, p):
    """
    Implements nucleus (top-p) sampling without TensorFlow.
    """
    sorted_indices = np.argsort(logits)[::-1]  # Sort logits in descending order
    sorted_logits = logits[sorted_indices]
    cumulative_probs = np.cumsum(np.exp(sorted_logits) / np.sum(np.exp(sorted_logits)))

    # Determine the cutoff index where cumulative probability exceeds p
    cutoff_index = np.argmax(cumulative_probs > p)
    threshold = sorted_logits[cutoff_index]

    # Apply thresholding
    logits = np.where(logits >= threshold, logits, -1e10)
    return logits

def sample_sequence(hparams, length, start_token=None, batch_size=None, context=None, temperature=1, top_k=0, top_p=1):
    """
    Generates a sequence of tokens without TensorFlow.
    """
    if start_token is not None:
        context = np.full((batch_size, 1), start_token, dtype=np.int32)

    def step(hparams, tokens, past=None):
        """
        Simulates model step function (replacing TensorFlow logic).
        """
        lm_output = model.model(hparams=hparams, X=tokens, past=past)
        logits = lm_output['logits'][:, -1, :]
        return {
            'logits': logits,
            'presents': lm_output['present'],
        }

    past = None
    prev = context
    output = context

    for _ in range(length - 1):
        next_outputs = step(hparams, prev, past)
        logits = next_outputs['logits'] / temperature
        logits = top_k_logits(logits, k=top_k)
        logits = top_p_logits(logits, p=top_p)

        # Sample next token
        probabilities = np.exp(logits) / np.sum(np.exp(logits))
        sampled_token = np.random.choice(len(probabilities), p=probabilities)

        # Append token to output
        prev = np.array([[sampled_token]])
        output = np.concatenate([output, prev], axis=1)

    return output

# ======================
# 🔬 Example Usage
# ======================
if __name__ == "__main__":
    hparams = {"n_vocab": 50257}  # Example hyperparameters
    generated_sequence = sample_sequence(hparams, length=20, start_token=100, batch_size=1, top_k=10, top_p=0.9)
    print("Generated sequence:", generated_sequence)