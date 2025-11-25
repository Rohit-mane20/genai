# what is lemmatization
# Lemmatization is the process of reducing a word to its base or dictionary form, known as the lemma. 
# Unlike stemming, which simply trims word endings, lemmatization considers the context and meaning of the word
# to ensure that the root form is a valid word in the language. 
# For example, the words "running," "ran," and "runs" would all be lemmatized to "run." 
# This process often involves using a vocabulary and morphological analysis of words.

# NLTK provides the WordNetLemmatizer class which is a thin wrapper around the WordNet database.

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')


lemmetizer = WordNetLemmatizer()

words = ["running", "runner", "ran", "easily", "fairly", "going", "goes", "gone" , "programming", "programmer", 
         "programmed", "happiness", "happy", "happily","eat","eating","eaten"]

for word in words:
    print(f" lemmatized word  {lemmetizer.lemmatize(word, 'v')} ")
    # 'v' indicates that we are lemmatizing verbs(Verb describes an action or a state of being) eg: run, eat, go
    # 'n' indicates nouns (nouns are words that represent people, places, things, or ideas) eg: cat, city, happiness
    # 'a' indicates adjectives (adjectives are words that describe or modify nouns) eg: happy, sad, large
    # 'r' indicates adverbs (adverbs are words that modify verbs, adjectives, or other adverbs) eg: quickly, very, well)
    
