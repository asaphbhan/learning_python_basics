#Movie Ticket program (Chat GPT given idea)
import time
seats=[[' ','A','B','C','D','E'],
       ['1','0','0','0','0','0'],
       ['2','0','0','0','0','0'],
       ['3','0','0','0','0','0'],
       ['4','0','0','0','0','0'],
       ['-','-','-','-','-','-'],]
rows=['A','B','C','D','E']
selection_row='A'
selection_column=0
while True:
    for row in seats:
        for column in row:
            print(column,end=' ')
        print()
    print("   Screen  \n0=Available\nX=Booked")
    selection_row=input("please enter column letter of the seat you want to book(Q to quit): ").upper()
    if selection_row=='Q':
        break
    while selection_row not in rows:
        selection_row = input("please enter column letter of the seat you want to book(Q to quit): ").upper()
    selection_column=int(input("Please enter the row of the seat you want to book: "))
    while selection_column not in range(1,5):
        selection_column=int(input("Please enter a valid row of the seat you want to book: "))

    selection_row=rows.index(selection_row)

    if seats[selection_column][selection_row+1] == 'X':
        print("!!!!Seat is already booked!!!!")
        print("\n\n")
        continue

    seats[selection_column][selection_row+1]='X'
    for row in seats:
        for column in row:
            print(column, end=' ')
        print()
    print("   Screen  \n0=Available\nX=Booked")
    print("-----------------------")
    time.sleep(3)