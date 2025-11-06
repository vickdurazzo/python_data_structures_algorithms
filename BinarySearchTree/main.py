class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self,value):
        if self.root is None:
            return False
        temp = self.root
        while (True):
            if value == temp.value:
                return True
            if value < temp.value:
                if temp.left == value:
                    return True
                if temp.left == None:
                    return False
                temp = temp.left
            else:
                if temp.right == value:
                    return True
                if temp.right == None:
                    return False
                temp = temp.right
    
    def print_tree(self):
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1  
        
        root = self.root
        nlevels = height(root)
        width = pow(2, nlevels+1)

        q = [(root, 0, width, 'c')]
        levels = []

        while q:
            node, level, x, align = q.pop(0)
            if node:            
                if len(levels) <= level:
                    levels.append([])
            
                levels[level].append([node, level, x, align])
                seg = width // (pow(2, level+1))
                q.append((node.left, level+1, x-seg, 'l'))
                q.append((node.right, level+1, x+seg, 'r'))

        for i, l in enumerate(levels):
            pre = 0
            preline = 0
            linestr = ''
            pstr = ''
            seg = width // (pow(2, i+1))
            for n in l:
                valstr = str(n[0].value)  # Changed from val to value
                if n[3] == 'r':
                    linestr += ' ' * (n[2]-preline-1-seg-seg//2) + '¯' * (seg + seg//2) + '\\'
                    preline = n[2] 
                if n[3] == 'l':
                    linestr += ' ' * (n[2]-preline-1) + '/' + '¯' * (seg+seg//2)  
                    preline = n[2] + seg + seg//2
                pstr += ' ' * (n[2]-pre-len(valstr)) + valstr
                pre = n[2]
            print(linestr)
            print(pstr)


# Test the tree
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

# Print the tree
print("\nTree visualization:")
my_tree.print_tree()

print(my_tree.contains(100))