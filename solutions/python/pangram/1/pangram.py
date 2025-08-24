
def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lower = sentence.lower()

    for letter in alphabet:
        if letter not in lower:
            return False
    return True
