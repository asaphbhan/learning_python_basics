import time as t
class Service:
    count=0
    services=[]
    def __init__(self,Name,Port,Version):
        Service.count+=1
        Service.services.append(self)
        self._Name=Name
        self._Port=Port
        self._Status = 'Down'
        self._Version = Version

    @property
    def Name(self):
        return self._Name

    @classmethod
    def identify_by_name(cls, name):
        for i in Service.services:
            if i._Name == name:
                return i
        else:
            return 'No such device found.'

    @property
    def Port(self):
        return self._Port

    @property
    def Status(self):
        return self._Status

    @property
    def Version(self):
        return self._Version

    def __str__(self) -> str:
        return (f"{self._Name} is connected to {self._Port},\n"
                f"is currently {self._Status} and running version {self._Version}.")

    @staticmethod
    def service_menu():
        print('=====Server Menu=====\n1. List services\n2. Start services\n3. Stop services\n4. Restart services\n'
              '5. Display service status\n6. Back')

    def start(self):
        if self._Status == "Down":
            print(f'{self._Name} is now Live.')
            self._Status='Live'
        else:
            print(f'{self._Name} is already Live')

    def stop(self):
        if self._Status == "Live":
            print(f'{self._Name} is now Down.')
            self._Status='Down'
        else:
            print(f'{self._Name} is already Down')

    def restart(self):
        if self._Status == "Down":
            print(f'{self._Name} is now Down,first start it.')
        else:
            print(f'{self._Name}is Restarting.',end='')
            for i in range(0,4):
                t.sleep(1)
                print('.',end='')
            print(f'The service named {self._Name} restarted successfully.')

    @classmethod
    def display_status(cls,service_name):
        found=False
        for i in cls.services:
            if i._Name == service_name:
                print(f'{i._Name} is currently {i._Status}.')
                found=True
                break
        if not found:
            print("A service with that name doesn't exist.")

if __name__ == '__main__':
    service1=Service('Bada Bawal',3,2.35)
    service2 = Service('Bada_Bakwas', 3, 2.35)
    service3 = Service('Not interested', 3, 2.35)
    for i in Service.services:
        print(i)