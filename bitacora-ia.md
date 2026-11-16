# Bitácora de IA - Banco de mediciones automatizado

Las diez consultas por ejercicio se conservaron como preguntas de estudio redactadas para repasar el código. Más abajo se distinguen los mensajes textuales realizados durante el desarrollo del repositorio.

Materia: Programación - Tecnicatura Universitaria en Telecomunicaciones, UTN FRBA  
Python 3.12.10

## 1. Identificación - `01_identificacion.py`

**El prompt**

> Che estoy con el 01, el *IDN? me devuelve todo en una sola linea con comas. como lo separo para guardar fabricante, modelo, serie y version? y el multimetro tiene 5 datos, eso como lo manejo?

**Qué contestó**

Nos explicó que `split(",")` separa cada dato en una lista y que después los podemos poner en un diccionario. También nos mostró `strip()` para sacar los espacios de sobra.

**Qué cambiamos**

Al principio la función tomaba directamente las cuatro posiciones. Nos dimos cuenta de que el multímetro agrega un quinto campo y que algunas respuestas no tienen datos suficientes. Dejamos que acepte cuatro o cinco campos, pero que guarde solo los primeros cuatro. Si falta algo, devuelve `None`.

**Cómo se comprueba**

Usamos una respuesta del osciloscopio, otra del multímetro y varias incorrectas. Probamos también una cadena vacía y `ERROR: comando desconocido`.

## 2. Magnitudes - `02_magnitudes.py`

**El prompt**

> Bueno ahora el 02. tengo que pasar valores como 1000 Hz a 1 kHz y 0.707 V a mV. no quiero hacer mil if, hay una forma mas simple? tambien tengo el caso ese de 999.9999 que al redondear se rompe

**Qué contestó**

Nos sugirió guardar los prefijos y sus potencias en una lista y recorrerla hasta encontrar una escala que sirva. Para convertir el texto recibido a un número se puede usar `float()`.

**Qué cambiamos**

Dejamos separadas `a_numero` y `con_unidad` para no mezclar dos cosas distintas. Después apareció el caso de `999.9999 Hz`: al redondear daba `1000 Hz`, cuando tenía que mostrar `1 kHz`. Agregamos otra comprobación después del redondeo.

**Cómo se comprueba**

Probamos `1000 Hz`, `2500 Hz`, `0.707 V`, `0 V` y el caso de `999.9999 Hz`. También pasamos un texto cualquiera para ver que `a_numero` devolviera `None`.

## 3. Comandos - `03_comandos.py`

**El prompt**

> En el 03 me piden revisar los comandos SCPI. como compruebo si empiezan con : o * y si terminan con ? y de paso controlar los espacios y argumentos? porque me estoy enredando con los if

**Qué contestó**

Nos mostró `startswith()`, `endswith()` y `count()`. También explicó que podemos devolver mensajes distintos según el error encontrado.

**Qué cambiamos**

Separamos las comprobaciones en varios `if`. Primero revisamos si está vacío y si empieza bien; después los espacios y los signos `?`. Por último distinguimos consultas de órdenes, porque una consulta no lleva argumentos.

**Cómo se comprueba**

En `03_comandos.py` quedaron pruebas con `assert` para `:CH1:DISPlay??`, `CH1:DISPlay ON` y `:CH1:SCALe 1 v`. Este último caso se agregó para comprobar que una orden con dos argumentos se rechace.

## 4. Configuración - `04_configurar.py`

**El prompt**

> Estoy haciendo el 04 y quiero usar validar del archivo 03_comandos.py, pero no me deja importarlo porque el nombre empieza con numero. como hago sin cambiar el nombre que pide el pdf?

**Qué contestó**

Nos indicó que `importlib.import_module("03_comandos")` permite cargar ese archivo sin cambiarle el nombre.

**Qué cambiamos**

Dejamos el nombre que pide la consigna y usamos `import_module` para llamar a `validar`. También comprobamos el canal antes de armar las cuatro órdenes; si no es CH1 o CH2, devolvemos `None`.

**Cómo se comprueba**

Comparamos los cuatro comandos generados con los del ejemplo y revisamos que todos pasen `validar()`. Probamos además un `CH3`, que no tiene que aceptarse.

## 5. Cliente de red - `05_cliente.py`

**El prompt**

> En el 05 tengo la conexion con socket pero cuando pregunto *IDN? se queda esperando. hay algo que tenga que mandar al final del comando? y como leo la respuesta completa sin que quede colgado?

**Qué contestó**

Nos explicó que el instrumento espera un salto de línea para saber que terminó el comando. También sugirió leer hasta el final de la línea, en vez de suponer que todo llega junto.

**Qué cambiamos**

Dejamos el `\n` dentro de `enviar()` para que no haya que acordarse de agregarlo cada vez. En `preguntar()` usamos el mismo método y leemos la respuesta hasta el salto de línea.

**Cómo se comprueba**

Con el instrumento virtual encendido, la consulta `*IDN?` tiene que devolver el modelo ADS3202. Después probamos consultas al estado del canal. Sin el instrumento abierto, la prueba avisa que falta iniciar el simulador.

## 6. Barrido - `06_barrido.py`

**El prompt**

> Para el 06 tengo que pedir 3 mediciones por cada canal, serian 6 consultas. puedo hacerlo con for para no repetir codigo? y si el equipo contesta error necesito guardar el texto igual

**Qué contestó**

Nos propuso recorrer una lista de canales y otra de magnitudes, armando el comando SCPI con una cadena de texto.

**Qué cambiamos**

Guardamos cada lectura en un diccionario con el canal, la magnitud, la unidad, la respuesta original y el valor convertido. Si el instrumento responde un error, dejamos el valor como `None` pero conservamos el mensaje.

**Cómo se comprueba**

Usamos una clase sencilla que tiene un método `preguntar()` y devuelve respuestas fijas. Con dos canales se deben obtener seis mediciones. También probamos una respuesta de error y un canal inválido.

## 7. Verificación - `07_verificacion.py`

**El prompt**

> En el 07 tengo un problema: el vrms que mide el equipo no da exactamente igual al que calculo. como lo comparo sin usar ==? la consigna habla de 2% de tolerancia y no me queda claro como aplicarlo

**Qué contestó**

Nos explicó el error relativo y que las mediciones tienen pequeñas variaciones. Para este ejercicio la tolerancia es del 2 %.

**Qué cambiamos**

Usamos `math.sqrt(2)` para calcular el Vrms de una senoide. Después agregamos controles para datos negativos, valores que no son números y cuando el teórico es cero, así evitamos divisiones incorrectas.

**Cómo se comprueba**

Probamos una medición cercana al valor esperado y otra bastante diferente. La prueba que más nos sirvió fue poner 2 Vpp y 1 Vrms: eso no corresponde a una senoide, así que tiene que dar `False`.

## 8. Registro - `08_log.py`

**El prompt**

> Revisame el 08, el mediciones.log tiene una linea con tabulaciones y otra con NaN. con split(" ") no me separa todo y float acepta el NaN. como valido eso y dejo registradas las lineas malas?

**Qué contestó**

Nos explicó que `split()` sin argumentos separa por cualquier espacio en blanco, incluidas las tabulaciones. También que `NaN` no sirve como medición aunque Python pueda convertirlo a `float`.

**Qué cambiamos**

Usamos `split()` y reutilizamos `a_numero()`, que controla que el número sea finito. Agregamos validaciones de cantidad de campos, hora, canal y magnitud. Las líneas vacías y los comentarios se ignoran; las que tienen errores se guardan con el motivo.

**Cómo se comprueba**

Con el registro suministrado se esperan 121 mediciones válidas, agrupadas en seis series, y ocho líneas rechazadas. La línea que tiene tabulaciones debe sumarse a las frecuencias de CH1.

## 9. Estadísticas - `09_estadistica.py`

**El prompt**

> Con el 09 tengo una duda. el desvio se divide por n-1 pero si hay un solo valor me tira division por cero. que hago en ese caso? y como compruebo el promedio con los datos del log?

**Qué contestó**

Nos recordó que el desvío de la muestra se calcula dividiendo por `n - 1`, y que con una sola medición la consigna pide devolver `0.0`.

**Qué cambiamos**

Primero revisamos si la lista está vacía. Después separamos el caso de un único valor. Para las otras listas usamos la suma de las diferencias al cuadrado y `math.sqrt()`.

**Cómo se comprueba**

Probamos una lista vacía, una de un solo valor y `[1, 2, 3]`. Con la frecuencia de CH1 del archivo real el promedio debería estar cerca de 1000 Hz y el desvío por debajo de 5 Hz.

## 10. Informe - `10_informe.py`

**El prompt**

> Ahora el 10, como junto todo para generar el informe? quiero que armar_informe devuelva el texto y no imprima nada adentro. despues lo muestro desde el main con las mediciones de los dos canales

**Qué contestó**

Nos mostró cómo ir agregando líneas a una lista con `append()` y unirlas al final con `"\n".join(lineas)`.

**Qué cambiamos**

Dejamos la función `armar_informe()` dedicada a construir el texto. La conexión, el barrido y la lectura del registro se hacen desde el bloque principal. Así se puede probar la función pasando datos preparados sin encender el instrumento.

**Cómo se comprueba**

Usamos `assert` para buscar el modelo del equipo, `n=2`, el promedio con unidades y el resultado de una verificación. Para la integración se inicia el instrumento en una terminal y se ejecuta `10_informe.py` en otra.



## Mensajes textuales registrados durante el desarrollo

Estos mensajes sí se copiaron literalmente de la conversación donde se trabajó sobre el proyecto. Son distintos de las diez preguntas de estudio anteriores.

### Preparación del repositorio

**El prompt**

> arma un repo en git con todo eso

**Qué contestó y qué se cambió**

La IA preparó el primer conjunto de archivos del proyecto, con funciones y pruebas de los diez ejercicios. También organizó el README y una primera bitácora.

**Cómo se verificó**

Se revisaron los archivos generados y posteriormente se subieron al repositorio de GitHub. El código requiere ejecutar sus pruebas después de cada revisión.

### Subida a GitHub

**El prompt**

> ya lo cree con el no,bre ahora hacelo ahí

**Qué contestó y qué se cambió**

La IA localizó el repositorio `tfi-banco-mediciones` y cargó allí los ejercicios y la documentación. Después se incorporaron `instrumento_virtual.py` y `mediciones.log` proporcionados en la conversación.

**Cómo se verificó**

Se consultaron los archivos subidos desde GitHub. El instrumento virtual se comparó con el archivo original y el log se revisó para contar las mediciones válidas y rechazadas.

### Versión de Python

**El prompt**

> Python 3.12.10 hacelo paraesta vercion y como si todo lo hiciera yo, y la ia fuece asistente

**Qué contestó y qué se cambió**

La IA adaptó las instrucciones del README para ejecutar los ejercicios con Python 3.12.10 en Windows, sin instalar paquetes externos.

**Cómo se verificó**

El README quedó actualizado en GitHub. La ejecución en la computadora de los integrantes debe comprobarse por separado.

### Revisión de legibilidad del código

**El prompt**

> Wey, hacelo como que todo lo escribimos personas no Ia, no tan perfecto, bien pero no ia

**Qué contestó y qué se cambió**

La IA reescribió partes de los diez ejercicios, simplificando variables, comentarios y algunas instrucciones. También se reforzaron pruebas relacionadas con el archivo de mediciones.

**Cómo se verificó**

Los cambios quedaron registrados en GitHub. Falta dejar constancia de la ejecución local final de esta versión con Python 3.12.10.

---

**Nota sobre el uso de IA:** La IA intervino tanto en la generación y revisión de código como en la organización y redacción de la documentación. Las diez preguntas por ejercicio son formulaciones para estudiar, no sustitutos de los mensajes literales. Este apartado recoge mensajes originales de la conversación, pero la bitácora debe completarse con otros intercambios y resultados de pruebas si se usa como registro exhaustivo.

