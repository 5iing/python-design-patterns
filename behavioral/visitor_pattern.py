from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def accept(self, miner: "Miner") -> int: ... 
    
class Miner(ABC):
    @abstractmethod 
    def mine(self) -> None: ... 
    
    @abstractmethod 
    def accept_visit(self, visitor: "Visitor") -> int: ...
    
class IncomeVisitor(Visitor): 
    def accept(self, miner: Miner) -> int:
        return miner.income
    
class TimesVisitor(Visitor): 
    def accept(self, miner: Miner) -> int:
        return miner.times_ago
    
class BitcoinMiner(Miner): 
    def __init__(self):
        self.income = 0
        self.times_ago = 0
    
    def mine(self) -> None: 
        self.income += 100
        self.times_ago += 1
        print("im mining bitcoin")
        print(f"i got {self.income}$")
        
    def accept_visit(self, visitor: Visitor) -> int:
        return visitor.accept(self)
        
if __name__ == '__main__': 
    miner = BitcoinMiner()
    income = IncomeVisitor()
    times = TimesVisitor()
    
    miner.mine()
    miner.mine()
    
    print("")
    
    now_income = miner.accept_visit(income)
    how_many_times = miner.accept_visit(times)
    print(f"{now_income}$, {how_many_times} times")