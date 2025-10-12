from abc import * 

class ChatRoom(): 
    def show_message(self, origin: str, message: str) -> None: 
        print(f"{origin}, {message}")
        
class User():
    def __init__(self, name: str, chatroom: ChatRoom) -> None:
        self.name = name
        self.chatroom = chatroom

    def send(self, message: str) -> None:
        self.chatroom.show_message(origin=self.name, message=message)
        
class System():
    def __init__(self, name: str, chatroom: ChatRoom) -> None:
        self.name = name
        self.chatroom = chatroom

    def send(self, message: str) -> None:
        self.chatroom.show_message(origin=self.__class__.__name__, message=message)
        
if __name__ == '__main__':
    chatroom = ChatRoom() 
    sainz = User("Sainz", chatroom)
    lewis = User("Lewis", chatroom)
    system = System("System", chatroom)
    
    sainz.send("Hello!")
    lewis.send("Hey!")
    system.send("Welcome!")