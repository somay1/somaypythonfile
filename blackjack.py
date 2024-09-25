import random
from art import logo



#user_choice=input("Do you want to play The Blackjack Game? Type 'y' or 'n' ")

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(c_score, u_score):
    if c_score == u_score:
        return "Draw"
    elif c_score==0:
        return "YOU lose The opponent has Blackjack"
    elif u_score==0:
        return "You win"
    elif u_score>21:
        return "YOU lose"
    elif c_score>21:
        return "opponent lose"
    elif u_score>c_score:
        return "you win"
    else:
        return "you lose"

def play_game():
    print(logo)

    user_card=[]
    computer_card=[]
    computer_score=-1
    user_score=-1
    game_over= False
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"your cards are {user_card} , current score is {user_score}")
        print(f"Computer first  card is {computer_card[0]} ")
        if user_score==0 or computer_score==0 or user_score>21:
            game_over=True
        else:
            user_should_deal=input("do you want to draw another card type 'y' or 'n'")
            if user_should_deal=="y":
                user_card.append(deal_card())
            else:
                game_over=True
    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)
    print(f"your final hand : {user_card} , final score is {user_score}")
    print(f"computer final hand : {computer_card} , final score is {computer_score}")
    print(compare(computer_score,user_score))


while input("do you want to play blackjack again type 'y' or 'n' ")=='y':
    print("\n"*20)
    play_game()














    




