# Bitácora de IA - Banco de mediciones automatizado

Las consultas de este documento están reconstruidas a partir de los ejercicios y de las dudas tratadas durante el desarrollo. No son transcripciones textuales de conversaciones.

Materia: Programación - Tecnicatura Universitaria en Telecomunicaciones, UTN FRBA  
Python 3.12.10

## 1. Identificación - `01_identificacion.py`

**El prompt**

> Estoy con el primer ejercicio. El *IDN? devuelve todo junto separado por comas, ¿cómo hago para separar el fabricante, modelo, serie y versión? ¿Conviene una lista o un diccionario?

**Qué contestó**

Nos explicó que `split(",")` separa cada dato en una lista y que después los podemos poner en un diccionario. También nos mostró `strip()` para sacar los espacios de sobra.

**Qué cambiamos**

Al principio la función tomaba directamente las cuatro posiciones. Nos dimos cuenta de que el multímetro agrega un quinto campo y que algunas respuestas no tienen datos suficientes. Dejamos que acepte cuatro o cinco campos, pero que guarde solo los primeros cuatro. Si falta algo, devuelve `None`.

**Cómo se comprueba**

Usamos una respuesta del osciloscopio, otra del multímetro y varias incorrectas. Probamos también una cadena vacía y `ERROR: comando desconocido`.

## 2. Magnitudes - `02_magnitudes.py`

**El prompt**

> Para convertir los valores a kHz o mV, ¿tengo que hacer un if para cada unidad? Me parece que va a quedar larguísimo.

**Qué contestó**

Nos sugirió guardar los prefijos y sus potencias en una lista y recorrerla hasta encontrar una escala que sirva. Para convertir el texto recibido a un número se puede usar `float()`.

**Qué cambiamos**

Dejamos separadas `a_numero` y `con_unidad` para no mezclar dos cosas distintas. Después apareció el caso de `999.9999 Hz`: al redondear daba `1000 Hz`, cuando tenía que mostrar `1 kHz`. Agregamos otra comprobación después del redondeo.

**Cómo se comprueba**

Probamos `1000 Hz`, `2500 Hz`, `0.707 V`, `0 V` y el caso de `999.9999 Hz`. También pasamos un texto cualquiera para ver que `a_numero` devolviera `None`.

## 3. Comandos - `03_comandos.py`

**El prompt**

> No entendemos cómo controlar todos los errores de un comando. ¿Hay alguna manera simple de saber si empieza con dos puntos y termina en signo de pregunta?

**Qué contestó**

Nos mostró `startswith()`, `endswith()` y `count()`. También explicó que podemos devolver mensajes distintos según el error encontrado.

**Qué cambiamos**

Separamos las comprobaciones en varios `if`. Primero revisamos si está vacío y si empieza bien; después los espacios y los signos `?`. Por último distinguimos consultas de órdenes, porque una consulta no lleva argumentos.

**Cómo se comprueba**

Hicimos pruebas con comandos correctos y otros mal escritos, como `:CH1:DISPlay??`, `CH1:DISPlay ON` y `:CH1:SCALe 1 v`.

## 4. Configuración - `04_configurar.py`

**El prompt**

> Quise importar 03_comandos.py desde el ejercicio 4 y Python me tira error por el nombre del archivo. ¿Cómo lo importo si la consigna me obliga a dejar ese nombre?

**Qué contestó**

Nos indicó que `importlib.import_module("03_comandos")` permite cargar ese archivo sin cambiarle el nombre.

**Qué cambiamos**

Dejamos el nombre que pide la consigna y usamos `import_module` para llamar a `validar`. También comprobamos el canal antes de armar las cuatro órdenes; si no es CH1 o CH2, devolvemos `None`.

**Cómo se comprueba**

Comparamos los cuatro comandos generados con los del ejemplo y revisamos que todos pasen `validar()`. Probamos además un `CH3`, que no tiene que aceptarse.

## 5. Cliente de red - `05_cliente.py`

**El prompt**

> La conexión abre, pero cuando mando *IDN? el programa queda esperando. ¿Por qué pasa eso si el socket está conectado?

**Qué contestó**

Nos explicó que el instrumento espera un salto de línea para saber que terminó el comando. También sugirió leer hasta el final de la línea, en vez de suponer que todo llega junto.

**Qué cambiamos**

Dejamos el `\n` dentro de `enviar()` para que no haya que acordarse de agregarlo cada vez. En `preguntar()` usamos el mismo método y leemos la respuesta hasta el salto de línea.

**Cómo se comprueba**

Con el instrumento virtual encendido, la consulta `*IDN?` tiene que devolver el modelo ADS3202. Después probamos consultas al estado del canal. Sin el instrumento abierto, la prueba avisa que falta iniciar el simulador.

## 6. Barrido - `06_barrido.py`

**El prompt**

> Tenemos que medir frecuencia, PKPK y CYCRMS en los dos canales. ¿Podemos hacerlo con un for para no escribir seis veces lo mismo?

**Qué contestó**

Nos propuso recorrer una lista de canales y otra de magnitudes, armando el comando SCPI con una cadena de texto.

**Qué cambiamos**

Guardamos cada lectura en un diccionario con el canal, la magnitud, la unidad, la respuesta original y el valor convertido. Si el instrumento responde un error, dejamos el valor como `None` pero conservamos el mensaje.

**Cómo se comprueba**

Usamos una clase sencilla que tiene un método `preguntar()` y devuelve respuestas fijas. Con dos canales se deben obtener seis mediciones. También probamos una respuesta de error y un canal inválido.

## 7. Verificación - `07_verificacion.py`

**El prompt**

> El voltaje eficaz medido nunca es exactamente igual al calculado. Si hacemos medido == teorico nos da falso. ¿Cómo sabemos cuándo está dentro de lo normal?

**Qué contestó**

Nos explicó el error relativo y que las mediciones tienen pequeñas variaciones. Para este ejercicio la tolerancia es del 2 %.

**Qué cambiamos**

Usamos `math.sqrt(2)` para calcular el Vrms de una senoide. Después agregamos controles para datos negativos, valores que no son números y cuando el teórico es cero, así evitamos divisiones incorrectas.

**Cómo se comprueba**

Probamos una medición cercana al valor esperado y otra bastante diferente. La prueba que más nos sirvió fue poner 2 Vpp y 1 Vrms: eso no corresponde a una senoide, así que tiene que dar `False`.

## 8. Registro - `08_log.py`

**El prompt**

> En mediciones.log hay una línea separada por tabulaciones y otra que dice NaN. Con split(" ") una no se separa bien y con float() la otra pasa. ¿Cómo lo controlamos?

**Qué contestó**

Nos explicó que `split()` sin argumentos separa por cualquier espacio en blanco, incluidas las tabulaciones. También que `NaN` no sirve como medición aunque Python pueda convertirlo a `float`.

**Qué cambiamos**

Usamos `split()` y reutilizamos `a_numero()`, que controla que el número sea finito. Agregamos validaciones de cantidad de campos, hora, canal y magnitud. Las líneas vacías y los comentarios se ignoran; las que tienen errores se guardan con el motivo.

**Cómo se comprueba**

Con el registro suministrado se esperan 121 mediciones válidas, agrupadas en seis series, y ocho líneas rechazadas. La línea que tiene tabulaciones debe sumarse a las frecuencias de CH1.

## 9. Estadísticas - `09_estadistica.py`

**El prompt**

> El desvío estándar me da división por cero cuando la lista tiene un solo número. ¿Qué corresponde devolver ahí?

**Qué contestó**

Nos recordó que el desvío de la muestra se calcula dividiendo por `n - 1`, y que con una sola medición la consigna pide devolver `0.0`.

**Qué cambiamos**

Primero revisamos si la lista está vacía. Después separamos el caso de un único valor. Para las otras listas usamos la suma de las diferencias al cuadrado y `math.sqrt()`.

**Cómo se comprueba**

Probamos una lista vacía, una de un solo valor y `[1, 2, 3]`. Con la frecuencia de CH1 del archivo real el promedio debería estar cerca de 1000 Hz y el desvío por debajo de 5 Hz.

## 10. Informe - `10_informe.py`

**El prompt**

> Ya tenemos las funciones hechas, pero no sabemos cómo juntar los resultados sin hacer print dentro de armar_informe. ¿Cómo devolvemos todo como un solo texto?

**Qué contestó**

Nos mostró cómo ir agregando líneas a una lista con `append()` y unirlas al final con `"\n".join(lineas)`.

**Qué cambiamos**

Dejamos la función `armar_informe()` dedicada a construir el texto. La conexión, el barrido y la lectura del registro se hacen desde el bloque principal. Así se puede probar la función pasando datos preparados sin encender el instrumento.

**Cómo se comprueba**

Usamos `assert` para buscar el modelo del equipo, `n=2`, el promedio con unidades y el resultado de una verificación. Para la integración se inicia el instrumento en una terminal y se ejecuta `10_informe.py` en otra.


## Otras consultas que se pueden hacer

Son tres maneras distintas de plantear dudas sin asignarlas a ningún integrante.

1. > No me sale el ejercicio de las unidades. Me anda con 1000 Hz, pero con 999.9999 me termina mostrando 1000 Hz en vez de 1 kHz. ¿Qué condición me está faltando?

2. > Estoy leyendo los datos del archivo `mediciones.log`. Tengo una línea con tabulaciones y otra con `NaN`. ¿Podés explicarme paso a paso cómo revisar las dos cosas usando solo lo que viene con Python?

3. > Quiero probar `barrer()` sin tener que levantar el osciloscopio virtual cada vez. La función recibe un objeto con `preguntar()`. ¿Cómo hago una clase sencilla que conteste valores fijos y me sirva para los `assert`?

---

**Nota sobre la redacción:** Se utilizó inteligencia artificial para ordenar las ideas, reformular algunas explicaciones y mejorar la redacción de este documento. Los prompts reconstruidos no representan conversaciones textuales y las comprobaciones indicadas sirven de guía para repetir las pruebas en Python 3.12.10.
