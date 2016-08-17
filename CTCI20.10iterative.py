import enchant
import string
from collections import deque

class WordNode:
    def __init__(self, word, parent):
        self.word = word
        self.parent = parent


def change_nth_index_in_string(word, index, character):
    dummy = list(word)
    dummy[index] = character
    return "".join(dummy)


def get_word_modifications(word):
    for index, char in enumerate(word):
        for letter in string.ascii_lowercase:
            if letter != char:
                yield change_nth_index_in_string(word, index, letter)


def convert_word(original, target, dictionary, words_used={}):
    if len(original) != len(target):
        return "Error"
    q = deque([WordNode(original, None)])
    words_used[original] = True
    while q:
        current = q.popleft()
        if current.word == target:
            to_return = ""
            while True:
                to_return += " " + current.word
                current = current.parent
                if not current:
                    break
            to_return = " ".join(reversed(to_return.split(" ")))
            return to_return  # Change this obviously
        for word in get_word_modifications(current.word):
            if dictionary.check(word) and word not in words_used:
                q.append(WordNode(word, current))
                words_used[word] = True
    return "nay"


if __name__ == "__main__":
    d = enchant.Dict("en_US")
    print convert_word("cheap", "quick", d)


# Can I just say I love playing with this algorithm
