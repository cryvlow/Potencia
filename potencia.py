# potencia.py

def potencia(base, exponente):
    """
    Calcula la potencia base**exponente.

    Parámetros
    ----------
    base : int | float
        La base de la potencia. Debe ser un número (int o float).
    exponente : int | float
        El exponente. Debe ser un número (int o float).

    Retorna
    -------
    int | float
        El resultado de elevar la base al exponente.

    Excepciones
    ----------
    TypeError
        Si alguno de los argumentos no es int ni float.
    ValueError
        Si base == 0 y exponente == 0 (0**0 es indefinido en este ejercicio).
    ZeroDivisionError
        Si base == 0 y exponente < 0 (division por cero).
    """
    # Validaciones de tipo
    if not isinstance(base, (int, float)) or not isinstance(exponente, (int, float)):
        raise TypeError("base y exponente deben ser números (int o float)")

    # Casos especiales
    if base == 0 and exponente == 0:
        raise ValueError("0 elevado a 0 es indefinido")

    if base == 0 and exponente < 0:
        # Evitar 0 ** negativo (division por cero)
        raise ZeroDivisionError("0 elevado a exponente negativo causa división por cero")

    # Cálculo
    return base ** exponente