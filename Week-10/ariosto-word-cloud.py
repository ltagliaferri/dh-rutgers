import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud

# This text needs to be in the same directory as this Python file
text = open('orlando-furioso.txt').read()

# Add official NLTK stopwords
officialstopwords = stopwords.words('italian')

# Add stopwords related to the text in question that you want to pull out
additionalstopwords = [
    "de", "né", "quel", "—", "sì", "poi", "avea", "re", "gran", "for", 
    "così", "ben", "or", "mai", "quando", "tanto", "già", "ch", "ch'io", 
    "lor", "far", "altri", "fin", "ogni", "chio", "pur" "fe", "molto", 
    "esser", "qual", "tutta", "tal", "prima", "dì", "chin", "ella", 
    "par", "là", " ", "ove", "l'alto", "parte", "ancor", "sé", "qui", 
    "senza", ",", "'", "?", "(", ")", ":", ";", "."
    ]

# Combine official stopwords with your stopwords
allstopwords = officialstopwords + additionalstopwords

# Word Cloud attributes
wc = WordCloud(
         width=600, height=300,
         background_color="white",
         max_words=5000,
         stopwords=allstopwords,
         max_font_size=60,
         min_font_size=6,
         random_state=80
         )

# Generate Word Cloud
wc.generate(text)

# Show Word Cloud
plt.figure(figsize=(20,10))
plt.imshow(wc)
plt.axis("off")
plt.show()
