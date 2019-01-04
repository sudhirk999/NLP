import nltk

paragraph = 'The Taj Mahal was bulit by Emperor Shah Jahan'

words = nltk.word_tokenize(paragraph)

tagged_word = nltk.pos_tag(words)

namesEnt = nltk.ne_chunk(tagged_word)
namesEnt.draw()