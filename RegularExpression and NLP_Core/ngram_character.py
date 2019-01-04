import random

# Sample data
text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

n = 6

ngram = {}

# Create N-Gram
for i in range(len(text)-n):
    gram = text[i:i+n]
    if gram not in ngram.keys():
        ngram[gram] = []
    ngram[gram].append(text[i+n])
    
# Testing N-Gram
current_gram = text[0:n]
result = current_gram
for i in range(100):
    if current_gram not in ngram.keys():
        break
    possibility = ngram[current_gram]
    next_gram = possibility[random.randrange(len(possibility))]
    result += next_gram
    current_gram = result[len(result)-n:len(result)]
print(result)