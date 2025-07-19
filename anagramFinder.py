from collections import defaultdict
import time
import sys


def load_words(path):
    """Return list of words read from the given file."""
    with open(path) as f:
        return f.read().splitlines()


def find_anagrams(words):
    """Return a list containing words that have at least one anagram."""
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return [w for grp in groups.values() if len(grp) > 1 for w in grp]


def main():
    start_time = time.time()
    try:
        words = load_words("anagram.txt")
    except FileNotFoundError as err:
        print(err)
        return 1

    anagram_words = find_anagrams(words)
    # print(anagram_words)
    print(time.time() - start_time)
    return 0


if __name__ == "__main__":
    sys.exit(main())
