"""Ejercicio 6: lectura de tres magnitudes en dos canales."""
from importlib import import_module
a_numero = import_module("02_magnitudes").a_numero
MAGNITUDES = (("FREQuency", "FREQ", "Hz"), ("PKPK", "PKPK", "V"), ("CYCRms", "CYCRMS", "V"))

def barrer(instrumento, canales):
    filas = []
    for canal in canales:
        if canal not in ("CH1", "CH2"):
            continue
        for nombre_scpi, magnitud, unidad in MAGNITUDES:
            crudo = instrumento.preguntar(f":MEASUrement:{canal}:{nombre_scpi}?")
            filas.append({"canal": canal, "magnitud": magnitud, "unidad": unidad,
                          "crudo": crudo, "valor": a_numero(crudo)})
    return filas

if __name__ == "__main__":
    class EquipoFalso:
        def __init__(self): self.comandos = []
        def preguntar(self, comando):
            self.comandos.append(comando)
            return "ERROR: comando desconocido" if "PKPK" in comando else "1.000E+03"
    falso = EquipoFalso()
    filas = barrer(falso, ["CH1", "CH2"])
    assert len(filas) == 6
    assert filas[1]["valor"] is None and filas[1]["crudo"].startswith("ERROR")
    assert falso.comandos[0] == ":MEASUrement:CH1:FREQuency?"
    assert barrer(falso, ["CH3"]) == []
    print("pruebas OK")
