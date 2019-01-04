import re

sentence = 'I was born in the year 1996'
sen1 = ''
sen2 = 'a'
re.match(r'.*',sentence)
re.match(r'.+',sen1)
re.match(r'.+', sentence)
re.match(r'[a-zA-Z]+',sentence)
re.match(r'ab?',sen2)

sent3 = '1996 was the year i was born'
re.match(r'[a-zA-z]+',sent3) # No  match
# Using Search
re.search(r'[a-zA-Z]+',sent3) # was is matched

# Start wiht 
if re.match(r'^1996',sent3):
    print('Match')
    
else: print('No Match')

if re.match(r'^I',sent3):# no match
    print('Match')
    
else: print('No Match')

# Ends with
if re.search(r'born$',sent3):
    print('Match')
    
else: print('No Match')

sent4 = 'I love Avengers'

print(re.sub(r'Avengers', 'Justice League', sent4))

sent4 = 'I love Avengers Avengers'

print(re.sub(r'Avengers', 'Justice League', sent4))

print(re.sub(r'[a-z]','0',sent4))


print(re.sub(r'[a-z]','0',sent4,flags=re.I))


print(re.sub(r'[a-z]','0',sent4, count=5 ,flags=re.I))


sentence1 = 'Welcome to the year 2018'
sentence2 = "Just ~& +++---- arrived at @Jack's place. # fun"
sentence3 = 'I        Love           u'

sentence1_modified = re.sub(r'\d','',sentence1)
sentence1_modified

sentence2_modified = re.sub(r'[~&+-@#\.\']',' ', sentence2)

sentence2_modified = re.sub(r'\w',' ',sentence2) # removes a-zA-Z0-9

sentence2_modified = re.sub(r'\W',' ',sentence2) #removes special symbols

#removing spaces
sentence2_modified = re.sub(r'\s+',' ',sentence2_modified)
# removing unnecessary s
sentence2_modified = re.sub(r'\s+[a-zA-Z]\s+',' ',sentence2_modified)

sentence3_modified = re.sub(r'\s+',' ',sentence3)








