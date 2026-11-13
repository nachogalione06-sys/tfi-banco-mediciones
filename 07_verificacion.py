# Ejercicio 7 - Comparar las mediciones con los valores calculados

import math


def vrms_teorico(vpp):
    if not isinstance(vpp, (int, float)):
        return None
    if not math.isfinite(vpp) or vpp < 0:
        return None

    return vpp / (2 * math.sqrt(2))


def coincide(medido, teorico, tolerancia=0.02):
    for numero in (medido, teorico, tolerancia):
        if not isinstance(numero, (int, float)):
            return False
        if not math.isfinite(numero):
            return False

    if tolerancia < 0:
        return False

    if teorico == 0:
        return medido == 0

    error = abs(medido - teorico) / abs(teorico)
    return error <= tolerancia


def verificar_canal(filas, canal):
    vpp = None
    vrms = None

    for fila in filas:
        if fila.get("canal") != canal:
            continue
        if fila["magnitud"].upper() == "PKPK":
            vpp = fila["valor"]
        elif fila["magnitud"].upper() == "CYCRMS":
            vrms = fila["valor"]

    calculado = vrms_teorico(vpp)

    return {
        "canal": canal,
        "vpp": vpp,
        "vrms_medido": vrms,
        "vrms_teorico": calculado,
        "coincide": coincide(vrms, calculado)
    }


if __name__ == "__main__":
    assert abs(vrms_teorico(2) - 0.70710678) < 0.00001
    assert vrms_teorico(-1) is None
    assert coincide(0.70, 0.70710678)
    assert not coincide(1, 0.70710678)

    filas = [
        {"canal": "CH1", "magnitud": "PKPK", "valor": 2},
        {"canal": "CH1", "magnitud": "CYCRMS", "valor": 1}
    ]
    assert not verificar_canal(filas, "CH1")["coincide"]
    assert not verificar_canal([], "CH2")["coincide"]
    print("pruebas OK")
