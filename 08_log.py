"""Ejercicio 8: lectura y validación del registro entregado por la cátedra."""
from datetime import datetime
from importlib import import_module
a_numero = import_module("02_magnitudes").a_numero

def analizar_linea(linea):
    if not linea.strip() or linea.lstrip().startswith("#"):
        return (None, None)
    partes = linea.split()
    if len(partes) != 6:
        return (None, "cantidad de campos incorrecta")
    fecha, hora, equipo, canal, magnitud, texto = partes
    try:
        datetime.strptime(fecha + " " + hora, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return (None, "fecha u hora inválida")
    if canal not in ("CH1", "CH2"):
        return (None, "canal inválido")
    if magnitud not in ("FREQ", "PKPK", "CYCRMS"):
        return (None, "magnitud inválida")
    valor = a_numero(texto)
    if valor is None:
        return (None, "valor no numérico")
    return ({"fecha": fecha, "hora": hora, "equipo": equipo, "canal": canal,
             "magnitud": magnitud, "valor": valor}, None)

def leer_log(ruta):
    series, rechazadas = {}, []
    with open(ruta, "r", encoding="utf-8") as archivo:
        for numero, linea in enumerate(archivo, 1):
            medicion, motivo = analizar_linea(linea)
            if medicion is not None:
                clave = (medicion["equipo"], medicion["canal"], medicion["magnitud"])
                series.setdefault(clave, []).append(medicion["valor"])
            elif motivo is not None:
                rechazadas.append({"linea": numero, "motivo": motivo, "texto": linea.rstrip("\n")})
    return series, rechazadas

if __name__ == "__main__":
    valido = "2026-09-08 09:14:02 ADS3202 CH1 FREQ 1.000431E+03"
    assert analizar_linea(valido)[0]["valor"] == 1000.431
    assert analizar_linea(valido.replace(" ", "\t"))[0] is not None
    assert analizar_linea("# comentario") == (None, None)
    assert analizar_linea(" ") == (None, None)
    assert analizar_linea(valido.replace("09:14:02", "25:61:00"))[1] is not None
    assert analizar_linea(valido.replace("CH1", "CH3"))[1] is not None
    print("pruebas OK")
