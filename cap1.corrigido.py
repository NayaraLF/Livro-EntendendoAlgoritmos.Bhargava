#Pesquisa binaria
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        # CORREÇÃO 1: Usar divisão inteira (//) para garantir que 'meio' seja um int.
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio

        if chute > item:
            alto = meio - 1
        else:  # se chute < item
            baixo = meio + 1

    # CORREÇÃO 2: Mover o 'return None' para fora do loop 'while'.
    # Ele só será executado se o loop terminar sem encontrar o item.
    return None


minha_lista = [1, 3, 5, 7, 9]

# Teste 1: Procurando por um item que existe na lista.
# O resultado esperado e correto é 1 (o índice do número 3).
print(f"Buscando o item 3: Índice {pesquisa_binaria(minha_lista, 3)}")

# Teste 2: Procurando por um item que NÃO existe na lista.
# O resultado esperado e correto é None.
print(f"Buscando o item -1: {pesquisa_binaria(minha_lista, -1)}")