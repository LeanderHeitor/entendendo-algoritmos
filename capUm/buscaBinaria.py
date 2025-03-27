def pesquisa_binaria(arrayOrdenado, item):
    """
    Realiza uma busca binária em uma lista ordenada.
    
    Args:
        arrayOrdenado (list): Lista ordenada onde será feita a busca.
        item: Elemento a ser procurado na lista.
    
    Returns:
        int: Índice do elemento na lista, ou None se não for encontrado.
    """

    # Definindo limites
    baixo = 0  # Índice do menor elemento da lista
    alto = len(arrayOrdenado) - 1  # Índice do maior elemento da lista
    
    # Enquanto a faixa de busca for válida (baixo <= alto)
    while baixo <= alto:
        meio = (baixo + alto) // 2  # Calcula o índice do meio (divisão inteira por contado do //)
        chute = arrayOrdenado[meio]  # Obtém o elemento na posição do meio
        
        if chute == item:  # Se o elemento do meio for o procurado, retorna seu índice
            return meio
        if chute > item:  # Se o elemento do meio for maior que o procurado
            alto = meio - 1  # Atualiza o limite superior para procurar na metade inferior
        else:  # Se o elemento do meio for menor que o procurado
            baixo = meio + 1  # Atualiza o limite inferior para procurar na metade superior
    
    return None  # Retorna None se o item não for encontrado
