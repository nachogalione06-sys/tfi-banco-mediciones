# Ejercicio 9 - Calcular valores de una serie de mediciones

import math


def resumen(valores):
    if len(valores) == 0:
        return None

    cantidad = len(valores)
    promedio = sum(valores) / cantidad

    if cantidad == 1:
        desvio = 0.0
    else:
        suma = 0
        for numero in valores:
            suma += (numero - promedio) ** 2
        desvio = math.sqrt(suma / (cantidad - 1))

    return {
        "n": cantidad,
        "minimo": min(valores),
        "maximo": max(valores),
        "promedio": promedio,
        "desvio": desvio
    }


def fuera_de_rango(valores, minimo, maximo):
    posiciones = []
    for i, numero in enumerate(valores):
        if numero < minimo or numero > maximo:
            posiciones.append(i)
    return posiciones


if __name__ == "__main__":
    assert resumen([]) is None
    assert resumen([2])["desvio"] == 0.0
    assert resumen([1, 2, 3])["promedio"] == 2
    assert abs(resumen([1, 2, 3])["desvio"] - 1) < 0.00001
    assert fuera_de_rango([0, 1, 2, 3], 1, 2) == [0, 3]
    assert fuera_de_rango([1, 2], 1, 2) == []
    print("pruebas OK")
