def encrypt(text):
    direction = input("Enter shift direction (R for Right, L for Left): ").upper()
    shift = 1 if direction == 'R' else -1

    result = ""

    for char in text:
        result += chr((ord(char) + shift) % 128)

    return result


def decrypt(text):
    result = ""

    for char in text:
        result += chr((ord(char) - 1) % 128)

    return result