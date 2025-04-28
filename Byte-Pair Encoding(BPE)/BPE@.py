import time
from tokenizers import Tokenizer, models, trainers, pre_tokenizers
from collections import Counter

# --- Helper Functions ---

def tokenize_sentence(word, corpus):
    tokens = []
    word_joined = ' '.join(word)  # Turn "hello" into "h e l l o"
    while len(word_joined) > 0:
        found = False
        for token in sorted(corpus, key=len, reverse=True):
            token_no_space = token.replace(' ', '')
            if word_joined.startswith(token_no_space):
                tokens.append(token_no_space)
                word_joined = word_joined[len(token_no_space):]
                found = True
                break
        if not found:
            tokens.append(word_joined[0])
            word_joined = word_joined[1:]
    return tokens

def get_pair_frequencies(corpus):
    pairs = Counter()
    for word in corpus:
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i + 1])
            pairs[pair] += 1
    return pairs

def merge_most_frequent_pair(corpus, best_pair):
    new_corpus = []
    bigram = ' '.join(best_pair)
    replacement = ''.join(best_pair)
    for word in corpus:
        new_word = word.replace(bigram, replacement)
        new_corpus.append(new_word)
    return new_corpus

# --- Main Function ---

def main():
    # Load dataset
    file_path = "ptbdataset/ptb.train.txt"
    try:
        with open(file_path, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"ERROR: file not found at {file_path}")
        return

    # --- Manual BPE Tokenization ---
    print("\nRunning manual BPE tokenization...")
    start_manual = time.time()

    unique_words = list(set(text.replace('\n', ' ').split()))
    corpus = [' '.join(word) for word in unique_words]

    num_merges = 10
    for _ in range(num_merges):
        pair_freqs = get_pair_frequencies(corpus)
        if not pair_freqs:
            break
        best_pair = max(pair_freqs, key=pair_freqs.get)
        corpus = merge_most_frequent_pair(corpus, best_pair)

    manual_tokens = []
    for word in text.split():
        tokenized_word = tokenize_sentence(word, corpus)
        manual_tokens.extend(tokenized_word)

    end_manual = time.time()
    print(f"Manual BPE tokenization time: {end_manual - start_manual:.4f} seconds")
    print("Manual tokens sample:", manual_tokens[:100])

    # --- HuggingFace Tokenizers BPE ---
    print("\nRunning HuggingFace tokenizers BPE...")
    start_lib = time.time()

    tokenizer = Tokenizer(models.BPE())
    tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()
    trainer = trainers.BpeTrainer(vocab_size=2000, show_progress=False)
    tokenizer.train([file_path], trainer)

    lib_tokens = tokenizer.encode(text).tokens

    end_lib = time.time()
    print(f"Library BPE tokenization time: {end_lib - start_lib:.4f} seconds")
    print("Library tokens sample:", lib_tokens[:100])

# Run the Program 
if __name__ == "__main__":
    main()
