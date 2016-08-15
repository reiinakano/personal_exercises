def number_of_ways(cents, max_coin=25):
    answer = 0
    if cents == 0:
        return 1
    if cents >= 25 and max_coin >= 25:
        answer += number_of_ways(cents-25, 25)
    if cents >=10 and max_coin >= 10:
        answer += number_of_ways(cents-10, 10)
    if cents >= 5 and max_coin >= 5:
        answer += number_of_ways(cents-5, 5)
    if cents >= 1 and max_coin >= 1:
        answer += number_of_ways(cents-1, 1)

    return answer


if __name__ == "__main__":
    print number_of_ways(400)