# tests/test_potencia.py
import pytest
from potencia import potencia

def test_potencia_correcto():
    # Caso correcto: 2**3 = 8
    assert potencia(2, 3) == 8

def test_potencia_limite_exponente_cero():
    # Caso límite: cualquier base distinta de 0 elevada a 0 es 1
    assert potencia(5, 0) == 1
    assert potencia(-3, 0) == 1

def test_potencia_error_0_0():
    # Caso error: 0**0 -> ValueError según nuestra especificación
    with pytest.raises(ValueError):
        potencia(0, 0)

def test_potencia_tipo_invalido():
    # Caso error: tipos inválidos
    with pytest.raises(TypeError):
        potencia("2", 3)

def test_potencia_division_por_cero():
    # Caso error: 0**-1 -> ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        potencia(0, -1)