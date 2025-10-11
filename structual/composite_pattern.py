from abc import *

class Component(ABC):
    @abstractmethod
    def get_size(self) -> int: ...
    
    @abstractmethod
    def display(self, indent: int = 0) -> None: ...
    
class File(Component):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
    
    def get_size(self) -> int:
        return self.size
    
    def display(self, indent: int = 0) -> None: 
        print(" " * indent + f"- {self.name} (file, {self.size} bytes)")
        
class Folder(Component):
    def __init__(self, name: str):
        self.name = name
        self.children: list[Component] = []

    def add(self, comp: Component) -> None:
        self.children.append(comp)

    def remove(self, comp: Component) -> None:
        self.children.remove(comp)

    def get_size(self) -> int:
        total = 0
        for c in self.children:
            total += c.get_size()
        return total

    def display(self, indent: int = 0) -> None:
        print(" " * indent + f"+ {self.name} (folder, {self.get_size()} bytes total)")
        for c in self.children:
            c.display(indent + 2)

if __name__ == '__main__':
    root = Folder("root")
    root.add(File("a.txt", 100))
    root.add(File("b.txt", 200))

    print("== tree ==")
    root.display()
    print("size:", root.get_size())