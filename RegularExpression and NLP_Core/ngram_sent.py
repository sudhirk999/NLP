import random
import nltk
# Sample data
text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

n = 3

ngram = {}
words = nltk.word_tokenize(text)
# Create N-Gram
for i in range(len(words)-n):
    gram = ' '.join(words[i:i+n])
    if gram not in ngram.keys():
        ngram[gram] = []
    ngram[gram].append(words[i+n])
    
# Testing N-Gram
current_gram = ' ' .join(words[0:n])
result = current_gram
for i in range(30):
    if current_gram not in ngram.keys():
        break
    possibility = ngram[current_gram]
    next_gram = possibility[random.randrange(len(possibility))]
    result += ' ' + next_gram
    rwords = nltk.word_tokenize(result)
    current_gram = ' '.join(rwords[len(rwords)-n:len(rwords)])
print(result)