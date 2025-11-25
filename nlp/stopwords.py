# what are stopwords in NLP?
# Stopwords are commonly used words in a language that carry minimal meaning and are often filtered out
# during natural language processing (NLP) tasks. These words are considered to be of little value in
# understanding the context or content of a text, as they do not contribute significantly to the overall meaning.
# Examples of stopwords in English include "is," "the," "and," "in," "to," "a," "of," and "that."
# Removing stopwords can help reduce noise in text data and improve the efficiency of NLP algorithms by focusing on more meaningful
# words that carry important information.
# eg : "The cat is sitting on the mat." -> after removing stopwords -> "cat sitting mat"


import nltk
from nltk.stem import PorterStemmer,SnowballStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")

stop_words = set(stopwords.words("english"))
porterStemmer = PorterStemmer()
snowballStemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()

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


filtered_words = [word for word in abdul_kalam_speech.split() if word.lower() not in stop_words]

# print(filtered_words)

stemmed_speech = " ".join([ snowballStemmer.stem(word) for word in filtered_words ])
# stemmed_speech = " ".join([ porterStemmer.stem(word) for word in filtered_words ])
lemmetized_speech = " ".join([lemmatizer.lemmatize(word , 'v') for word in filtered_words])
print(stemmed_speech)
print("------------------------------------------------------")
print(lemmetized_speech)


