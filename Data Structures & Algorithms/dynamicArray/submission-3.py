class DynamicArray:
    
    def __init__(self, capacity: int):
        self.main = [None] * capacity if capacity > 0 else [None]


    def get(self, i: int) -> int:
        return self.main[i]


    def set(self, i: int, n: int) -> None:
        self.main[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.main[self.getSize()] = n


    def popback(self) -> int:
        position = self.getSize() - 1
        value = self.main[position]
        self.main[position] = None
        return value

    def resize(self) -> None:
        self.main = [self.main[i] for i in range(len(self.main))] + ([None] * len(self.main))


    def getSize(self) -> int:
        size = 0
        for i in self.main:
            size += 1 if i != None else 0
        return size
        
    
    def getCapacity(self) -> int:
        return len(self.main)
