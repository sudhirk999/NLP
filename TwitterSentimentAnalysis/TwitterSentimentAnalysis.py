import re
import numpy as np
import pickle
import matplotlib.pyplot as plt
import tweepy
from tweepy import OAuthHandler

# Initializing the keys
consumer_key = 'KH466ruzj0tO5DPFtVaoOg18x'
consumer_secret = 'CTotNaBVeoh0HHhjBULGxiA8WrWq6xokWK8uNsv7PsprCGJ6na'
access_token = '3501410834-uiXhzdFeSiAuRyUmMnWB1zgvNxOhNoHUcH4NiVU'
access_secret = '01Yr7tU8FHdwc9E68KoUit6KFJXdbNPim3IzcDVJoXgTB'

# Initializing the token
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

args = ['tesla']
api = tweepy.API(auth_handler=auth,timeout=10)

# Fetching the tweets
list_tweets = []

query = args[0] # 0 for indexing the first argument if there were more than 1 argument to be searched

if len(args) == 1:
    for status in tweepy.Cursor(api.search, q=query+' -filter:retweets', lang='en', result_type='recent',).items(100):
        list_tweets.append(status.text) # Status is the jason file

with open('tfidfmodel.pickle','rb') as f:
    vectorizer = pickle.load(f)
    

with open('classifier.pickle','rb') as f:
    cls = pickle.load(f)

pos_count = 0
neg_count = 0

# Preprocessing the tweets
for tweet in list_tweets:
    tweet = re.sub(r'^https://t.co/[a-zA-Z0-9]*\s',' ', tweet)
    tweet = re.sub(r'\s+https://t.co/[a-zA-Z0-9]*\s',' ', tweet)
    tweet = re.sub(r'\s+https://t.co/[a-zA-Z0-9]*$',' ', tweet)
    tweet = tweet.lower()
    tweet = re.sub(r"wasn't","was not", tweet)
    tweet = re.sub(r"wouldn't","would not", tweet)
    tweet = re.sub(r"isn't","is not", tweet)
    tweet = re.sub(r"won't","will not", tweet)
    tweet = re.sub(r"should't","should not", tweet)
    tweet = re.sub(r"could't","could not", tweet)
    tweet = re.sub(r"can't","cann not", tweet)
    tweet = re.sub(r"he's","he is", tweet)
    tweet = re.sub(r"she's","she is", tweet)
    tweet = re.sub(r"they're","they are", tweet)
    tweet = re.sub(r"who're","who are", tweet)
    tweet = re.sub(r"i'm","i am", tweet)
    tweet = re.sub(r"that's","that is", tweet)
    tweet = re.sub(r"who's","who is", tweet)
    tweet = re.sub(r"what's","what is", tweet)
    tweet = re.sub(r"where's","where is", tweet)
    tweet = re.sub(r"there's","there is", tweet)
    tweet = re.sub(r"it's","it is", tweet)
    tweet = re.sub(r'\W',' ',tweet)
    tweet = re.sub(r'\d',' ',tweet)
    tweet = re.sub(r'\s+[a-z]\s+',' ', tweet)
    tweet = re.sub(r'^[a-z]\s+',' ', tweet)
    tweet = re.sub(r'\s+[a-z]$',' ', tweet)
    tweet = re.sub(r'\s+',' ', tweet)
    sent = cls.predict(vectorizer.transform([tweet]).toarray())
    if sent[0] == 1:
        pos_count += 1
    else:
        neg_count += 1
        
# Visualizing the results
objects = ['Positive',"Negative"]
y_pos = np.arange(len(objects))

plt.bar(y_pos,[pos_count,neg_count],alpha=0.5)
plt.xticks(y_pos,objects)
plt.ylabel('Number')
plt.title('Number of Positive and Negative Tweets')
plt.show()