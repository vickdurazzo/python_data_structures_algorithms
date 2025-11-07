class HashTable:
    
    def __init__(self, size = 10):
        """
        Inicializa a Tabela Hash (o "armário") com 'size' gavetas.
        Cada gaveta é uma lista vazia para tratar colisões.
        """
        self.data_map = [[] for _ in range(size)]

    def __hash(self, key):
        """
        Método privado para calcular o índice (a "gaveta") para uma chave.
        """
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23)
        
        # Usa o módulo para garantir que o índice caiba no data_map
        index = my_hash % len(self.data_map)
        return index

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f'{i}: ', end='')
            if val:  # if the bucket is not empty
                if len(val) == 1:  # if there's only one item
                    print(f'{val[0][0]}: {val[0][1]}')
                else:  # if there are multiple items (collision)
                    print('[', end='')
                    for j, item in enumerate(val):
                        if j == len(val) - 1:  # last item
                            print(f'{item[0]}: {item[1]}', end='')
                        else:
                            print(f'{item[0]}: {item[1]}, ', end='')
                    print(']')
            else:  # if the bucket is empty
                print('None')
    
    def set(self, key, value):
        """
        Adiciona um par [chave, valor] na tabela.
        """
        # Passo 1: Calcular o índice
        index = self.__hash(key)
        # Passo 2: Criar o par de dados
        key_value_pair = [key, value]
        # Passo 3: Adicionar o par na gaveta (lista) correta
        self.data_map[index].append(key_value_pair)

    def get(self, key):
        """
        Busca e retorna o VALOR associado a uma CHAVE.
        """
        # Passo 1: Calcular o índice
        index = self.__hash(key)
        # Passo 2: Acessar a gaveta (a lista)
        bucket = self.data_map[index]
        
        # Passo 3: Percorrer a lista na gaveta
        # (Usando um 'for' simples que é um pouco mais legível)
        for pair in bucket:
            # pair[0] é a chave, pair[1] é o valor
            if key == pair[0]:
                return pair[1]  # Retorna o valor
                
        # Se o loop terminar e não encontrar, retorna None
        return None

    def keys(self):
        """
        Retorna uma lista de todas as chaves na tabela.
        """
        all_keys = []
        # Loop 1: Passa por todas as gavetas
        for bucket in self.data_map:
            # Loop 2: Passa por todos os pares [chave, valor] na gaveta
            for key_value_pair in bucket:
                all_keys.append(key_value_pair[0])
        
        return all_keys

        


# Teste da HashTable
my_hash_table = HashTable()

my_hash_table.set("maçã", 5)
my_hash_table.set("laranja", 3)
my_hash_table.set("uva", 12)
my_hash_table.set("abacaxi", 7)
#my_hash_table.set("manga", 4)

print("\nVisualizando a HashTable:")
my_hash_table.print_table()

print(my_hash_table.get("manga"))
        