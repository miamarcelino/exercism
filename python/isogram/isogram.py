def is_isogram(string):
    phrase = string.lower()  # make it case-insensitive
    seen = []                # keep track of letters we've seen

    for char in phrase:
        if char.isalpha():   # only check letters (ignore spaces and hyphens)
            if char in seen:
                return False
            seen.append(char)

    return True
