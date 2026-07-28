current_balance=2500.00

def check_balance(x):
    print(f"\n\nYour current balance is: ${x:^10.2f}")

def deposit(x):
    depo=float(input('Please enter the amount you want to deposit: '))
    while depo<0 :
        depo=float(input(f'Please enter a valid amount:'))
    x = x + depo
    print(f'Thank you, Your current balance is: ${x:^10.2f}')
    return x

def withdraw(x):
    withdrawal=float(input('Please enter the amount you want to Withdraw: '))
    while withdrawal<0 or withdrawal>x:
        withdrawal=float(input(f'Please enter a valid amount, your current balance is ${x:.2f} :'))
    x = x - withdrawal
    print(f'Thank you, Your current balance is: ${x:^10.2f}')
    return x

def bank_menu():
    choose=range(1,5)
    print('====BANK MENU====')
    print('1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit')
    y =int(input("Please select your option(1,2,3,4): "))
    while y not in choose:
        y = int(input("Please select a valid option(1,2,3,4): "))
    return y

print('Welcome to your account')
choices = 0
while choices != 4:
    choices = int(bank_menu(choices))
    match(choices):
        case 1:
            check_balance()
            print("\n\n\n")


        case 2:
            current_balance=deposit(current_balance)
            print("\n\n\n")


        case 3:
            current_balance=withdraw(current_balance)
            print("\n\n\n")
print('\n\nThank you for banking with us.')