import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize


porterStemmer = PorterStemmer()
tfidf = TfidfVectorizer(max_features=100, ngram_range=(2,2))


nltk.download("stopwords")
nltk.download("wordnet")


def preprocess_text(sentence):
    tokens = word_tokenize(sentence.lower())
    filtered_tokens = [ porterStemmer.stem(token)  for token in tokens if token.isalpha() and token not in stop_words ]
    return filtered_tokens

documents = [
    """Congratulations! You've won a $1,000 Walmart gift card. Click here to claim your prize.
    This is not a scam. Act now to secure your winnings.""",
    
    """Limited time offer! Don't miss out on this exclusive deal just for you.
    To claim your gift card, visit our website and enter your details.""",
    
    """Hurry, this offer expires soon! Free money waiting for you.
    Click now to get your reward before it's too late.""",
    
    """Hello, this is a legitimate email from your bank regarding your account.
    Please review your recent transactions and contact us if you notice any issues.""",
    
    """Meeting scheduled for tomorrow at 10 AM. Please bring the project reports.
    We will discuss the quarterly results and future plans."""
]
stop_words = set(stopwords.words("english"))

preprocessed_docs = [ preprocess_text(doc) for doc in documents]
print(preprocessed_docs)
transformed = tfidf.fit_transform([" ".join(doc) for doc in preprocessed_docs])

print(transformed.toarray())
print(tfidf.get_feature_names_out())

