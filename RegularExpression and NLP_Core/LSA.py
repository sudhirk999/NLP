from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import nltk
# Sample Data
dataset = ["The amount of polution is increasing day by day",
           "The concert was just great",
           "I love to see Gordon Ramsay cook",
           "Google is introducing a new technology",
           "AI Robots are examples of great technology present today",
           "All of us were singing in the concert",
           "We have launch campaigns to stop pollution and global warming"]

dataset = [words.lower() for words in dataset]

vectorizer = TfidfVectorizer() ## Converts the data into tfidf formate
X = vectorizer.fit_transform(dataset)

print(X[0])

lsa = TruncatedSVD(n_components = 4, n_iter = 100) # different components are formed
lsa.fit(X)

row1 = lsa.components_[0]
row2 = lsa.components_[1]

terms = vectorizer.get_feature_names()

concept_words = {}

for i,comp in enumerate(lsa.components_):
    component_terms = zip(terms,comp)
    sorted_terms = sorted(component_terms, key= lambda x:x[1], reverse=True)
    sorted_terms = sorted_terms[:10]
    concept_words['Component '+str(i)] = sorted_terms
    
for key in concept_words.keys():
    sentence_scores = []
    for data in dataset:
        words = nltk.word_tokenize(data)
        score = 0
        for word in words:
            for word_with_score in concept_words[key]:
                if word == word_with_score[0]:
                    score += word_with_score[1]
        sentence_scores.append(score)
    print('\n'+key+':')
    for sentence_score in sentence_scores:
        print(sentence_score)
    
    
    
    
    
    
    
    
    
    
    
    
    