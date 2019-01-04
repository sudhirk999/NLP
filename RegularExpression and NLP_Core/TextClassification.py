import nltk
import re
import numpy as np
from nltk.corpus import stopwords
from sklearn.datasets import load_files
import pickle
nltk.download('stopwords')

# import datasets
reviews = load_files('txt_sentoken/')
X,y = reviews.data, reviews.target

# Picking the data
with open('X.pickle','wb') as f:
    pickle.dump(X,f)
    
with open('y.pickle','wb') as f:
    pickle.dump(y,f)

# Unpickling data
with open('X.pickle','rb') as f:
    pickle.load(f)
    
with open('y.pickle','rb') as f:
    pickle.load(f)
    
# Preprocessing data
corpus = []
for i in range(len(X)):
    review = re.sub(r'\W',' ', str(X[i])).lower()
    review = re.sub(r'\s+[a-z]\s+',' ',review)
    review = re.sub(r'^[a-z]\s+',' ',review)
    review = re.sub(r'\s+',' ',review)
    corpus.append(review)    
    
'''   
# Creating BagOfWord Model
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features=3000, min_df = 4, max_df=0.6,
                             stop_words = stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()

# Creating TFIDF Model using bagOfWord Model
from sklearn.feature_extraction.text import TfidfTransformer
tfidf = TfidfTransformer()
X = tfidf.fit_transform(X).toarray()
'''

# Creating TFIDF model directly
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=2000, min_df=3, max_df=0.6,
                             stop_words = stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()

# Splitting theh data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

# Training the classifier
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train,y_train)

# Testing the model
sent_pred = classifier.predict(X_test)

# Finding the accuracy
from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(y_test,sent_pred)
acc = accuracy_score(y_test,sent_pred)

# Saving the model
 # Saving the classifier
with open('classifier.pickel','wb') as f:
     pickle.dump(classifier,f)
     
 # Saving the tfidf model
with open('tfidfmodel.pickel','wb') as f:
     pickle.dump(vectorizer,f)
     
# Unpickling the vectorizer and classifier
with open('classifier.pickel','rb') as f:
     cls = pickle.load(f)
     
with open('tfidfmodel.pickel','rb') as f:
     tfidf_vect = pickle.load(f)
     
sample = ['I am vey happy from my team, they played realll well..!!!']
sample = tfidf_vect.transform(sample).toarray()
sample_pred = cls.predict(sample)










