Representación de la Información — 7. Representación de caracteres



7.1 De los números a las letras

Un ordenador solo entiende secuencias de 0 y 1. Para que pueda manejar texto, necesitamos una tabla de correspondencia entre caracteres humanos (letras, símbolos, signos de puntuación) y códigos numéricos en binario.
Este proceso se llama codificación de caracteres.

Ejemplo simple:
	•	La letra 'A' se representa con el número 65.
	•	En binario (1 byte): 01000001.
Cuando escribes 'A' en un editor, en la memoria del ordenador en realidad hay ese byte.



7.2 ASCII: el punto de partida

ASCII (American Standard Code for Information Interchange) fue creado en los años 60 como estándar de codificación de caracteres en inglés.
	•	Cada carácter ocupa 7 bits (128 posibles símbolos).
	•	Se incluyen:
	•	Letras mayúsculas y minúsculas (A–Z, a–z).
	•	Dígitos (0–9).
	•	Signos de puntuación.
	•	Caracteres de control (ENTER, tabulador, borrar…).

Ejemplo:
	•	'A' = 65 = 01000001
	•	'a' = 97 = 01100001
	•	'0' = 48 = 00110000

Limitación: ASCII solo sirve bien para el inglés. No incluye la ñ, tildes, ni caracteres de otros idiomas.



7.3 Extensiones de ASCII y códigos locales

Para otros idiomas, se amplió ASCII a 8 bits (256 símbolos), dando lugar a ISO-8859 y variantes.
Por ejemplo:
	•	ISO-8859-1 (Latin-1): incluye letras acentuadas y la ñ (ñ = 241 = 11110001).
	•	Otros conjuntos se adaptaron a cirílico, griego, árabe, etc.

Problema: cada país tenía su propia codificación → confusión al intercambiar documentos.



7.4 Unicode: un estándar global

La solución fue Unicode, un estándar que asigna un número único a cada carácter de cualquier idioma.
Se usa en internet, sistemas modernos y móviles.
	•	Puede representar más de 1 millón de caracteres.
	•	Incluye letras de todos los alfabetos, símbolos matemáticos, ideogramas chinos, emojis, etc.

Ejemplo:
	•	'ñ' = U+00F1 (decimal 241).
	•	'Ω' (omega griega) = U+03A9.
	•	'😊' (emoji) = U+1F60A.

Unicode no es un formato, sino un conjunto universal de códigos. Para almacenarlos/transmitirlos existen implementaciones como UTF-8 o UTF-16.



7.5 UTF-8: el rey de la web

UTF-8 es la codificación más utilizada actualmente. Sus ventajas:
	•	Compatible con ASCII (los primeros 128 caracteres son iguales).
	•	Usa 1 a 4 bytes por carácter:
	•	1 byte para caracteres básicos (ASCII).
	•	Más bytes para caracteres especiales (ej.: chino, emojis).
	•	Ahorra espacio en textos en inglés, pero permite representar cualquier idioma.

Ejemplo:
	•	'A' → 1 byte → 01000001.
	•	'ñ' → 2 bytes → 11000011 10110001.
	•	'😊' → 4 bytes → 11110000 10011111 10011000 10101010.



7.6 Problemas comunes de codificación

Seguro que alguna vez has visto símbolos raros como: Ã± o �.
Esto ocurre cuando un texto en una codificación (ej.: UTF-8) se interpreta como si fuera otra (ej.: ISO-8859-1). Se llaman errores de mojibake.

Por eso, en desarrollo web y aplicaciones modernas, se recomienda usar siempre UTF-8.



7.7 Ejemplos cotidianos
	•	Cuando escribes un WhatsApp con emojis, en realidad envías secuencias de bytes en UTF-8 que el receptor interpreta.
	•	Los navegadores muestran páginas correctamente porque especifican <meta charset="UTF-8">.
	•	Un PDF o un archivo .txt puede corromperse si lo abres con un editor que espera otra codificación.



7.8 Mini-ejercicios
	1.	¿Qué código ASCII corresponde a la letra 'Z'? Escríbelo en decimal y en binario.
	2.	¿Por qué ASCII no sirve para escribir en japonés?
	3.	¿Cuántos bytes puede usar UTF-8 como máximo para un carácter?
	4.	Explica por qué 'A' ocupa 1 byte en UTF-8 pero '😊' ocupa 4.



Soluciones rápidas
	1.	'Z' = 90 decimal = 01011010 en binario.
	2.	Porque ASCII solo tiene 128 símbolos, y el japonés necesita miles de caracteres.
	3.	Hasta 4 bytes.
	4.	Porque UTF-8 es variable: usa 1 byte para ASCII básico y más bytes para caracteres fuera de ese rango.



7.9 Resumen
	•	ASCII: 7 bits, inglés básico.
	•	Extensiones ISO: 8 bits, adaptadas a idiomas europeos.
	•	Unicode: estándar universal (incluye todos los idiomas y símbolos).
	•	UTF-8: codificación más usada hoy, eficiente y compatible con ASCII.
	•	Todo texto que ves en pantalla es, al final, una secuencia de bytes interpretada con una tabla de correspondencia.


