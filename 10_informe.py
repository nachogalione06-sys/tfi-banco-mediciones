# Ejercicio 10 - Juntar los resultados y mostrar el informe

from pathlib import Path
from importlib import import_module

parsear_idn = import_module("01_identificacion").parsear_idn
con_unidad = import_module("02_magnitudes").con_unidad
Instrumento = import_module("05_cliente").Instrumento
barrer = import_module("06_barrido").barrer
verificar_canal = import_module("07_verificacion").verificar_canal
leer_log = import_module("08_log").leer_log
resumen = import_module("09_estadistica").resumen


def armar_informe(idn, series, verificaciones):
    if isinstance(idn, str):
        idn = parsear_idn(idn)

    if idn is None:
        idn = {
            "fabricante": "desconocido",
            "modelo": "desconocido",
            "serie": "-",
            "version": "-"
        }

    lineas = []
    lineas.append("INFORME DEL BANCO DE MEDICIONES")
    lineas.append(f"Equipo: {idn['fabricante']} {idn['modelo']}")
    lineas.append(f"Serie: {idn['serie']}  Version: {idn['version']}")
    lineas.append("")
    lineas.append("Estadisticas del registro:")

    for clave, valores in sorted(series.items()):
        equipo, canal, magnitud = clave
        datos = resumen(valores)
        if datos is None:
            continue

        unidad = "Hz" if magnitud == "FREQ" else "V"
        promedio = con_unidad(datos["promedio"], unidad)
        minimo = con_unidad(datos["minimo"], unidad)
        maximo = con_unidad(datos["maximo"], unidad)

        linea = (f"{equipo} {canal} {magnitud}: n={datos['n']}, "
                 f"promedio={promedio}, minimo={minimo}, maximo={maximo}")
        lineas.append(linea)

    lineas.append("")
    lineas.append("Verificaciones:")
    for verificacion in verificaciones:
        if verificacion["coincide"]:
            estado = "COINCIDE"
        else:
            estado = "NO COINCIDE"
        lineas.append(f"{verificacion['canal']}: {estado}")

    return "\n".join(lineas)


if __name__ == "__main__":
    idn_prueba = "OWON,ADS3202,25470803,V1.2.0"
    series_prueba = {("ADS3202", "CH1", "FREQ"): [999, 1001]}
    verificaciones_prueba = [{"canal": "CH1", "coincide": True}]

    texto = armar_informe(idn_prueba, series_prueba, verificaciones_prueba)
    assert "ADS3202" in texto
    assert "n=2" in texto
    assert "1 kHz" in texto
    assert "CH1: COINCIDE" in texto
    assert "desconocido" in armar_informe(None, {}, [])
    print("pruebas de informe OK")

    if not Path("mediciones.log").is_file():
        print("No se encontro mediciones.log")
    else:
        try:
            equipo = Instrumento()
        except OSError as error:
            print("Para probar todo hay que iniciar instrumento_virtual.py:", error)
        else:
            try:
                identificacion = parsear_idn(equipo.preguntar("*IDN?"))
                mediciones = barrer(equipo, ["CH1", "CH2"])

                verificaciones = []
                for canal in ("CH1", "CH2"):
                    verificaciones.append(verificar_canal(mediciones, canal))

                series, rechazadas = leer_log("mediciones.log")
                informe = armar_informe(identificacion, series, verificaciones)
                print(informe)
                print(f"\nLineas rechazadas del log: {len(rechazadas)}")
            finally:
                equipo.cerrar()
