#here i am learning how to read and write files using python.
import csv
import datetime as dt
import random as rd

components=["Network","Storage",'Backup','Power Supply']

def record_logs(file_path): #takes the status of the components and writes it on the csv file
    with open(file_path,'a',newline='')  as logbook:
        writer=csv.writer(logbook)
        writer.writerow(i for i in get_health().values())
    print('Log updated successfully')

def get_datetime(): #gets the date and time of when saving a diagnostic, separated so that if needed, may be able to alter the formating as per needs.
    now = dt.datetime.now()
    now_datetime = now.strftime('%R:%S %d/%m/%y')
    return now_datetime

def get_health(): #generates what the health status is going to be for the different components
    health={'Date Time': get_datetime()}
    status=['Stable','Critical']
    for i in components:
        health[i]=rd.choice(status) #selecting one state of the two and adding it to a dictionary which will later be a
    return health

def read_log(file_path):
    try:
        with open(file_path,'r') as logbook:
            content = csv.reader(logbook)
            for line in content:

                if len(line) == 5:
                    print(f'-------------------------\n{line[0]}\nNetwork - {line[1]}\nStorage - {line[2]}\nBackup  - {line[3]}\nPower   - {line[4]}\n-------------------------\n')
                else:
                    print("----------------------------------------\n"
                          "The record for this date are incomplete.\n"
                          "-----------------------------------------")

    except FileNotFoundError:
        print('Please add a log before printing any')

def menu():
    print('\n--------------------------\n'
          'What would you like to do?\n'
          '1. Print log data\n'
          '2. Add log data\n'
          '3. Exit\n'
          '--------------------------')

log_file_path="health_log.csv"
choice=0
while choice != 3:
    menu()
    try:
        choice=int(input("Please enter your choice: "))
        match(choice):
            case 1:
                read_log(log_file_path)
            case 2:
                record_logs(log_file_path)
            case 3:
                break
            case _:
                print("Please enter one of the three options.")
    except ValueError:
        print('Please enter something valid from the menu.')