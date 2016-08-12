def print_parenthesis_combinations(N, available_opening=None, available_closing=0, so_far=""):
    if available_opening is None:
        available_opening = N
    if available_opening == 0 and available_closing == 0:
        print so_far
    if available_opening > 0:
        print_parenthesis_combinations(N, available_opening-1, available_closing+1, so_far+"(")
    if available_closing > 0:
        print_parenthesis_combinations(N, available_opening, available_closing-1, so_far+")")


if __name__ == "__main__":
    print_parenthesis_combinations(4)