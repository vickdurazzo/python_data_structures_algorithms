"""
Diferente dos algoritmos O(n²) (Bubble, Selection, Insertion) que tentam ordenar a lista "no lugar", 
o Merge Sort quebra o problema em pedaços menores, resolve os pedaços e depois os junta de forma inteligente.
"""

def merge_sort(lista):
    # --- 1. Caso Base (A "parada" da recursão) ---
    # Se a lista tem 1 elemento ou menos, ela já está ordenada.
    if len(lista) <= 1:
        return lista
    
    # --- 2. Fase de Divisão ---
    # Encontra o índice do meio
    meio = len(lista) // 2
    
    # Cria a metade da esquerda e a metade da direita
    metade_esquerda = lista[:meio]
    metade_direita = lista[meio:]
    
    # Chama o merge_sort recursivamente para cada metade
    esquerda_ordenada = merge_sort(metade_esquerda)
    direita_ordenada = merge_sort(metade_direita)
    
    # --- 3. Fase de Conquista (Merge) ---
    # Agora mescla as duas metades ordenadas
    
    lista_mesclada = []
    i = 0 # Ponteiro para a lista da esquerda
    j = 0 # Ponteiro para a lista da direita
    
    # Loop enquanto houver elementos em AMBAS as listas
    while i < len(esquerda_ordenada) and j < len(direita_ordenada):
        # Compara os elementos
        if esquerda_ordenada[i] < direita_ordenada[j]:
            # Elemento da esquerda é menor, adiciona à lista
            lista_mesclada.append(esquerda_ordenada[i])
            i += 1 # Avança o ponteiro da esquerda
        else:
            # Elemento da direita é menor (ou igual)
            lista_mesclada.append(direita_ordenada[j])
            j += 1 # Avança o ponteiro da direita
            
    # --- 4. Limpeza ---
    # Ao final do loop, uma das listas terá "sobrado".
    # Adicionamos o restante dessa lista (que já está ordenado).
    # (Apenas uma dessas linhas 'extend' será executada)
    lista_mesclada.extend(esquerda_ordenada[i:])
    lista_mesclada.extend(direita_ordenada[j:])
    
    return lista_mesclada

# --- Testando o código ---
minha_lista = [64, 34, 25, 12, 22, 11, 90, 5, 1, 4, 2]
print(f"Lista original: {minha_lista}")

lista_ordenada = merge_sort(minha_lista)
print(f"Lista ordenada: {lista_ordenada}")

# Teste com o exemplo da explicação
lista_exemplo = [5, 1, 4, 2]
print(f"\nLista exemplo: {merge_sort(lista_exemplo)}")

"""
Vantagens e Desvantagens

    Vantagem (A MAIOR): 
        - Sua complexidade de tempo é O(n log n).
        - É um algoritmo estável (elementos de mesmo valor mantêm sua ordem original).

    Desvantagem: 
        - Usa memória extra. O Merge Sort não ordena "no lugar". Ele precisa criar novas listas temporárias (lista_mesclada) para fazer a mesclagem. Sua complexidade de espaço é O(n).
"""