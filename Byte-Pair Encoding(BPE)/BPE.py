import pandas as pd 
from tokenizers import Tokenizer, models, trainers, pre_tokenizers


'''using tokenizers lib '''

def tokenize():
    
    tokenizer = Tokenizer(models.BPE())
    tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

    trainer = trainers.BpeTrainer(vocab_size=2000, show_progress=True)

    files = ["ptbdataset\\ptb.train.txt"]
    tokenizer.train(files, trainer)

    print(tokenizer.encode("hello world").tokens)


'''from scratch implementation implementation '''

# extracting the unique words from the corpus 
def get_unique_words_in_file(file_path):
    lines=[]
    unique_words=set()
    
    try:
        with open(file_path ,'r') as file:
            content = file.read()
            
            cleaned_content = content.replace('\n', ' ')
            
            words = cleaned_content.split(" ")
            
            for word in words:
                unique_words.add(word)
       
        return list(unique_words)
        
    except FileNotFoundError:
        print(f"ERORR: file not found at {file_path}")


# function for extracting base vocabulary
def base_vocabulary(unique_words):
    base_vocabulary=set()
    for word in unique_words:
        for char in word:
            base_vocabulary.add(char)
    return base_vocabulary

# character frequency in the file
def char_frequency_in_file(base_vocab, unique_words):
    char_freq={}
    for char in base_vocab:
        char_freq[char]=0
    for words in unique_words:
        for char in words:
            char_freq[char]+=1
    return char_freq
        
# The BPE function  
def byte_pair_encoding():
    
    unique_words = get_unique_words_in_file("ptbdataset//ptp.dummy.txt")
    print(unique_words)
    base_vocab=base_vocabulary(unique_words)
    print(base_vocab)
    freq=char_frequency_in_file(base_vocab, unique_words)
    print(freq)

# Merge the pair to create a new subword unit

 
def merge(unique_words):
    corpus=[]
    for word in unique_words:
        corpus.append(list(word))
    
    
    for list_word in corpus:
        freq_count={}
        for i in range(len(list_word)-1):
            pair=list_word[i]+list_word[i+1]
            if pair in freq_count:
                freq_count[pair]+=1
            else:
                freq_count[pair]=1
    
    max_freq= max(freq_count,key=freq_count.get)
    
    for list_word in corpus:
        if max_freq in list_word:
            pass 
    
                
    
                
            
            
        
    
    

    
def main():
    byte_pair_encoding()
      
if __name__ == "__main__":
    print("check")
    main()
    

