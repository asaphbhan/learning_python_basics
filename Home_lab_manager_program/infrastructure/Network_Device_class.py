from .Device_Class import Device
class Network_device(Device):
    count = 0
    net_device = []
    def __init__(self, Name, IP, Status,OS,no_of_potes,device_type,):
        super().__init__(Name,IP,Status,OS)
        self._no_of_ports=no_of_potes
        self._device_type=device_type
        self._ports={i: 'Open' for i in range(1,no_of_potes+1)}
        Network_device.net_device.append(self)
        Network_device.count+=1

    @property
    def no_of_ports(self):
        return self._no_of_ports

    @property
    def device_type(self):
        return self._device_type

    @property
    def ports(self):
        return self._ports

    @classmethod
    def identify_by_name(cls, name):
        for i in Network_device.net_device:
            if i._Name == name:
                return i
        else:
            return 'No such device found.'

    @staticmethod
    def Network_Device_menu():
        print('=====Device Menu=====\n1. List Network Devices\n2. List Ports\n3. Show Connections\n4. Connect Device\n5. Disconnect Device\n'
            '6. Back')

    def list_ports(self):
        for i,j in self._ports.items():
            print(f'{i} : {j}')

    def show_connections(self):
        connections_found=True
        for i,j in self._ports.items():
            if j != 'Open':
                print(f'{i} : {j}')
                connections_found=False
        if connections_found:
            print("No connections found.")

    def data(self):
        print(f'{super().details()}\nIt is a {self._device_type} with the following ports:')
        self.list_ports()
        return ''

    def connect_device(self):
        print(f"Here's the lisf of all the ports in {self._Name}:")
        self.list_ports()
        port=int(input("Please enter the port you want to use: "))
        while port not in self._ports.keys():
            port = int(input("Please enter a valid port: "))
        serv=input('Please enter the device connection to be assigned to this port: ')
        self._ports[port]=serv
        print("Your device has been updated:")
        self.list_ports()

    def disconnect_device(self):
        print(f"Here's all the ports in {self._Name}")
        self.list_ports()
        port=int(input("Please enter the port you want to free up: "))
        while port not in self._ports.keys():
            port=int(input("Please enter a valid port: "))
        if self._ports[port] == 'Open':
            print('The port is already open.')
        else:
            self._ports[port]="Open"
            print('The port is now open: ')
            self.list_ports()

if __name__ == '__main__':
    router1 = Network_device("Main Router","192.168.1.1","Live","Cisco IOS",4,"Router")
    switch1 = Network_device("Core Switch","192.168.1.2","Live","Cisco IOS",8,"Switch")
    switch2 = Network_device("Backup Switch","192.168.1.3","Dead","Cisco IOS",16,"Switch")

    for i in Network_device.net_device:
        print(i.data())
        print('\n')

    # print("enable a dead server: ")
    # pass
    # print('\n')
    #
    # print("disabling a running device: ")
    # pass
    # print('\n')
    #
    # print("Add a service to a port in server 1, port 2: ")
    # Network_device.net_device[1].connect_device()
    # print('\n')
    #
    # print("reopening port 2 in server 1: ")
    # Network_device.net_device[1].disconnect_device()
    # print('\n')