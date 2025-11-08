class Node:
    # O "construtor" é chamado sempre que um novo nó é criado (ex: Node(10))
    def __init__(self, value):
        # Armazena o valor (ex: 10) que este nó representa
        self.value = value
        # O "ponteiro" para o filho da esquerda. Começa como None (vazio).
        self.left = None
        # O "ponteiro" para o filho da direita. Começa como None (vazio).
        self.right = None

class BinarySearchTree:
    # O construtor da árvore
    def __init__(self):
        # A árvore começa vazia. O "root" (raiz) é o nó inicial (o topo da árvore).
        # Se self.root é None, a árvore está vazia.
        self.root = None

    ## --- Método de Inserção ---
    def insert(self, value):
        # 1. Cria um novo nó com o valor fornecido
        new_node = Node(value)
        
        # 2. Verifica se a árvore está vazia
        if self.root is None:
            # Se estiver vazia, o novo nó se torna a raiz
            self.root = new_node
            return True  # Inserção bem-sucedida

        # 3. Se a árvore NÃO está vazia, encontramos onde inserir
        # Começamos pela raiz
        temp = self.root 
        
        # 4. Loop infinito (que será quebrado com um 'return')
        while (True):
            # 5. Verifica se o valor já existe
            if new_node.value == temp.value:
                # BSTs geralmente não permitem duplicatas.
                return False  # Falha na inserção (valor duplicado)

            # 6. Onde o novo nó deve ir?
            if new_node.value < temp.value:
                # Se o novo valor for MENOR, vamos para a ESQUERDA
                if temp.left is None:
                    # 7. Se o "espaço" à esquerda está vazio, inserimos aqui
                    temp.left = new_node
                    return True # Inserção bem-sucedida
                # 8. Se não estiver vazio, descemos na árvore
                temp = temp.left # 'temp' agora é o filho da esquerda e o loop repete
            else:
                # Se o novo valor for MAIOR, vamos para a DIREITA
                if temp.right is None:
                    # 7. Se o "espaço" à direita está vazio, inserimos aqui
                    temp.right = new_node
                    return True # Inserção bem-sucedida
                # 8. Se não estiver vazio, descemos na árvore
                temp = temp.right # 'temp' agora é o filho da direita e o loop repete

    ## --- Método de Busca (Contains) ---
    
    def contains(self, value):
        # 1. Se a árvore está vazia, não pode conter o valor
        # (Neste código, o 'while' abaixo já cuida disso, mas é bom saber)
        
        # 2. Começamos pela raiz
        temp = self.root
        
        # 3. Loop: continue enquanto 'temp' não for None (ou seja, enquanto
        # não "caírmos" da árvore)
        while temp is not None:
            # 4. Compara o valor procurado com o nó atual
            if value < temp.value:
                # Valor é menor? Vá para a esquerda.
                temp = temp.left
            elif value > temp.value:
                # Valor é maior? Vá para a direita.
                temp = temp.right
            else:
                # 5. Não é menor nem maior, é IGUAL! Encontramos.
                return True
                
        # 6. Se o loop terminar (temp se tornou None), é porque
        # chegamos ao fim de um galho e não encontramos o valor.
        return False

    ## --- Método de Visualização ---
    # Este é um método complexo apenas para "desenhar" a árvore no terminal.
    # A lógica dele não é central para a BST, mas sim para a visualização.
    def print_tree(self):
        # Função auxiliar interna para calcular a altura da árvore
        def height(root):
            # Se o nó não existe, sua altura é -1. Se existe, é 1 + a altura do maior filho.
            return 1 + max(height(root.left), height(root.right)) if root else -1
        
        # Pega a raiz da nossa árvore
        root = self.root
        # Calcula a altura total e a largura necessária para o "desenho"
        nlevels = height(root)
        width = pow(2, nlevels+1)

        # 'q' é uma fila (Queue) para fazer uma Busca em Largura (BFS).
        # Armazena (nó, nível, posição_x, alinhamento)
        q = [(root, 0, width, 'c')]
        levels = [] # Armazena os nós separados por nível

        # Loop BFS para coletar todos os nós, nível por nível
        while q:
            # Pega o próximo nó da fila
            node, level, x, align = q.pop(0)
            if node:
                # Se o nível ainda não existe na lista, cria
                if len(levels) <= level:
                    levels.append([])
                
                # Adiciona o nó e suas infos de posição na lista do nível
                levels[level].append([node, level, x, align])
                
                # Calcula o "segmento" (espaço) para os filhos
                seg = width // (pow(2, level+1))
                
                # Adiciona os filhos (esquerdo e direito) na fila para processar depois
                q.append((node.left, level+1, x-seg, 'l'))
                q.append((node.right, level+1, x+seg, 'r'))

        # Agora, itera sobre os níveis coletados para imprimir
        for i, l in enumerate(levels):
            pre = 0
            preline = 0
            linestr = '' # String para desenhar as linhas / e \
            pstr = ''    # String para desenhar os números (valores)
            
            # Calcula o segmento para o nível atual
            seg = width // (pow(2, i+1))
            
            # Itera sobre cada nó no nível atual
            for n in l:
                valstr = str(n[0].value) # Pega o valor do nó como string
                
                # Lógica para desenhar as linhas de conexão (galhos)
                if n[3] == 'r': # Se for um filho da direita
                    linestr += ' ' * (n[2]-preline-1-seg-seg//2) + '¯' * (seg + seg//2) + '\\'
                    preline = n[2] 
                if n[3] == 'l': # Se for um filho da esquerda
                    linestr += ' ' * (n[2]-preline-1) + '/' + '¯' * (seg+seg//2)
                    preline = n[2] + seg + seg//2
                
                # Adiciona o valor do nó na string 'pstr', com espaçamento
                pstr += ' ' * (n[2]-pre-len(valstr)) + valstr
                pre = n[2]
            
            # Imprime as linhas e depois os valores
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