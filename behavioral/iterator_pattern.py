from abc import * 

class Iterator(ABC):
    @abstractmethod
    def __iter__(self): ...
        
    @abstractmethod
    def __next__(self) -> str: ...

class NameCollection:
    def __init__(self, names: list[str]) -> None:
        self.names = names
    
    def get_first_name_iterator(self):
        return FirstNameIterator(self.names)
    
    def get_last_name_iterator(self):
        return LastNameIterator(self.names)

class FirstNameIterator(Iterator):
    def __init__(self, names: list[str]) -> None:
        self.names = names
        self._index = 0
        
    def __iter__(self): 
        return self
    
    def __next__(self) -> str: 
        if self._index >= len(self.names):
            raise StopIteration
        name = self.names[self._index]
        self._index += 1
        return name.split()[0]  
        
class LastNameIterator(Iterator):
    def __init__(self, names: list[str]) -> None:
        self.names = names
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self._index >= len(self.names):
            raise StopIteration
        name = self.names[self._index]
        self._index += 1
        return name.split()[-1]

if __name__ == '__main__':
    names = ["yeonwoo lee", "liam lawson", "calros sainz"]
    collection = NameCollection(names)

    for first_name in collection.get_first_name_iterator():
        print(first_name)

    print("")

    for last_name in collection.get_last_name_iterator():
        print(last_name)