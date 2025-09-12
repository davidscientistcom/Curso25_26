Representación de la Información — 3. Unidades básicas de información



3.1 El bit: la unidad mínima

El ordenador funciona gracias a los transistores, pequeños dispositivos electrónicos que actúan como interruptores:
	•	Están abiertos o cerrados,
	•	Conducen o no conducen,
	•	Dejan pasar corriente o no.

Ese comportamiento binario se traduce en dos estados lógicos: 0 y 1.

Así nace el bit (del inglés binary digit = dígito binario), la unidad mínima de información digital.

Un bit solo puede tener dos valores:
	•	0 → nivel bajo
	•	1 → nivel alto

Aunque parezca poca cosa, con la combinación de muchos bits se puede representar cualquier información: números, letras, imágenes, música, vídeos…

Ejemplo intuitivo:
Un interruptor de la luz tiene dos estados: encendido/apagado. Eso es un bit.
Si tienes 8 interruptores en una habitación, puedes combinarlos de muchas formas distintas (todos apagados, uno encendido, varios encendidos…). Pues bien, con 8 bits se pueden formar 256 combinaciones distintas.



3.2 El byte: agrupando bits

Trabajar con bits de forma aislada sería poco práctico. Desde los primeros ordenadores se estableció la costumbre de agruparlos en bloques de 8 bits, llamados bytes.
	•	1 byte = 8 bits
	•	Con 1 byte se pueden representar 2⁸ = 256 valores diferentes (de 0 a 255).

El byte se convirtió en la unidad estándar de almacenamiento y transmisión en informática. La mayoría de los sistemas de codificación de caracteres, como ASCII o Unicode, asignan al menos un byte por símbolo.

Ejemplos:
	•	El carácter 'A' en ASCII se guarda como 01000001.
	•	El número 200 se representa como 11001000 (un byte).



3.3 Múltiplos del byte

La cantidad de información creció rápidamente, y se hizo necesario definir múltiplos más grandes:
	•	Kilobyte (KB): 1 KB = 1024 bytes
	•	Megabyte (MB): 1 MB = 1024 KB = 1.048.576 bytes
	•	Gigabyte (GB): 1 GB = 1024 MB ≈ 1.073 millones de bytes
	•	Terabyte (TB): 1 TB = 1024 GB ≈ 1,1 billones de bytes

⚠️ Atención:
En la publicidad de discos duros y memorias USB se usa a menudo el sistema decimal (1 KB = 1000 bytes). Esto provoca diferencias: un disco de “1 TB” suele mostrar unos 931 GB en el ordenador, que emplea la definición binaria.



3.4 La palabra (word) en informática

Además de los bytes, existe el concepto de palabra (word), que se refiere al número de bits que un procesador maneja de una sola vez en sus registros internos.
	•	Procesadores antiguos de 16 bits → palabra = 16 bits.
	•	Procesadores de 32 bits → palabra = 32 bits.
	•	Procesadores modernos de 64 bits → palabra = 64 bits.

La palabra determina:
	•	El tamaño máximo de dato que la CPU puede procesar directamente.
	•	La capacidad de direccionamiento de memoria (ejemplo: con 32 bits → 2³² posiciones = 4 GB).



3.5 El crecimiento exponencial de la información

El número de combinaciones posibles con n bits es:

\text{Combinaciones posibles} = 2^n

Ejemplos:
	•	1 bit → 2 valores posibles.
	•	2 bits → 4 valores posibles.
	•	3 bits → 8 valores posibles.
	•	8 bits (1 byte) → 256 valores posibles.
	•	16 bits → 65.536 valores posibles.

Caso real:
El alfabeto español tiene 27 letras + ñ + símbolos básicos. Con menos de 7 bits (2⁷ = 128 combinaciones) ya se puede codificar. Por eso ASCII usa originalmente 7 bits.



3.6 Analogía cotidiana

Imagina una cerradura con varias llaves:
	•	Con 1 llave (1 bit) solo hay dos estados posibles: cerrada o abierta.
	•	Con 2 llaves (2 bits) ya hay 4 combinaciones posibles (ninguna, solo la primera, solo la segunda, ambas).
	•	Con 8 llaves (1 byte) se disparan las posibilidades: 256 combinaciones diferentes.

Esa explosión combinatoria es lo que permite que, con unos pocos bytes, podamos representar imágenes de millones de colores o sonidos complejos.



3.7 Ejemplos prácticos del mundo real
	•	Una página de texto con 1800 caracteres ocupa ~1800 bytes (≈ 1,8 KB).
	•	Una canción en MP3 de 3 minutos ocupa ~3 MB.
	•	Una foto de móvil de 12 MP en JPEG puede ocupar entre 3 y 5 MB.
	•	Una película en Full HD ronda los 4 GB.

Esto ayuda a entender por qué necesitamos múltiplos tan grandes (MB, GB, TB) en la vida diaria.



3.8 Mini-ejercicios
	1.	¿Cuántos valores diferentes se pueden representar con 10 bits?
	2.	Si tienes una memoria de 2 KB, ¿cuántos bytes reales caben en ella? ¿y cuántos bits?
	3.	Un procesador de 32 bits, ¿cuántas posiciones de memoria puede direccionar como máximo?
	4.	Si quieres codificar 50 símbolos diferentes, ¿cuántos bits mínimos necesitas?



Soluciones rápidas
	1.	2¹⁰ = 1024 valores.
	2.	2 KB = 2 × 1024 = 2048 bytes = 16.384 bits.
	3.	2³² ≈ 4.294.967.296 posiciones (≈ 4 GB).
	4.	Se necesita n tal que 2ⁿ ≥ 50 → 2⁵ = 32 (no alcanza), 2⁶ = 64 (sí). → 6 bits.



3.9 Resumen
	•	El bit es la unidad mínima de información: 0 o 1.
	•	El byte (8 bits) es la unidad básica de almacenamiento y transmisión.
	•	Los múltiplos (KB, MB, GB, TB) permiten medir volúmenes grandes.
	•	La palabra depende de la arquitectura del procesador (16, 32, 64 bits).
	•	Con pocos bits se pueden generar muchísimas combinaciones gracias al crecimiento exponencial.

