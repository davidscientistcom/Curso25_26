Representación de la Información — 4. Sistemas de numeración


4.1 La necesidad de diferentes sistemas de numeración

Los humanos estamos acostumbrados a trabajar con el sistema decimal, que tiene como base el número 10, seguramente porque tenemos 10 dedos. Cada cifra en un número decimal puede tomar valores entre 0 y 9, y la posición de esa cifra le da un peso distinto (unidades, decenas, centenas…).

Pero los ordenadores no funcionan en base 10. Sus circuitos electrónicos solo distinguen dos estados, por lo que el sistema natural para ellos es el binario (base 2). Además, para facilitar la lectura humana, se suelen usar otros sistemas intermedios como el octal (base 8) y el hexadecimal (base 16), que son atajos para agrupar bits.



4.2 Sistemas posicionales

Un sistema de numeración posicional se basa en dos ideas:
	1.	Cada dígito pertenece a un conjunto limitado de símbolos (ej.: {0..9} en decimal, {0..1} en binario).
	2.	El valor de cada dígito depende de su posición dentro del número y de la base del sistema.

Ejemplo en decimal:
El número 473 se interpreta como:

473 = 4 \times 10^2 + 7 \times 10^1 + 3 \times 10^0 = 400 + 70 + 3



4.3 Sistema binario (base 2)

En binario, solo existen dos símbolos: 0 y 1. Cada posición tiene un peso que es una potencia de 2.

Ejemplo:
El número binario 1011 equivale a:

1011 = 1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0 = 8 + 0 + 2 + 1 = 11

Nota: un bit es una sola cifra binaria. Varios bits juntos representan números más grandes.



4.4 Sistema octal (base 8)

El sistema octal usa los símbolos {0,1,2,3,4,5,6,7}. Cada posición es una potencia de 8.

Se usa a veces como abreviatura del binario, porque 3 bits equivalen exactamente a 1 dígito octal (2³ = 8).

Ejemplo:
Número binario 110010 → en grupos de 3 bits: 110 010 = (6)(2) = 62 en octal.



4.5 Sistema hexadecimal (base 16)

El hexadecimal utiliza 16 símbolos:
{0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F}, donde A=10, B=11, …, F=15.

Es muy utilizado en informática porque 4 bits = 1 dígito hexadecimal (2⁴ = 16).
Esto hace que sea fácil traducir binario ↔ hexadecimal.

Ejemplo:
Binario 11011010 → en grupos de 4 bits: 1101 1010 = (D)(A) → DA en hexadecimal.



4.6 Conversión entre sistemas

De binario a decimal

Se aplica la fórmula de las potencias de 2.
Ejemplo: 101101 = 1·2⁵ + 0·2⁴ + 1·2³ + 1·2² + 0·2¹ + 1·2⁰ = 45.

De decimal a binario

Se divide sucesivamente entre 2 y se recogen los restos.
Ejemplo: 45 ÷ 2 = 22 (resto 1) → 22 ÷ 2 = 11 (resto 0) → 11 ÷ 2 = 5 (resto 1) → 5 ÷ 2 = 2 (resto 1) → 2 ÷ 2 = 1 (resto 0) → 1 ÷ 2 = 0 (resto 1).
Leyendo restos en orden inverso: 101101.

De binario a hexadecimal

Agrupamos de 4 en 4.
Ejemplo: 11110010 → 1111 (F) y 0010 (2) → F2.

De hexadecimal a binario

Cada símbolo se pasa a 4 bits.
Ejemplo: 3A → 3 = 0011, A = 1010 → 00111010.



4.7 Operaciones básicas en binario

Las operaciones se realizan igual que en decimal, pero con base 2.

Suma binaria

0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 10  (es decir, 0 y llevamos 1)

Ejemplo:

  1011  (11 en decimal)
+ 1101  (13 en decimal)
------
11000   (24 en decimal)

Resta binaria

Se hace como en decimal, pero con base 2, pidiendo “prestado” cuando hace falta.

Ejemplo:

  1010  (10 en decimal)
-  0111 (7 en decimal)
------
   0011 (3 en decimal)

Multiplicación binaria

Se hace igual que en decimal, solo que los factores son 0 y 1.
Ejemplo: 101 × 11 = 1111 (5 × 3 = 15).



4.8 Importancia práctica
	•	Memoria: las direcciones se manejan en hexadecimal (ej.: 0xFF09).
	•	Colores en web: expresados en hexadecimal (ej.: #FF0000 = rojo puro).
	•	Ensamblador/máquinas: instrucciones y direcciones se representan en hex.
	•	Depuración: los programadores leen volcado de memoria en hex, no en binario.



4.9 Mini-ejercicios
	1.	Convierte el número binario 110011 a decimal.
	2.	Convierte 245 (decimal) a binario.
	3.	Convierte el binario 11101011 a hexadecimal.
	4.	Realiza la suma: 1011 + 1110.
	5.	¿Cuántos dígitos hexadecimales se necesitan para representar un byte?



Soluciones rápidas
	1.	110011 = 51 en decimal.
	2.	245 = 11110101 en binario.
	3.	11101011 = EB en hex.
	4.	1011 + 1110 = 11001 (11 + 14 = 25).
	5.	2 dígitos hexadecimales (porque 1 byte = 8 bits = 2×4 bits).



4.10 Resumen
	•	Los ordenadores trabajan en binario (base 2), pero usamos octal y hexadecimal como atajos.
	•	La conversión entre sistemas es mecánica y se basa en potencias de la base.
	•	Las operaciones (suma, resta, multiplicación) se hacen igual que en decimal, pero en base 2.
	•	Hexadecimal es imprescindible en programación, memoria y colores.

