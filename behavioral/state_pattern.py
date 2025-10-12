from abc import * 

class LightState(ABC):
    @abstractmethod
    def toggle(self): ...
    
class OnState(LightState):
    def toggle(self, context):
        print("turn off")
        context.set_state(OffState())
        
class OffState(LightState):
    def toggle(self, context):
        print("turn on")
        context.set_state(OnState())
        
class Light():
    def __init__(self): 
        self.state = OffState()
        
    def set_state(self, state):
        self.state = state
        
    def press(self):
        self.state.toggle(self)
        
if __name__ == '__main__':
    light = Light()
    light.press()
    light.press()
    light.press()
        