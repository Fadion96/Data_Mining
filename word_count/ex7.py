import utils

BOOK_DIR = "./bnw"
PREFIX = "bnw_"

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
    print(utils.sort_by_tf_idf("boy", chapters))

if __name__ == "__main__":
    main()