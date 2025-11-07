# --- Inicio da Classe ---
class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(f'\nVértice {vertex}:')
            if not self.adj_list[vertex]:
                print('   (nenhuma conexão)')
            else:
                for adj_vertex in self.adj_list[vertex]:
                    print(f'   → {adj_vertex}')

    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self,v1,v2):
        if (v1 not in self.adj_list.keys()) or (v2 not in self.adj_list.keys()):
            return False
        
        # Adiciona a conexão mútua
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
        return True
    
    def remove_vertex(self,vertex):
        if vertex not in self.adj_list:
            return False
        
        # Remove todas as arestas associadas ao vértice
        # Usamos list() para criar uma cópia, 
        # pois não é seguro modificar uma lista enquanto iteramos sobre ela
        for adj_vertex in list(self.adj_list[vertex]): 
            self.remove_edge(vertex, adj_vertex)
        
        # Remove o vértice do grafo
        del self.adj_list[vertex]
        return True
    
    def remove_edge(self,v1,v2):
        # Checa se os vértices existem
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                # Remove a conexão mútua
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                return True
            except ValueError:
                # Caso a aresta não exista entre eles
                return False
        return False

# --- Fim da Classe ---


# --- teste ---
meu_grafo = Graph()

# Adicionando cidades (vértices)
meu_grafo.add_vertex('São Paulo')
meu_grafo.add_vertex('Rio de Janeiro')
meu_grafo.add_vertex('Belo Horizonte')
meu_grafo.add_vertex('Curitiba')

# Adicionando estradas (arestas)
meu_grafo.add_edge('São Paulo', 'Rio de Janeiro')
meu_grafo.add_edge('São Paulo', 'Curitiba')
meu_grafo.add_edge('São Paulo', 'Belo Horizonte')
meu_grafo.add_edge('Rio de Janeiro', 'Belo Horizonte')

# Vamos ver o resultado
meu_grafo.print_graph()