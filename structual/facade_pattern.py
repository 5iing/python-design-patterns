from abc import *

class Device(ABC):
    @abstractmethod
    def power_on(self) -> None: ...
    
    @abstractmethod
    def power_off(self) -> None: ...
    
    @abstractmethod
    def volume_up(self) -> None: ... 
    
    @abstractmethod 
    def volume_down(self) -> None: ...
    
class Speaker(Device): 
    def power_on(self):
        print(self.__class__.__name__, ": power on")
        
    def power_off(self):
        print(self.__class__.__name__, ": power off")
        
    def volume_up(self):
        print(self.__class__.__name__, ": volume up")
        
    def volume_down(self):
        print(self.__class__.__name__, ": volume down")

class Light(ABC):
    @abstractmethod
    def power_on(self) -> None: ...
    
    @abstractmethod
    def power_off(self) -> None: ...
    
class MoodLantern(Light): 
    def power_on(self):
        print(self.__class__.__name__, ": power on")
        
    def power_off(self):
        print(self.__class__.__name__, ": power off")
    
    
class IotControllerFacade:
    def __init__(self, l: Light, d: Device):
        self.light = l
        self.device = d
        
    def light_on(self) -> None: 
        self.light.power_on()
    
    def light_off(self) -> None: 
        self.light.power_off()
    
    def device_on(self) -> None: 
        self.device.power_on()
    
    def device_off(self) -> None: 
        self.device.power_off()
    
if __name__ == '__main__': 
    speaker = Speaker() 
    lantern = MoodLantern()
    
    facade = IotControllerFacade(lantern, speaker)
    
    
    facade.light_on()
    facade.device_on()
    
    facade.device.volume_up()
    facade.device.volume_down()
    
    facade.light_off()
    facade.device_off()
    