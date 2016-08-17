def largest_sum(sequence):
    current_largest = 0
    current_sequence_sum = 0
    for i in sequence:
        current_sequence_sum += i
        if current_sequence_sum > current_largest:
            current_largest = current_sequence_sum
        if current_sequence_sum < 0:
            current_sequence_sum = 0
    return current_largest


if __name__ == "__main__":
    print largest_sum([-1, 0, -1, 5, -2, 33, -14, -2, 2])
