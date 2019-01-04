import nltk
from nltk.corpus import wordnet

sentence = 'I am not happy with the team performance'

words = nltk.word_tokenize(sentence)

new_word = []

temp_word = ''

for word in words:
    antonyms = []
    if word == 'not':
        temp_word = 'not_'
    elif temp_word == 'not_':
        for sys in wordnet.synsets(word):
            for s in sys.lemmas():
                for a in s.antonyms():
                    antonyms.append(a.name())
        if len(antonyms) >= 1:
            word = antonyms[0]
        else:
            word = temp_word + word
        temp_word = ''
    if word != 'not':
        new_word.append(word)

sentence = ' '.join(new_word)
