from random import randint


def find_list_of_subrows_from(row, i=0):
    list_of_valid_subrows = []
    length = len(row)
    for ending in range(i+1, length):
        for starting in range(i, ending):
            flag = False
            for coordinate in range(starting, ending+1):
                if not row[coordinate]:
                    flag = True
                    break
            if not flag:
                list_of_valid_subrows.append((starting, ending))
    return list_of_valid_subrows


def find_max_square_from_row(array, row_number):
    max_square_size = 0
    max_square_row_and_top_corners = None
    subrow_list = find_list_of_subrows_from(array[row_number])
    for start, end in subrow_list:
        if end - start + 1 > max_square_size:
            if end-start <= len(array) - row_number - 1:
                valid_square = True
                for i in range(row_number, row_number + end - start + 1):
                    if not array[i][start]:
                        valid_square = False
                        break
                if valid_square:
                    for i in range(row_number, row_number + end - start + 1):
                        if not array[i][end]:
                            valid_square = False
                            break
                if valid_square:
                    for i in range(start, end + 1):
                        if not array[row_number+end-start][i]:
                            valid_square = False
                            break
                if valid_square:
                    max_square_size = end - start + 1
                    max_square_row_and_top_corners = (row_number, start, end)
    return max_square_size, max_square_row_and_top_corners


def determine_max_subsquare(array):
    if len(array) != len(array[0]):
        return "Invalid array"
    max_square_size = 0
    max_square_row_and_top_corners = 0
    for index, row in enumerate(array):
        max_square_size_from_this_row, mstrc_from_this_row = find_max_square_from_row(array, index)
        if max_square_size < max_square_size_from_this_row:
            max_square_size = max_square_size_from_this_row
            max_square_row_and_top_corners = mstrc_from_this_row
    return max_square_size, max_square_row_and_top_corners


if __name__ == "__main__":
    array_size = 20
    my_array = []

    for i in range(array_size):
        my_array.append([])
    for i in range(array_size):
        for j in range(array_size):
            my_array[i].append(None)

    for i in range(array_size):
        for j in range(array_size):
            if randint(0, 8) > 1:
                my_array[i][j] = True

    for row in my_array:
        to_print = ""
        for column in row:
            if column:
                to_print += "x "
            else:
                to_print += "- "
        print to_print

    size, row_and_top = determine_max_subsquare(my_array)
    print "Max subsquare of size " + str(size) + " at row " + str(row_and_top[0]) + " and corners " + str(row_and_top[1]) + " and " + str(row_and_top[2])

    for index_row, row in enumerate(my_array):
        to_print = ""
        for index_column, column in enumerate(row):
            if column:
                if index_row == row_and_top[0] and row_and_top[1] <= index_column <= row_and_top[2]:
                    to_print += "O "
                elif index_row == row_and_top[0] + size - 1 and row_and_top[1] <= index_column <= row_and_top[2]:
                    to_print += "O "
                elif row_and_top[0] <= index_row <= row_and_top[0] + size - 1 and (index_column == row_and_top[1] or index_column == row_and_top[2]):
                    to_print += "O "
                else:
                    to_print += "x "
            else:
                to_print += "- "
        print to_print