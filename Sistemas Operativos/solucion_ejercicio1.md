
# Ejercicios y soluciones (explicación detallada)



## 1) **De binario a decimal:** convertir (110110_2) a decimal.

**Idea básica:** en binario cada dígito (bit) representa una potencia de 2. Empezando desde la derecha, los lugares valen (2^0,2^1,2^2,\dots).

Escribe el número con las potencias:
[
110110_2 = 1\cdot 2^5 + 1\cdot 2^4 + 0\cdot 2^3 + 1\cdot 2^2 + 1\cdot 2^1 + 0\cdot 2^0
]

Calcula cada término:

* (1\cdot2^5 = 32)
* (1\cdot2^4 = 16)
* (0\cdot2^3 = 0)
* (1\cdot2^2 = 4)
* (1\cdot2^1 = 2)
* (0\cdot2^0 = 0)

Suma todo:
[
32 + 16 + 0 + 4 + 2 + 0 = 54
]

**Respuesta:** (110110_2 = 54_{10}).

---

## 2) **De decimal a binario:** representar (59_{10}) en binario.

**Método (divisiones sucesivas):**
Divides entre 2 y anotas los restos; los restos escritos de abajo arriba forman el binario.

* (59 \div 2 = 29) resto **1**
* (29 \div 2 = 14) resto **1**
* (14 \div 2 = 7) resto **0**
* (7 \div 2 = 3) resto **1**
* (3 \div 2 = 1) resto **1**
* (1 \div 2 = 0) resto **1**

Lee los restos de abajo hacia arriba: **111011**

**Chequeo rápido:** (1\cdot2^5 +1\cdot2^4 +1\cdot2^3 +0\cdot2^2 +1\cdot2^1 +1\cdot2^0 = 32+16+8+0+2+1 =59).

**Respuesta:** (59_{10} = 111011_2).

---

## 3) **De hexadecimal a decimal:** convertir (A5_{16}) a decimal.

**Idea:** en hexadecimal las posiciones valen potencias de 16; A = 10 en decimal.

[
A5_{16} = 10\cdot16^1 + 5\cdot16^0 = 10\cdot16 + 5 = 160 + 5 = 165
]

**Respuesta:** (A5_{16} = 165_{10}).

---

## 4) **De decimal a binario (número más grande):** convertir (150_{10}) a binario.

Usamos divisiones por 2:

* (150 \div 2 = 75) resto **0**
* (75 \div 2 = 37) resto **1**
* (37 \div 2 = 18) resto **1**
* (18 \div 2 = 9) resto **0**
* (9 \div 2 = 4) resto **1**
* (4 \div 2 = 2) resto **0**
* (2 \div 2 = 1) resto **0**
* (1 \div 2 = 0) resto **1**

Lee restos de abajo arriba: **10010110**

**Chequeo (rápido):** (1\cdot2^7 +0\cdot2^6 +0\cdot2^5 +1\cdot2^4 +0\cdot2^3 +1\cdot2^2 +1\cdot2^1 +0\cdot2^0 =128+0+0+16+0+4+2+0=150).

**Respuesta:** (150_{10} = 10010110_2).

---

## 5) **De binario a decimal (byte):** calcular el valor decimal de (10110101_2).

Es un byte (8 bits). Anotamos potencias (de izquierda a derecha, índices 7→0):
[
10110101_2 = 1\cdot2^7 + 0\cdot2^6 + 1\cdot2^5 + 1\cdot2^4 + 0\cdot2^3 + 1\cdot2^2 + 0\cdot2^1 + 1\cdot2^0
]

Calcula:

* (1\cdot2^7 = 128)
* (0\cdot2^6 = 0)
* (1\cdot2^5 = 32)
* (1\cdot2^4 = 16)
* (0\cdot2^3 = 0)
* (1\cdot2^2 = 4)
* (0\cdot2^1 = 0)
* (1\cdot2^0 = 1)

Suma: (128 + 0 + 32 + 16 + 0 + 4 + 0 + 1 = 181).

**Respuesta:** (10110101_2 = 181_{10}).

---

## 6) **Codificación ASCII:** representación binaria (8 bits por carácter) de la palabra **"Code"**.

ASCII usa un byte (8 bits) por carácter en su forma básica. Convierte cada letra a su código ASCII decimal y luego a binario (8 bits).

Códigos (decimal → binario 8 bits):

* 'C' → 67 → (01000011)
* 'o' → 111 → (01101111)
* 'd' → 100 → (01100100)
* 'e' → 101 → (01100101)

**Respuesta (secuencia de bytes):**

```
01000011 01101111 01100100 01100101
```

(y corresponde a "Code").

---

## 7) **Decodificación ASCII:** decodifica la secuencia

`01010000 01111001 01110100 01101000 01101111 01101110`.

Convertimos cada byte binario a decimal y luego al carácter ASCII:

* `01010000` → 80 → 'P'
* `01111001` → 121 → 'y'
* `01110100` → 116 → 't'
* `01101000` → 104 → 'h'
* `01101111` → 111 → 'o'
* `01101110` → 110 → 'n'

**Respuesta:** la palabra codificada es **"Python"**.

---

## 8) **Identificación de codificación:** secuencia hex `C3 AD`.

* Si la decodificas **como ASCII**, ¿qué obtienes?
* Si la decodificas **como UTF-8**, ¿a qué carácter corresponde?

**Explicación clara:**

* **ASCII** solo define códigos del 0x00 al 0x7F (0–127). Los bytes `0xC3` y `0xAD` (>0x7F) **no son caracteres ASCII válidos** imprimibles. Si un programa intenta interpretarlos como ASCII normalmente mostrará caracteres inválidos o sustitutos (por ejemplo, signos de interrogación o caracteres raros), porque ASCII no incluye esos valores.
  En otras codificaciones de un byte (ISO-8859-1 / Latin-1), `0xC3` = 'Ã' y `0xAD` = carácter "soft hyphen" (a veces no visible). Así que interpretarlo como ASCII puro no tiene sentido y suele dar resultados incorrectos o caracteres extraños.

* **UTF-8:** en UTF-8 la secuencia `C3 AD` es la codificación correcta del punto de código **U+00ED**, que es la letra **'í'** (i con acento agudo).
  Por eso, si el texto originalmente era `í` y alguien volcó los bytes `C3 AD`, el decodificador UTF-8 mostrará **"í"**.

**Respuesta:**

* Como ASCII: no es válido / caracteres no imprimibles (o símbolos raros).
* Como UTF-8: **`C3 AD` → 'í' (U+00ED).**

---

## 9) **Codificación UTF-8:** punto de código Unicode para el corazón '❤' y su representación en bytes UTF-8. ¿Cuántos bytes se usan?

* El carácter **'❤'** (corazón negro/black heart suit) tiene el punto de código **U+2764**.
* Para U+2764 (que está en el rango U+0800 a U+FFFF) UTF-8 lo codifica con **3 bytes**.

El encoding UTF-8 en hex es:
[
U+2764 \rightarrow \texttt{E2 9D A4}
]

**Respuesta:** El corazón '❤' es **U+2764** y en UTF-8 se codifica como los bytes **E2 9D A4** (3 bytes).

*(nota: si se muestra como emoji rojo en algunos contextos se añade una secuencia de "VS16" U+FE0F, pero el carácter base '❤' es U+2764 y ocupa 3 bytes en UTF-8).*

---

## 10) **Codificación y decodificación completa:** frase **"¡Hola!"** — puntos de código Unicode y la secuencia de bytes hex al codificar en UTF-8.

Primero los puntos de código Unicode de cada carácter:

* '¡' → **U+00A1** (signo de apertura de exclamación invertido)
* 'H' → **U+0048**
* 'o' → **U+006F**
* 'l' → **U+006C**
* 'a' → **U+0061**
* '!' → **U+0021**

Ahora, codificación UTF-8:

* U+00A1 (no está en ASCII puro) se codifica en 2 bytes: **C2 A1**
* Los otros (U+0048, U+006F, U+006C, U+0061, U+0021) están en el rango ASCII y se codifican en 1 byte cada uno:

  * 'H' → 0x48
  * 'o' → 0x6F
  * 'l' → 0x6C
  * 'a' → 0x61
  * '!' → 0x21

Por tanto la secuencia de bytes hex (UTF-8) para `"¡Hola!"` es:

**`C2 A1 48 6F 6C 61 21`**

Si quieres verla en binario (opcional):

* C2 = 11000010
* A1 = 10100001
* 48 = 01001000
* 6F = 01101111
* 6C = 01101100
* 61 = 01100001
* 21 = 00100001

**Respuesta final:**

* Puntos de código: `U+00A1 U+0048 U+006F U+006C U+0061 U+0021`
* Secuencia de bytes UTF-8 (hex): **`C2 A1 48 6F 6C 61 21`**.
