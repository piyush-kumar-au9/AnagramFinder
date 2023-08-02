# optimized solution

from collections import defaultdict
import time

start_time = time.time()

try:
    with open("anagram.txt") as fileobj:
        words = fileobj.read().splitlines()
except FileNotFoundError as e:
    print(e)

# Group words based on their lengths using defaultdict(list)
word_groups = defaultdict(list)
for word in words:
    word_groups[len(word)].append(word)

# Find anagram words using a dictionary
anagram_words = []
anagram_dict = defaultdict(list)
for word in words:
    sorted_word = ''.join(sorted(word))
    anagram_dict[sorted_word].append(word)

for sorted_word, anagrams in anagram_dict.items():
    if len(anagrams) > 1:
        anagram_words.extend(anagrams)

# print(anagram_words)
print(time.time() - start_time)
