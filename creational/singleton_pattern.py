from abc import * 

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta): 
    def __init__(self):
        print("Log initialized")
    
    def log(self, text): 
        print(f"[LOG]: {text}")
        
if __name__ == '__main__':
    first_logger = Logger() 
    second_logger = Logger() 
    
    first_logger.log("dkdk")
    second_logger.log("hello")
    
    print("is first_logger == second_logger?", first_logger is second_logger)