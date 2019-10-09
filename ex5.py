from collections import Counter
from nltk.corpus import stopwords
import re
import string
stopw = stopwords.words('english')
with open("bnw_1.txt") as f:
    with open("stop_words.txt") as stop:
        stopwords = [word for line in stop for word in line.split()]
        words = [ word.lower().translate(str.maketrans("", "",string.punctuation)) for line in f for word in line.split()]
        filtered = [word for word in words if not word in stopwords]
        filtered2 = [word for word in words if not word in stopw]
        print(Counter(filtered).most_common(10))
        print(Counter(filtered2).most_common(10))
