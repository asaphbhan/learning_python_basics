#Created a Slot machine game to practice my functions and the random library
Balance=int(100)
slot=('Cherry','Lemon','Star','Orange',"Bell")
import random
def win_cash(bets):
    global Balance
    Balance=Balance + bets*2

def lose_cash(bets):
    global Balance
    Balance=Balance - bets

def win_check(res,bets):
    if res[0] == res[1] == res[2]:
        print("Congratulations on your win")
        win_cash(bets)
    else:
        print("You lose")
        lose_cash(bets)

def slot_machine(bets):
    result=['','','']
    for i in range(0, 3):
        result[i] = random.choice(slot)
    display(result)
    win_check(result,bets)

def display(slots):
    print("==========================")
    for i in slots:
        print(i, end=" | ")
    print("\n==========================")


play='Y'
while play!="N":
    if Balance==0:
        print('You have exhausted your money, current balance is 0')
        break
    bet=int(input("Please enter your bet: "))
    while not 0<bet<=Balance:
        bet=int(input("Please enter a valid bet: "))
    slot_machine(bet)
    print(f"Your current balance is {Balance}")
    play=input("Would you like to play again? (Y/N): ").capitalize()
    while play not in ['Y', 'N']:
        play = input("Enter Y or N: ")