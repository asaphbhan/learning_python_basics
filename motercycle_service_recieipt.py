#bike service receipt generator(learn *args and **kwargs)
def services(name,*serv_ls,**genserv_ls):
    total=0
    print("==========================\nMOTORCYCLE SERVICE RECEIPT\n==========================")
    print(f"Customer name: {name}")
    print("Services performed:")
    for ser in serv_ls:
        print(f"- {ser}")

    print("\nAdditional cost:")
    for ser,pri in genserv_ls.items():
        if ser=="name":
            continue
        print(f"- {ser}: Rs. {pri}")
        total+=pri
    print(f"Your total is: Rs. {total}")

    

services_ls=[]


c_name=(input("Please enter customer name: ")).capitalize()

service=input("Please enter the service done on the bike(q to quit): ")
while service!= 'q':
    services_ls.append(service)
    service = input("Please enter the next service done(q to quit): ")

services(c_name,*services_ls,Labour=500,GST=15,pickup_charges=200,)
