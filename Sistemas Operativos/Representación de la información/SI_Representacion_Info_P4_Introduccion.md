Representación de la Información — 4. Sistemas de numeración



4.1 La necesidad de diferentes sistemas de numeración

Los humanos utilizamos de forma natural el sistema decimal (base 10). Probablemente la razón está en algo tan simple como que tenemos 10 dedos. En decimal, cada cifra puede tomar valores de 0 a 9, y la posición determina su peso: unidades, decenas, centenas…

Sin embargo, los ordenadores no funcionan en base 10. Sus circuitos electrónicos distinguen únicamente dos estados (nivel bajo y nivel alto), por lo que el sistema que mejor se adapta es el binario (base 2).

Además del binario, en informática se emplean otros sistemas intermedios como el octal (base 8) y el hexadecimal (base 16), que sirven como atajos para representar grandes cantidades de bits de manera más legible.



4.2 Sistemas posicionales

Un sistema de numeración posicional se basa en dos principios:
	1.	Cada dígito pertenece a un conjunto limitado de símbolos (ej.: {0..9} en decimal, {0..1} en binario).
	2.	El valor de cada dígito depende de su posición y de la base.

Ejemplo en decimal:
El número 473 se interpreta como:

473 = 4 \times 10^2 + 7 \times 10^1 + 3 \times 10^0 = 400 + 70 + 3

Lo mismo ocurre en cualquier base: la posición determina la potencia de la base.



4.3 Sistema binario (base 2)

El binario solo tiene dos símbolos: 0 y 1.
Cada posición corresponde a una potencia de 2.

Ejemplo:
1011 = 1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0 = 8 + 0 + 2 + 1 = 11

Un solo dígito binario = bit.
Un conjunto de bits permite representar números más grandes.



4.4 Sistema octal (base 8)

El sistema octal usa símbolos del 0 al 7. Cada posición es una potencia de 8.

Su utilidad está en que 3 bits equivalen exactamente a 1 dígito octal (2³ = 8).
Esto lo convierte en un atajo del binario.

Ejemplo:
Binario 110010 → agrupamos de 3 en 3: 110 010 → (6)(2) = 62 en octal.



4.5 Sistema hexadecimal (base 16)

El hexadecimal emplea 16 símbolos:
{0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F}, donde A=10, B=11, …, F=15.

En informática es muy útil porque 4 bits = 1 dígito hexadecimal (2⁴ = 16).
Esto facilita la traducción directa entre binario y hexadecimal.

Ejemplo:
Binario 11011010 → agrupamos en grupos de 4: 1101 1010 = (D)(A) → DA en hexadecimal.



4.6 Conversión entre sistemas

De binario a decimal

Se aplica la fórmula de potencias de 2.
Ejemplo:
101101 = 1·2⁵ + 0·2⁴ + 1·2³ + 1·2² + 0·2¹ + 1·2⁰ = 45.

De decimal a binario

Se divide entre 2 sucesivamente y se recogen los restos en orden inverso.
Ejemplo:
45 ÷ 2 = 22 (resto 1) → 22 ÷ 2 = 11 (resto 0) → 11 ÷ 2 = 5 (resto 1) → 5 ÷ 2 = 2 (resto 1) → 2 ÷ 2 = 1 (resto 0) → 1 ÷ 2 = 0 (resto 1).
Leyendo restos al revés: 101101.

De binario a hexadecimal

Agrupamos de 4 en 4.
Ejemplo: 11110010 → 1111 (F) y 0010 (2) → F2.

De hexadecimal a binario

Cada símbolo se traduce a 4 bits.
Ejemplo: 3A → 3 = 0011, A = 1010 → 00111010.



4.7 Operaciones básicas en binario

Las operaciones se realizan igual que en decimal, pero con base 2.

Suma binaria

0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 10 (0 y llevamos 1)

Ejemplo:

  1011  (11 en decimal)
+ 1101  (13 en decimal)
------
11000   (24 en decimal)

Resta binaria

Se hace igual que en decimal, pidiendo “prestado” cuando es necesario.

Ejemplo:

  1010  (10 en decimal)
- 0111  (7 en decimal)
------
  0011  (3 en decimal)

Multiplicación binaria

Como en decimal, pero los factores solo son 0 o 1.

Ejemplo:
101 × 11 = 1111 (5 × 3 = 15).



4.8 Importancia práctica
	•	Memoria: direcciones expresadas en hexadecimal (ej.: 0xFF09).
	•	Colores en la web: expresados en hex (#FF0000 = rojo puro).
	•	Lenguaje ensamblador: instrucciones y direcciones en hex.
	•	Depuración: leer volcados de memoria es inviable en binario, pero legible en hexadecimal.



4.9 Mini-ejercicios
	1.	Convierte el binario 110011 a decimal.
	2.	Convierte 245 (decimal) a binario.
	3.	Convierte el binario 11101011 a hexadecimal.
	4.	Realiza la suma: 1011 + 1110.
	5.	¿Cuántos dígitos hexadecimales se necesitan para representar un byte?



Soluciones rápidas
	1.	110011 = 51 en decimal.
	2.	245 = 11110101 en binario.
	3.	11101011 = EB en hex.
	4.	1011 + 1110 = 11001 (11 + 14 = 25).
	5.	2 dígitos hexadecimales (porque 8 bits = 2×4 bits).



4.10 Resumen
	•	Los ordenadores trabajan en binario (base 2), pero usamos octal (base 8) y hexadecimal (base 16) como atajos para simplificar la lectura.
	•	La conversión entre sistemas es mecánica y se basa en potencias de la base.
	•	Las operaciones se hacen igual que en decimal, adaptadas a base 2.
	•	El hexadecimal es imprescindible en programación, manejo de memoria y definición de colores.
