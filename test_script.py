from august_cipher import encrypt, decrypt
from hash_function import attach_hash, verify_hash

text = input("Enter message: ")

combined = attach_hash(text)
print("Message + Hash:", combined)


encrypted = encrypt(combined)
print("Encrypted:", encrypted)


decrypted = decrypt(encrypted)
print("Decrypted:", decrypted)

valid, original = verify_hash(decrypted)

if valid:
    print("Valid Message")
    print("Original Message:", original)
else:
    print("Message Tampered")