# what is bag of words?
# Bag of Words (BoW) is a simple and commonly used technique in natural language processing
# to represent text data. In this model, a text (such as a sentence or a document) is represented as a
# "bag" (multiset) of its words, disregarding grammar and word order but keeping multiplicity.
# The main idea is to create a vocabulary of unique words from the text corpus and then
# represent each document as a vector indicating the presence or absence (or frequency) of each word in the vocabulary.

from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
review1 = "the food is good"
review2 = "the food is bad"
review3  = "pizza is amazing"

vocubulary = set(review1.split() + review2.split() + review3.split())
vocubulary = list(vocubulary)
vocubulary = [word.lower() for word in vocubulary if word not in stop_words] 

print(stop_words.__contains__("is"), 'is')
print(stop_words.__contains__("the"), 'the')


frequency_vectors = [
    [
        review1.lower().split().count(word) if word not in stop_words else 0
        for word in vocubulary
    ],
    [
        review2.lower().split().count(word) if word not in stop_words else 0
        for word in vocubulary
    ],
    [
        review3.lower().split().count(word) if word not in stop_words else 0
        for word in vocubulary
    ],
]
print("Vocabulary:", vocubulary)
print("Bag of Words Frequency Vectors:")
print(frequency_vectors)
