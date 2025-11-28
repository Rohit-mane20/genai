import pandas as pd
import re
import nltk
from nltk.stem import PorterStemmer 
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()


sms_spam_data = """
label,message
ham,Hey there! How are you doing today?
spam,Congratulations! You've won a $1000 Walmart gift card. Click here to claim your prize.
ham,Don't forget our meeting tomorrow at 10 AM.
spam,Get cheap meds now!!! Limited time offer, buy one get one free.
ham,Can you send me the report by tonight?
spam,You have been selected for a free vacation to Bahamas! Call now.
ham,Let's grab lunch this weekend.
spam,Win a brand new car! Text WIN to 12345 now. 
ham,Happy birthday! Wishing you a wonderful day filled with joy.
spam,Exclusive deal just for you! 50% off on all electronics. Shop now.
"""

corpus = []
for index, line in enumerate(sms_spam_data.split("\n")):
    if "," not in line or index < 2:
        continue
    label, message = line.split(',', 1)
    message = re.sub('[^a-zA-Z]', ' ', message).lower().split()
    message = [ ps.stem(word) for word in message if word not in stop_words ]
    message = " ".join(message)  
    corpus.append(message)

print(corpus)