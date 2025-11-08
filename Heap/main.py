class MinHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, valor):
        # Etapa 1: Adicionar ao final
        self.heap.append(valor)
        indice_atual = len(self.heap) - 1

        # Etapa 2: "Borbulhar para cima" (Bubble Up)
        while indice_atual > 0:
            indice_pai = (indice_atual - 1) // 2
            
            if self.heap[indice_atual] < self.heap[indice_pai]:
                # Troca
                self.heap[indice_pai], self.heap[indice_atual] = self.heap[indice_atual], self.heap[indice_pai]
                indice_atual = indice_pai
            else:
                break # A regra está satisfeita

    def remover(self):
        if len(self.heap) == 0:
            return None # Heap está vazio

        if len(self.heap) == 1:
            return self.heap.pop() # Se só há um item

        valor_removido = self.heap[0]

        # Pega o último item e move para o topo
        ultimo_valor = self.heap.pop()
        self.heap[0] = ultimo_valor
            
        # Etapa 3: "Borbulhar para baixo"
        self._bubble_down(0)

        return valor_removido

    def _bubble_down(self, indice_pai):
        
        # Continua enquanto o filho esquerdo existir
        while (2 * indice_pai) + 1 < len(self.heap):
            indice_filho_esq = (2 * indice_pai) + 1
            indice_filho_dir = (2 * indice_pai) + 2
            
            indice_menor_filho = indice_filho_esq 

            # Checa com segurança se o direito existe E é menor
            if indice_filho_dir < len(self.heap) and self.heap[indice_filho_dir] < self.heap[indice_filho_esq]:
                indice_menor_filho = indice_filho_dir

            if self.heap[indice_pai] > self.heap[indice_menor_filho]:
                # Troca
                self.heap[indice_pai], self.heap[indice_menor_filho] = self.heap[indice_menor_filho], self.heap[indice_pai]
                # Atualiza o indice_pai para continuar descendo
                indice_pai = indice_menor_filho
            else:
                break # A regra está satisfeita

# --- ÁREA DE TESTE 🚀 ---

print("Iniciando teste do Min Heap...")
meu_heap = MinHeap()

# 1. Inserir itens fora de ordem
print("Inserindo: 10, 5, 20, 3, 8")
meu_heap.inserir(10)
meu_heap.inserir(5)
meu_heap.inserir(20)
meu_heap.inserir(3)
meu_heap.inserir(8)

# Vamos espiar o array interno.
# NÃO estará ordenado, mas deve seguir a regra do heap.
print(f"\nArray interno do Heap (esperado: [3, 5, 20, 10, 8]):")
print(meu_heap.heap)

# 2. Remover itens
print("\nRemovendo itens (devem sair em ordem crescente):")

# Loop para remover itens até o heap ficar vazio
item_removido = meu_heap.remover()
while item_removido is not None:
    print(f"Removido: {item_removido}")
    item_removido = meu_heap.remover()

print("Teste concluído.")