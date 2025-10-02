from abc import *
import base64

class FileFormat(ABC):
    @abstractmethod
    def read(self): ...
    
class TxtFormat(FileFormat):
    def __init__(self, content): 
        self.type = 'txt'
        self.content = content
        
    def read(self):
        print(f"TXT: {self.content}")

class RtfLibrary():
    def __init__(self, content): 
        self.type = 'rtf'
        
        self.encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        content = self.encoded_content
        self.content = content
        
    def get_encoded_data(self):
        print(f"RTF: {self.content}")
        
class RtfAdaptor(): 
    def __init__(self, content):
        self.decoded = base64.b64decode(content.encode('utf-8')).decode('utf-8')
        
    def get_data(self):
        print(f"RTF(decoded): {self.decoded}")
        
class FileViewer(): 
    def read_file(self, textfile: FileFormat):
        textfile.read()
        
class FileViewrAdaptor(FileViewer):
    def read_file(self, textfile: FileFormat):
        if textfile.type == 'rtf':
            decoded_content = base64.b64decode(textfile.content.encode('utf-8')).decode('utf-8')
            print(f"RTF (decoded): {decoded_content}")
        else:
            textfile.read()
            
if __name__ == '__main__':
    txt = TxtFormat("hello wordl")
    rtf = RtfLibrary("abcdefghijk")
    
    fv = FileViewer()
    rta = RtfAdaptor(rtf.content)
    
    fv.read_file(txt)
    rtf.get_encoded_data()
    rta.get_data()    