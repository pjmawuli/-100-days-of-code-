import art;

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decode:\n"
print(art.logo)

game_on = True
while game_on:
    direction = input("Do you want to decode or encode? \n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction.lower() == "decode":   
        shift *= -1

    def ceaser(text, shift, direction):
        new_text = ""

        for char in text:

            if char not in alphabet:
                new_text += char
                continue
            else:
                position = alphabet.index(char)
                new_position = position
                new_position += shift

                if direction.lower() == "decode":
                    new_position %= 26
                    new_text += alphabet[new_position]
                elif direction.lower() == "encode":
                    new_position %= 26
                    new_text += alphabet[new_position]
        print(new_text)

    ceaser(text, shift, direction)

    call = input("Wanna have another go at it? ")
    if call.lower() == "no":
        break