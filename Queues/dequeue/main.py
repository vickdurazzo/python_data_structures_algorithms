class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
        
    def print_queue(self):
        if self.first is None:
            print("\nQueue: empty")
            return
            
        print("\nQueue Visualization:")
        print(f"Length: {self.length}")
        print("-------------------")
        print("  FIRST              LAST")
        print("   ↓                  ↓")
        temp = self.first
        queue_items = []
        
        while temp is not None:
            if temp == self.first and temp == self.last:
                queue_items.append(f"[{temp.value}]*")  # Both first and last
            elif temp == self.first:
                queue_items.append(f"[{temp.value}]")  # First element
            elif temp == self.last:
                queue_items.append(f"[{temp.value}]")  # Last element
            else:
                queue_items.append(f"[{temp.value}]")  # Middle elements
            temp = temp.next
            
        # Print the queue with proper spacing
        print("  " + " → ".join(queue_items))
        print("\n* Note: [X]* means the element is both FIRST and LAST")
        print("-------------------")

    def enqueue(self,value):
        
        new_node = Node(value)
        if self.first ==  None:
            
            self.first = new_node
            self.last = new_node
            self.length = 1
            return True
        
        self.last.next = new_node
        self.last = new_node
        self.length +=1
        return True
    
    def dequeue(self):
        temp = self.first
        if self.first == None:
            return None
        if self.first.next == None:
            self.first = None
            self.last = None
            self.length -=1
            return temp
        
        self.first = temp.next 
        self.length -=1
        
        return temp
        

my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.print_queue()
# (2) Items - Returns 2 Node
print(my_queue.dequeue().value)
my_queue.print_queue()
# (1) Item -  Returns 1 Node
print(my_queue.dequeue().value)
my_queue.print_queue()
# (0) Items - Returns None
print(my_queue.dequeue())



"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    None

"""