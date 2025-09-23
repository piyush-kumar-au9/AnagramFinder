# optimized solution

from collections import defaultdict
import time


def find_anagrams(filepath="anagram.txt"):
    """Return a list of anagram words from *filepath* and print execution time."""
    start_time = time.time()
    try:
        with open(filepath) as fileobj:
            words = fileobj.read().splitlines()
    except FileNotFoundError as e:
        print(e)
        return []

    # Group words based on their lengths using defaultdict(list)
    word_groups = defaultdict(list)
    for word in words:
        word_groups[len(word)].append(word)

    # Find anagram words using a dictionary
    anagram_words = []
    anagram_dict = defaultdict(list)
    for word in words:
        sorted_word = "".join(sorted(word))
        anagram_dict[sorted_word].append(word)

    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            anagram_words.extend(anagrams)

    # print(anagram_words)
    print(time.time() - start_time)
    return anagram_words


if __name__ == "__main__":
    find_anagrams()
