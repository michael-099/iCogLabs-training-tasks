import pandas as pd 
from tokenizers import Tokenizer, models, trainers, pre_tokenizers


#  using tokenizers lib
def tokenize():
    
    tokenizer = Tokenizer(models.BPE())
    tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

    trainer = trainers.BpeTrainer(vocab_size=2000, show_progress=True)

    files = ["ptbdataset\ptb.train.txt"]
    tokenizer.train(files, trainer)

    print(tokenizer.encode("hello world").tokens)


# from scratch implementation implementation 

def get_words_in_file(file_path):
    lines=[]
    unique_words=set()
    
    try:
        with open(file_path ,'r') as file:
            content = file.read()
            
            cleaned_content = content.replace('\n', ' ')
            print(cleaned_content)
            
           
            words = cleaned_content.split(" ")
            print(words)
            
            for word in words:
                unique_words.add(word)
        print(unique_words)
            
        print("completed")
        print(len(unique_words))
        return list(unique_words)
        
    except FileNotFoundError:
        print(f"ERORR: file not found at {file_path}")

def base_vocabulary():


words_in_file("ptbdataset/ptp.dummy.txt")

