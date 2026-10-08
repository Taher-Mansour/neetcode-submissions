class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.size = 0
        self.tab = [0] * capacity


    def get(self, i: int) -> int:
        return self.tab[i]



    def set(self, i: int, n: int) -> None:
        self.tab[i]=n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize() 
        self.tab[self.size] = n
        self.size += 1

    def popback(self) -> int:
        x=self.tab[self.size-1]
        self.size=self.size-1
        return x
    def resize(self):
        new_tab = [0] * (self.capacity * 2)
        for i in range(self.size):           
            new_tab[i] = self.tab[i]
        self.tab = new_tab                  
        self.capacity *= 2 


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
