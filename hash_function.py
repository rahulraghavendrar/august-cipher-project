import hashlib

secret = "xy"

def attach_hash(message):
    hash_value = hashlib.sha256((message + secret).encode()).hexdigest()
    return message + hash_value


def verify_hash(full_text):
    message = full_text[:-64]
    received_hash = full_text[-64:]

    new_hash = hashlib.sha256((message + secret).encode()).hexdigest()

    if new_hash == received_hash:
        return True, message
    else:
        return False, None