from abc import * 

class Beverage(ABC):
    def boil_water(self) -> None:
        print("boiling water..")
    
    def pour_in_cup(self) -> None:
        print("pouring in cup..")
        
    def prepare_beverage(self) -> None:
        self.boil_water()
        self.pour_in_cup
        self.brew()
        
    @abstractmethod
    def brew(self): ...
    
class Coffee(Beverage):
    def brew(self):
        print("im brewing coffe with coffee machine")
        
class Tea(Beverage):
    def brew(self):
        print("im brewing tea with Tea bag")
        
if __name__ == '__main__':
    coffee = Coffee() 
    tea = Tea()
    
    coffee.brew()
    tea.brew()