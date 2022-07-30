import random;
import hangman_list;
import hangman_art;

chosen_word = random.choice(hangman_list.word_list);
#print(chosen_word);
print(f"💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥");
print(f"{hangman_art.logo}\n");
print(f"💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥");
print("\nWelcome to Hangman!!!\n");


# This provides players with the short dashes that need to be filled
display = [];
for space in chosen_word:
    display.append("_");
print(display);

# The lives the player has
lives = 6;

# This block just tells us what word we're currently working on just for testing purposes
print(f"\npssst, the word is {chosen_word}.");


# This block checks the guessed letter and then fills in the list if it is inside
game_running = True;

while game_running:
    guess = input("Guess a letter you think is in the word. ").lower();
    letter_i = 0;
    if guess in display:
        print("You've already guessed this letter. \n");
    for letter in chosen_word:
         if letter == guess:
            display[letter_i] = letter;
         letter_i += 1;
    if guess not in chosen_word:
        print(hangman_art.stages[-(lives)]);
        print(f"sorry, {guess} isn't in the word.");
        lives -= 1;
        print(f"You've only got {lives} left. Careful. \n");

    # this part of the code checks if the player has lost the game
    if lives == 0:
        game_running = False;
        print("Oops, looks like you lost the game.");

    # This part of the code checks if the player has won the game
    print(display);
    if "_" not in display:
        game_running= False;
        print("Yay you won the game.");
    