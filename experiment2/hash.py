import hashlib

text = "HELLO"

hash_value = hashlib.sha256(text.encode()).hexdigest()

print("Original:", text)
print("Hash:", hash_value)