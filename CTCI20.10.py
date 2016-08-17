# I used recursion to solve this problem. Using iteration seems more appropriate though. Python hits recursion limit for some
# five letter words and most six letter words.
# I have an iterative version of this code. It's much better.
import enchant
import string

def change_nth_index_in_string(word, index, character):
    dummy = list(word)
    dummy[index] = character
    return "".join(dummy)


def convert_word(original, target, dictionary, path_so_far="", used_words={}, previously_changed_index=-1):
    used_words[original] = True
    if len(original) != len(target):
        return "lengths not the same"
    if original == target:
        return path_so_far + target

    index = 0
    for char1, char2 in zip(original, target):
        if char1 != char2:
            dummy = change_nth_index_in_string(original, index, char2)
            if dictionary.check(dummy) and dummy not in used_words:
                valid_path = convert_word(dummy, target, dictionary, path_so_far + original + " ", used_words, index)
                if valid_path is not None:
                    return valid_path
        index += 1

    index = 0
    for char1, char2 in zip(original, target):
        if char1 != char2 and index != previously_changed_index:
            for letter in string.ascii_lowercase:
                dummy = change_nth_index_in_string(original, index, letter)
                if dictionary.check(dummy) and dummy not in used_words:
                    valid_path = convert_word(dummy, target, dictionary, path_so_far + original + " ", used_words, index)
                    if valid_path is not None:
                        return valid_path
        index += 1

    index = 0
    for char in original:
        if index != previously_changed_index:
            for letter in string.ascii_lowercase:
                dummy = change_nth_index_in_string(original, index, letter)
                if dictionary.check(dummy) and dummy not in used_words:
                    valid_path = convert_word(dummy, target, dictionary, path_so_far + original + " ", used_words, index)
                    if valid_path is not None:
                        return valid_path
        index += 1


    return None


if __name__ == "__main__":
    d = enchant.Dict("en_US")
    print convert_word("candy", "sweet", d)