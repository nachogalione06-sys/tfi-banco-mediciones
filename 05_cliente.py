"""Ejercicio 5: cliente TCP para consultas SCPI."""
import socket
from importlib import import_module
parsear_idn = import_module("01_identificacion").parsear_idn
class Instrumento:
    def __init__(self, direccion="127.0.0.1", puerto=5555, timeout=5):
        self.conexion = socket.create_connection((direccion, puerto), timeout=timeout)
        self.conexion.settimeout(timeout)
        self.entrada = self.conexion.makefile("rb")

    def enviar(self, comando):
        self.conexion.sendall((comando + "\n").encode("ascii"))

    def preguntar(self, comando):
        self.enviar(comando)
        respuesta = self.entrada.readline()
        if not respuesta:
            raise ConnectionError("El instrumento cerró la conexión")
        return respuesta.decode("utf-8").rstrip("\r\n")

    def cerrar(self):
        try:
            self.entrada.close()
        finally:
            self.conexion.close()

if __name__ == "__main__":
    # Comprobaciones de la interfaz sin necesitar red.
    assert callable(Instrumento.enviar)
    assert callable(Instrumento.preguntar)
    assert callable(Instrumento.cerrar)
    assert parsear_idn("OWON,ADS3202,25470803,V1.2.0")["modelo"] == "ADS3202"
    try:
        equipo = Instrumento()
    except OSError as exc:
        print("Pruebas locales OK. Encendé instrumento_virtual.py para la prueba TCP:", exc)
    else:
        try:
            respuesta = equipo.preguntar("*IDN?")
            assert parsear_idn(respuesta)["modelo"] == "ADS3202"
            print("Pruebas TCP OK")
        finally:
            equipo.cerrar()
