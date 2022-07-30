import random;

name_string = input("Give me everyone's name seperated by a comma: \n");
name_list = name_string.split(", ");
# print(name_list);

index = random.randint(0, len(name_list)-1);

sucker = name_list[index];

print(f"Looks like {sucker} is going to have to pay the bill.");