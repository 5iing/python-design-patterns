from abc import *

class Strategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> int: ...
    
class Add(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a + b

class Multiply(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a * b

class Calculator:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def calculate(self, a: int, b: int) -> int:
        return self._strategy.execute(a, b)

if __name__ == '__main__':
    calc = Calculator(Add())
    print(calc.calculate(3, 5))

    calc.set_strategy(Multiply())
    print(calc.calculate(3, 5))