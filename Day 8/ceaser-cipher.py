alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
func_call = input("Do you want to decrypt or encrypt? ")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    text = list(text)
    encrypted_text = text.copy()

    for char in alphabet:
        if char in text:
            alphabet_i = alphabet.index(char)
            alphabet_i += shift
            alphabet_i = alphabet_i % 26

            for index in range(len(encrypted_text)):
                if encrypted_text[index] == char:
                    encrypted_text[index] = alphabet[alphabet_i]
    ceaser_text = ""
    print(ceaser_text.join(encrypted_text))

def decrypt(text, shift):
    text = list(text)
    decrypted_text = text.copy()

    for char in alphabet:
        if char in text:
            alphabet_i = alphabet.index(char)
            alphabet_i -= shift

            for index in range(len(decrypted_text)):
                if decrypted_text[index] == char:
                    decrypted_text[index] = alphabet[alphabet_i]
    ceaser_text = ""
    print(ceaser_text.join(decrypted_text))

if func_call.lower() == "decrypt":
    decrypt(text, shift)
elif func_call.lower() == "encrypt":
    encrypt(text, shift)

