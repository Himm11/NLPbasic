import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

df = pd.read_csv('text1.txt', sep=' ')
cf=pd.read_csv('text2.txt', sep=' ')

d=df['Text1']
c=cf['Text2']

#converting to string
d=d.to_string()
print(d)
c=c.to_string()
print(c)

def text_similarity(text1, text2):
    # Tokenize and lemmatize the texts
    tokens1 = word_tokenize(text1)
    tokens2 = word_tokenize(text2)
    lemmatizer = WordNetLemmatizer()
    tokens1 = [lemmatizer.lemmatize(token) for token in tokens1]
    tokens2 = [lemmatizer.lemmatize(token) for token in tokens2]

    # Remove stopwords
    stop_words = stopwords.words('english')
    tokens1 = [token for token in tokens1 if token not in stop_words]
    tokens2 = [token for token in tokens2 if token not in stop_words]
    print(type(tokens1))
    # Creating the TF-IDF vectors
    vectorizer = TfidfVectorizer()
    vector1 = vectorizer.fit_transform(tokens1)
    vector2 = vectorizer.transform(tokens2)

    # COSINE SIMILARITY
    cos_sim_mat = cosine_similarity(vector1, vector2)
    print("Cosine Similarity matrix:", cos_sim_mat)

    #JACCARD SIMILARITY
    intersection = len(list(set(tokens1).intersection(tokens2)))
    union = (len(tokens1) + len(tokens2)) - intersection
    #calculating jaccardian similirity as intersection of texts
    #upon union of texts
    print("Jaccardian similarity:", float(intersection) / union)



text_similarity(d,c)