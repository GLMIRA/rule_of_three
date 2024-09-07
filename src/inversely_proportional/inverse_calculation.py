def valida_valor(numbers: list) -> list:
    for number in numbers:
        try:
            isinstance(number, float)
        except:
            ValueError
