Representación de la Información — 5. Representación de números enteros



5.1 Enteros sin signo

El caso más simple: representar únicamente números enteros positivos (incluido el 0).
Si tenemos N bits, podemos representar desde 0 hasta 2^N - 1.

Ejemplo:
	•	Con 3 bits: del 0 al 7.
	•	Con 8 bits (1 byte): del 0 al 255.
	•	Con 16 bits: del 0 al 65.535.

Este sistema se llama “enteros sin signo” (unsigned integers en inglés).
Se usa mucho en programación cuando sabemos que los valores no serán negativos (ej.: contar objetos, tamaños de archivos, direcciones de memoria).



5.2 La necesidad de representar números negativos

El problema es que muchas operaciones del mundo real requieren números negativos (temperaturas, deudas, desplazamientos hacia atrás, etc.).
El ordenador solo entiende 0 y 1, pero debemos inventar un modo de reservar un bit para el signo. A partir de ahí, hay varios métodos.



5.3 Representación con signo y magnitud

La forma más intuitiva:
	•	El primer bit indica el signo (0 = positivo, 1 = negativo).
	•	El resto de los bits representan la magnitud (valor absoluto).

Ejemplo con 4 bits (1 para signo, 3 para valor):
	•	0101 = +5
	•	1101 = -5

Problema: el 0 tiene dos representaciones (0000 y 1000), lo que complica operaciones aritméticas.
Por eso, este método casi no se usa en hardware, aunque sirve para introducir la idea.



5.4 Complemento a 1

En este método, los números negativos se obtienen invirtiendo los bits del número positivo correspondiente.

Ejemplo con 4 bits:
	•	+5 = 0101
	•	-5 = 1010 (inversión de todos los bits)

Problema: igual que antes, hay dos ceros (0000 y 1111), lo que complica.



5.5 Complemento a 2 (el estándar actual)

El complemento a 2 es el sistema usado en prácticamente todos los ordenadores modernos, porque simplifica la aritmética binaria.

Cómo se obtiene un número negativo en complemento a 2
	1.	Representar el valor absoluto en binario.
	2.	Invertir todos los bits (complemento a 1).
	3.	Sumar 1 al resultado.

Ejemplo (con 4 bits, valor = 5):
	•	Paso 1: +5 = 0101.
	•	Paso 2: invertimos → 1010.
	•	Paso 3: sumamos 1 → 1011.

Resultado: 1011 representa -5 en complemento a 2.

Ventaja
	•	Solo hay un 0 (0000).
	•	La suma/resta se hace igual para positivos y negativos, sin reglas especiales.

Rango representable

Con N bits, el rango es:
[-2^{N-1}, \; 2^{N-1} - 1]

Ejemplo con 8 bits:
	•	Desde -128 hasta +127.



5.6 Ejemplo práctico de suma con complemento a 2

Queremos calcular 7 + (-5) con 4 bits.
	•	+7 → 0111
	•	-5 → 1011 (como vimos antes)

Suma:

  0111
+ 1011
------
 10010

Nos quedamos solo con los 4 bits menos significativos: 0010 = 2.
¡Correcto!



5.7 Desbordamiento (overflow)

Con un número fijo de bits, no podemos representar cualquier valor.
Ejemplo: con 4 bits en complemento a 2, el rango es [-8, +7].

Si intentamos calcular 7 + 3 = 10, no se puede representar y se produce un overflow.
El resultado que da el hardware no es el esperado, y por eso los lenguajes de programación incluyen verificaciones o tipos de datos más grandes.



5.8 Usos prácticos en programación
	•	En C, Java, Python, etc., existen tipos como int, short, long, que corresponden a enteros en complemento a 2 de diferentes longitudes.
	•	Unsigned int en C permite aprovechar todo el rango positivo, pero no admite negativos.
	•	Muchos errores de software (bugs de seguridad incluidos) se deben a desbordamientos de enteros.



5.9 Analogía para alumnos

Imagina un reloj digital de 12 horas:
	•	Si son las 10 y le sumas 3 horas → aparece la 1.
	•	Algo parecido pasa con los bits: cuando se desborda, “da la vuelta” y vuelve a empezar desde el extremo negativo o positivo.



5.10 Mini-ejercicios
	1.	Representa el número -6 con 8 bits en complemento a 2.
	2.	¿Cuál es el rango representable con 16 bits en complemento a 2?
	3.	Calcula 12 + (-9) con 5 bits en complemento a 2.
	4.	¿Por qué es mejor el complemento a 2 que el signo y magnitud?



Soluciones rápidas
	1.	6 = 00000110 → invertimos: 11111001 → sumamos 1: 11111010.
	2.	Rango = [-32768, +32767].
	3.	12 = 01100, -9 = 10111 → suma = 10011 = -13 → pero ojo: con 5 bits el rango es [-16..+15], y el resultado es válido.
	4.	Porque tiene un solo 0 y simplifica las operaciones aritméticas (suma/resta igual para positivos y negativos).



5.11 Resumen
	•	Enteros sin signo: de 0 a 2^N - 1.
	•	Con signo y magnitud: simple pero ineficiente (dos ceros).
	•	Complemento a 1: mejora, pero mantiene el problema del doble 0.
	•	Complemento a 2: el estándar actual, eficiente y práctico.
	•	El rango de N bits es [-2^{N-1}, 2^{N-1} - 1].
	•	El overflow es un límite real de la representación que hay que tener en cuenta.

