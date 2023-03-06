import random

def roll_dices():
    return random.randint(1,6) + random.randint(1,6)

def main():
    player1 = input("Enter Player1 name:\n")
    player2 = input("Enter Player2 name:\n")
    
    player1_total = roll_dices()
    player2_total = roll_dices()

    if player1_total > player2_total:
        print(player1,'Wins')
    elif player1_total < player2_total:
        print(player2,'Wins')
    else:
        print("TIE")


main()