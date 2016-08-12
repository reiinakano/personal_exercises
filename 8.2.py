def find_number_of_paths(N, i=0, j=0): # find number of paths for an NxN grid starting from coordinates (i,j)
    paths = 0
    if i == N-1 and j == N-1:
        return 1

    if i < N-1:
        paths += find_number_of_paths(N, i+1, j)

    if j < N-1:
        paths += find_number_of_paths(N, i, j+1)

    return paths


if __name__ == "__main__":
    for i in range(13):
        print "A/An " + str(i+1) + "x" + str(i+1) + " grid has " + str(find_number_of_paths(i+1)) + " total path/s."