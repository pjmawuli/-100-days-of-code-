print("Welcome to the Band Name Generator.");
city_name = input("What's the name of the city you grew up in?\n");
pet_name = input("What's the name of your pet?\n");

band_name = f"{city_name.title()} {pet_name.title()}";

print(f"You can name your band The {band_name}.");
print("You're welcome 😎.")