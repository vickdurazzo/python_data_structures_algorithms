"""
A ideia central é encontrar o menor elemento da lista e 
colocá-lo na primeira posição. Depois, encontrar o segundo menor 
elemento e colocá-lo na segunda posição, e assim por diante.
"""
def selection_sort(lista):
    # 'n' é o número total de elementos
    n = len(lista)

    # Loop externo: passa por cada posição da lista (de 0 até n-1)
    # 'i' é o índice da posição que estamos preenchendo
    for i in range(n):
        
        # Assume que o menor elemento é o primeiro da parte não ordenada
        min_idx = i 

        # Loop interno: procura pelo verdadeiro menor elemento
        # 'j' vai da posição 'i+1' até o final da lista
        for j in range(i + 1, n):
            # Se encontrar um elemento menor que o 'min_idx' atual
            if lista[j] < lista[min_idx]:
                # Atualiza 'min_idx' para guardar o índice do novo menor
                min_idx = j
                
        # Fim do loop interno. Agora 'min_idx' guarda o índice
        # do menor elemento da parte não ordenada.
        
        # Realiza UMA ÚNICA troca:
        # Pega o menor elemento (lista[min_idx]) e o coloca
        # na posição 'i' (o início da parte não ordenada).
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        
        # (O elemento que estava em 'i' vai para a antiga posição do 'min_idx')

    return lista

# --- Testando o código ---
minha_lista = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {minha_lista}")

lista_ordenada = selection_sort(minha_lista)
print(f"Lista ordenada: {lista_ordenada}")

# Teste com o exemplo da explicação
lista_exemplo = [5, 1, 4, 2]
print(f"\nLista exemplo: {selection_sort(lista_exemplo)}")

""" Vantagens e Desvantagens


    Vantagem: 
        - É simples de entender.
        - É muito eficiente no número de trocas. Ele faz no máximo n trocas (uma por passagem). Isso é útil se a operação de "trocar" elementos for muito custosa.

    Desvantagem: 
        - É ineficiente nas comparações. Ele sempre faz O(n²) comparações, mesmo que a lista já esteja ordenada. Ele não tem a "otimização" do Bubble Sort de parar mais cedo.
"""