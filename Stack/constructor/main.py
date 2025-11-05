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


my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""