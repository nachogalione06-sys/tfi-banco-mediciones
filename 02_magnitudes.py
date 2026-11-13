"""Ejercicio 2: conversión de magnitudes y prefijos SI."""
import math

PREFIJOS = ((-12, "p"), (-9, "n"), (-6, "u"), (-3, "m"), (0, ""), (3, "k"), (6, "M"), (9, "G"))

def a_numero(texto):
    try:
        numero = float(texto)
        return numero if math.isfinite(numero) else None
    except (TypeError, ValueError):
        return None

def con_unidad(valor, unidad):
    if not isinstance(valor, (int, float)) or not math.isfinite(valor):
        return None
    if valor == 0:
        return f"0 {unidad}"
    exponente = max(-12, min(9, 3 * math.floor(math.log10(abs(valor)) / 3)))
    escalado = valor / (10 ** exponente)
    escalado = round(escalado, 3)
    if abs(escalado) >= 1000 and exponente < 9:
        exponente += 3
        escalado = round(valor / 10 ** exponente, 3)
    prefijo = dict(PREFIJOS)[exponente]
    texto = f"{escalado:g}"
    return f"{texto} {prefijo}{unidad}"

if __name__ == "__main__":
    assert a_numero("1.000000E+03") == 1000.0
    assert a_numero("texto") is None
    assert a_numero("nan") is None
    assert con_unidad(2500, "Hz") == "2.5 kHz"
    assert con_unidad(0.707, "V") == "707 mV"
    assert con_unidad(0.0005, "s") == "500 us"
    assert con_unidad(999.9999, "Hz") == "1 kHz"
    print("pruebas OK")
