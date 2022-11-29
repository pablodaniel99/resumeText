import bs4 as bs
import urllib.request
import re
import nltk
import requests
import heapq
from bs4 import BeautifulSoup
from inscriptis import get_text
#import Translator
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize,sent_tokenize
nltk.download('punkt')



link = "https://es.wikipedia.org/wiki/Minas_de_Rodalquilar"
html = urllib.request.urlopen(link).read().decode('utf-8')

text = get_text(html)

entireText = text
entireText = entireText.replace("[ edit ]", "")
print()

entireText = re.sub(r'\s+', ' ', entireText)
entireText = re.sub(r'\[[0-9]*\]', ' ', entireText)

formatted_entireText = re.sub('[^a-zA-Z]', ' ', entireText)
formatted_entireText = re.sub(r'\s+', ' ', formatted_entireText)

#TOKENIZAION DEL TEXTO
sentence_list = nltk.sent_tokenize(entireText)

#FRECUENCIA DE CADA PALABRA
stopwords = set(stopwords.words('spanish'))

word_frecuencies = {}

for word in nltk.word_tokenize(formatted_entireText):
    if word not in stopwords:
        if word not in word_frecuencies.keys():
            word_frecuencies[word] = 1
        else: 
            word_frecuencies[word] += 1


#
maximun_freq = max(word_frecuencies.values())


for word in word_frecuencies.values():
    word_frecuencies[word] = (word_frecuencies[word]/maximun_freq)


sentence_scores = {}

for sent in sentence_list:
    for word in nlkt.word_tokenize(sent.lower()):
        if word in wor_frecuencies.keys():
            if len(sent.split(' ')) < 3:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frecuencies[word]
                else:
                    sentence_scores[sent] += word_frecuencies[word]


summary_sentences = heapq.nlargest(10, sentence_scores, key = sentence_scores.get(key))

summary = ' '.join(summary_sentences)
print(summary)





