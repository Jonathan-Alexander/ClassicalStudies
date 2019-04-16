import pandas as pd
import numpy as np
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

def clean(text):
    # Convert to lowercase
    text = text.lower()
    # Remove numbers
    clean_text = ''.join([i for i in text if not i.isdigit()])
    # Remove punctuation
    clean_text = clean_text.translate(str.maketrans('', '', string.punctuation))
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(clean_text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]    
    clean_text = ' '.join(filtered_sentence)
    # Remove stemwords
    # porter = PorterStemmer()
    # word_tokens = word_tokenize(clean_text)
    # return ' '.join([porter.stem(word) for word in word_tokens])
    return clean_text



if __name__ == "__main__":
    df = pd.read_csv('full-data.csv')
    df["clean"] = df["Text"].map(lambda r: clean(r))
    df.to_csv('full-data-clean.csv')
    # print(df["Text"][0])
    # print("\n\n\n\n\n")
    # print(df["clean"][0])
