def response(hey_bob):
    msg = hey_bob.strip()

    if not msg:
        return "Fine. Be that way!"

    is_question = msg.endswith("?")

    letters = [ch for ch in msg if ch.isalpha()]
    is_yelling = bool(letters) and all(ch.isupper() for ch in letters)

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."