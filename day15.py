def play(numbers, turn):
    spoken = {}
    current = 0
    previous = 0
    for idx, number in enumerate(numbers):
        spoken[number] = idx + 1
        previous = number

    for i in range(len(numbers) + 1, turn + 1):
        if previous in spoken:
            current = i - 1 - spoken.get(previous)
        else:
            current = 0
        spoken[previous] = i - 1
        previous = current
    return current


starting_numbers = [2, 1, 10, 11, 0, 6]
print('Teil 1:', play(starting_numbers, 2020))
print('Teil 2:', play(starting_numbers, 30000000))
