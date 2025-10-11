from abc import * 

class Service(ABC):
    @abstractmethod
    def request(self) -> None: ...
    

class UserService(Service):
    def request(self) -> None: 
        print(self.__class__.__name__, "handled!")
      
        
class ProxyService(Service): 
    def __init__(self, svc: Service):
        self.svc = svc
    
    def request(self) -> None: 
        print("proxy handled!")
        self.svc.request()
        

if __name__ == '__main__': 
    
    usvc = UserService() 
    usvc.request()
    
    print("")
    
    psvc = ProxyService(usvc)
    psvc.request()