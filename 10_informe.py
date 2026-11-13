"""Ejercicio 10: integración de identificación, barrido, log e informe."""
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
    if not idn:
        idn = {"fabricante": "desconocido", "modelo": "desconocido", "serie": "-", "version": "-"}
    lineas = ["INFORME DEL BANCO DE MEDICIONES",
              f"Equipo: {idn['fabricante']} {idn['modelo']} | Serie: {idn['serie']} | Versión: {idn['version']}",
              "", "Estadísticas del registro:"]
    for (equipo, canal, magnitud), valores in sorted(series.items()):
        estad = resumen(valores)
        if estad is None:
            continue
        unidad = "Hz" if magnitud == "FREQ" else "V"
        lineas.append(f"{equipo} {canal} {magnitud}: n={estad['n']}, "
                      f"promedio={con_unidad(estad['promedio'], unidad)}, "
                      f"mínimo={con_unidad(estad['minimo'], unidad)}, "
                      f"máximo={con_unidad(estad['maximo'], unidad)}")
    lineas.extend(["", "Verificación de canales:"])
    for verificacion in verificaciones:
        resultado = "COINCIDE" if verificacion["coincide"] else "NO COINCIDE"
        lineas.append(f"{verificacion['canal']}: {resultado}")
    return "\n".join(lineas)

if __name__ == "__main__":
    idn_prueba = "OWON,ADS3202,25470803,V1.2.0"
    texto = armar_informe(idn_prueba, {("ADS3202", "CH1", "FREQ"): [999, 1001]},
                          [{"canal": "CH1", "coincide": True}])
    assert "ADS3202" in texto
    assert "n=2" in texto and "1 kHz" in texto
    assert "CH1: COINCIDE" in texto
    assert "Estadísticas" in armar_informe(None, {}, [])
    print("Pruebas de informe OK")
    if not Path("mediciones.log").is_file():
        print("Falta mediciones.log: solicitá el original a la cátedra para ejecutar el informe completo.")
    else:
        try:
            equipo = Instrumento()
        except OSError as exc:
            print("Falta iniciar instrumento_virtual.py para la integración:", exc)
        else:
            try:
                idn_real = parsear_idn(equipo.preguntar("*IDN?"))
                filas = barrer(equipo, ["CH1", "CH2"])
                verificaciones = [verificar_canal(filas, canal) for canal in ("CH1", "CH2")]
                series, rechazadas = leer_log("mediciones.log")
                print(armar_informe(idn_real, series, verificaciones))
                print(f"\nLíneas rechazadas del log: {len(rechazadas)}")
            finally:
                equipo.cerrar()
