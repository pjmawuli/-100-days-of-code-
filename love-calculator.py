print("💕💕💕Welcome to the Love Calculator! 💕💕💕");
name1 = input("What's your name? ");
name2 = input("And what's the name of your crush? ");

name1 = name1.lower();
counter11 = 0;
counter12 = 0;

counter11 += name1.count("t");
counter11 += name1.count("r");
counter11 += name1.count("u");
counter11 += name1.count("e");

counter12 += name1.count("l");
counter12 += name1.count("o");
counter12 += name1.count("v");
counter12 += name1.count("e");

#print(counter11);
#print(counter12);

name2 = name2.lower();
counter21 = 0;
counter22 = 0;

counter21 += name2.count("t");
counter21 += name2.count("r");
counter21 += name2.count("u");
counter21 += name2.count("e");

counter22 += name2.count("l");
counter22 += name2.count("o");
counter22 += name2.count("v");
counter22 += name2.count("e");

#print(counter21);
#print(counter22);

t_counter = counter11 + counter21;
l_counter = counter12 + counter22;

score = f"{t_counter}{l_counter}";

score = int(score);

if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos 🤯💥💥❤️‍🔥");
if score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together 💕💕");

print(f"Your score is {score}%");
