from wordcloud import WordCloud
import matplotlib.pyplot as plt
import utils

BOOK_DIR = "./bnw"
PREFIX = "bnw_"


def main():
    words = utils.get_wordlist_from_files(BOOK_DIR, PREFIX)
    words = utils.translate_words(words)
    words = utils.tokenize_words(words)
    words = utils.lower_words(words)
    words = utils.filter_stopwords(words)
    words = utils.stem_words(words)
    c_words = utils.count_words(words)
    wordcloud = WordCloud().generate_from_frequencies(c_words)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    main()
