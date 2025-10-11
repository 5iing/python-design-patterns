from abc import *

class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...

class Light:
    def __init__(self):
        self.on = False
    
    def turn_on(self):
        self.on = True
        print("Light turned on")
    
    def turn_off(self):
        self.on = False
        print("Light turned off")

class TV:
    def __init__(self):
        self.on = False
    
    def turn_on(self):
        self.on = True
        print("TV turned on")
    
    def turn_off(self):
        self.on = False
        print("TV turned off")

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()

class TVOnCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv
    
    def execute(self):
        self.tv.turn_on()

class TVOffCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv
    
    def execute(self):
        self.tv.turn_off()

class RemoteControl:
    def __init__(self):
        self.command = None
    
    def set_command(self, command: Command):
        self.command = command
    
    def press_button(self):
        if self.command:
            self.command.execute()

if __name__ == '__main__':
    light = Light()
    tv = TV()
    
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    tv_on = TVOnCommand(tv)
    tv_off = TVOffCommand(tv)
    
    remote = RemoteControl()
    
    remote.set_command(light_on)
    remote.press_button()
    
    remote.set_command(tv_on)
    remote.press_button()
    
    remote.set_command(light_off)
    remote.press_button()
    
    remote.set_command(tv_off)
    remote.press_button()