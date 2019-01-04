from nltk.corpus import wordnet

synonyms = []
antonyms = []

wordnet.synsets('good')
for sys in wordnet.synsets('good'):
    for s in sys.lemmas():
        synonyms.append(s.name())
        for a in s.antonyms():
            antonyms.append(a.name())
            
print(set(synonyms))
print(set(antonyms))