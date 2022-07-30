row1 = ['🟪', '🟪', '🟪'];
row2 = ['🟧', '🟧', '🟧'];
row3 = ['🟦', '🟦', '🟦'];

map = [row1, row2, row3];
print(f"{row1}\n{row2}\n{row3}");

location = input("Where do you want to put the treasure? ");
item = input("Now what do you want to put there? ");

i1 = int(location[0]) - 1;
i2 = int(location[1]) - 1;

map[i1][i2] = item;

print(f"{row1}\n{row2}\n{row3}");
