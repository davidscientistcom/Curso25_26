### Ejercicios de Conversión Numérica Resueltos



#### De Binario a Decimal

**1. Convierte $1101_2$ a decimal.**

* $1101_2 = (1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$
* $ = 8 + 4 + 0 + 1$
* $ = 13_{10}$

**2. Convierte $10010_2$ a decimal.**

* $10010_2 = (1 \times 2^4) + (0 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$
* $ = 16 + 0 + 0 + 2 + 0$
* $ = 18_{10}$



#### De Decimal a Binario

**1. Convierte $25_{10}$ a binario.**

* $25 \div 2 = 12$ (resto 1)
* $12 \div 2 = 6$ (resto 0)
* $6 \div 2 = 3$ (resto 0)
* $3 \div 2 = 1$ (resto 1)
* $1 \div 2 = 0$ (resto 1)
* El resultado es $11001_2$.

**2. Convierte $42_{10}$ a binario.**

* $42 \div 2 = 21$ (resto 0)
* $21 \div 2 = 10$ (resto 1)
* $10 \div 2 = 5$ (resto 0)
* $5 \div 2 = 2$ (resto 1)
* $2 \div 2 = 1$ (resto 0)
* $1 \div 2 = 0$ (resto 1)
* El resultado es $101010_2$.



### Ejercicios de Codificación de Texto Resueltos

Para estos ejercicios, usaremos las tablas de referencia estándar de ASCII y UTF-8.

#### 1. Codificación ASCII

* **Palabra "DAM" a binario de 8 bits:**
    * La letra 'D' en ASCII es 68, que en binario es `01000100`.
    * La letra 'A' en ASCII es 65, que en binario es `01000001`.
    * La letra 'M' en ASCII es 77, que en binario es `01001101`.
    * La representación binaria completa es: `01000100 01000001 01001101`.

* **Frase "Hola Mundo" a binario:**
    * 'H': 72 (`01001000`)
    * 'o': 111 (`01101111`)
    * 'l': 108 (`01101100`)
    * 'a': 97 (`01100001`)
    * ' ': 32 (`00100000`)
    * 'M': 77 (`01001101`)
    * 'u': 117 (`01110101`)
    * 'n': 110 (`01101110`)
    * 'd': 100 (`01100100`)
    * 'o': 111 (`01101111`)
    * La representación completa es: `01001000 01101111 01101100 01100001 00100000 01001101 01110101 01101110 01100100 01101111`.

#### 2. Identificación de Codificación

* **Secuencia `43 61 66 65`:**
    * Si asumimos **ASCII**, cada byte corresponde a un carácter:
        * `43` (hex) = 67 (dec) = **'C'**
        * `61` (hex) = 97 (dec) = **'a'**
        * `66` (hex) = 102 (dec) = **'f'**
        * `65` (hex) = 101 (dec) = **'e'**
    * La palabra es **"Cafe"**. Esto funciona porque los caracteres de esta palabra se encuentran en el rango de 7 bits de ASCII.

* **Secuencia `E2 82 AC`:**
    * **Decodificación ASCII:** El byte inicial `E2` (que en binario es `11100010`) tiene el bit más significativo en '1'. El estándar ASCII original no usa este rango, por lo que un programa que solo use ASCII no podría decodificarlo, y probablemente mostraría un carácter ilegible como 'â' o 'ä' dependiendo del sistema.
    * **Decodificación UTF-8:** El byte `E2` (`1110xxxx`) es el inicio de una secuencia de 3 bytes. Los bytes `82` (`10xxxxxx`) y `AC` (`10xxxxxx`) son bytes de continuación. Al unirlos, forman el punto de código `U+20AC`, que corresponde al símbolo **'€'** (euro).

#### 3. Codificación Multilingüe (UTF-8)

* **Letra 'ñ' (`U+00F1`):**
    * El punto de código `U+00F1` está en el rango que requiere 2 bytes.
    * El patrón de 2 bytes es `110xxxxx 10xxxxxx`.
    * El valor binario de `U+00F1` es `11110001`.
    * Insertando los bits en el patrón: `110**00011** 10**110001**`.
    * La representación en bytes hexadecimales es **`C3 B1`**.

* **Símbolo del euro '€' (`U+20AC`):**
    * El punto de código `U+20AC` está en el rango de 3 bytes.
    * El valor binario es `0010000010101100`.
    * El patrón de 3 bytes es `1110xxxx 10xxxxxx 10xxxxxx`.
    * Insertando los bits: `1110**0010** 10**001010** 10**110000**`.
    * La representación en bytes hexadecimales es **`E2 82 AC`**.

* **Emoji '🚀' (`U+1F680`):**
    * El punto de código `U+1F680` requiere **4 bytes** para su representación.
    * El valor binario es `00011111011010000000`.
    * El patrón de 4 bytes es `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`.
    * Insertando los bits: `11110**000** 10**011111** 10**011010** 10**000000**`.
    * La representación en bytes hexadecimales es **`F0 9F 9A 80`**.