import numpy
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# Initialize a list to collect all the words in a text file
allwords = []

# Add official stopwords from NLTK
officialstopwords = stopwords.words('italian')

# Add stopwords that you don't want to count
additionalstopwords = [
    "de", "né", "quel", "—", "sì", "poi", "avea", "re", "gran", 
    "for", "così", "ben", "or", "mai", "quando", "tanto", "già", 
    "ch", "ch'io", "lor", "far", "altri", "fin", "ogni", "chio", 
    "pur" "fe", "molto", "esser", "qual", "tutta", "tal", 
    "prima", "dì", "chin", "ella", "par", "là", " ", "ove", 
    "l'alto", "parte", "ancor", "sé", "qui", "senza", ",", "'", 
    "?", "(", ")", ":", ";", "."
    ]

# Combine stop words
allstopwords = officialstopwords + additionalstopwords

# Comment back in if you want to check that your stopwords are looking good!
# print(stopwords[:10])

# Open the text file and read line by line
with open('orlando-furioso.txt') as input:
    book_lines = input.readlines()

# Comment back in if you want to check that it's reading the lines from your file
# print(book_lines[:10])

# Isolate the words from the lines, make them lower case, make sure they're not a stopword
for line in book_lines:
    words = word_tokenize(line)
    for w in words:
        w = w.lower()
        if w not in allstopwords:
            allwords.append(w)

# Comment back in if you want to check that the words are tokenized
# print(allwords[:10])

# Make a chart!
freqdist = nltk.FreqDist(allwords)
plt.figure(figsize=(16,5))
freqdist.plot(50)
