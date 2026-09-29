from .Device_Class import Device
from .Services_class import Service
class Server(Device): #This Should hold the data of the servers running
    count = 0
    servers=[]
    def __init__(self, Name, IP, Status, OS, CPU, RAM, Storage, Type):
        super().__init__(Name, IP, Status, OS)
        Server.servers.append(self)
        Server.count+=1
        self._CPU = CPU
        self._RAM = RAM
        self._Storage = Storage
        self._Type = Type
        self._Service=[]
        self._Status = Status

    @property
    def CPU(self):
        return self._CPU

    @property
    def RAM(self):
        return self._RAM

    @property
    def Storage(self):
        return self._Storage

    @property
    def Type(self):
        return self._Type

    @property
    def Service(self):
        return self._Service

    @classmethod
    def identify_by_name(cls, name):
        for i in Server.servers:
            if i._Name == name:
                return i
        else:
            return 'No such device found.'

    @staticmethod
    def Server_menu():
        print('=====Service Menu=====\n1. List Servers\n2. Add Service\n3. Remove Service\n4. List Service\n5. Start Server\n'
            '6. Stop Server\n7. Reboot Server\n8. Back')

    def data(self): #Displays all the details of the servers
        return (f'{super().details()}The Device has {self._CPU} processor, {self._RAM} GB RAM, {self._Storage} GB of storage, '
                f'is of {self._Type} type, and holds {self._Service} services.')

    def list_services(self):
        for i in self._Service:
            print(i.Name)

    def remover_service(self):
        print(f"Which among the following services do you want to remove:")
        self.list_services()
        choice=input(':')
        deleted=True
        for i in self._Service:
            if choice==i.Name:
                print(f'{choice} has been removed')
                self._Service.remove(i)
                deleted=False
                break
        if deleted:
            print("Couldn't find that service")

    def add_service(self):
        Name=input("Please enter the name of the service: ")
        Port=int(input("Which port should it be added to: "))
        Version=float(input("What is the version of the service added: "))
        service=Service(Name,Port,Version)
        self._Service.append(service)

if __name__ == '__main__':
    server1=  Server('Web server','192.168.1.10','Live','Ubuntu',8,16,500,'Web')
    server2 = Server('Database Server', '192.168.1.20', 'Live', 'Ubuntu', 16, 32, 1, 'Database')
    server3 = Server('Backup Server', '192.168.1.30', 'Dead', 'Windows Server', 4, 8, 2, 'Backup')

    for i in Server.servers:
        print(i.data())

    # print('Testing the server start function with a live server: ')
    # server1.start()
    # print('\n')
    #
    # print('Testing the server start function with a dead server: ')
    # pass
    # print('\n')
    #
    # print('Testing the stop function with a already dead server')
    # server3.stop()
    # print('\n')
    #
    # print('Testing the stop function with a live server: ')
    # pass
    # print('\n')
    #
    # print('Testing the reboot function with a dead server: ')
    # server3.Reboot()
    # print('\n')
    #
    # print('Testing the reboot function with a Live server: ')
    # pass
    # print('\n')
    #
    # print('Testing the add service function to the server: ')
    # server1.add_service()
    # print(server1)
    # print('\n')
    #
    # print('Testing the list services function on server1: ')
    # server1.list_services()
    # print('\n')
    #
    # print("Testing the remove service function with server1: ")
    # server1.remover_service()
    # server1.list_services()