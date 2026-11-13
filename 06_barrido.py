# Ejercicio 6 - Pedir las mediciones de cada canal

from importlib import import_module

a_numero = import_module("02_magnitudes").a_numero

magnitudes = [
    ("FREQuency", "FREQ", "Hz"),
    ("PKPK", "PKPK", "V"),
    ("CYCRms", "CYCRMS", "V")
]


def barrer(instrumento, canales):
    mediciones = []

    for canal in canales:
        if canal not in ("CH1", "CH2"):
            continue

        for comando, magnitud, unidad in magnitudes:
            consulta = f":MEASUrement:{canal}:{comando}?"
            respuesta = instrumento.preguntar(consulta)

            medicion = {
                "canal": canal,
                "magnitud": magnitud,
                "unidad": unidad,
                "crudo": respuesta,
                "valor": a_numero(respuesta)
            }
            mediciones.append(medicion)

    return mediciones


if __name__ == "__main__":
    # Para probar sin tener que prender el instrumento virtual
    class EquipoFalso:
        def __init__(self):
            self.comandos = []

        def preguntar(self, comando):
            self.comandos.append(comando)
            if "PKPK" in comando:
                return "ERROR: comando desconocido"
            return "1.000E+03"

    falso = EquipoFalso()
    filas = barrer(falso, ["CH1", "CH2"])

    assert len(filas) == 6
    assert filas[1]["valor"] is None
    assert filas[1]["crudo"].startswith("ERROR")
    assert falso.comandos[0] == ":MEASUrement:CH1:FREQuency?"
    assert barrer(falso, ["CH3"]) == []
    print("pruebas OK")
