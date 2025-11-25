# what is stemming in NLP?
# Stemming is the process of reducing words to their root or base form.
# eg: "running", "runner", "ran" -> "run" => run is stem
#      "going", "goes", "gone" -> "go" => go is stem 
#  by using stemming we can reduce the no of vectors in our text data


from nltk.stem import PorterStemmer
from nltk.stem import RegexpStemmer
from nltk.stem import SnowballStemmer # better than porter stemmer for some languages
words = ["running", "runner", "ran", "easily", "fairly", "going", "goes", "gone" , "programming", "programmer", 
         "programmed", "happiness", "happy", "happily","eat","eating","eaten"]

porterStemmer = PorterStemmer()
regexpStemmer = RegexpStemmer('ing$|s$|e$|able$')
snowballStemmer = SnowballStemmer("english")
# 'ing$'   # Matches "ing" at the END → "eating" → "eat"
# '^ing'   # Matches "ing" at the START → "ingredients" → "redients"  
# 'ing'    # Matches "ing" ANYWHERE (first occurrence)
# '^ing$'  # Matches ONLY the word "ing" (entire string is just "ing")


for word in words:
    stemmed_word = porterStemmer.stem(word)
    # print(f"Original word: {word} --> Stemmed word: {stemmed_word}")


stemmed  = regexpStemmer.stem("ingsssssshwoeifh")

ing = "ing ping singing bringing"
stemmed_ing = regexpStemmer.stem(ing)



# words = porterStemmer.stem(ing).split()
# stemmed_words = [regexpStemmer.stem(word) for word in words]
# print(f"Stemmed word for {ing} using RegexpStemmer: {stemmed_words}") # prints: ['', 'p', 'sing', 'bring']


for word in words:
    pass
    # print(f" Snowball Stemmed word: {snowballStemmer.stem(word)} porterStemmer Stemmed word: {porterStemmer.stem(word)} ")
    
    
words2 = ["goes", "go"]
    
for word in words2:
    print(f" Snowball Stemmed word: {snowballStemmer.stem(word)} porterStemmer Stemmed word: {porterStemmer.stem(word)} ")

