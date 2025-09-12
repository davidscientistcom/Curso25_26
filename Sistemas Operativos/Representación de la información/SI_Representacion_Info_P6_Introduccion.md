Representación de la Información — 6. Representación de números reales



6.1 ¿Por qué necesitamos representar reales?

En la vida cotidiana no todo son números enteros. Necesitamos decimales para muchas cosas:
	•	Temperatura: 36,7 ºC.
	•	Dinero: 12,45 €.
	•	Distancias: 3,14 m.
	•	Ciencia: 6,022 × 10²³ (constante de Avogadro).

Un ordenador debe manejar estos valores para cálculos científicos, financieros, gráficos, etc.
El problema es que un ordenador solo tiene un número finito de bits, por lo que no puede representar todos los reales posibles: siempre habrá limitaciones de precisión.



6.2 Representación en coma fija

La coma fija consiste en reservar una parte de los bits para la parte entera y otra para la parte fraccionaria.
La posición de la coma (decimal) es fija.

Ejemplo (8 bits, 5 para parte entera, 3 para fraccionaria):

Parte entera  Parte fraccionaria
 10101           110

Se interpreta como:

1 \times 2^4 + 0 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 + 1 \times 2^{-1} + 1 \times 2^{-2} + 0 \times 2^{-3}

= 16 + 4 + 1 + 0,5 + 0,25 = 21,75

Ventajas:
	•	Fácil de implementar en hardware sencillo.
	•	Útil para aplicaciones donde la precisión es fija (ej.: microcontroladores en electrónica).

Inconvenientes:
	•	La precisión es limitada y constante.
	•	No se pueden representar números demasiado grandes ni demasiado pequeños a la vez.
	•	No es eficiente para cálculos científicos.



6.3 Representación en coma flotante

Para solventar estas limitaciones, se usa la coma flotante, que se inspira en la notación científica:

-5.471 \times 10^6

Se representa mediante tres partes:
	1.	Signo (positivo/negativo).
	2.	Mantisa o significando (los dígitos significativos).
	3.	Exponente (potencia de la base, que “mueve la coma”).

En binario, la base es 2, por lo que un número se representa como:

\text{valor} = (-1)^{signo} \times (1 + \text{mantisa}) \times 2^{exponente - \text{bias}}



6.4 Estándar IEEE 754 (coma flotante)

Es el estándar más usado en los procesadores modernos. Define cómo representar y operar con números reales.

Formatos principales:
	•	Simple precisión (32 bits):
	•	1 bit signo
	•	8 bits exponente
	•	23 bits mantisa
	•	Doble precisión (64 bits):
	•	1 bit signo
	•	11 bits exponente
	•	52 bits mantisa

Ejemplo en simple precisión (32 bits):

Número decimal: -13,25
	1.	Pasamos 13,25 a binario: 1101,01
(13 = 1101, 0,25 = 0,01).
→ 1101,01
	2.	Normalizamos en notación científica binaria:
1,10101 × 2³
	3.	Componentes:
	•	Signo: 1 (negativo)
	•	Exponente: 3 + 127 = 130 = 10000010
	•	Mantisa: 10101 (rellenamos hasta 23 bits)

Resultado en binario IEEE 754 (32 bits):

1 | 10000010 | 10101000000000000000000




6.5 Limitaciones y errores de coma flotante
	•	Precisión finita: no todos los números decimales se pueden representar exactamente.
Ejemplo: 0,1 en binario es periódico → se almacena una aproximación.
	•	Errores de redondeo: pequeñas diferencias que se acumulan en cálculos.
	•	Números muy grandes o pequeños: el exponente tiene límites → aparece overflow (infinito) o underflow (casi 0).

Ejemplo famoso:
En muchos lenguajes de programación:

0.1 + 0.2

da como resultado 0.30000000000000004 en lugar de 0.3.
Esto se debe a la representación binaria aproximada de 0,1 y 0,2.



6.6 Usos prácticos
	•	Coma fija: control industrial, robótica, sistemas embebidos.
	•	Coma flotante (IEEE 754): cálculo científico, gráficos 3D, inteligencia artificial, simulaciones físicas.



6.7 Mini-ejercicios
	1.	Representa el número 6,25 con 8 bits en coma fija (5 enteros, 3 fraccionarios).
	2.	Convierte el número 10,5 a binario en notación científica (base 2).
	3.	¿Qué rango aproximado se puede representar con un número en IEEE 754 simple precisión?
	4.	¿Por qué 0,1 no se representa de forma exacta en binario?



Soluciones rápidas
	1.	6,25 = 110,010 → en coma fija (5 enteros, 3 decimales) = 00110,010.
	2.	10,5 = 1010,1 → normalizado: 1,0101 × 2³.
	3.	Entre ~10⁻³⁸ y 10³⁸.
	4.	Porque 0,1 = 1/10, y en binario es una fracción periódica infinita (como 1/3 en decimal).



6.8 Resumen
	•	Coma fija: simple, pero con precisión limitada y rango fijo.
	•	Coma flotante: más flexible, usa mantisa y exponente.
	•	IEEE 754: estándar universal, con simple (32 bits) y doble precisión (64 bits).
	•	Siempre existen errores de redondeo y límites de representación.



