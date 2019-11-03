import utils
import numpy as np
import secrets

BOOK_DIR = "./bnw"
PREFIX = "bnw_"


def main():
    words = utils.get_wordlist_from_files(BOOK_DIR, PREFIX)
    words = utils.translate_words(words)
    words = utils.tokenize_words(words)
    words = utils.lower_words(words)
    words = utils.filter_stopwords(words)
    words = utils.stem_words(words)
    words_set = set(words)
    words_np = np.array(words)
    occurences = dict([(word, np.where(words_np == word)[0]) for word in words_set])
    for a in occurences:
        occurences[a] = [words[i + 1] for i in occurences[a] if i < len(words) - 1]
        occurences[a] = utils.count_words(occurences[a])
        occurences[a] = occurences[a].most_common(5)
        # occurences[a] = occurences[a]
    # print(occurences)
    print(test("linda", 10, occurences))

def test(word, size, occurences):
    sentence = word
    next_w = word
    for _ in range(size):
        next_w = secrets.choice(occurences[next_w])[0]
        sentence += f' {next_w}'
    return sentence
if __name__ == "__main__":
    main()