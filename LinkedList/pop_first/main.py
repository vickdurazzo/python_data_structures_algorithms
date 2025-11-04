class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        values.append("None")
        print(" -> ".join(values))
            
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        
        current_head = self.head
        self.head = self.head.next  
        current_head.next = None
        self.length -= 1
        if self.length == 0 :
            self.tail = None
        return current_head
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)


def test_pop_first_until_empty(linked_list):
    print("--- Testing pop_first until list is empty ---")
    while linked_list.length > 0:
        popped_node = linked_list.pop_first()
        print(f"\nPopped Node Value: {popped_node.value}")
        print(f"Current Length: {linked_list.length}")
        if linked_list.head:
            print(f"New Head: {linked_list.head.value}")
        else:
            print("New Head: None")
        linked_list.print_list()
    
    # Test popping from an already empty list
    print("\n--- Testing pop_first on an empty list ---")
    popped_node = linked_list.pop_first()
    print(f"Popped Node: {popped_node}")
    print(f"Current Length: {linked_list.length}")
    print(f"Head: {linked_list.head}")
    print(f"Tail: {linked_list.tail}")
    linked_list.print_list()
    print("------------------------------------------")


test_pop_first_until_empty(my_linked_list)

"""

print('Before pop():')
print('----------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()


print('\n\nAfter pop():')
print('---------------')
print('Popped Node Value:', my_linked_list.pop_first().value)
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()



print("\n----- Additional Tests for pop_first() -----\n")
# (1) Item -  Returns 1 Node
print(my_linked_list.pop_first().value)
print("Head:", my_linked_list.head)
print("Tail:", my_linked_list.tail)
print("Length:", my_linked_list.length, "\n")
print("Linked List:")
my_linked_list.print_list()

print("\n----- Additional Tests for pop_first() -----\n")
# (0) Items - Returns None
print(my_linked_list.pop_first())

"""

"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
