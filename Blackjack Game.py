import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, comp_score):
        if comp_score > 21:
            return "You won, Congratulations!!!"
        elif user_score > 21:
            return "You lost, Better luck next time :("
        elif user_score == 0:
            return "You won, Congratulations!!!"
        elif comp_score == 0:
            return "You lost, Better luck next time :("
        elif user_score > comp_score:
            return "You won, Congratulations!!!"
        elif user_score > comp_score:
            return "You won, Congratulations!!!"
        elif user_score < comp_score:
            return "You lost, Better luck next time :("
        elif user_score == comp_score:
            return "You drew"

def play_game():
    print(logo)
    user_cards = []
    comp_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not is_game_over:
        user_score = calc_score(user_cards)
        comp_score = calc_score(comp_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit_me == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
        
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calc_score(comp_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 1000)
    play_game()
