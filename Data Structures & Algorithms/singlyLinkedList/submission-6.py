class LinkedList:
    
    def __init__(self):
        #initialize an empty linked list
        self.head = None

    def get(self, index: int) -> int:
        #return the value of the ith node (0-indexed)
        #If the index is out of bounds, return -1
        current = self.head
        i = 0

        if index < 0:
            return -1

        while i < index:
            if current == None:
                return -1

            current = current.next
            i += 1

        if current == None:
            return -1

        return current.data

    def insertHead(self, val: int) -> None:
        #will insert a node with val at the head of the list
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        #insert a node with val at the tail of the list
        #go through to the until you reach last node, insert new node
        current = self.head
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        while current.next is not None:
            current = current.next

        current.next = new_node

    def remove(self, index: int) -> bool:
        #remove the ith node (0-indexed) 
        #If the index is out of bounds, return false, otherwise return true
        
        current = self.head #idex 0
        i = 0 #keep track with current

        if self.head is None:
            return False


        if index == 0:
            self.head = self.head.next
            return True

        while index-1 > i:
            if current.next == None:
                return False
            current = current.next
            i += 1
        if current.next == None:
            return False
        else:
            current.next = current.next.next
            return True

    def getValues(self) -> List[int]:
        #return an array of all the values in the linked list, ordered from head to tail
        values = []
        current = self.head
        while current != None:
            values.append(current.data)
            current = current.next
        return values

class Node:
    def __init__(self, data):
        self.data = data    # The value stored in the node
        self.next = None    # Reference to the next node (initially None)
