# Trabajo Final Integrador — Programación (UTN, Telecomunicaciones, 2026)

Implementación del **banco de mediciones automatizado en Python**, organizada en diez ejercicios conforme a la consigna `TUT-PROG-TFI-Consigna.pdf`.

## Integrantes

- **Completar nombre y apellido antes de entregar.**

## Estado y archivos faltantes

Los diez ejercicios están implementados con pruebas `assert`. **Faltan los dos archivos originales que debe proporcionar la cátedra:** `instrumento_virtual.py` y `mediciones.log`. No se generaron sustitutos ni se modificaron, porque la consigna lo prohíbe. Hasta disponer de ambos, la prueba integral con datos reales está pendiente. La implementación debe verificarse contra el simulador original antes de entregar.

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
