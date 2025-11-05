class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if self.head is None:
            print("Empty list")
            return
            
        temp = self.head
        print("\nDoubly Linked List Visualization:")
        print(f"Length: {self.length}\n")
        while temp is not None:
            prev_val = temp.prev.value if temp.prev else "None"
            next_val = temp.next.value if temp.next else "None"
            
            # Add indicators for head and tail nodes
            node_position = []
            if temp == self.head:
                node_position.append("HEAD")
            if temp == self.tail:
                node_position.append("TAIL")
            position_str = " (" + ", ".join(node_position) + ")" if node_position else ""
            
            print(f'Node: {temp.value}{position_str}')
            print(f'← Prev: {prev_val}')
            print(f'→ Next: {next_val}')
            print('-------------------')
            #print(temp.value)
            temp = temp.next
                
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length ==0:
            return None
        
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        
        if self.length >= 2 :
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
            
            self.length -= 1
            
            
            return temp
        
    def prepend(self,value):
        
        new_node = Node(value)
        
        if self.head is None:
            self.append(new_node.value)
            
            return True
        else:
            temp = self.head
            new_node.next = temp
            temp.prev = new_node
            self.head = new_node
            self.length += 1
            return True 
    
    def pop_first(self):
        if self.head is None:
            return None
        if self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        
        temp = self.head
        
        temp_next = temp.next
        self.head = temp_next
        self.head.prev = None
        self.length -= 1
        return temp
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.prev
        return temp 
        
        


my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)

my_doubly_linked_list.print_list()


print('Get node from first half of DLL:')
print(my_doubly_linked_list.get(1).value)

print('\nGet node from second half of DLL:')
print(my_doubly_linked_list.get(2).value)


"""
    EXPECTED OUTPUT:
    ----------------
    Get node from first half of DLL:
    1

    Get node from second half of DLL:
    2

"""