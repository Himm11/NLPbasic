import pandas as pd
import matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud
import string
import collections
import nltk
import numpy as np

# reading data
df = pd.read_csv('KimNamjoonUNspeech.txt', sep=' ')

f=df['Speech']

#converting to string
f=f.to_string()
print(f)

#convert to lowercase
print("lowercase conversion")
f=f.lower()

f=f.split()

print(f)

#stop-word removal : removing frequently occuring words
stopwords = nltk.corpus.stopwords.words('english')

def remove_stopwords(text):
    output= [i for i in text if i not in stopwords]
    return output

print("After removing stopwords:")
f=remove_stopwords(f)
print(f)


#Creating list of words with their frequencies
text = collections.Counter(f)
most_words=text.most_common(10)
print(most_words)

words=[]
for i in range(10):
    words.append(most_words[i][0])

#converting list to string
def listToString(s):
    str1 = ""

    for i in s:
        str1 += i + " "

    return str1

text=listToString(words)

# Creating word_cloud
wordcloud = WordCloud(width=800, height=800,background_color='white').generate(text)

# plot the WordCloud image
plt.imshow(wordcloud)
plt.axis("off")
plt.show()




"""
#creating word cloud
word_cloud = WordCloud(collocations = False, background_color = 'white').generate(most_words)
# Display the generated Word Cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()  """


