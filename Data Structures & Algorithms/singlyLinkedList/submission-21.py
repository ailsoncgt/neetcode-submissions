class Node:
    def __init__(self, val: int):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0
    
    def get(self, index: int) -> int:
        cur = self.head
        pos = 0
        while cur and pos != index:
            cur = cur.next
            pos += 1
        return cur.value if cur else -1

    def insertHead(self, val: int) -> None:
        head = Node(val)
        old_head = self.head
        head.next = old_head
        self.head = head
        self.tail = head if(self.tail is None and self.head.next is None) else self.tail
        self.lenght += 1
        

    def insertTail(self, val: int) -> None:
        tail = Node(val)
        old_tail = self.tail
        self.tail = tail
        if old_tail:
            old_tail.next = tail
        self.head = tail if self.head is None else self.head
        self.lenght += 1

    def remove(self, index: int) -> bool:
        if self.lenght <= index:
            return False
        if index == 0 and self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next if self.head else None
            return True
        elif not self.head:
            return False
        
        # self.print()
        cur = self.head
        prev = cur
        pos = 0
        while cur and pos != index:
            prev = cur
            cur = cur.next
            pos += 1
        if pos == index:
            prev.next = cur.next if cur else None
            if cur == self.tail:
                self.tail = cur.next if cur.next else prev
            return True
        return False

        

    def getValues(self) -> List[int]:
        lst = []
        cur = self.head
        while cur:
            lst.append(cur.value)
            cur = cur.next
        return lst
        
        
