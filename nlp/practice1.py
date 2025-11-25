import nltk
from nltk.stem import PorterStemmer,  RegexpStemmer, SnowballStemmer,WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.chunk import ne_chunk # named entity recognition
from nltk.tokenize import sent_tokenize,word_tokenize # converts paragraph to sentences, words
from nltk.tag import pos_tag


review1 = "This product is great! I loved it and will buy it again."
review2 = "Terrible experience. The product broke after one use and customer service was unhelpful."
review3 = "Average quality, nothing special. It works as expected but doesn't exceed my expectations."



#

regexpStemmer = RegexpStemmer("ing$|s$,is$") # Removes: ing, s, is from end of words
porterStemmer = PorterStemmer() # Applies linguistic rules like: SSES → SS (caresses → caress) relational → relate
snowBallStemmer = SnowballStemmer("english") # better than porterStemmer and regexpStemmer and more accurate
lemmatizer = WordNetLemmatizer()
unique_stopwords = set ( stopwords.words("english"))

words = "ing ping singing bringing"
# regexed_word = [ regexpStemmer.stem(word) for word in words.split(" ")  ]
# print(regexed_word)


# port_stemmed = [ porterStemmer.stem(word) for word in words.split()  ]
# print(port_stemmed)

# snow_stemmed = [ snowBallStemmer.stem(word) for word in words.split()]
# print(snow_stemmed)



# ...existing code...

lemmatization_demo = """
The runner was running fastest among all runners in the race. 
Children were playing happily while their parents watched them carefully. 
The studies showed that better results came from studying consistently. 
Geese flew over the beautiful lakes while wolves were hunting nearby. 
She went to multiple cities and saw many mice in the old buildings. 
The cacti were growing well, and the fungi appeared on the leaves.
"""

# Tokenize and lemmatize
tokenized_word = word_tokenize(lemmatization_demo)
lemmatized = [lemmatizer.lemmatize(word) for word in tokenized_word]

tokenized_words = word_tokenize(lemmatization_demo)
tokkenized_senetences = sent_tokenize(lemmatization_demo)

# print(tokenized_words)
# for sentence in tokkenized_senetences:
#     print(sentence)
    
# lemmetized_words = [  lemmatizer.lemmatize(word, pos="v") for word in tokenized_words ]  
# print(lemmatization_demo , " original text")
# print(lemmetized_words, "lemmatized words")



essay = """
The quick brown fox jumps over the lazy dog in the park. 
It is a beautiful day and the sun is shining brightly. 
I am going to the store because I need to buy some groceries. 
She was very happy when she got the job offer from the company. 
They are planning to travel around the world next year. 
We should not waste our time on things that do not matter. 
He has been working on this project for the last three months. 
Is this the best way to solve the problem or should we try something else?
"""

# stopword are the commonly used words in a language that carry minimal meaning and are often filtered out during 
# natural language processing (NLP) tasks.eg: is, the, and , in , to , a , of , that

# eassy_without_stopwords = " ".join([word for word in essay.split() if word.lower() not in unique_stopwords])

# print(eassy_without_stopwords, " essay without stopwords")


# parts_of_speech  (pos_tag )

pos_demo = """
The brilliant scientist quickly discovered a revolutionary cure. 
John runs faster than anyone in his team. 
She has been teaching English at the university for ten years.
The old man was sitting quietly and reading his favorite book.
They will have completed the amazing project by tomorrow.
"""
# NN - Noun eg: cat, dog, city
# VB - Verb     eg: run, eat, is
# JJ - Adjective eg: beautiful, quick
# RB - Adverb    eg: quickly, silently
# DT - Determiner  eg: the, a, an
# IN - Preposition  eg: in, on, at
# PRP - Pronoun     eg  : he, she, they
# CC - Conjunction   eg : and, but, or


# pos_tagged = pos_tag(word_tokenize(pos_demo))

# print(pos_tagged," pos tagged demo")


# named_entities = ne_chunk(pos_tagged)

# for chunk in named_entities:
#     if hasattr(chunk, 'label'):
#         print(f"{' '.join(c[0] for c in chunk)} --> {chunk.label()}")


nums = [8,12,10,10,21,7,27,12,7,18,20,10,20]
sum_nums = 0
for num in nums:
    sum_nums += num
    
print(sum_nums / 60 , " sum of nums")