
import math

# Golden Ratio (Φ)
PHI = 1.618

def entropy_stabilization(t):
    """
    Placeholder for the entropy stabilization function H(t).
    In the original paper, H(t) is used to prevent runaway complexity.
    You can replace this function with a more sophisticated version
    as needed for your application.
    """
    # For demonstration, we return the input or a fixed value.
    return t  # or simply return 1 if you wish to fix it

def recursive_R(n, H_value=1):
    """
    Computes the recursive stabilization function R(n) recursively.
    
    Based on the paper's definition, we interpret the formula as:
    
        R(n) = R(n-1) + term(n)
    
    where the term at each recursion level is given by:
    
        term(n) = (1/PHI) * exp(- (pi/4) * H_value) * exp(-pi * n**2) * exp(-pi * n)
    
    with a base case:
    
        R(0) = 0
    
    This design ensures that the function is computed recursively rather than in a linear loop.
    """
    if n <= 0:
        return 0
    else:
        # Compute the recursive term
        term = (1 / PHI) * math.exp(- (math.pi / 4) * entropy_stabilization(H_value)) \
               * math.exp(- math.pi * (n ** 2)) * math.exp(- math.pi * n)
        # Recursive call: sum the previous terms with the current term
        return recursive_R(n - 1, H_value) + term

# Example usage: This section can be integrated into your AGI system for testing.
if __name__ == '__main__':
    # For demonstration, compute R(n) for n = 1 to 10.
    print("Recursive Stabilization Function Values:")
    for i in range(1, 11):
        result = recursive_R(i)
        print(f"R({i}) = {result:.6e}")

import json
import re
import sys

def build_encoder(corpus):
    """
    Splits the corpus into tokens using a simple regex, then builds a token → id mapping.
    This produces a minimal encoder.json dictionary.
    """
    # Tokenize on words and punctuation
    tokens = re.findall(r'\w+|[^\w\s]', corpus, re.UNICODE)
    unique_tokens = sorted(set(tokens))
    encoder = {token: idx for idx, token in enumerate(unique_tokens)}
    return encoder

def build_vocab_bpe():
    """
    Returns a minimal vocab.bpe file content.
    GPT-2 expects the first line to be a version header.
    No merge rules are added here.
    """
    return "#version: 0.2\n"

def main():
    # If a corpus file is provided as a command-line argument, use it.
    # Otherwise, use a built-in sample corpus.
    if len(sys.argv) > 1:
        corpus_file = sys.argv[1]
        with open(corpus_file, 'r', encoding='utf-8') as f:
            corpus = f.read()
    else:
        corpus = (
            "Hello, this is a sample corpus for building a minimal tokenizer for Sidekick. "
            "It includes various words and punctuation! "
            "Feel free to expand this corpus to better suit your AGI needs."
        )

    encoder = build_encoder(corpus)
    vocab_bpe = build_vocab_bpe()

    # Write encoder.json with pretty printing
    with open("encoder.json", "w", encoding="utf-8") as f:
        json.dump(encoder, f, ensure_ascii=False, indent=4)
    # Write vocab.bpe
    with open("vocab.bpe", "w", encoding="utf-8") as f:
        f.write(vocab_bpe)

    print("Generated encoder.json and vocab.bpe successfully.")

if __name__ == '__main__':
    main()