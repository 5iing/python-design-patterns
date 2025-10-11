from abc import *

class Coffee(ABC): 
    @abstractmethod
    def drink(self) -> None: ...
    
    @abstractmethod
    def get_cost(self) -> int: ...

class VanillaLatte(Coffee):
    def drink(self) -> None: 
        print("Vanilla Latte drunk")
        
    def get_cost(self) -> int:
        return 4000

class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    
    def drink(self) -> None:
        self._coffee.drink()
    
    def get_cost(self) -> int:
        return self._coffee.get_cost()

class Sugar(CoffeeDecorator):
    def drink(self) -> None:
        print("Sugar added")
        super().drink()
    
    def get_cost(self) -> int:
        return super().get_cost() + 500

class Milk(CoffeeDecorator):
    def drink(self) -> None:
        print("Milk added")
        super().drink()
    
    def get_cost(self) -> int:
        return super().get_cost() + 800

class WhippedCream(CoffeeDecorator):
    def drink(self) -> None:
        print("Whipped cream added")
        super().drink()
    
    def get_cost(self) -> int:
        return super().get_cost() + 1000

if __name__ == '__main__': 
    
    basic_coffee = VanillaLatte()
    basic_coffee.drink()
    print(f"Cost: {basic_coffee.get_cost():,}won")
    
    print("")

    coffee_with_sugar = Sugar(basic_coffee)
    coffee_with_sugar.drink()
    print(f"Cost: {coffee_with_sugar.get_cost():,}won")
    
    print("")
    
    coffee_with_milk = Milk(coffee_with_sugar)
    coffee_with_milk.drink()
    print(f"Cost: {coffee_with_milk.get_cost():,}won")
    
    print("")
    
    coffee_with_cream = WhippedCream(coffee_with_milk)
    coffee_with_cream.drink()
    print(f"Cost: {coffee_with_cream.get_cost():,}원")