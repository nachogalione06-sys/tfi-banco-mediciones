# Ejercicio 8 - Leer las mediciones que quedaron guardadas

from datetime import datetime
from importlib import import_module

a_numero = import_module("02_magnitudes").a_numero


def analizar_linea(linea):
    if not linea.strip() or linea.lstrip().startswith("#"):
        return None, None

    # split() tambien separa los datos si estan separados por tabulaciones
    datos = linea.split()
    if len(datos) != 6:
        return None, "Cantidad incorrecta de campos"

    fecha, hora, equipo, canal, magnitud, texto = datos

    try:
        datetime.strptime(fecha + " " + hora, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None, "Fecha u hora incorrecta"

    if canal not in ("CH1", "CH2"):
        return None, "Canal incorrecto"

    if magnitud not in ("FREQ", "PKPK", "CYCRMS"):
        return None, "Magnitud incorrecta"

    valor = a_numero(texto)
    if valor is None:
        return None, "El valor no es un numero"

    medicion = {
        "fecha": fecha,
        "hora": hora,
        "equipo": equipo,
        "canal": canal,
        "magnitud": magnitud,
        "valor": valor
    }
    return medicion, None


def leer_log(ruta):
    series = {}
    rechazadas = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        for numero, linea in enumerate(archivo, 1):
            medicion, motivo = analizar_linea(linea)

            if medicion is not None:
                clave = (medicion["equipo"], medicion["canal"], medicion["magnitud"])
                if clave not in series:
                    series[clave] = []
                series[clave].append(medicion["valor"])

            elif motivo is not None:
                rechazadas.append({
                    "linea": numero,
                    "motivo": motivo,
                    "texto": linea.rstrip("\n")
                })

    return series, rechazadas


if __name__ == "__main__":
    linea = "2026-09-08 09:14:02 ADS3202 CH1 FREQ 1.000431E+03"
    assert analizar_linea(linea)[0]["valor"] == 1000.431
    assert analizar_linea(linea.replace(" ", "\t"))[0] is not None
    assert analizar_linea("# comentario") == (None, None)
    assert analizar_linea(" ") == (None, None)
    assert analizar_linea(linea.replace("09:14:02", "25:61:00"))[1] is not None
    assert analizar_linea(linea.replace("CH1", "CH3"))[1] is not None
    print("pruebas OK")
