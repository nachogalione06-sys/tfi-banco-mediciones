# Ejercicio 2 - Pasar mediciones a numeros y unidades mas faciles de leer

import math

prefijos = [
    (-12, "p"),
    (-9, "n"),
    (-6, "u"),
    (-3, "m"),
    (0, ""),
    (3, "k"),
    (6, "M"),
    (9, "G")
]


def a_numero(texto):
    try:
        numero = float(texto)
        if math.isfinite(numero):
            return numero
    except (ValueError, TypeError):
        pass
    return None


def con_unidad(valor, unidad):
    if not isinstance(valor, (int, float)):
        return None
    if not math.isfinite(valor):
        return None
    if valor == 0:
        return f"0 {unidad}"

    exponente = 0
    for potencia, prefijo in prefijos:
        convertido = abs(valor) / (10 ** potencia)
        if 1 <= convertido < 1000:
            exponente = potencia
            break
    else:
        # Si queda fuera de los prefijos disponibles, usamos el extremo
        exponente = -12 if abs(valor) < 1e-12 else 9

    numero = round(valor / (10 ** exponente), 3)

    # Puede pasar que al redondear 999.9999 termine siendo 1000
    if abs(numero) >= 1000 and exponente < 9:
        exponente += 3
        numero = round(valor / (10 ** exponente), 3)

    prefijo = dict(prefijos)[exponente]
    return f"{numero:g} {prefijo}{unidad}"


if __name__ == "__main__":
    assert a_numero("1.000000E+03") == 1000.0
    assert a_numero("texto") is None
    assert a_numero("nan") is None
    assert con_unidad(2500, "Hz") == "2.5 kHz"
    assert con_unidad(0.707, "V") == "707 mV"
    assert con_unidad(0.0005, "s") == "500 us"
    assert con_unidad(999.9999, "Hz") == "1 kHz"
    print("pruebas OK")
