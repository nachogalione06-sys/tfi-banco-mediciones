# Ejercicio 1 - Identificar el instrumento

def parsear_idn(respuesta):
    if not isinstance(respuesta, str):
        return None

    if respuesta.strip() == "" or respuesta.strip().startswith("ERROR:"):
        return None

    datos = respuesta.split(",")

    # El multimetro tiene un dato extra al final, que no necesitamos
    if len(datos) != 4 and len(datos) != 5:
        return None

    datos = [dato.strip() for dato in datos]
    if not all(datos[:4]):
        return None

    return {
        "fabricante": datos[0],
        "modelo": datos[1],
        "serie": datos[2],
        "version": datos[3]
    }


if __name__ == "__main__":
    assert parsear_idn("OWON,ADS3202,25470803,V1.2.0")["modelo"] == "ADS3202"
    assert parsear_idn(" OWON, XDM1041, 25470803, V4.4.0, 3 ")["version"] == "V4.4.0"
    assert parsear_idn("OWON,ADS3202,254") is None
    assert parsear_idn("ERROR: comando desconocido") is None
    assert parsear_idn("") is None
    print("pruebas OK")
