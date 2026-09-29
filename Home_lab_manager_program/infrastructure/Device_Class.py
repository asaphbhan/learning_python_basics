import time as t

class Device: #Papa class
    count=0
    devices=[]
    def __init__(self, Name, IP, Status,OS) : #Constructor
        Device.devices.append(self)
        self._Name = Name
        self._IP = IP
        self._Status = Status #Live or Dead
        self._OS = OS
        self._ID = (Device.count +1) * 1000
        Device.count += 1

    #create getter function for each attribute
    @property
    def Name(self):
        return self._Name

    @property
    def IP(self):
        return self._IP

    @property
    def Status(self):
        return self._Status

    @property
    def OS(self):
        return self._OS

    @property
    def ID(self):
        return self._ID

    @staticmethod
    def Device_menu():
        print('=====Device Menu=====\n1. List Devices\n2. Identify Device\n3. Start Device\n4. Stop Device\n5. Reboot Device\n'
              '6. Change Status\n7. Back')

    @classmethod
    def identify_by_name(cls,name):
        for i in Device.devices:
            if i._Name == name:
                return i
        else:
            return 'No such device found.'

    def details(self): #get info method
        return f"{self._Name} has the IP: {self._IP}.\nIt is currently {self._Status} and running {self._OS} with device ID: {self._ID}\n"

    def start(self): #Used to start any targeted server
        if self.Status == 'Live': #Stops a already live server from taking the start input
            print('The server is already running')

        else:
            print(f'Starting {self.Name}.',end='')
            for i in range(1,4):
                t.sleep(1)
                print('.',end='')
            print('\nThe server is now running')
            self._Status='Live'

    def stop(self):  # Used to stop any targeted server
        if self.Status == 'Dead':  # stops any already dead server from taking the stop input
            print('The server is already dead')

        else:
            print(f'Stopping {self.Name}.', end='')
            for i in range(1, 4):
                t.sleep(1)
                print('.', end='')
            print('\nThe server is now down')
            self._Status = 'Dead'

    @staticmethod
    def Status_validity(status):  # validate the status
        stat = ["Live", "Dead"]
        if status in stat:
            return True
        else:
            return False


    def Status_change(self,new_stat): #can change the status attribute of the asked object
        new_stat=str(new_stat).capitalize()
        while not Device.Status_validity(new_stat):
            new_stat=input("Please enter a valid status(Live/Dead): ").capitalize()
        if self.Status!=new_stat:
            self._Status=new_stat
            print(f'status for {self.Name} has been changed to {self.Status}')
        else:
            print(f"The new status is same as the old one")

    @classmethod #identify a device from its unique ID
    def identify(cls, unique_num):
        for i in cls.devices:
            if i.ID == unique_num:
                return f"The device with ID: {unique_num}, is {i.Name}"
        return "Device with this ID doesn't exist"

    def Reboot(self): #Reboots live devices and rejects dead devices
        if self.Status == 'Live':
            print(f"{self.Name} is rebooting.",end="")
            for i in range(0,6):
                t.sleep(1)
                print('.',end='')
            print(f'\n{self.Name} was successfully rebooted')
        else:
            print(f"{self.Name} is currently {self.Status}.\nDevice should be live to be rebooted.")

if __name__ == '__main__':
    device1 = Device('Bakwas', '123:456:78:9', 'Live', 'Ubuntu Server')
    device2 = Device('Baklol', '123:456:78:9', 'Live', 'Ubuntu Server')
    device3 = Device('Bhadvai', '123:456:78:9', 'Dead', 'Ubuntu Server')

    Device.devices[0]