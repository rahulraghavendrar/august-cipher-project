# August Cipher with Type D Hashing

## Introduction

This implements the August Cipher along with a hashing technique using SHA-256. The aim is to understand how encryption and hashing can be combined to provide both security and integrity.

---

## August Cipher (ASCII Based)

In this implementation, I used an ASCII-based shift instead of limiting to alphabets.

Each character is shifted by 1 using modulo 128:

* Works for letters, numbers, and symbols
* Example:

  * 'a' → 'b'
  * '1' → '2'
  * '@' → next ASCII character

---

## Hashing Method

SHA-256 from hashlib is used.

Steps followed:

1. Plaintext is combined with a secret value ("xy")
2. SHA-256 hash is generated
3. The hash is appended to the plaintext

Final format:
plaintext + hash(plaintext + secret)

---

## Working Process

### Encryption:

1. Input plaintext
2. Generate hash using plaintext + "xy"
3. Append hash to plaintext
4. Encrypt entire string using ASCII shift

### Decryption:

1. Decrypt the ciphertext
2. Extract plaintext and hash
3. Recompute hash using plaintext + "xy"
4. Compare both hashes

If match → valid
Else → tampered

---

## How to Run

```bash
python test_script.py
```

---

## Example 1

Plaintext:
hello

Combined:
hello + hash

Encrypted:
ifmmp...

Decrypted:
hello...

Result:
Valid Message

---

## Example 2

Plaintext:
abc123

Combined:
abc123 + hash

Encrypted:
bcd234...

Decrypted:
abc123...

Result:
Valid Message

---

## Files

* august_cipher.py
* hash_function.py
* test_script.py

---

## Understanding Through Prompts

To understand the concepts better, I explored using these prompts:

* "Why is hashing done before encryption in some systems?"
* "Why is SHA-256 preferred over MD5?"
* "How does adding a secret key improve hashing security?"
* "Advantage of SHA-256 over normal prime number or XOR hashing?"

These helped me understand the importance of combining encryption with hashing for secure communication.

---

## Conclusion

This project helped me understand how encryption ensures confidentiality and hashing ensures integrity. Combining both provides a more secure system.
