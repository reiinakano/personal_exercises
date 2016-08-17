def find_all_pairs(array, sum):
    my_dict = {}
    for number in array:
        difference = sum - number
        if difference in my_dict:
            for i in range(my_dict[difference]):
                print str(difference) + ", " + str(number)
        if number in my_dict: my_dict[number] += 1
        else: my_dict[number] = 1


if __name__ == "__main__":
    find_all_pairs([1, 4, 2, 4, 25, 34, 33, 2, 1], 67)


# This algorithm finds ALL possible pairs regardless of whether the pair of values has appeared before.
# Example: The pair 1 at index 0, 4 at index 1 AND the pair 1 and index 0, 4 at index 3 will be printed separately.
