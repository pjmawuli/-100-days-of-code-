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

    def deal(deck, score):
        deck.append(random.choice(cards))
        score = sum(deck)
        print(f"Player's deck: {deck}, Player's score: {score}")

    while game_active:
        response = input(f"Type 'y' to be dealt another card, type 'n' to pass.")
        if response == 'n':
            if player_score > 21:
                print(f"Whoops looks like you've lost.")
                black_jack()
            elif player_score == 21:
                print(f"Hurrayyyy!!! You've beat the dealer.")
                black_jack()
            elif player_score < 21:
                if dealer_score == 21:
                    print(f"Looks like the dealer won this one.")
                elif dealer_score <= 16:
                    deal(dealer_cards, dealer_score)
                elif dealer_score > player_score:
                    print(f"The dealer has won this round.")
                elif dealer_score == player_score:
                    print(f"Looks like it's a draw")
        elif response == 'y':
            deal(player_cards, player_score)
            

black_jack()
