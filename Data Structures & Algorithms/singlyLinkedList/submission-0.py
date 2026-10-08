class Node:
    def __init__(self, val: int):
        self.val= val
        self.next= None

class LinkedList:
    
    def __init__(self):
        self.head= None

    
    def get(self, index: int) -> int:
        current= self.head
        current= self.head
        i=0
        while current is not None:
            if(i == index):
                return current.val
            else:
                current= current.next
                i = i+1
        return -1
        
        

    def insertHead(self, val: int) -> None:
        N=Node(val)
        N.next=self.head
        self.head= N
        
    def insertTail(self, val: int) -> None:

        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node


    def remove(self, index: int) -> bool:
        if(self.head is None):
            return False
        current= self.head
        i=0
        if(index==0):
            self.head=self.head.next
            return True
        while(current.next is not None):
            if(i+1== index):
                current.next=current.next.next
                return True
            current=current.next
            i+=1
            
        return False

    def getValues(self) -> List[int]:
        T= []
        current= self.head
        while current is not None:
            T.append(current.val)
            current=current.next
        return T

        
        
        
