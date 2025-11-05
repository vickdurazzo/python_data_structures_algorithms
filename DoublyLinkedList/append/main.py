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
        print(f"Length: {self.length}")
        while temp is not None:
            prev_val = temp.prev.value if temp.prev else "None"
            next_val = temp.next.value if temp.next else "None"
            print(f'Node: {temp.value}')
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
            


my_doubly_linked_list = DoublyLinkedList(1)

my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)


print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')

print('Doubly Linked List:')
my_doubly_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Doubly Linked List:
    1
    2
    
"""
