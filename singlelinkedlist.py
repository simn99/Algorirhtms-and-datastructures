

#Single linked list 

from numpy import nonzero


class Node(): # paretn class 
    
    def __init__(self,data):

        self.data = data
        self.next = None

class linkedlist(Node): #child class
    
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

    def delete(self,data):
        
        current = self.head
        if current is not None:
            if current.data == data:
                self.head =current.next
                return
        
        # Search for the key to be deleted,
        while (current is not None):

            if current.data ==data:
                break
            prev = current
            current = current.next

        prev.next= current.next
        
        #if data was not present in linked list 

        if current ==None: 
            return

    def show(self): 
        #will display the nodes present in the list
        current =self.head

        if self.head is None: 
            return 
        while current is not None: 
            print(current.data,end=" ")
            current = current.next


def main():

    obj = linkedlist()
    obj.add_node(2)
    obj.add_node(5)

    obj.add_node(20)
    obj.delete(5)
    obj.show()

if __name__ == "__main__":
    main()





            


