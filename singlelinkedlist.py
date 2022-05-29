

#Single linked list 

class Node(): # children class 
    
    def __init__(self,data):

        self.data = data
        self.next = None

class linkedlist(Node):
    
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self,data):
        #creating new node
        newnode = Node(data)
        #checks whether the head is equal to null which means the list is empty 
        if self.head is None: 
        
         #If the list is empty, both head and tail will point to the newly added node
            self.head = newnode
            self.tail = newnode
        
        # list is not empty-->new node will be added to end of the list
        else:
            self.tail.next = newnode ##tail's next will point to the newly added node
            self.tail = newnode 

    
    def show(self): 
        #will display the nodes present in the list
        current =self.head

        if self.head is None: 
            return 
        while current is not None: 
            print(current.data,end=" ")
            current = current.next



obj = linkedlist()
obj.add_node(2)
obj.add_node(4)

obj.show()





            


