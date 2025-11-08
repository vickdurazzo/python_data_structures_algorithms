class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self,current_node,value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left,value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right,value)
        return current_node
    
          
    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root,value)
    

    def __r_contains(self,current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
    
    def contains(self,value):
        return self.__r_contains(self.root, value)
    
    def __delete_node(self,current_node,value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left,value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right,value)
        else:
            return current_node
    
    def delete_node(self,value):
        self.__delete_node()
    
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
my_tree = BinarySearchTree() # Cria uma nova árvore (vazia)
my_tree.insert(47) # Insere 47 (se torna a raiz)
my_tree.insert(21) # 21 < 47, vai para a esquerda
my_tree.insert(76) # 76 > 47, vai para a direita
my_tree.insert(18) # 18 < 47 (esquerda), 18 < 21 (esquerda)
my_tree.insert(27) # 27 < 47 (esquerda), 27 > 21 (direita)
my_tree.insert(52) # 52 > 47 (direita), 52 < 76 (esquerda)
my_tree.insert(82) # 82 > 47 (direita), 82 > 76 (direita)

# Print the tree
print("\nTree visualization:")
my_tree.print_tree()

# Testando o método 'contains'
print("\nA árvore contém 100?", my_tree.contains(100)) # Deve ser False
print("A árvore contém 27?", my_tree.contains(27))   # Deve ser True