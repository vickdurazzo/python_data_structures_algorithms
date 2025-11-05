class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        if self.top is None:
            print("\nStack: empty")
            return
            
        print("\nStack Visualization:")
        print(f"Height: {self.height}")
        print("-------------")
        temp = self.top
        while temp is not None:
            if temp == self.top:
                print(f"    {temp.value} ← TOP")
            else:
                print(f"    {temp.value}")
            print("    ↓")
            temp = temp.next
        print("  None")
        print("-------------")
        
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height +=1
        return True 


my_stack = Stack(2)

print('Stack before push(1):')
my_stack.print_stack()

my_stack.push(1)

print('\nStack after push(1):')
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before push(1):
    2

    Stack after push(1):
    1
    2   

"""
