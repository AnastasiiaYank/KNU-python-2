from collections import Counter
S = '123+44/7'
counter = Counter(S)


def count_symbols(string):
    character_count = Counter(string)

    digit_count = 0
    operator_count = 0
    for character in character_count:
        if character.isdigit():
            digit_count += character_count[character]
        elif character in "+-*/":
            operator_count += character_count[character]

    return digit_count, operator_count


print(count_symbols(S))
