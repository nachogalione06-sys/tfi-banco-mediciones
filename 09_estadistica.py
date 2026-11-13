"""Ejercicio 9: resumen estadístico de una serie."""
import math

def resumen(valores):
    if not valores:
        return None
    n = len(valores)
    promedio = sum(valores) / n
    desvio = math.sqrt(sum((v - promedio) ** 2 for v in valores) / (n - 1)) if n > 1 else 0.0
    return {"n": n, "minimo": min(valores), "maximo": max(valores),
            "promedio": promedio, "desvio": desvio}

def fuera_de_rango(valores, minimo, maximo):
    return [i for i, valor in enumerate(valores) if valor < minimo or valor > maximo]

if __name__ == "__main__":
    assert resumen([]) is None
    assert resumen([2])["desvio"] == 0.0
    assert resumen([1, 2, 3])["promedio"] == 2
    assert abs(resumen([1, 2, 3])["desvio"] - 1) < 1e-12
    assert fuera_de_rango([0, 1, 2, 3], 1, 2) == [0, 3]
    assert fuera_de_rango([1, 2], 1, 2) == []
    print("pruebas OK")
