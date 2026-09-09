# Ceaser cipher
text = input("Enter the text: ")
shift = int(input("Enter the number of shift: "))

def ceaser_encrypt(text, shift):
    result = ""
    shift = shift % 26

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            new_pos = (ord(char) - base + shift) % 26
            result += chr(base + new_pos)
        else:
            result += char

    return result

print(ceaser_encrypt(text, shift))