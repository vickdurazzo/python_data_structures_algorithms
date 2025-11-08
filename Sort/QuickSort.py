"""
A ideia central do Quick Sort é o Particionamento (Partition)

O processo é:

    1 - Escolha um "Pivô": Pegue qualquer elemento da lista para ser o seu "pivô". (Pode ser o primeiro, o último, um aleatório, etc.)

    2 - Particione: Reorganize a lista inteira de forma que:

        Todos os elementos menores que o pivô fiquem à sua esquerda.

        Todos os elementos maiores que o pivô fiquem à sua direita.

    3 - Resultado da Partição: No final desse processo, o pivô magicamente "cai" na sua posição final correta (a posição que ele teria se a lista estivesse ordenada).

    4 - Repita (Recursão): Agora você tem duas sub-listas menores (uma à esquerda e outra à direita do pivô). Você aplica o mesmo processo (escolhe um pivô, particiona) recursivamente para essas sub-listas.

    5 - Caso Base: A recursão para quando uma sub-lista tem 0 ou 1 elemento (pois ela já está ordenada).
"""
# Esta é a função principal que "desenrola" a lógica
# Ela ordena a lista "in-place" (na própria lista)
def _quick_sort(lista, inicio, fim):
    # Caso base: se a sub-lista tem 0 ou 1 elemento, já está ordenada
    if inicio < fim:
        # p_idx (índice do pivô) é o índice onde o pivô
        # "aterrissou" após a partição
        p_idx = partition(lista, inicio, fim)
        
        # Recursivamente ordena a sub-lista à ESQUERDA do pivô
        _quick_sort(lista, inicio, p_idx - 1)
        
        # Recursivamente ordena a sub-lista à DIREITA do pivô
        _quick_sort(lista, p_idx + 1, fim)

# Esta função faz o trabalho pesado de "particionar"
def partition(lista, inicio, fim):
    # Escolhemos o último elemento como pivô (Esquema de Lomuto)
    pivot = lista[fim]
    
    # 'i' rastreia a fronteira dos elementos "menores que o pivô"
    # Começa "antes" da lista
    i = inicio - 1
    
    # Percorre de 'inicio' até 'fim-1' (sem incluir o pivô)
    for j in range(inicio, fim):
        # Se o elemento atual (j) for menor que o pivô...
        if lista[j] <= pivot:
            # ...avança a fronteira 'i'
            i += 1
            # ...e troca o elemento 'j' (menor) para
            # dentro da fronteira 'i'
            lista[i], lista[j] = lista[j], lista[i]
            
    # Fim do loop. Todos elementos de 'inicio' até 'i' são <= pivô.
    # Agora, colocamos o pivô (que está em lista[fim])
    # em seu lugar correto (i + 1)
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    
    # Retorna o índice onde o pivô está agora
    return i + 1

# Função "wrapper" (invólucro) para facilitar a chamada inicial
def quick_sort(lista):
    _quick_sort(lista, 0, len(lista) - 1)
    return lista

# --- Testando o código ---
minha_lista = [64, 34, 25, 12, 22, 11, 90, 5, 1, 7, 2, 6]
print(f"Lista original: {minha_lista}")

lista_ordenada = quick_sort(minha_lista)
print(f"Lista ordenada: {lista_ordenada}")

# Teste com o exemplo da explicação
lista_exemplo = [5, 1, 7, 2, 6]
print(f"\nLista exemplo: {quick_sort(lista_exemplo)}")