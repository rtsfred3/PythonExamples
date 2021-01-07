class Node:
    def __init__(self, value):
        self.before = None
        self.value = value
        self.next = None

class DList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    
    def addNode(self, value):
        node = Node(value)
        r = self.head
        while(r.next != None):
            r = r.next
        r.next = node
        r.next.before = r
    
    def insertNode(self, idx, value):
        r = self.head
        count = 1
        while count != idx:
            r = r.next
            r.next.before = r
            count+=1
        node = Node(value)
        node.next = r.next
        node.before = r
        r.next = node
        r.next.next.before = r.next
    
    def removeNode(self, value):
        r = self.head
        if r.value == value:
            self.head = r.next
            self.head.before = None
        else:
            while r.next != None and r.next.value != value:
                r = r.next
                r.next.before = r
            if r.next.next == None:
                r.next = None
            else:
                r.next = r.next.next
                r.next.before = r
    
    def printAllValues(self, msg=""):
        r = self.head     
        print("\nHead points to ", id(self.head))
        print("Printing the values in the list ---", msg, "---")
        while(r.next != None):
            print(id(r), id(r.before), r.value, id(r.next))
            r = r.next        
        print(id(r), id(r.before), r.value, id(r.next))

  
list = DList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.printAllValues("Attempt 1")

list.removeNode(9)
list.removeNode(1)
list.removeNode(5)
list.addNode(4)
list.addNode(5)
list.printAllValues("Attempt 2")

list.insertNode(2, 2)
list.insertNode(1, 3)
list.printAllValues("Attempt 3")