# Ejercicio 5 - Conectarnos al instrumento usando la red local

import socket
from importlib import import_module

parsear_idn = import_module("01_identificacion").parsear_idn


class Instrumento:
    def __init__(self, direccion="127.0.0.1", puerto=5555, timeout=5):
        self.conexion = socket.create_connection((direccion, puerto), timeout=timeout)
        self.conexion.settimeout(timeout)
        self.entrada = self.conexion.makefile("rb")

    def enviar(self, comando):
        # El salto de linea indica que termino el comando
        mensaje = comando + "\n"
        self.conexion.sendall(mensaje.encode("ascii"))

    def preguntar(self, comando):
        self.enviar(comando)
        respuesta = self.entrada.readline()

        if not respuesta:
            raise ConnectionError("El instrumento cerro la conexion")

        return respuesta.decode("utf-8").rstrip("\r\n")

    def cerrar(self):
        try:
            self.entrada.close()
        finally:
            self.conexion.close()


if __name__ == "__main__":
    assert callable(Instrumento.enviar)
    assert callable(Instrumento.preguntar)
    assert callable(Instrumento.cerrar)
    assert parsear_idn("OWON,ADS3202,25470803,V1.2.0")["modelo"] == "ADS3202"

    try:
        equipo = Instrumento()
    except OSError as error:
        print("Pruebas basicas OK. Para probar la conexion hay que encender el instrumento:", error)
    else:
        try:
            respuesta = equipo.preguntar("*IDN?")
            assert parsear_idn(respuesta)["modelo"] == "ADS3202"
            assert equipo.preguntar(":CH1:DISPlay?") in ("ON", "OFF")
            assert equipo.preguntar(":CH1:COUPling?") in ("AC", "DC", "GND")
            print("Pruebas TCP OK")
        finally:
            equipo.cerrar()
