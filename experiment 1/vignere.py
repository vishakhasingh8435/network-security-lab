# encryption
# text = input("Enter text: ")
# key = input("Enter key: ")

# result = ""

# for i, char in enumerate(text.upper()):
#     shift = ord(key[i % len(key)].upper()) - ord('A')
#     result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

# print("Encrypted:", result)

# decryption
text = input("Enter encrypted text: ")
key = input("Enter key: ")

result = ""

for i, char in enumerate(text.upper()):
    shift = ord(key[i % len(key)].upper()) - ord('A')
    result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

print("Decrypted:", result)