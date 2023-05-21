#Lab 3:Spacy Language Processor
#Python code to read a text document and perform basic pre-processing
#techniques on the text like tokenization, stop-word-removal, lemmatization etc.

import pandas as pd
import re
import string
import nltk
nltk.download('wordnet')
df=pd.read_csv('textfileOne.txt', sep=' ')

#textfile
f=df['Title']
print(f)


#converting to string
f=f.to_string()
print(f)


#convert to lowercase
print("lowercase conversion")
f=f.lower()
print(f)

#remove punctuation
print("punctuation removal")
#defining the function to remove punctuation
def remove_punctuation(text):
    punctuation_free="".join([i for i in text if i not in string.punctuation])
    return punctuation_free

nf=remove_punctuation(f)
print(nf)


#tokenization
def tokenization(text):
    tokens = re.split('  ',text)
    return tokens

print("After tokenization")
tf=tokenization(nf)
print(tf)


#stop-word removal : removing frequently occuring words
stopwords = nltk.corpus.stopwords.words('english')
print("Top 10 stopwprds in nltk library")
print(stopwords[0:10])

def remove_stopwords(text):
    output= [i for i in text if i not in stopwords]
    return output

print("After removing stopwords:")
sf=remove_stopwords((tf))
print(sf)


#lemmatization: convert words to root form
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

def lemmatizer(text):
    lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in text]
    return lemm_text

print("After lemmatization")
lf=lemmatizer((sf))
print(lf)


#stemming: removing suffix
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

def stemming(text):
    stem_text = [porter_stemmer.stem(word) for word in text]
    return stem_text

print("After stemming")
stf= stemming(lf)
print(stf)


