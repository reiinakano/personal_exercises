words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]


def find_rotation(words, index=0):
    length = len(words)
    mid = length/2
    if words[0] <= words[mid - 1] and words[mid] <= words[length-1]:
        if words[mid - 1] > words[mid]:
            return mid + index
        else:
            return index
    elif words[0] > words[mid - 1]:
        new = words[:mid]
        return find_rotation(new, index)
    elif words[mid] > words[length-1]:
        new = words[mid:]
        return find_rotation(new, index + mid)


if __name__ == "__main__":
    print find_rotation(words)
