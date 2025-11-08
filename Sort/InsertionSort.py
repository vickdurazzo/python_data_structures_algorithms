"""
A lógica dele é muito intuitiva, pois é como a maioria das pessoas organiza um baralho de cartas na mão.

A ideia central é construir a lista ordenada, um elemento de cada vez. Você pega um elemento da parte "não ordenada" e o insere na posição correta dentro da parte "já ordenada".
"""
def insertion_sort(lista):
    # O loop externo começa no SEGUNDO elemento (índice 1)
    # (Assumimos que o primeiro elemento, índice 0, já está "ordenado")
    for i in range(1, len(lista)):
        
        # 'chave' é o elemento que vamos inserir na parte ordenada
        chave = lista[i]
        
        # 'j' é o último índice da parte ORDENADA
        j = i - 1
        
        # Loop interno: "desliza" os elementos da parte ordenada
        # que são MAIORES que a 'chave' para a direita.
        #
        # Continua enquanto 'j' for um índice válido (>= 0) E
        # o elemento em 'lista[j]' for maior que a 'chave'.
        while j >= 0 and chave < lista[j]:
            # "Desliza" o elemento para a direita
            lista[j + 1] = lista[j]
            # Move 'j' para a esquerda, para comparar com o próximo
            j = j - 1
            
        # Fim do while. Encontramos o local certo.
        # 'j+1' é a posição correta para inserir a 'chave'
        # (porque 'j' parou no elemento ANTERIOR ao local de inserção)
        lista[j + 1] = chave
        
    return lista

# --- Testando o código ---
minha_lista = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {minha_lista}")

lista_ordenada = insertion_sort(minha_lista)
print(f"Lista ordenada: {lista_ordenada}")

# Teste com o exemplo da explicação
lista_exemplo = [5, 1, 4, 2]
print(f"\nLista exemplo: {insertion_sort(lista_exemplo)}")


"""
Vantagens e Desvantagens

    Vantagem:
        - Muito eficiente para listas pequenas ou listas que estão quase ordenadas. Se a lista já estiver ordenada, ele é super rápido (complexidade O(n)).
        - É um algoritmo "online", o que significa que ele pode ordenar a lista à medida que recebe novos elementos, sem precisar ter todos os dados de antemão.
        - Assim como o Selection Sort, é simples de implementar.

    Desvantagem: 
        - Assim como o Bubble e o Selection, é ineficiente para listas grandes e desordenadas (complexidade O(n²)).
"""