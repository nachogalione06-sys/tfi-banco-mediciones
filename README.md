# Trabajo final de Programación - Banco de mediciones

Tecnicatura en Telecomunicaciones - UTN FRBA (2026)

El trabajo consiste en hacer un programa en Python que se conecte a un instrumento virtual, lea mediciones y arme un informe. Está dividido en diez ejercicios, como pide la consigna.

## Integrantes

- Ignacio Galione
- Falta agregar nombre y apellido
- Falta agregar nombre y apellido
- Falta agregar nombre y apellido

Somos hasta cuatro personas en total. Antes de entregar hay que completar los nombres.

## Archivos

Los ejercicios van del `01_identificacion.py` al `10_informe.py`.

También están `instrumento_virtual.py` y `mediciones.log`, que son los archivos de la cátedra. Esos dos no se modifican.

## Para probarlo

Usamos **Python 3.12.10** en Windows. No hay que instalar paquetes con pip.

Abrir la carpeta del proyecto en VS Code y entrar a la terminal. Para comprobar Python:

```powershell
python --version
```

Para probar un ejercicio, por ejemplo:

```powershell
python 01_identificacion.py
```

Cada archivo tiene pruebas con `assert`. Se pueden ejecutar del 1 al 10.

Para probar la conexión al osciloscopio, abrir **dos terminales** en la carpeta del proyecto.

En la primera:

```powershell
python instrumento_virtual.py
```

Dejarla abierta. En la segunda:

```powershell
python 05_cliente.py
python 10_informe.py
```

El primero comprueba la conexión y el segundo muestra el informe completo. Para apagar el instrumento se usa `Ctrl+C` en la primera terminal.

## Cosas que revisamos

- El instrumento virtual usa el puerto 5555 para el osciloscopio y el 5556 para el multímetro.
- Se miden frecuencia, voltaje pico a pico y voltaje eficaz de CH1 y CH2.
- El archivo `mediciones.log` tiene 121 mediciones válidas y 8 líneas rechazadas por errores en los datos.
- Las mediciones tienen pequeñas variaciones, por eso se comparan con una tolerancia y no con `==`.

Antes de entregar tenemos que ejecutar todo en nuestras computadoras, completar los integrantes y asegurarnos de poder explicar cada ejercicio en la defensa.

## Uso de IA

La asistencia de IA durante el desarrollo se registra en `bitacora-ia.md`, como pide la consigna.
