from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 
import string
import math
import os, os.path

def get_number_of_chapters(dir):
    return len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))])

def get_wordlist_from_file(filename):
    with open(filename) as f:
        words = f.read()
    
        # words = [ word for line in f for word in line.split()]
        return words

def get_wordlist_from_files(dir, prefix):
    nr_chapters = get_number_of_chapters(dir)
    words = ""
    # words =  []
    for i in range(nr_chapters):
        words += get_wordlist_from_file(dir + f'/{prefix}{i+1}.txt')
    return words

def tokenize_words(words):
    return word_tokenize(words)

def translate_words(words):
    # return [word.translate(str.maketrans("", "",string.punctuation)) for word in words]
    return words.translate(str.maketrans("", "",string.punctuation))

def lower_words(words):
    return [word.lower() for word in words]

def filter_stopwords(words):
    stopw = stopwords.words('english')
    return [word for word in words if not word in stopw]

def stem_words(words):
    ps = PorterStemmer() 
    return [ps.stem(word) for word in words]

def count_words(words):
    return Counter(words)

def compute_tf_idf(word, document, documents):
    tf = document.count(word)
    idf = compute_idf(word, documents)
    return tf * idf

def compute_idf(word, documents):
    apperances = sum([1 for document in documents if word in document])
    return math.log(len(documents) /  (1 + apperances))

def sort_by_tf_idf(word, chapters):
    tf_idfs = [(i + 1, compute_tf_idf(word,chapter,chapters)) for i, chapter in enumerate(chapters) ]
    return sorted(tf_idfs, key=lambda tup: tup[1], reverse=True)