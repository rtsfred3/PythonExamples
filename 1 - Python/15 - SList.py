class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    
    def addNode(self, value):
        node = Node(value)
        r = self.head
        while(r.next != None):
            r = r.next
        r.next = node
    
    def removeNode(self, value):
        r = self.head
        if r.value == value:
            self.head = r.next
        else:
            while r.next.value != value:
                r = r.next
            r.next = r.next.next
    
    def printAllValues(self, msg=""):
        r = self.head     
        print("\nHead points to ", id(self.head))
        print("Printing the values in the list ---", msg, "---")
        while(r.next != None):
            print(id(r), r.value, id(r.next))
            r = r.next        
        print(id(r), r.value, id(r.next))

  
list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.printAllValues("Attempt 1")

list.removeNode(9)
list.removeNode(5)
list.removeNode(1)
list.printAllValues("Attempt 2")