import copy 
from abc import * 
from typing import Self

class DocumentTemplate(ABC): 
    @abstractmethod        
    def peek(self) -> None: ...

    @abstractmethod
    def clone(self) -> Self: ...
            
class JobApplyTemplate(DocumentTemplate): 
    def __init__(self, title: str, body: str, stack: str):
        self.title = title 
        self.body = body 
        self.stack = stack
        
    def peek(self) -> None:
        print(f"{self.title}, {self.body}, {self.stack}")
        
    def clone(self) -> Self:
        return copy.deepcopy(self)

class InviteTemplate(DocumentTemplate):
    def __init__(self, person_name: str, date: str):
        self.person_name = person_name
        self.data = date
    
    def peek(self) -> None: 
        print(f"{self.person_name} tryna hangout at {self.date}?")
        
    def clone(self) -> Self:
        return copy.deepcopy(self)
    
def main():
    first_application = JobApplyTemplate(title='a', body='b', stack='c')
    first_application.peek()
    second_application = first_application.clone()
    second_application.peek() 
    
if __name__ == '__main__':
    main()