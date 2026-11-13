# Trabajo Final Integrador — Programación (UTN, Telecomunicaciones, 2026)

Implementación del **banco de mediciones automatizado en Python**, organizada en diez ejercicios conforme a la consigna `TUT-PROG-TFI-Consigna.pdf`.

## Integrantes

- **Completar nombre y apellido antes de entregar.**

## Estado de archivos y pruebas

Los diez ejercicios están implementados. Se incluyen los dos archivos originales de la cátedra, `instrumento_virtual.py` y `mediciones.log`, que **no deben modificarse**.

- Se ejecutaron las pruebas `assert` de los diez ejercicios.
- Se comprobó una conexión TCP real al instrumento virtual ADS3202 en el puerto 5555, identificación y barrido de ambos canales. La verificación dio coincidencia en ambos casos.
- Se revisó el registro proporcionado: 121 mediciones válidas, 8 líneas rechazadas y 11 líneas ignoradas (incluida la línea terminal vacía). La línea separada por tabulaciones es válida.
- Pendientes antes de entregar: completar nombre y apellido de todos los integrantes, revisar/completar el registro literal de uso de IA y preparar la defensa individual.

## Requisitos

- Python 3, sin paquetes externos.
- Copiar en la raíz los archivos originales `instrumento_virtual.py` y `mediciones.log`.

## Ejecución

Cada ejercicio se ejecuta solo desde la raíz:

```bash
python3 01_identificacion.py
python3 02_magnitudes.py
# ... hasta
python3 10_informe.py
```

Para la integración, iniciar en otra terminal:

```bash
python3 instrumento_virtual.py
```

Después:

```bash
python3 05_cliente.py
python3 06_barrido.py
python3 10_informe.py
```

`06_barrido.py` utiliza un instrumento simulado en memoria para sus pruebas; el programa integrado realiza el barrido real por TCP. Puertos de la cátedra: osciloscopio 127.0.0.1:5555, multímetro 127.0.0.1:5556.

## Notas de implementación

- Se usan `importlib.import_module` para importar módulos con nombres que comienzan por números, como exige la consigna.
- `leer_log` devuelve `(series, rechazadas)` con series indexadas por `(equipo, canal, magnitud)`.
- Las mediciones fluctuantes se comparan con tolerancia relativa, no igualdad exacta.
- Antes de la defensa, estudiar y revisar todas las funciones y pruebas; la cátedra exige explicarlas individualmente.
- **Pendiente:** comprobar la compatibilidad exacta del protocolo contra el simulador original y ejecutar estadísticas sobre el log real.

## Uso de IA

Ver `bitacora-ia.md`. Debe mantenerse al día con cada uso posterior de IA que afecte la entrega.
