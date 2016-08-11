def main():
    my_string = raw_input("Input string with parentheticals: ")
    my_num = int(raw_input("Input position of opening parenthetical: "))
    assert my_string[my_num] == "("
    stack = 1
    for index, character in enumerate(my_string[my_num + 1:]):
        if character == "(":
            stack += 1
        elif character == ")":
            stack -= 1
            if stack == 0:
                return index + my_num + 1
        else: None

if __name__ == "__main__":
    print main()