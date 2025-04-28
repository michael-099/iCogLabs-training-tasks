

'''from scratch implementation implementation '''


# Extracting unique words from the corpus
def get_unique_words_in_file(file_path):
    unique_words = set()
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            cleaned_content = content.replace('\n', ' ')
            words = cleaned_content.split(" ")
            for word in words:
                if word:
                    unique_words.add(word)
        return list(unique_words)
    except FileNotFoundError:
        print(f"ERROR: file not found at {file_path}")
        return []

# Function for extracting base vocabulary
def base_vocabulary(unique_words):
    base_vocab = set()
    for word in unique_words:
        for char in word:
            base_vocab.add(char)
    return base_vocab

# Character frequency in the file
def char_frequency_in_file(base_vocab, unique_words):
    char_freq = {char: 0 for char in base_vocab}
    for word in unique_words:
        for char in word:
            char_freq[char] += 1
    return char_freq

# Count pair frequencies
def get_pair_frequencies(corpus):
    pairs = Counter()
    for word in corpus:
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i + 1])
            pairs[pair] += 1
    return pairs

# Merge the most frequent pair
def merge_most_frequent_pair(corpus, best_pair):
    new_corpus = []
    bigram = ' '.join(best_pair)
    replacement = ''.join(best_pair)

    for word in corpus:
        new_word = word.replace(bigram, replacement)
        new_corpus.append(new_word)
    return new_corpus

# The BPE function
def byte_pair_encoding(num_merges=10):
    unique_words = get_unique_words_in_file("ptbdataset/ptb.train.txt")
    if not unique_words:
        return

    # Turn words into list of characters joined with spaces (e.g., "h e l l o")
    corpus = [' '.join(word) for word in unique_words]
    print(f"Initial corpus: {corpus}")

    for i in range(num_merges):
        print(f"\n--- Merge {i+1} ---")
        pair_freqs = get_pair_frequencies(corpus)
        if not pair_freqs:
            break
        
        best_pair = max(pair_freqs, key=pair_freqs.get)
        print(f"Most frequent pair: {best_pair} -> {pair_freqs[best_pair]} times")

        corpus = merge_most_frequent_pair(corpus, best_pair)
        print(f"Corpus after merge {i+1}: {corpus}")

def main():
    print("Running BPE from scratch...")
    byte_pair_encoding(num_merges=100)  

if __name__ == "__main__":