# IMPORT THE ART AND GAME DATA NEEDED
import art
import game_data

# IMPORT THE RANDOM MODULE FOR THE GAME
import random


# CREATE A GAME FUNCTION THAT RANDOMLY PICKS OUT ITEMS FROM THE GAME DATA
def item_create():
    item = random.choice(game_data.data)
    game_data.data.remove(item)

    return item


# CREATE A FUNCTION THAT COMPARES 2 ITEMS AND DETERMINES THE GREATER ONE BASED ON THE FOLLOWER COUNT
def item_compare(item1, item2):
    if item1['follower_count'] > item2['follower_count']:
        return item1

    else:
        return item2


# LET THE GAME BEGIN
# CREATE A WHILE LOOP THAT CONTINUES TO ASK THE PLAYER TO DETERMINE WHO HE THINKS HAS THE GREATER FOLLOWER COUNT

game_active = True
current_score = 0

print(art.logo)
item_a = item_create()

while game_active:
    print(f"Compare A: {item_a['name']}, a {item_a['description']} from {item_a['country']}")
    item_b = item_create()
    print(art.vs)
    print(f"To B: {item_b['name']}, a {item_b['description']} from {item_b['country']}")

    response = input("Who has more followers type 'A' or 'B'? ")
    next_item = item_compare(item_a, item_b)
    if response == "A" and item_a == next_item:
        current_score += 1
        print(f"You're right!, {item_a['name']} has {item_a['follower_count']}million followers, current score = {current_score}")
        item_a = next_item
    elif response == "B" and item_b == next_item:
        current_score += 1
        print(f"You're right!, {item_b['name']} has {item_b['follower_count']}million followers, current score = {current_score}")
        item_b = next_item
    else:
        print(f"Nope, you're wrong, you old-schooled freak!! ")
        print(f"Your current score is {current_score}")
        break
