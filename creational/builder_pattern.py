from abc import * 
from typing import Self

class Pizza():
    def __init__(self):
        self.parts = []
        
    def add(self, param) -> None:
        self.parts.append(param)
    
    def show(self) -> None: 
        print(f"\033[92myour pizza with {self.parts}\033[0m")


class Builder(ABC):
    @abstractmethod
    def reset(self): ...
    
    @abstractmethod
    def prepare_dough(self): ...
    
    @abstractmethod
    def spread_tomato_sauce(self): ...
    
    @abstractmethod
    def sprinkle_cheese(self): ...
    
    @abstractmethod
    def add_topping(self): ...
    
    @abstractmethod
    def grill(self): ...
    
    
class PotatoPizzaBuilder(Builder):
    def __init__(self):
        self.pizza = Pizza()
    
    def reset(self) -> Self:
        self.pizza = Pizza()
        return self
        
    def prepare_dough(self) -> Self:
        self.pizza.add('thin dough')
        self.pizza.show()
        return self
        
    def spread_tomato_sauce(self) -> Self:
        self.pizza.add('tomato sauce')
        self.pizza.show() 
        return self
    
    def sprinkle_cheese(self) -> Self:
        self.pizza.add('cheese')
        self.pizza.show() 
        return self
    
    def add_topping(self) -> Self:
        self.pizza.add('potato')
        self.pizza.add('bacon')
        self.pizza.add('mayo')
        self.pizza.show() 
        return self 
    
    def grill(self) -> Pizza:
        print("your pizza is here!")
        return self.pizza
    
class PeperoniPizzaBuilder(Builder):
    def __init__(self):
        self.pizza = Pizza()
    
    def reset(self) -> Self:
        self.pizza = Pizza()
        return self
        
    def prepare_dough(self) -> Self:
        self.pizza.add('thin dough')
        self.pizza.show()
        return self
        
    def spread_tomato_sauce(self) -> Self:
        self.pizza.add('tomato sauce')
        self.pizza.show() 
        return self
    
    def sprinkle_cheese(self) -> Self:
        self.pizza.add('cheese')
        self.pizza.show() 
        return self
    
    def add_topping(self) -> Self:
        self.pizza.add('peperoni')
        self.pizza.add('more peperoni')
        self.pizza.add('moooooore peperoni')
        self.pizza.show() 
        return self 
    
    def grill(self) -> Pizza:
        print("your pizza is here!")
        return self.pizza
    
def main():
    potato_pizza = (PotatoPizzaBuilder()
          .prepare_dough()
          .spread_tomato_sauce()
          .sprinkle_cheese()
          .add_topping()
          .grill()
         )
    
    pepr_pizza_without_dough = (PeperoniPizzaBuilder().add_topping().grill())
    
if __name__ == '__main__':
    main()
    