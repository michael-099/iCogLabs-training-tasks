def tokenize():
    
#     tokenizer = Tokenizer(models.BPE())
#     tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

#     trainer = trainers.BpeTrainer(vocab_size=2000, show_progress=True)

#     files = ["ptbdataset\ptb.train.txt"]
#     tokenizer.train(files, trainer)

#     print(tokenizer.encode("hello world").tokens)