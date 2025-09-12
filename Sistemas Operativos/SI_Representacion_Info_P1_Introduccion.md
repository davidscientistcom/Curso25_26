# Representación de la Información — **1. Introducción**

> Objetivo de este capítulo: entender qué es la **información**, en qué se diferencia de un **dato**, qué son las **señales** y por qué los ordenadores representan todo con **0 y 1**. Dejas listo el terreno para, en los siguientes capítulos, entrar en bits/bytes, bases numéricas y multimedia.



## 1.1 ¿Qué es la información?

**Información** es aquello que **reduce incertidumbre** sobre algo. Si no cambia lo que sabes o puedes decidir, no aporta información.  
Un **dato** es una **medición o registro crudo** (un número, un texto, una señal). La **información** emerge cuando **interpretas** ese dato **en contexto** para un propósito.

- **Dato:** `19.3`  
- **Contexto:** “temperatura ambiente (°C) en el aula ahora”.  
- **Información:** “Hace fresco; enciende la calefacción”.

> Reglas simples:
> - **Dato → Información:** Dato + Contexto + Interpretación.
> - **Información → Conocimiento:** Información verificada y reutilizable en el tiempo.
> - **Conocimiento → Decisión/Acción:** Aplicación práctica en un caso real.

**Medida de información (intuición):** si la respuesta es **sí/no**, se necesita **1 bit** de información. Si hay **4 opciones igualmente probables**, necesitas **2 bits** (porque \( \log_2(4)=2 \)). No hace falta formalismo ahora; quédate con que **más opciones ⇒ más bits**.



## 1.2 Del mundo físico a lo digital: señales

Una **señal** es una magnitud física que **varía en el tiempo** (tensión eléctrica, presión del aire, luz…). Con señales representamos y transportamos datos.

- **Señal analógica:** varía de manera **continua** (cualquier valor de un rango). Ej.: la vibración del aire cuando hablas.
- **Señal digital:** varía de manera **discreta** (valores “cuantizados”). Ej.: una onda cuadrada con dos niveles (bajo/alto).

```
Analógica (continua)           Digital (discreta)
     ~~~~                        ┌───┐   ┌───┐
  ~~~    ~~~                     │   │   │   │
 ~~        ~~                    │   │   │   │
~            ~                   └───┴───┴───┴─→ t
```

**¿Por qué lo digital?**  
1) **Robustez al ruido:** un pequeño error de tensión no cambia un **0** en **1** si no traspasa el **umbral**.  
2) **Copia sin degradación:** duplicar bits no empeora la señal.  
3) **Procesamiento y almacenamiento eficientes:** los circuitos lógicos y la memoria trabajan con niveles discretos.  
4) **Integridad y seguridad:** es más fácil detectar/corregir errores y cifrar.



## 1.3 ¿Por qué 0 y 1? (visión física y lógica)

Los ordenadores están construidos con **transistores** que actúan como **interruptores electrónicos**. A nivel de circuitos, se definen dos **niveles lógicos** (por ejemplo, “bajo” y “alto”) que se **codifican** como **0** y **1**. Aunque la tensión eléctrica sea continua, **el hardware la discretiza** y **solo considera dos estados estables**. Con esa base binaria se representa *cualquier* tipo de información (números, texto, imagen, sonido). fileciteturn0file1

> Puntos finos pero importantes:
> - **0/1 son convenciones lógicas.** Un “0” **no** significa “0 voltios exactos”: hay rangos tolerados (según la tecnología, p. ej. TTL/CMOS).
> - El motivo de usar dos estados es **fiabilidad** y **simplicidad**: más estados ⇒ más sensibles al ruido y más costosos.



## 1.4 Del fenómeno físico al archivo: la “tubería” mental

Cuando un ordenador “tiene información” sobre algo real, típicamente ha pasado por esta cadena:

1) **Sensado:** un **sensor** convierte un fenómeno físico en una **señal eléctrica** (micrófono, cámara, termistor…).  
2) **Muestreo (sampling):** medimos la señal a **intervalos regulares** (tomas por segundo).  
3) **Cuantificación:** redondeamos cada muestra a uno de **N niveles** posibles.  
4) **Codificación:** asignamos a cada nivel un **patrón binario** (0/1).  
5) **Almacenamiento/Transmisión:** guardamos o enviamos esas secuencias de bits.

> En capítulos siguientes detallaremos estos pasos para **audio**, **imagen** y **vídeo**, y veremos cómo entran conceptos como **frecuencia de muestreo**, **profundidad de bits** y **compresión**.



## 1.5 Vocabulario mínimo (lo justo para arrancar)

- **Señal analógica:** magnitud continua en el tiempo.  
- **Señal digital:** magnitud discreta con niveles definidos.  
- **Nivel lógico:** rango de tensión asociado a “0” o “1”.  
- **Bit:** unidad mínima de información; puede ser 0 o 1. (Ampliaremos en el cap. 3). fileciteturn0file13  
- **Codificación:** mapeo entre símbolos del mundo “humano” (letras, colores, notas) y patrones binarios.



## 1.6 Errores típicos que conviene cortar de raíz

- **“Digital = exacto perfecto”.** Falso: hay **ruido**, **cuantización** y **errores**, solo que podemos **detectarlos/mitigarlos** mejor.  
- **“Binario es solo para números”.** No: **todo** se codifica en binario (texto, imágenes, audio…). fileciteturn0file7  
- **Confundir dato con información.** Un número sin contexto **no** te dice qué hacer.  
- **Pensar que 0/1 son voltajes exactos.** Son **rangos**; por eso el sistema es robusto.



## 1.7 Mini‑ejercicios (de calentamiento)

1) **Dato vs Información.** Clasifica cada ítem y explica por qué:  
   a) “72” · b) “72 ppm” (pulso en reposo) · c) “Pulso bajo; consulta si te mareas”.  

2) **Analógico o digital.** Marca **A** o **D**:  
   a) Termómetro de mercurio. b) Pulsador on/off. c) Salida de un micrófono. d) Texto en un archivo `.txt`.

3) **Bits e incertidumbre (intuición).** ¿Cuántos bits **mínimos** necesitas para identificar 8 destinos de envío equiprobables? ¿Y 3 destinos? (Pista: \( \log_2 \)).

**Soluciones rápidas:**  
- 1) a) Dato (sin contexto). b) Dato + contexto (puede empezar a informar). c) Información (acción).  
- 2) a) A · b) D · c) A · d) D (internamente, texto = binario).  
- 3) 8 destinos ⇒ \( \log_2(8)=3 \) bits. 3 destinos ⇒ entre 1 y 2 bits; el mínimo entero para codificar sin ambigüedad son **2 bits**.



## 1.8 Resumen para llevar

- **Información** = dato **con** contexto que **reduce incertidumbre**.  
- El mundo es **analógico**, el ordenador **digitaliza** para trabajar **con 0 y 1** por **fiabilidad**. fileciteturn0file1  
- La “tubería” mental: **sensar → muestrear → cuantificar → codificar → guardar/transmitir**.  
- En los siguientes capítulos aterrizamos estas ideas en **bits/bytes, bases numéricas, operaciones**, y **multimedia (texto, imagen, audio, vídeo)**.
