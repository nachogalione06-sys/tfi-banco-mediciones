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
    # Controlamos la frecuencia del canal 1 del registro
    from pathlib import Path
    from importlib import import_module
    if Path("mediciones.log").is_file():
        leer_log = import_module("08_log").leer_log
        series, _ = leer_log("mediciones.log")
        frecuencias = series[("ADS3202", "CH1", "FREQ")]
        datos = resumen(frecuencias)
        assert abs(datos["promedio"] - 1000) / 1000 < 0.005
        assert datos["desvio"] < 5

    print("pruebas OK")
