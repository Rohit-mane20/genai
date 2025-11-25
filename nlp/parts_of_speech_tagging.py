# what is parts of speech tagging in NLP?
# Parts of Speech (POS) tagging is the process of assigning grammatical categories to words
# in a sentence, such as nouns, verbs, adjectives, adverbs, etc. This helps in understanding the
# syntactic structure and meaning of the text. POS tagging is essential for various NLP tasks like
# information extraction, machine translation, and sentiment analysis. 

# most common POS tags
# NN - Noun, singular or mass
# NNS - Noun, plural
# NNP - Proper noun, singular (eg. John, London)
# NNPS - Proper noun, plural (eg. Americans, Londons)
# VB - Verb, base form (eg. go, eat)
# VBD - Verb, past tense (eg. went, ate)


import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
nltk.download('averaged_perceptron_tagger_eng')
unique_stopwords = set(stopwords.words("english"))

abdul_kalam_speech = """My dear brothers and sisters, I am happy to join you today in your celebrations marking the 14th anniversary of
the founding of this esteemed institution. At the outset, I congratulate the management, faculty, staff, and students of this institution for their dedication
and commitment to excellence in education. Education is the most powerful weapon which you can use to change the world. It is through education that we can empower individuals, uplift communities, and transform nations.
As students, you are the torchbearers of our nation's future. You have the potential to shape the destiny of our country through your knowledge, skills, and values.
I urge you to embrace the spirit of learning with enthusiasm and curiosity. Seek knowledge not only from textbooks but also from experiences, interactions, and the world around you. Be open to new ideas, challenge conventional wisdom, and strive for innovation.
In your pursuit of knowledge, remember that education is not just about acquiring degrees or certifications. It is about developing a holistic understanding of the world, cultivating critical thinking skills, and nurturing a sense of social responsibility.
As you embark on your educational journey, I encourage you to set high goals for yourselves. Dream big, work hard, and persevere in the face of challenges. Success is not achieved overnight; it requires dedication, discipline, and a relentless pursuit of excellence.
I also urge you to be compassionate and empathetic individuals. Use your education to make a positive impact on society. Be mindful of the needs of others and contribute to the betterment of your communities. Remember that true success is measured not only by personal achievements but also by the positive difference you make in the lives of others.
In conclusion, I would like to reiterate the importance of education in shaping a brighter future for our nation. Embrace the opportunities that education provides, and use your knowledge and skills to build a better world for yourselves and for generations to come.
Thank you, and may you all have a successful and fulfilling educational journey ahead."""


words = ([ word for word in abdul_kalam_speech.split(" ") if word.lower() not in unique_stopwords])

pos_tags = nltk.pos_tag(words)

print(pos_tags)