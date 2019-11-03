import utils
from wordcloud import WordCloud
import matplotlib.pyplot as plt

BOOK_DIR = "./bnw"
PREFIX = "bnw_"
CLOUD_DIR = "./clouds"

def main():
    number_of_chapters = utils.get_number_of_chapters(BOOK_DIR)
    chapters = []
    for i in range(number_of_chapters):
        chapter = utils.get_wordlist_from_file(f'{BOOK_DIR}/{PREFIX}{i+1}.txt')
        chapter = utils.translate_words(chapter)
        chapter = utils.tokenize_words(chapter)
        chapter = utils.lower_words(chapter)
        chapter = utils.filter_stopwords(chapter)
        chapter = utils.stem_words(chapter)
        chapters.append(chapter)
    
    tf_idfs = [[(word, utils.compute_tf_idf(word, chapter, chapters)) for word in set(chapter)] for chapter in chapters]
    tf_idfs = [dict(chapter) for chapter in tf_idfs]

    for i, tfs in enumerate(tf_idfs):
        wordcloud = WordCloud().generate_from_frequencies(tfs)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig(f'{CLOUD_DIR}/{PREFIX}{i+1}.jpg')
        # plt.show()

    book = [word for word in chapter for chapter in chapters]
    book_tf_idfs  = dict([(word, utils.compute_tf_idf(word, book, book)) for word in set(book)])
    wordcloud = WordCloud().generate_from_frequencies(book_tf_idfs)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(f'{CLOUD_DIR}/{PREFIX}book.jpg')

if __name__ == "__main__":
    main()