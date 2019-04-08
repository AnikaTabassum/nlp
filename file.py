import nltk
import pandas as pd
#nltk.download("punkt")
import string
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

path = 'C:/Users/Anika/Desktop/5thSem/DBMS/aclImdb/test/neg'
token_dict = {}

def uniquewords():
    unique=list()
    with open("C:/Users/Anika/Desktop/5thSem/DBMS/token.txt", "r", encoding="utf8") as f:
        text = f.read()

        if text not in unique:
             unique.append(text.split("\n"))

    #print(len(unique))
    return unique

def count(unique):
    for f in files:
        fname = os.path.join(dirpath, f)
        print("fname=", fname)
        with open(fname, encoding="utf8") as pearl:
            text = pearl.read()
            i =0
            arr=list()
            df = pd.DataFrame(unique)
            for words in unique:
                cnt=0
                #print(words)
                if str(words) in text:
                    cnt+=1
                arr.append(cnt)
            df1=pd.DataFrame(arr,columns=unique)
            df.append(df1)

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems

for dirpath, dirs, files in os.walk(path):
    '''output = open("C:/Users/Anika/Desktop/5thSem/DBMS/newFile.txt", "a+",encoding="utf-8")
    for f in files:
        fname = os.path.join(dirpath, f)
        print ("fname=", fname)
        with open(fname,encoding="utf8") as pearl:
            text = pearl.read()
            output.write(text)
            #print(text)
            token_dict[f] = text.lower().translate(string.punctuation)'''
'''
writ= open("C:/Users/Anika/Desktop/5thSem/DBMS/token.txt","a+",encoding="utf8")
set(stopwords.words('english'))
with open("C:/Users/Anika/Desktop/5thSem/DBMS/newFile.txt", "r",encoding="utf8") as f:
    text= f.read()
    #example_sent = "This is a sample sentence, showing off the stop words filtration."
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    #print(word_tokens)
    #print(filtered_sentence)

    ps = PorterStemmer()
    for w in filtered_sentence:
        #print(ps.stem(w))
        writ.write(ps.stem(w))
        writ.write("\n")
'''

unique=uniquewords()
count(unique)

