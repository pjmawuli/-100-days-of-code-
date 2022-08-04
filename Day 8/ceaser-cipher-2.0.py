import art;

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decode:\n"
print(art.logo)
direction = input("Do you want to decode or encrypt? \n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction.lower() == "decode":
    shift *= -1

def ceaser(text, shift, direction):
    new_text = ""

    for char in text:
        position = alphabet.index(char)
        new_position = position
        new_position += shift
        new_text += alphabet[new_position]
    print(new_text)

ceaser(text, shift, direction)