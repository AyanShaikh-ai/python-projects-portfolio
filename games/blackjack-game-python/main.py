from art import logo
import random
cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card_choice():
    card1 = random.choice(cards_deck)
    card2 = random.choice(cards_deck)
    score = card1 + card2
    return card1, card2, score

def additional_card():
    next_card = random.choice(cards_deck)
    return next_card

def computer_play(deck, score):
    if score > 21:
        deck, score = ace(deck, score, is_user = False)
    while score < 17:
        next_card = additional_card()
        deck.append(next_card)
        score += next_card
        if score > 21:
            deck, score = ace(deck, score, is_user = False)
    return deck, score



def winner(u_score,c_score):
    if c_score <= 21:
        if u_score < c_score:
            print("YOU LOSE!")
        elif u_score == c_score:
            print("YOU DREW!")
        else: print("YOU WON!")
    else: print("Computer went over, You WON")

def ace(deck,score, is_user):

    for i in range(len(deck)):
        if score <= 21:
            break
        if deck[i] == 11:
            deck[i] = 1
            score -= 10

            if is_user:
                print(
                    f"You passed 21, but you have an Ace.\n"
                    f"Your 11 has been turned into a 1.\n"
                    f"Your new deck is {deck}, new score is {score}"
                )
    return deck, score


game = True
while game:
    user_deck = []
    computer_deck = []
    start = input("do you want to play a game of blackjack? type y or n: \n").lower()
    if start == "y":
        print(" \n " * 20)
        print(logo)
        card1_user, card2_user, score_user = card_choice()
        user_deck.append(card1_user)
        user_deck.append(card2_user)
        print(f"Your cards: {user_deck}, current score: {score_user}")
        if score_user == 21:
            print("BLACKJACK! You win!")
            continue
        card1_computer, card2_computer, score_computer = card_choice()
        computer_deck.append(card1_computer)
        computer_deck.append(card2_computer)
        if score_computer == 21:
            print("Computer has BLACKJACK!")
            print(f"Computer's cards: {computer_deck}, score: {score_computer}")
            continue
        else:
            print(f"computer's first card: {card1_computer}")
        draw = True
        while draw:
            another_card = input("type y to get another card, type n to pass").lower()
            if another_card == "y":
                next_card = additional_card()
                user_deck.append(next_card)
                score_user += next_card
                print(f"Your cards: {user_deck}, current score: {score_user}")
                if score_user > 21:
                    user_deck, score_user = ace(user_deck, score_user, is_user = True)
                    if score_user > 21:
                        draw = False
                        print(f"Your final hand: {user_deck}, score: {score_user}")
                        print("you went over 21, you lose")
            else:
                draw = False
                print(f"Your final hand: {user_deck}, final score: {score_user}")
                final_deck_computer, final_score_computer = computer_play(computer_deck, score_computer )
                print(f"computer's final deck: {final_deck_computer}, final score: {final_score_computer}")
                winner(score_user, final_score_computer)
    else: game = False
