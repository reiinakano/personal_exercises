def helper_print(columns_taken):
    for num in columns_taken:
        string_to_print = ""
        for i in range(8):
            if i == int(num):
                string_to_print += "x "
            else:
                string_to_print += "- "
        print string_to_print
    print ""

def print_all_possible(columns_taken=""):
    if len(columns_taken) == 8:
        helper_print(columns_taken)
        #print columns_taken
    else:
        for num in range(8):
            if str(num) not in columns_taken:
                valid = True
                length = len(columns_taken)
                for index, char in enumerate(columns_taken):
                    x_distance = num - int(char)
                    y_distance = length - index
                    if abs(x_distance) == abs(y_distance):
                        valid = False
                if valid:
                    print_all_possible(columns_taken+str(num))


if __name__ == "__main__":
    print_all_possible()