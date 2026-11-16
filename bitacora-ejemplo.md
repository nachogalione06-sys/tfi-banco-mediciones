# Bitácora de IA - Ejemplo de redacción

> **Ejemplo inventado para orientar la escritura.** Las consultas, correcciones y pruebas de este archivo son situaciones hipotéticas. **No es el registro real del grupo ni reemplaza `bitacora-ia.md`.** Antes de usar una entrada en la entrega hay que reemplazarla por lo que realmente se preguntó, se modificó y se probó.

## 1. Identificación del equipo

**El prompt (ejemplo):** "No entiendo bien cómo separar la respuesta que manda el instrumento. ¿Cómo puedo guardar fabricante, modelo, serie y versión?"

**Qué contestó:** Nos mostró que podíamos usar `split(",")` para separar los datos y después guardarlos en un diccionario.

**Qué cambiamos (ejemplo):** Nos dimos cuenta de que el multímetro devuelve un dato de más y que algunas respuestas pueden venir vacías. Entonces agregamos controles antes de armar el diccionario.

**Cómo lo verificaríamos:** Con `assert` para una respuesta de cuatro campos, una de cinco y otra que no sirva.

## 2. Magnitudes

**El prompt (ejemplo):** "¿Cómo hacemos para que 1000 Hz aparezca como 1 kHz sin cambiar el valor de la medición?"

**Qué contestó:** Explicó los prefijos y mostró cómo recorrer distintas escalas con un `for`.

**Qué cambiamos (ejemplo):** Separamos la conversión a número de la parte que arma el texto con la unidad. También tuvimos en cuenta el caso en que el redondeo convierte 999.9999 en 1000.

**Cómo lo verificaríamos:** Probando 1000 Hz, 0.707 V, 0 V y el caso de 999.9999 Hz.

## 3. Comandos

**El prompt (ejemplo):** "¿Cómo sé si un comando SCPI es una consulta o una orden?"

**Qué contestó:** Nos explicó cómo usar `endswith("?")` y revisar los espacios del comando.

**Qué cambiamos (ejemplo):** Dividimos las comprobaciones en condiciones cortas para saber qué error tiene el texto, en lugar de devolver siempre el mismo mensaje.

**Cómo lo verificaríamos:** Con comandos correctos y otros con dos signos de pregunta, espacios de más o argumentos donde no van.

## 4. Configuración del canal

**El prompt (ejemplo):** "Los archivos empiezan con un número y Python no me deja importarlos normalmente. ¿Qué puedo hacer?"

**Qué contestó:** Nos indicó que se puede usar `import_module` de `importlib`.

**Qué cambiamos (ejemplo):** Dejamos los nombres como los pide la consigna y usamos esa forma de importar `validar` desde el tercer ejercicio.

**Cómo lo verificaríamos:** Comprobando que los cuatro comandos de CH1 sean los esperados y que todos pasen por `validar`.

## 5. Conexión con el instrumento

**El prompt (ejemplo):** "El instrumento queda esperando y no devuelve nada cuando pregunto. ¿Puede ser por cómo mando el comando?"

**Qué contestó:** Nos explicó que el comando debe terminar con `\n`, porque así el instrumento sabe cuándo termina la línea.

**Qué cambiamos (ejemplo):** Dejamos el salto de línea dentro de `enviar` para no tener que agregarlo cada vez que hacemos una consulta.

**Cómo lo verificaríamos:** Encendiendo el instrumento virtual en otra terminal y preguntándole `*IDN?`.

## 6. Barrido de los canales

**El prompt (ejemplo):** "Tenemos tres mediciones por canal. ¿Hace falta escribir seis consultas una por una?"

**Qué contestó:** Propuso recorrer canales y magnitudes con dos bucles.

**Qué cambiamos (ejemplo):** Guardamos el texto original de la respuesta además del número convertido, porque si hay un error queremos saber qué contestó el instrumento.

**Cómo lo verificaríamos:** Con un instrumento falso que devuelva respuestas fijas y comprobar que haya seis resultados.

## 7. Verificación de voltajes

**El prompt (ejemplo):** "Si el Vrms medido no da exactamente igual que el calculado, ¿cómo comprobamos si está bien?"

**Qué contestó:** Explicó el error relativo y sugirió comparar con una tolerancia.

**Qué cambiamos (ejemplo):** Dejamos una tolerancia de 2 % y controlamos que no se intente calcular con datos vacíos o inválidos.

**Cómo lo verificaríamos:** Una medición cercana al valor teórico debería dar verdadero y una onda cuadrada de 2 Vpp y 1 Vrms debería dar falso.

## 8. Lectura del archivo log

**El prompt (ejemplo):** "Una línea del archivo está separada por tabulaciones y no la toma bien. ¿Cómo la separamos?"

**Qué contestó:** Explicó la diferencia entre `split(" ")` y `split()`.

**Qué cambiamos (ejemplo):** Usamos la segunda opción para no perder datos válidos. También controlamos las horas y los números que no sirven, como `NaN`.

**Cómo lo verificaríamos:** Leyendo el archivo de la cátedra y comprobando las mediciones aceptadas y las rechazadas.

## 9. Estadísticas

**El prompt (ejemplo):** "¿Por qué el desvío me da error si solo hay una medición?"

**Qué contestó:** Nos señaló que, para una muestra, la cuenta divide por `n - 1`.

**Qué cambiamos (ejemplo):** Agregamos una condición especial para devolver desvío 0.0 cuando hay un único valor.

**Cómo lo verificaríamos:** Con una lista vacía, una lista de un elemento y otra de varios números cuyo promedio podamos calcular a mano.

## 10. Informe

**El prompt (ejemplo):** "¿Cómo juntamos las mediciones y estadísticas para mostrar un informe sin imprimir desde la función?"

**Qué contestó:** Sugirió guardar cada línea en una lista y al final unirlas con `"\n".join(lineas)`.

**Qué cambiamos (ejemplo):** Dejamos `armar_informe` solo para armar el texto y pusimos el `print` en el bloque principal.

**Cómo lo verificaríamos:** Pasándole datos fijos y comprobando con `assert` que aparezcan el nombre del equipo, los promedios y el resultado de cada canal.

---

Este documento es una **muestra de estilo**, no una bitácora auténtica. Para la entrega hay que conservar las consultas originales y describir únicamente modificaciones y pruebas realizadas de verdad.
