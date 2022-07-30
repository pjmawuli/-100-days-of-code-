import random;

choice = input("Heads or Tails? ");

rd_num = random.randint(0, 1);

outcome = 0;

if rd_num == 0:
    outcome = "Heads";
elif rd_num == 1:
    outcome = "Tails";

if choice == outcome:
    print(f"You win, it's {outcome}");

else:
    print(f"Sorry, {outcome}");