def valida_valor(numbers_list: list) -> list:
    """valida os numeros que recebo do front

    Args:
        numbers (list): lista dos numeros que serao usados para os calculos

    Returns:
        list: se os valores digitados forem somente numeros
        ele deixa inicia o codigo
    """
    for number in numbers_list:
        try:
            isinstance(number, float)
            return True
        except:
            teste = ValueError
            return teste
