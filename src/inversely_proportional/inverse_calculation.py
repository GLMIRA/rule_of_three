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


def calculate_inverse_rule_of_three(numbers_list: list) -> list:

    validate_number = valida_valor(numbers_list)

    if not validate_number:
        return validate_number

    number_1, number_2, number_3 = numbers_list

    result = (number_1 * number_2) / number_3

    return result
