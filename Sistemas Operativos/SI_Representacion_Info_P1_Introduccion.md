# Capítulo 1 — Representación de la Información

## 1. Introducción

El objetivo de este capítulo es comprender qué entendemos por **información**, cómo se diferencia de un **dato**, y por qué los ordenadores representan todo con **ceros y unos**. También se presentan los conceptos de **señal analógica** y **digital**, así como el proceso por el que un fenómeno físico (un sonido, una imagen, una medida de temperatura) se convierte en un archivo informático.

Este punto de partida es esencial: solo cuando comprendemos que la base de toda la informática es la **codificación binaria de la información** podemos entender cómo funcionan las operaciones, la memoria, la comunicación en redes o los sistemas multimedia.



## 1.1 ¿Qué es la información?

En informática, la **información** es aquello que permite **reducir la incertidumbre** sobre una situación. Sin embargo, es importante diferenciar entre **dato** e **información**, pues no son lo mismo:

* Un **dato** es un registro objetivo, sin contexto, que por sí solo no transmite significado.
* La **información** surge cuando ese dato se **interpreta dentro de un contexto** y **sirve para un propósito**.

**Ejemplo:**

* Dato: `19.3`
* Información: “La temperatura actual en el aula es 19.3 °C.”
* Conocimiento: “Hace fresco, por tanto conviene encender la calefacción.”

Podemos describir la relación de la siguiente manera:

* **Dato → Información → Conocimiento → Decisión.**

Desde un punto de vista formal, la **teoría de la información** (Claude Shannon, 1948) propone que la información es una medida de la reducción de incertidumbre. La cantidad de información necesaria para identificar un estado dentro de un conjunto de posibilidades se expresa con el logaritmo en base 2:

$$
I = \log_2(N)
$$

donde $N$ es el número de opciones igualmente probables.

* Si la pregunta admite solo **sí/no**, basta con **1 bit**.
* Si existen **4 opciones**, se necesitan **2 bits** ($\log_2(4) = 2$).
* Para **8 opciones**, se requieren **3 bits** ($\log_2(8) = 3$).

Así, **más opciones ⇒ más información necesaria**.



## 1.2 Del mundo físico a lo digital: señales

La información del mundo real se transmite a través de **señales**, es decir, magnitudes físicas que **varían en el tiempo** (voltaje, presión del aire, intensidad de la luz, etc.).

* **Señales analógicas:** varían de forma continua, pudiendo tomar infinitos valores dentro de un rango.

  * Ejemplo: la onda sonora producida al hablar.

* **Señales digitales:** toman valores discretos, limitados a un conjunto finito de niveles.

  * Ejemplo: una onda cuadrada que solo adopta “alto” o “bajo”.

```
Analógica (continua)           Digital (discreta)
     ~~~~                        ┌───┐   ┌───┐
  ~~~    ~~~                     │   │   │   │
 ~~        ~~                    │   │   │   │
~            ~                   └───┴───┴───┴─→ t
```

### ¿Por qué preferimos lo digital?

1. **Robustez al ruido:** un pequeño error en el voltaje no altera el significado si no supera el umbral que separa un 0 de un 1.
2. **Copia sin degradación:** duplicar bits no deteriora la señal, mientras que las copias analógicas pierden calidad.
3. **Procesamiento eficiente:** los circuitos electrónicos y memorias funcionan de forma más fiable con estados discretos.
4. **Seguridad e integridad:** es más fácil detectar y corregir errores, así como cifrar la información.



## 1.3 ¿Por qué 0 y 1?

Los ordenadores se construyen con **transistores**, que funcionan como **interruptores electrónicos**. Cada transistor puede estar en dos estados estables: conducción (encendido) o corte (apagado).

Por convenio, estos estados se representan como:

* **0** → nivel bajo.
* **1** → nivel alto.

Aunque la tensión eléctrica es continua, el hardware define **rangos de voltaje** que corresponden a 0 o 1, evitando la ambigüedad.

El uso de dos estados no es casual:

* **Fiabilidad:** con más de dos estados, los circuitos serían muy sensibles al ruido.
* **Simplicidad:** la aritmética binaria permite construir sistemas universales de cómputo con una base mínima.



## 1.4 Del fenómeno físico al archivo digital

Para que un fenómeno del mundo real pueda ser procesado por un ordenador, sigue un flujo de conversión:

1. **Sensado:** un sensor transforma el fenómeno físico en señal eléctrica (ej. micrófono, cámara, termómetro).
2. **Muestreo (sampling):** se toma la señal a intervalos regulares en el tiempo.
3. **Cuantificación:** cada muestra se aproxima a un nivel discreto dentro de un rango finito.
4. **Codificación:** a cada nivel se le asigna una secuencia binaria (0 y 1).
5. **Almacenamiento o transmisión:** los bits resultantes se guardan en memoria o se envían por una red.

Este proceso es la base de la digitalización de audio, imágenes y vídeo. Conceptos como **frecuencia de muestreo** o **profundidad de bits** derivan de estas etapas.



## 1.5 Vocabulario mínimo

* **Señal analógica:** magnitud física continua en el tiempo.
* **Señal digital:** magnitud discreta con un conjunto limitado de valores.
* **Nivel lógico:** rango de voltaje asociado a “0” o “1”.
* **Bit:** unidad mínima de información, que puede tomar los valores 0 o 1.
* **Codificación:** asignación entre símbolos del mundo real (letras, colores, notas musicales) y combinaciones de bits.



## 1.6 Errores comunes

* **“Digital = perfecto”.** Falso: lo digital también sufre ruido y errores, aunque es más fácil corregirlos.
* **“El binario es solo para números”.** Incorrecto: todo puede codificarse en binario (texto, imágenes, sonido, vídeo).
* **“Dato = Información”.** Un número aislado no es información hasta que se interpreta en contexto.
* **“0 y 1 son voltajes exactos”.** No: son rangos de tensión definidos por la tecnología (TTL, CMOS, etc.).



## 1.7 Actividades de repaso

1. **Dato vs Información**
   Clasifica los siguientes ejemplos como dato, información o conocimiento:
   a) “72”
   b) “72 ppm de pulso en reposo”
   c) “El pulso es bajo, deberías consultar al médico si te mareas”.

2. **Analógico o Digital**
   Indica si el ejemplo es analógico (A) o digital (D):
   a) Termómetro de mercurio
   b) Interruptor de luz
   c) Señal de un micrófono
   d) Texto en un archivo `.txt`

3. **Incertidumbre y bits**
   ¿Cuántos bits son necesarios como mínimo para codificar:
   a) 8 destinos posibles.
   b) 3 destinos posibles.

**Soluciones:**

1. a) Dato · b) Dato en contexto (información inicial) · c) Información interpretada (conocimiento aplicado).
2. a) A · b) D · c) A · d) D.
3. a) $\log_2(8) = 3$ bits. · b) $\log_2(3) ≈ 1.58$, por tanto se necesitan **2 bits**.



## 1.8 Resumen

* La **información** es un dato con contexto que reduce la incertidumbre.
* Todo el mundo físico es **analógico**, pero los ordenadores trabajan en **digital** porque es más robusto y eficiente.
* La digitalización sigue la secuencia: **sensado → muestreo → cuantificación → codificación → almacenamiento/transmisión**.
* El binario (0 y 1) es la base universal de representación, gracias a la fiabilidad y simplicidad de los transistores.
* Todo lo que los ordenadores procesan —números, texto, imágenes, sonido o vídeo— es, en última instancia, una **combinación de bits**.
