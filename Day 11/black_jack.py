import art
import random


def black_jack():
    game_active = True
    print(art.logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = [random.choice(cards), random.choice(cards)]
    player_score = sum(player_cards)

    dealer_cards = [random.choice(cards), random.choice(cards)]
    dealer_score = sum(dealer_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {dealer_cards[0]}")

    def player_deal(deck, score):
        deck.append(random.choice(cards))
        score = sum(deck)
        print(f"Player's deck: {deck}, Player's score: {score}")
        return deck, score

    def dealer_deal(deck, score):
        deck.append(random.choice(cards))
        score = sum(deck)
        print(f"Dealer's deck: {deck}, Dealer's score: {score}")
        return deck, score

    while game_active:
        if player_score == 21:
            print("Blackjack! You win!")
            game_active = False
            break
        elif player_score > 21:
            print("Bust!. You lose.")
            game_active = False
            break
        else:
            response = input("Would you like to 'Hit' or 'Stand'? H/S: ")
            if response == "H":
                player_cards, player_score = player_deal(player_cards, player_score)

            elif response == "S":
                break

    print(f"Dealer's Cards: {dealer_cards}, Dealer's Score: {dealer_score}")

    while game_active:
        if player_score == dealer_score:
            print("Push!! Its a draw")
            break
        else:
            if dealer_score == 21:
                print(f"The Dealer wins this round")
                break
            elif dealer_score > 21:
                print(f"Yay!! You win this round")
                break
            elif 16 < dealer_score < 21:
                if dealer_score > player_score:
                    print("The dealer wins this round")
                    break
                elif player_score > dealer_score:
                    print("The player winds this round")
                    break
            else:
                while dealer_score <= 16:
                    dealer_cards, dealer_score = dealer_deal(dealer_cards, dealer_score)

    if input("would you like to have another go at this? Y/N: ") == "Y":
        black_jack()


black_jack()
