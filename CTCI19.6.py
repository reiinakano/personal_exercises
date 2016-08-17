one_to_nineteen = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ",
                   "Nine ", "Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ",
                   "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]
tens_array = ["Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]

def print_hundreds(N):
    tens = N % 100
    if tens == 0:
        tens_string = ""
    elif tens <= 19:
        tens_string = one_to_nineteen[tens]
    else:
        ones = tens % 10
        tens = tens / 10

        tens_string = tens_array[tens-2] + one_to_nineteen[ones]
    hundreds = N/100
    if hundreds == 0:
        hundreds_string = ""
    else:
        hundreds_string = one_to_nineteen[hundreds] + "Hundred "
    return hundreds_string + tens_string

def print_english(N):
    if N < 0 or N > 999999:
        return "Error"
    if N == 0:
        return "Zero"
    first_three_digits = N % 1000
    first_three_digits_string = print_hundreds(first_three_digits)
    last_three_digits = N / 1000
    if last_three_digits == 0:
        last_three_digits_string = ""
    else:
        last_three_digits_string = print_hundreds(last_three_digits) + "Thousand"
        if first_three_digits_string != "":
            last_three_digits_string += ", "
    return last_three_digits_string + first_three_digits_string


if __name__ == "__main__":
    print print_english(584204)