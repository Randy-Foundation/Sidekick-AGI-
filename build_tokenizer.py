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