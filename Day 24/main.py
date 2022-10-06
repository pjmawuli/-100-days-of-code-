# First lets see if we can create multiple files for each name

# List of names of people
names = []

# The folder with the names we want
with open("./Input/Names/invited_names.txt") as name_file:
    for name in name_file.readlines():
        names.append(name.strip())

# Let's read from the file we want to multiply
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

for name in names:
    with open(f"./Input/Letters/{name}.txt", mode="w") as file:
        file.write(letter.replace("[name]", name))

