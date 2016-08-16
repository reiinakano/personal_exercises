def compute_trailing_zeros(n):
    number_of_twos = 0
    number_of_fives = 0
    if n < 0: return "Invalid"
    elif n == 0: return 0
    for factor in xrange(1,n+1):
        current = factor
        while current % 2 == 0:
            current /= 2
            number_of_twos += 1
        while current % 5 == 0:
            current/= 5
            number_of_fives += 1
    return min(number_of_fives, number_of_twos)


if __name__ == "__main__":
    n = 512
    print "The number of trailing zeros in " + str(n) + "! is " + str(compute_trailing_zeros(n))
