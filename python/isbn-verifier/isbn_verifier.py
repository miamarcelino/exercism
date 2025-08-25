def is_valid(isbn):
    # remove hyphens
    isbn = isbn.replace("-", "")

    # must be exactly 10 characters
    if len(isbn) != 10:
        return False

    total = 0
    for i, char in enumerate(isbn):
        if char == "X":
            if i != 9:  # X can only appear as the last character
                return False
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False
        total += value * (10 - i)

    return total % 11 == 0