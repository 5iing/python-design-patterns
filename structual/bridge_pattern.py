from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def power_on(self): ...
    @abstractmethod
    def volume_up(self): ...
    @abstractmethod
    def volume_down(self): ...
    
class TV(Device):
    def __init__(self):
        self.power = 'off'
        self.volume = 0
    
    def power_on(self) -> str:
        self.power = 'on'
        return self.power
        
    def volume_up(self) -> int:
        self.volume += 1
        return self.volume
    
    def volume_down(self):
        self.volume -= 1
        return self.volume
    
class Radio(Device):
    def __init__(self):
        self.power = 'off'
        self.volume = 0
    
    def power_on(self) -> str:
        self.power = 'on'
        return self.power
        
    def volume_up(self) -> int:
        self.volume += 1
        return self.volume
    
    def volume_dowm(self):
        self.volume -= 1
        return self.volume
    
class Controller(ABC):
    @abstractmethod
    def power_button(self): ...
    @abstractmethod
    def volume_up_button(self): ...
    @abstractmethod
    def volume_down_button(self): ...
    
class RemoteController(Controller):
    def __init__(self, target: Device):
        self.target = target
    
    def power_button(self):
        self.target.power_on()
        print(f"power on, {self.target.__class__.__name__}")
        
    def volume_up_button(self):
        self.target.volume_up()
        print(f"volume up, {self.target.volume} {self.target.__class__.__name__}")
        
    def volume_down_button(self):
        self.target.volume_down()
        print(f"volume down, {self.target.volume} {self.target.__class__.__name__}")
        
if __name__ == '__main__':
    tv = TV()
    r = RemoteController(tv)
    
    r.power_button()
    r.volume_up_button() 
    r.volume_down_button()