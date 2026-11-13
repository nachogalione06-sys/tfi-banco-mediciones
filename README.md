# Trabajo Final Integrador — Programación (UTN, Telecomunicaciones, 2026)

Implementación del **banco de mediciones automatizado en Python**, organizada en diez ejercicios conforme a la consigna `TUT-PROG-TFI-Consigna.pdf`.

## Integrantes

- **Completar nombre y apellido de quien o quienes presentan el trabajo.**

## Estado de archivos y pruebas

Los diez ejercicios están implementados. Se incluyen los dos archivos originales de la cátedra, `instrumento_virtual.py` y `mediciones.log`, que **no deben modificarse**.

- Se ejecutaron las pruebas `assert` de los diez ejercicios.
- Se comprobó una conexión TCP real al instrumento virtual ADS3202 en el puerto 5555, identificación y barrido de ambos canales. La verificación dio coincidencia en ambos casos.
- Se revisó el registro proporcionado: 121 mediciones válidas, 8 líneas rechazadas y 11 líneas ignoradas (incluida la línea terminal vacía). La línea separada por tabulaciones es válida.
- Pendientes antes de entregar: completar nombre y apellido de todos los integrantes, revisar/completar el registro literal de uso de IA y preparar la defensa individual.

## Requisitos

- **Python 3.12.10** (versión utilizada por el estudiante en Windows).
- Solo biblioteca estándar de Python: no es necesario ejecutar `pip install`.
- Los archivos originales `instrumento_virtual.py` y `mediciones.log` ya están en la raíz; conservarlos sin cambios.

## Cómo lo ejecuto en Windows con Python 3.12.10

Descargo el repositorio de GitHub y extraigo el ZIP. Abro la carpeta con VS Code y, desde su terminal PowerShell, compruebo la versión:

```powershell
python --version
```

Debe mostrar `Python 3.12.10`. Si tengo varias versiones instaladas, puedo usar `py -3.12` en lugar de `python`.

Para ejecutar cada ejercicio y sus pruebas `assert`:

```powershell
python 01_identificacion.py
python 02_magnitudes.py
python 03_comandos.py
python 04_configurar.py
python 05_cliente.py
python 06_barrido.py
python 07_verificacion.py
python 08_log.py
python 09_estadistica.py
python 10_informe.py
```

Para probar todo junto, primero abro **una terminal** y ejecuto:

```powershell
python instrumento_virtual.py
```

Dejo esa terminal abierta y, en **otra terminal** de la misma carpeta, ejecuto:

```powershell
python 05_cliente.py
python 10_informe.py
```

El instrumento virtual escucha en `127.0.0.1:5555` (osciloscopio) y `127.0.0.1:5556` (multímetro). Para apagarlo, pulso `Ctrl+C` en la primera terminal.

Las pruebas de `06_barrido.py` usan un instrumento falso en memoria para comprobar casos estables; `10_informe.py` es la prueba integrada con red y el log original.

## Desarrollo y revisión

Organizo el trabajo en diez archivos, uno por ejercicio. Utilizo IA como herramienta auxiliar para generar propuestas de código, detectar problemas, preparar pruebas y revisar el funcionamiento. **La revisión personal, la comprensión de cada función y la defensa oral son responsabilidad de quien presenta el trabajo.** El registro de la asistencia recibida se encuentra en `bitacora-ia.md` y debe completarse con los cambios y pruebas realizados por el estudiante.

## Notas de implementación

- Se usan `importlib.import_module` para importar módulos con nombres que comienzan por números, como exige la consigna.
- `leer_log` devuelve `(series, rechazadas)` con series indexadas por `(equipo, canal, magnitud)`.
- Las mediciones fluctuantes se comparan con tolerancia relativa, no igualdad exacta.
- Antes de la defensa, estudiar y revisar todas las funciones y pruebas; la cátedra exige explicarlas individualmente.
- Con el simulador y el log ya incorporados, antes de entregar debo volver a ejecutar las pruebas en mi equipo con Python 3.12.10, registrar los resultados y verificar que puedo explicar cada archivo.

## Uso de IA

Ver `bitacora-ia.md`. Debe mantenerse al día con cada uso posterior de IA que afecte la entrega.
