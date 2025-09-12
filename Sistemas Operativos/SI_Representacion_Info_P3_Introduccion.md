Representación de la Información — 3. Unidades básicas de información



3.1 El bit: la unidad mínima

Un ordenador funciona con transistores que actúan como interruptores: están abiertos o cerrados, conducen o no conducen, pasan corriente o no. Este comportamiento binario se traduce en dos estados lógicos: 0 y 1.

A partir de ahí se define la unidad mínima de información digital, llamada bit (del inglés binary digit = dígito binario).
Un bit solo puede tomar dos valores:
	•	0 → nivel bajo
	•	1 → nivel alto

Aunque parezca muy poco, con solo bits podemos representar absolutamente todo: números, letras, imágenes, música, vídeos… Es cuestión de combinar muchos.

Ejemplo intuitivo:
Piensa en un interruptor de la luz: tiene dos estados (encendido/apagado). Eso es un bit. Ahora imagina una habitación con 8 interruptores. Puedes combinarlos de muchas maneras (todos apagados, algunos encendidos, todos encendidos…). Pues bien, con 8 bits se pueden formar 256 combinaciones diferentes.



3.2 El byte: agrupando bits

Trabajar con bits aislados sería incómodo. Por eso, desde los primeros ordenadores, se decidió agruparlos en bloques de 8 bits, a lo que llamamos byte.
	•	1 byte = 8 bits
	•	Con 1 byte podemos representar 2⁸ = 256 combinaciones diferentes (números del 0 al 255, letras, símbolos…).

El byte se convirtió en la unidad estándar de almacenamiento y transmisión de datos en informática. La mayoría de los sistemas de codificación de caracteres (como ASCII o Unicode) usan al menos un byte para representar un símbolo.

Ejemplo:
	•	El carácter 'A' en ASCII se codifica con el byte 01000001.
	•	El número 200 en binario se guarda como 11001000 (un byte).



3.3 Múltiplos del byte

A medida que la informática avanzó, los datos crecieron exponencialmente. Para manejar cantidades grandes, se definieron múltiplos:
	•	Kilobyte (KB): 1 KB = 1024 bytes
	•	Megabyte (MB): 1 MB = 1024 KB = 1.048.576 bytes
	•	Gigabyte (GB): 1 GB = 1024 MB ≈ 1.073 millones de bytes
	•	Terabyte (TB): 1 TB = 1024 GB ≈ 1,1 billones de bytes

⚠️ Nota importante:
En el ámbito comercial (discos duros, memorias USB), muchos fabricantes usan el sistema decimal (1 KB = 1000 bytes). Por eso, cuando compras un disco de “1 TB”, tu ordenador suele mostrar algo menos (~931 GB), porque el sistema operativo usa la definición binaria.



3.4 La palabra (word) en informática

Además de bytes, existe el concepto de palabra (word).
Una palabra es el número de bits que un procesador puede manejar de una sola vez.
	•	En procesadores antiguos de 16 bits → una palabra = 16 bits.
	•	En procesadores de 32 bits → una palabra = 32 bits.
	•	En procesadores modernos de 64 bits → una palabra = 64 bits.

La palabra define aspectos como:
	•	El tamaño máximo de datos que la CPU puede manejar directamente.
	•	El tamaño de las direcciones de memoria (ej.: con 32 bits se direccionan 2³² posiciones = 4 GB).



3.5 Cómo crece la información con los bits

El número de combinaciones posibles con n bits es:

\text{Combinaciones posibles} = 2^n

Ejemplo práctico:
	•	Con 1 bit → 2 combinaciones (0 y 1).
	•	Con 2 bits → 4 combinaciones (00, 01, 10, 11).
	•	Con 3 bits → 8 combinaciones.
	•	Con 8 bits (1 byte) → 256 combinaciones.
	•	Con 16 bits → 65.536 combinaciones.

Esto se aplica tanto para números como para símbolos o colores de una imagen.

Caso real:
Si quieres codificar los caracteres del alfabeto español (27 letras + ñ + símbolos básicos), te bastaría con menos de 7 bits (2⁷ = 128). Por eso ASCII usa 7 bits originalmente.



3.6 Analogía cotidiana

Piensa en una cerradura con varias llaves:
	•	Con 1 llave (1 bit) solo hay dos estados: cerrada o abierta.
	•	Con 2 llaves (2 bits), ya tienes 4 posibles combinaciones (ninguna, solo la primera, solo la segunda, ambas).
	•	Con 8 llaves (1 byte), las combinaciones explotan a 256.

Este crecimiento exponencial explica por qué, con unos cuantos bytes, ya se pueden representar imágenes complejas o sonidos.



3.7 Ejemplos reales de uso de bytes
	•	Una página de texto con 1800 caracteres ocupa ~1800 bytes (≈ 1,8 KB).
	•	Una canción en MP3 de 3 minutos ocupa ~3 MB.
	•	Una foto de móvil de 12 MP puede ocupar entre 3 y 5 MB en JPEG.
	•	Una película en FullHD puede ocupar ~4 GB.



3.8 Mini-ejercicios
	1.	¿Cuántos valores diferentes puede representar un sistema con 10 bits?
	2.	Si tienes una memoria de 2 KB, ¿cuántos bytes reales caben en ella? ¿y cuántos bits?
	3.	Un procesador de 32 bits, ¿cuántas posiciones de memoria distintas puede direccionar?
	4.	Si quieres codificar 50 símbolos diferentes, ¿cuántos bits mínimos necesitas?



Soluciones rápidas
	1.	2¹⁰ = 1024 valores.
	2.	2 KB = 2 × 1024 = 2048 bytes = 16.384 bits.
	3.	2³² ≈ 4.294.967.296 posiciones (≈ 4 GB).
	4.	Necesitas n tal que 2ⁿ ≥ 50 → 2⁵ = 32 (no llega), 2⁶ = 64 (sí). → 6 bits.



3.9 Resumen
	•	El bit es la unidad mínima: 0 o 1.
	•	Los bytes (8 bits) son la unidad básica de almacenamiento y transmisión.
	•	Los múltiplos (KB, MB, GB, TB) permiten expresar grandes cantidades.
	•	La palabra depende de la arquitectura del procesador (16, 32, 64 bits).
	•	El crecimiento es exponencial: con pocos bits se pueden representar muchísimas combinaciones.



👉 Así, en este capítulo tus alumnos ya entienden cómo se mide y organiza la información en un ordenador. En el Capítulo 4 (sistemas de numeración) veremos cómo se usan esos bits para representar números en binario, hexadecimal, etc.



¿Quieres que te prepare este capítulo 3 en un .md independiente como los anteriores, o prefieres que cuando acabemos toda la unidad te dé un único documento completo con todos los capítulos seguidos?