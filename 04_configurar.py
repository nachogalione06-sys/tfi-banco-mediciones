# Ejercicio 4 - Preparar los comandos para configurar un canal

from importlib import import_module

validar = import_module("03_comandos").validar


def comandos_de_canal(canal, display, acoplamiento, sonda, escala):
    if canal != "CH1" and canal != "CH2":
        return None

    comandos = [
        f":{canal}:DISPlay {display}",
        f":{canal}:COUPling {acoplamiento}",
        f":{canal}:PROBe {sonda}",
        f":{canal}:SCALe {escala}"
    ]
    return comandos


if __name__ == "__main__":
    esperado = [
        ":CH1:DISPlay ON",
        ":CH1:COUPling DC",
        ":CH1:PROBe 10X",
        ":CH1:SCALe 1v"
    ]

    resultado = comandos_de_canal("CH1", "ON", "DC", "10X", "1v")
    assert resultado == esperado
    assert comandos_de_canal("CH3", "ON", "DC", "10X", "1v") is None
    assert all(validar(comando) is None for comando in resultado)
    assert len(comandos_de_canal("CH2", "OFF", "AC", "1X", "2v")) == 4
    print("pruebas OK")
