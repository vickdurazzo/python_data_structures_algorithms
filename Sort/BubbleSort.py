"""
A ideia central é percorrer a lista várias vezes, comparando pares de elementos adjacentes 
(lado a lado) e trocando-os de lugar se estiverem na ordem errada.
"""
def bubble_sort(lista):
    # 'n' é o número total de elementos na lista
    n = len(lista)

    # Loop externo: controla o número de passagens.
    # Repetimos 'n' vezes (no pior caso).
    # 'i' representa quantos elementos JÁ ESTÃO no lugar certo no final.
    for i in range(n):
        
        # Otimização: Se não houver nenhuma troca em uma passagem,
        # a lista já está ordenada e podemos parar.
        trocou = False

        # Loop interno: faz as comparações e trocas.
        # Vamos de j=0 até (n - i - 1).
        # (n - 1) é o último índice.
        # (n - i - 1) porque os 'i' últimos elementos já estão ordenados.
        for j in range(0, n - i - 1):

            # Compara o elemento atual (j) com o próximo (j+1)
            if lista[j] > lista[j+1]:
                
                # Se estiverem fora de ordem, troca!
                # Esta é a "bolha" trocando de lugar
                lista[j], lista[j+1] = lista[j+1], lista[j]
                
                # Marca que uma troca ocorreu nesta passagem
                trocou = True

        # Otimização: Se 'trocou' ainda for False após o loop interno,
        # significa que ninguém trocou de lugar. A lista está ordenada.
        if not trocou:
            break # Interrompe o loop externo
            
    return lista

# --- Testando o código ---
minha_lista = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {minha_lista}")

lista_ordenada = bubble_sort(minha_lista)
print(f"Lista ordenada: {lista_ordenada}")

# Teste com o exemplo da explicação
lista_exemplo = [5, 1, 4, 2]
print(f"\nLista exemplo: {bubble_sort(lista_exemplo)}")

"""
 Vantagens e Desvantagens

Vantagem: É extremamente simples de entender e de implementar. Ótimo para fins didáticos.

Desvantagem: É muito ineficiente para listas grandes. Sua complexidade é O(n²), 
o que significa que se você dobrar o tamanho da lista, o tempo de execução quadruplica. 
Ele não é usado em aplicações práticas que exigem performance.
"""