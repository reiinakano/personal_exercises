def process(solution, guess):
    if len(solution) != len(guess):
        print "Invalid guess"
        return None
    solution = solution.lower()
    guess = guess.lower()
    wrong_guesses = []
    unguessed = {}
    hit = 0
    pseudo_hit = 0
    for solution_char, guess_char in zip(solution, guess):
        if solution_char != guess_char:
            wrong_guesses.append(guess_char)
            if solution_char in unguessed: unguessed[solution_char] += 1
            else: unguessed[solution_char] = 1
        else:
            hit += 1
    for char in wrong_guesses:
        if char in unguessed and unguessed[char] > 0:
            unguessed[char] -= 1
            pseudo_hit += 1
    print "The number of pseudohits is " + str(pseudo_hit) + " while the number of hits is " + str(hit)
    return hit, pseudo_hit


if __name__ == "__main__":
    process("rggb", "grrb")