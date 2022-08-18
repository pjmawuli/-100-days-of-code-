import art
import clearpy

running = True

persons_list = []


def list_people(bidder_name, bid_amount):
    person_dictionary = {"name": bidder_name, "bid": bid_amount}

    persons_list.append(person_dictionary)


while running:
    print(art.logo)
    print("Welcome to the Secret Auction Program ")

    name = input("What's your name? ")
    bid = int(input("How much are you willing to bid? "))

    list_people(name, bid)

    response = input("Would anyone else like to bid? ")
    if response == "no":
        running = False
    else:
        clearpy.clear()

highest_bid = persons_list[0]["bid"]
highest_bidder = persons_list[0]

for person in persons_list:

    if person["bid"] >= highest_bid:
        highest_bid = person["bid"]
        highest_bidder = person

highest_bidder_name = highest_bidder["name"]
highest_bidder_bid = highest_bidder["bid"]

print(f"Looks like {highest_bidder_name} with a bid of {highest_bidder_bid} has won the auction.")
