from infrastructure.Device_Class import Device
from infrastructure.Network_Device_class import Network_device
from infrastructure.Server_class import Server
from infrastructure.Services_class import Service
def main_menu():
    print('======Hom Lab Manager======\n'
          '1.Devices\n'
          '2. Servers\n'
          '3. Network Devices\n'
          '4. Services\n'
          '5. Exit')

def device_works():
      c2 = 0
      while c2 != 7:
            Device.Device_menu()
            c2 = int(input('What would you like to do: '))
            while c2 not in range(1, 8):
                  c2 = int(input('Please enter a valid input: '))
            if c2 == 7:
                  break
            match c2:
                  case 1:  # List Devices
                        for i in Device.devices:
                              print(i.details())

                  case 2:  # Identify a device by device id
                        identity = int(input('Please enter the device ID: '))
                        print(Device.identify(identity))

                  case 3:  # Start a device
                        start_this = input("Please enter the name of the device you want to start: ")
                        Device.start(Device.identify_by_name(start_this))

                  case 4:  # Stop a device
                        stop_this = input("Please enter the name of the device you want to stop: ")
                        Device.stop(Device.identify_by_name(stop_this))

                  case 5:  # Restart a device
                        restart_this = input("Please enter the name of the device you want to restart: ")
                        Device.Reboot(Device.identify_by_name(restart_this))

                  case 6:  # change status of the device
                        changer = input("Please enter the name of the device you want to change the status of: ")
                        changer = Device.identify_by_name(changer)
                        new_status = input('Please enter the new status you want(Live/Dead): ')
                        changer.Status_change(new_status)

def server_works():
      c2 = 0
      while c2 != 8:
            Server.Server_menu()
            c2 = int(input('What would you like to do: '))
            while c2 not in range(1, 9):
                  c2 = int(input('Please enter a valid input: '))
            if c2 == 8:
                  break
            match c2:
                  case 1: #List all the server details
                        for i in Server.servers:
                              print(i.data())
                              print('\n')
                  case 2: #add services
                        server_choice=input("please enter the name of the server you want to add the service in: ")
                        Server.identify_by_name(server_choice).add_service()

                  case 3: #remove services
                        server_choice = input("please enter the name of the server you want to remove the service from: ")
                        Server.identify_by_name(server_choice).remove_service()

                  case 4: #List services
                        server_choice = input("please enter the name of the server you want to list the services of: ")
                        Server.identify_by_name(server_choice).list_services()

                  case 5: #start server
                        server_choice = input("please enter the name of the server you want to start: ")
                        Server.identify_by_name(server_choice).start()

                  case 6: #stop server
                        server_choice = input("please enter the name of the server you want to stop: ")
                        Server.identify_by_name(server_choice).stop()

                  case 7: #reboot server
                        server_choice = input("please enter the name of the server you want to add the service in: ")
                        Server.identify_by_name(server_choice).Reboot()

def Network_works():
      c2 = 0
      while c2 != 6:
            Network_device.Network_Device_menu()
            c2 = int(input('What would you like to do: '))
            while c2 not in range(1, 7):
                  c2 = int(input('Please enter a valid input: '))
            if c2 == 6:
                  break
            match c2:
                  case 1: #list the network devices
                        for i in Network_device.net_device:
                              print(i.data())
                              print('\n')

                  case 2: #List ports
                        device_choice=input('Please enter the device you want to list the ports of: ')
                        Network_device.identify_by_name(device_choice).list_ports()

                  case 3: #Show connections
                        device_choice=input("Please enter the device who's connections you want to see: ")
                        Network_device.identify_by_name(device_choice).show_connections()

                  case 4: #connect device
                        device_choice=input('Please enter the name of the device you want to establish new connections for: ')
                        Network_device.identify_by_name(device_choice).connect_device()

                  case 5: #disconnect device
                        device_choice = input('Please enter the name of the device you want to establish new disconnections for: ')
                        Network_device.identify_by_name(device_choice).disconnect_device()

def services_work():
      c2 = 0
      while c2 != 6:
            Service.service_menu()
            c2 = int(input('What would you like to do: '))
            while c2 not in range(1, 7):
                  c2 = int(input('Please enter a valid input: '))
            if c2 == 6:
                  break
            match c2:
                  case 1: #List the server
                        for i in Service.services:
                              print(i)
                              print('\n')

                  case 2: #start service
                        server_select=input("Please enter the service you want to start: ")
                        Service.identify_by_name(server_select).start()

                  case 3: #stop service
                        server_choice = input("Please enter the name of the service you want to stop: ")
                        Server.identify_by_name(server_choice).stop()

                  case 4: #restart services
                        server_choice = input("Please enter the name of the service you want to stop: ")
                        Server.identify_by_name(server_choice).restart()
                  case 5: #Display service status
                        service_choice=input('Chose the service you want to check the status of: ')
                        Service.display_status(service_choice)



print('WELCOME TO HOME LAB MANAGER')
c1=0
while c1!=5:
      main_menu()
      c1=int(input('What would you like to do: '))
      while c1 not in range(1,6):
            c1 = int(input('Please enter a valid input: '))
            if c1 == 5:
                  break
            match c1:
                  case 1:
                        device_works()
                  case 2:
                        server_works()
                  case 3:
                        Network_works()
                  case 4:
                        services_work()