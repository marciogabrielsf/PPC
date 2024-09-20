import threading
class Garrafa:
    
    def __init__(self, id: int):
        self.id = id
        self.semaphore = threading.Semaphore(1);

        
    def pegar(self, name):
        return self.semaphore.acquire(timeout=1)
            
        
    def soltar(self, name):
        self.semaphore.release()
        print(name + " soltou a garrafa")
        
    def livre(self):
        return self.semaphore._value > 0