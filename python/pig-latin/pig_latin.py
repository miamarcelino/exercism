def translate(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:
        w = word.lower()

        if w.startswith(("xr", "yt")) or w[0] in vowels:
            result.append(word + "ay")
            continue

        if "qu" in w:
            idx = w.index("qu")
            if idx == 0 or all(c not in vowels for c in w[:idx]):
                result.append(word[idx+2:] + word[:idx+2] + "ay")
                continue

        if "y" in w:
            idx = w.index("y")
            if idx > 0 and all(c not in vowels for c in w[:idx]):
                result.append(word[idx:] + word[:idx] + "ay")
                continue

        for i, ch in enumerate(w):
            if ch in vowels:
                result.append(word[i:] + word[:i] + "ay")
                break

    return " ".join(result)
