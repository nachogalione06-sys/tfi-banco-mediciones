"""Ejercicio 1: identificación SCPI."""
def parsear_idn(respuesta):
    if not isinstance(respuesta, str) or respuesta.strip().startswith("ERROR:"):
        return None
    campos = [campo.strip() for campo in respuesta.strip().split(",")]
    if len(campos) not in (4, 5) or not all(campos[:4]):
        return None
    return dict(zip(("fabricante", "modelo", "serie", "version"), campos[:4]))

if __name__ == "__main__":
    assert parsear_idn("OWON,ADS3202,25470803,V1.2.0")["modelo"] == "ADS3202"
    assert parsear_idn(" OWON, XDM1041, 25470803, V4.4.0, 3 ")["version"] == "V4.4.0"
    assert parsear_idn("OWON,ADS3202,254") is None
    assert parsear_idn("ERROR: comando desconocido") is None
    assert parsear_idn("") is None
    print("pruebas OK")
