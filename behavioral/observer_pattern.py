from abc import * 

class Observer(ABC):
    @abstractmethod
    def update(self): ...
    
class Subject():
    def __init__(self):
        self.observers = []
        self.state = None
        
    def get_state(self) -> object:
        return self.state
    
    def attach(self, observer: Observer):
        self.observers.append(observer)
    
    def detach(self, observer: Observer): 
        self.observers.remove(observer)
    
    def set_state(self, state): 
        self.state = state
        self.notify()
    
    def notify(self):
        for i in self.observers:
            i.update(self)
            
class ConsoleObserver(Observer):
    def update(self, subject):
        print(f"console: {subject.get_state()}")

class AlertObserver(Observer):
    def update(self, subject):
        print(f"alert: {subject.get_state()}")


if __name__ == '__main__':
    subj = Subject() 
    
    console = ConsoleObserver() 
    alert = AlertObserver() 
    
    subj.observers = [console, alert]
    subj.set_state("hello")