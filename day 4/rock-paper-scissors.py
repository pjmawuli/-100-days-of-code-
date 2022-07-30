import random;

# Rock
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors. "));
player_hand = 0;
if choice == 0:
    player_hand = rock;
    print(player_hand);
elif choice == 1:
    player_hand = paper;
    print(player_hand);
elif choice == 2:
    player_hand = scissors;
    print(player_hand);

pc_choice = random.randint(0,2);
pc_hand = 0;
if pc_choice == 0:
    pc_hand = rock;
    print(pc_hand);
elif pc_choice == 1:
    pc_hand = paper;
    print(pc_hand);
elif pc_choice == 2:
    pc_hand = scissors;
    print(pc_hand);

if pc_hand == player_hand:
    print("Looks like it's a draw.\n");
elif pc_hand == paper and player_hand == rock:
    print("Looks like you lost to your computer.\n");
elif pc_hand == rock and player_hand == paper:
    print("You won!!!\n");
elif pc_hand == scissors and player_hand == paper:
    print("You lost to a machine.\n");
elif pc_hand == paper and player_hand == scissors:
    print("Your won this time.\n");
elif pc_hand == rock and player_hand == scissors:
    print("AI has won against man this time around.\n");
elif pc_hand == scissors and player_hand == rock:
    print("You won against AI.\n");
