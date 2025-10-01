from abc import * 

class Coffee():
    def drink(self): 
        print("im drinking coffee")

class CoffeeFactory(ABC):
    @abstractmethod
    def make_coffee(self) -> Coffee:
        ... 

class ConcreteCoffeeFactory(CoffeeFactory):
    def make_coffee(self) -> Coffee:
        return Coffee()
    
if __name__ == '__main__':
    fac = ConcreteCoffeeFactory()
    c = fac.make_coffee()
    c.drink()