def find_twos_between_one_to_N(N):
    upper = 10
    lower = 1
    num = 0
    while N/lower > 0:
        num += N/(upper) * (lower)
        if N % (upper) >= 2*(lower):
            num += min(lower, N%upper-(2*lower-1))
        lower = upper
        upper *= 10
    return num


if __name__ == "__main__":
    i = 514
    print "The number of 2's from 1 to " + str(i) + " is " + str(find_twos_between_one_to_N(i))


# This is if we only need to access this function a few times for large values.
# If we need this function repeatedly we can simply store the calculates results in a hash table and access that.
# Or if we need the values for consecutive values of N, we can make it much more efficient by calculating the value
        # based on the previous answer.