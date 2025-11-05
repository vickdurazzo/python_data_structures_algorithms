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



my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)

my_doubly_linked_list.print_list()
# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop().value)
my_doubly_linked_list.print_list()
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop().value)
my_doubly_linked_list.print_list()
# (0) Items - Returns None
print(my_doubly_linked_list.pop())



"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
