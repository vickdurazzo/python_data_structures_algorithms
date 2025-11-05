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
        
my_queue = Queue(1)

print('Queue before enqueue(2):')
my_queue.print_queue()

my_queue.enqueue(2)

my_queue.enqueue(3)

my_queue.enqueue(4)

print('\nQueue after enqueue(2):')
my_queue.print_queue()



"""
    EXPECTED OUTPUT:
    ----------------
    Queue before enqueue(2):
    1

    Queue after enqueue(2):
    1
    2

"""