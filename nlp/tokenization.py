import nltk
from nltk.tokenize import sent_tokenize,word_tokenize # converts paragraph to sentences, words  


# Download required NLTK data
nltk.download('punkt_tab')

corpus = """This is a sample paragraph.
It contains multiple sentences. 
Each sentence will be treated as a document."""

tokenized = sent_tokenize(corpus)

for index, sentence in enumerate(tokenized):
    pass
    # print(f" index: {index} sentence: {sentence} ")
    

# convert paragraph to words

tokenized_words = word_tokenize(corpus)

for index, word in enumerate(tokenized_words):
    print(f" index: {index} word: {word} ")