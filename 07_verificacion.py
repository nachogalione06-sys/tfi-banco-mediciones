"""Ejercicio 7: comparación de mediciones contra senoides ideales."""
import math

def vrms_teorico(vpp):
    if not isinstance(vpp, (int, float)) or not math.isfinite(vpp) or vpp < 0:
        return None
    return vpp / (2 * math.sqrt(2))

def coincide(medido, teorico, tolerancia=0.02):
    if any(not isinstance(v, (int, float)) or not math.isfinite(v) for v in (medido, teorico, tolerancia)):
        return False
    if tolerancia < 0:
        return False
    if teorico == 0:
        return medido == 0
    return abs(medido - teorico) / abs(teorico) <= tolerancia

def verificar_canal(filas, canal):
    valores = {fila["magnitud"].upper(): fila["valor"] for fila in filas if fila.get("canal") == canal}
    vpp = valores.get("PKPK")
    medido = valores.get("CYCRMS")
    teorico = vrms_teorico(vpp)
    return {"canal": canal, "vpp": vpp, "vrms_medido": medido,
            "vrms_teorico": teorico, "coincide": coincide(medido, teorico)}

if __name__ == "__main__":
    assert abs(vrms_teorico(2) - 0.70710678) < 0.00001
    assert vrms_teorico(-1) is None
    assert coincide(0.70, 0.70710678)
    assert not coincide(1, 0.70710678)
    filas = [{"canal": "CH1", "magnitud": "PKPK", "valor": 2},
             {"canal": "CH1", "magnitud": "CYCRMS", "valor": 1}]
    assert not verificar_canal(filas, "CH1")["coincide"]
    assert not verificar_canal([], "CH2")["coincide"]
    print("pruebas OK")
