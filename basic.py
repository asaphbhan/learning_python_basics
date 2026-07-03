#Mad libs game
# print("This is a madlibs game, so enjoy the story")
# name=input("Enter the name of our MC:")
# place=input("Enter the place out MC is from:")
# quality=input("Enter a quality of the MC(Eg. brave, lazy, etc.):")
# artifact=input("Enter the name of the legendary artifact our MC is searching for:")
# print(f"One day, a ",quality," explorer named ",name," traveled to ",place," looking for a legendary",artifact)

#Simple calculator
# print("Simple calculator")
# int1=int(input("Please enter the first operant:"))
# int2=int(input("Please enter the second operant:"))
# opp=input("Please select the operation you want to perform (+,-,*,/) :")
# if opp=="+":
#     print(int1+int2)
# elif opp=="-":
#     if int1>int2:
#         print(int1-int2)
#     elif int2>int1:
#         print("no negativity here")
#         print(int2-int1)
# elif opp=="*":
#     print(int1*int2)
# elif opp == "/":
#     if int2!= 0 :
#         print(int1/int2)
#     else:
#         print("Anything divided by zero is zero")
# else:
#     print("Please enter a valid operation")

#SI to cgs and vice versa weight converter
# print("SI to cgs weight converter")
# print("**Warning: the function inputs here are case-sensitive, so please be mindful**")
# conv=input("Enter the unit you have(kg or lbs only):")
# mass=float(input("Enter the numerical measure: "))
# if conv == "kg" :
#     print(mass*2.204623," lbs")
# elif conv == "lbs":
#     print(mass/2.204623," kg")
# else:
#     print("Please enter a valid function")

#Temperature converter
# print("Temperature converter (Converts to Celsius only):D\nThe functions are case-sensitive here")
# unit=input("enter the unit you have(c, k or f)")
# measure=float(input("Enter the numerical value: "))
# match unit:
#     case "c":
#         print("Congratulations I can't help you")
#
#     case "f":
#         print(5/9*(measure-32)," Celsius")
#
#     case "k":
#         print(measure-273.15," Celsius")
#
#     case _:
#         print("Please enter a valid function")

#Compound interest calculator
# print("This is a Compound interest calculator")
# principal=float(input("Enter Principal amount:"))
# while principal <= 0:
#     print("Invalid Principal amount entered.")
#     principal=float(input("Enter Principal amount:"))
#
# time=int(input("Enter the time period of investment: "))
# while time<=0:
#     print("Invalid time period entered.")
#     time = int(input("Enter the time period of investment: "))
#
# rate=int(input("Enter the rate of interest: "))
# while rate<0:
#     print("Invalid rate of interest entered.")
#     rate = int(input("Enter the rate of interest: "))
#
# result=principal*pow((1+rate/100),time)
#
# print(f"after {time} years, you'll end up with ₹{result:6,.2f}")

# #count down program
# import time
# print("Countdown program")
# tim=int(input("Enter the time in seconds: "))
# while tim<=0:
#     print("Please enter a positive number.")
#     tim = int(input("Enter the time in seconds: "))
#
# for x in range(tim,0,-1):
#     ct= x
#     hr = int(ct / 3600)
#     ct = ct % 3600
#     minute = int(ct / 60)%60
#     sec = ct % 60
#     print(f"{hr:02}H:{minute:02}M:{sec:02}S")
#     time.sleep(1)
# print("Time up!")

#symbol rectangle printer (Learn nested loops)
# symbol=input("Enter the symbol the rectangle is to be made of:")
# row=int(input("Enter the number of rows:"))
# while row<=0:
#     print("Enter a positive number of rows.")
#     row = int(input("Enter the number of rows:"))
# column=int(input("Enter the number of columns:"))
# while column<=0:
#     print("Enter a positive number of columns.")
#     row = int(input("Enter the number of columns:"))
#
# for x in range(row):
#     for y in range(column):
#         print(f"{symbol}",end="")
#     print()

#show a keypad in a phone using tuples
# number=((1,2,3),(4,5,6),(7,8,9),('*',0,'#'))
# for num in number:
#     for n in num:
#         print(n,end=' ')
#     print()

#number guessing game
# import random
# low=1
# high=50
# chance=12
# answer=random.randint(low,high)
# print(f"Here is a number guessing game, The number ranges between {low} and {high} "
#       f"You get {chance} chances to guess the number")
# counter=chance
#
# for i in range(0,chance):
#     print(f"{counter} guesses left")
#     guess=int(input("Enter the guess"))
#
#     if guess<low or guess>high:
#         print("Please enter a number in range")
#
#     elif guess==answer:
#         print("Correct answer")
#         break
#
#     elif guess<answer:
#         print("Guess higher")
#
#     elif guess>answer:
#         print("Guess lower")
#
#     counter -= 1
#     if counter==0:
#         print(f"Game Over, The answer was{answer}")

#Rock paper scissor game
# import random
# Options=('Rock','Paper','Scissor')
# pc_score=0
# player_score=0
# res="Win"
# while True:
#     pc_chose = random.choice(Options)
#     player_chose=input("Please enter your choice(q to quit)\n(Rock, Paper, Scissor):").capitalize()
#     if player_chose=="Q":
#         break
#     while player_chose not in Options:
#         player_chose=input("Please enter a valid choice: ").capitalize()
#     print("PC chose", pc_chose)
#     if player_chose==pc_chose:
#         print("Draw")
#
#     elif player_chose=="Rock":
#         if pc_chose=="Paper":
#             print("You lose")
#             pc_score+=1
#         elif pc_chose=="Scissor":
#             print("You win")
#             player_score+=1
#
#     elif player_chose=="Paper":
#         if pc_chose=="Rock":
#             print("You win")
#             player_score+=1
#         elif pc_chose=="Scissor":
#             print("You lose")
#             pc_score+=1
#
#     elif player_chose=="Scissor":
#         if pc_chose=="Rock":
#             print("You lose")
#             pc_score+=1
#         elif pc_chose=="Paper":
#             print("You win")
#             player_score+=1
#     print(f"Your score: {player_score}\nPC's score: {pc_score}")
#
# if player_score>pc_score:++
#     res="Won"
# else:
#     res="Lost"
# if player_score!=pc_score:
#     print(f"You {res} by {abs(player_score-pc_score)}")
# else:
#     print("It was a draw with each having",{player_score})


#Dice rolling program
# import random
# inp=('y','e')
# low=1
# high=6
# while True:
#     chose=input("Do you want to role the dice[yes=y / exit=e]: ").lower()
#     while chose not in inp:
#         chose = input("Please enter a valid input [y/e]: ").lower()
#     if chose=='e':
#         break
#
#     else:
#         print(f"The dice roled a {random.randint(low,high)}")
# print("Thank you for playing")

#count up timer
# import time
# goal=int(input("Please enter the time in seconds: "))
# def print_time(ti):
#     for x in range (1,ti+1):
#         time.sleep(1)
#         print(f"00H : 00 M: {x:02}S")
# print_time(goal)
# print("Time Up")

#Phone number generator
# codes={"USA":1,"UK":44,"Japan":81,"China":86,"India":91}
# country=input("Please enter your country(USA, UK, Japan, China, India): ").capitalize()
# if country == "Usa" or country=="Uk":
#     country=country.upper()
# while country not in codes:
#     country = input("Please enter a valid country(USA, UK, Japan, China, India): ").capitalize()
#     if country == "Usa" or country == "Uk":
#         country = country.upper()
#
# def find_country(coun):
#     return codes.get(coun)
#
# phone_number=input("Please enter the number: ")
# while len(phone_number)!=10 or not phone_number.isdigit():
#     phone_number=input("Please enter a valid phone number: ")
#
# print(f"The number is +{find_country(country)} {phone_number}")
