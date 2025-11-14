DE HEXADECIMAL A DECIMAL

Hexadecimal es base 16.
Los dígitos van:
0 1 2 3 4 5 6 7 8 9 A B C D E F
(donde A=10, B=11, … F=15)

Para convertir hex → dec, haces lo mismo que con binario o con decimal normal:
multiplicas cada dígito por 16 elevado a su posición (contando desde 0 por la derecha).

Ejemplo:

Convierte 1A3₁₆ a decimal.

Posiciones:
	•	3 → posición 0
	•	A → posición 1
	•	1 → posición 2

Sustituyes A por 10:

1 × 16² + 10 × 16¹ + 3 × 16⁰
= 1 × 256 + 10 × 16 + 3 × 1
= 256 + 160 + 3
= 419

1A3₁₆ = 419₁₀

DE DECIMAL A HEXADECIMAL

Aquí lo que se hace es dividir entre 16 e ir quedándose con los restos.

Pasos:
	1.	Divide el número entre 16.
	2.	Apunta el resto (ese será un dígito hex).
	3.	Coge el cociente y vuelve a dividir por 16.
	4.	Repite hasta que el cociente sea 0.
	5.	Los restos se leen de abajo arriba.

Ejemplo:

Convierte 419₁₀ a hex.

Dividimos:

División	Cociente	Resto
419 ÷ 16 = 26	26	3
26 ÷ 16 = 1	1	10 → A
1 ÷ 16 = 0	0	1

Lees restos de abajo arriba:

1 A 3 → 1A3₁₆

¿Quieres un truco rápido?

De decimal a hex:
	•	Menos de 16 → cambia directamente:
15 = F, 11 = B, etc.

De hex a decimal:
	•	Si tienes dos dígitos, piensa:
primero × 16 + segundo

Ej.: 3F
3×16 + 15 = 48 + 15 = 63
