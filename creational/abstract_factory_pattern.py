from abc import * 

class Food(ABC):
    @abstractmethod
    def eat(self): ...
    
class Beverage(ABC):
    @abstractmethod
    def drink(self): ...


class Bibimbap(Food):
    def eat(self):
        print("im eating bibimbap")
        
class Sikhye(Beverage):
    def drink(self):
        print("im drinking sikhye")
        

class Ramen(Food):
    def eat(self):
        print("im eating ramen")
        
class Matcha(Beverage):
    def drink(self):
        print("im drinking matcha")
        

class FnbFactory(ABC):
    @abstractmethod
    def make_food(self) -> Food: ... 
    
    @abstractmethod
    def make_beverage(self) -> Beverage: ...
    
class ConcreteKoreanFnbFactory(FnbFactory):
    def make_food(self) -> Food:
        return Bibimbap()
    
    def make_beverage(self) -> Beverage:
        return Sikhye()
    
class ConcreteJapaneseFnbFactory(FnbFactory):
    def make_food(self) -> Food:
        return Ramen()
    
    def  make_beverage(self) -> Beverage:
        return Matcha()
    
def main():
    for factory in [ConcreteKoreanFnbFactory(), ConcreteJapaneseFnbFactory()]:
        food = factory.make_food()
        beverage = factory.make_beverage()
        food.eat()
        beverage.drink()
    
if __name__ == '__main__':
    main()