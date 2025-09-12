Representación de la Información — 2. De lo Analógico a lo Digital

Objetivo: comprender qué son las señales analógicas y digitales, cómo funciona la conversión analógico-digital (ADC) y por qué los ordenadores trabajan exclusivamente con señales digitales.



2.1 Señales analógicas

Una señal analógica es una magnitud que puede tomar infinitos valores dentro de un rango continuo. Su forma suele representarse como una curva suave que cambia con el tiempo.

Ejemplo clásico: la voz humana.
	•	Cuando hablas, las cuerdas vocales vibran y generan ondas de presión en el aire.
	•	Esas ondas son continuas: entre dos valores cualesquiera siempre hay infinitos intermedios.
	•	Si colocas un micrófono, la presión del aire se convierte en una señal eléctrica analógica que también varía suavemente en el tiempo.

Características principales:
	•	Amplitud variable: puede valer, por ejemplo, 0,735 V en un instante y 0,736 V al siguiente.
	•	Tiempo continuo: la señal existe en cada instante, sin saltos.
	•	Sensibilidad al ruido: pequeños cambios externos (temperatura, interferencias) alteran la señal.
	•	Degradación con la copia: al duplicarla se arrastra ruido acumulado.

Ejemplos de señales analógicas:
	•	Onda sonora de un instrumento musical.
	•	Intensidad de la luz en una bombilla incandescente.
	•	Señal de vídeo en televisores antiguos (antes de lo digital).



2.2 Señales digitales

Una señal digital solo puede tomar un número finito de valores. Lo más habitual es que sean dos: bajo (0) y alto (1).

Ejemplo: un pulsador que enciende o apaga un LED. Está apagado (0) o encendido (1), sin estados intermedios válidos.

Tiempo →      ┌───┐       ┌───┐
Nivel alto    │   │       │   │
              │   │       │   │
Nivel bajo ───┘   └───────┘   └───

Características principales:
	•	Valores discretos: por ejemplo, 0 V = “0”, 5 V = “1”.
	•	Resistencia al ruido: si la señal es 4,7 V sigue interpretándose como “1”.
	•	Fácil procesamiento: los circuitos electrónicos trabajan mucho mejor con niveles discretos.
	•	Almacenamiento/transmisión eficiente: se pueden comprimir, cifrar y copiar sin degradación.

Ejemplos de señales digitales:
	•	Los datos de un archivo .mp3.
	•	Una foto en formato .jpg.
	•	La información que viaja por internet como paquetes binarios.



2.3 Conversión analógico-digital (ADC)

Como el mundo real es analógico y los ordenadores solo entienden digital, necesitamos traducir de un dominio a otro. Eso lo hace el convertidor analógico-digital (ADC).

El proceso tiene dos fases clave:

1. Muestreo (Sampling)
	•	Se mide el valor de la señal a intervalos de tiempo regulares.
	•	La frecuencia de muestreo indica cuántas muestras por segundo tomamos (Hz).
	•	Según el teorema de Nyquist, para representar bien una señal, hay que muestrearla al menos al doble de su frecuencia máxima.

Ejemplo:
	•	El oído humano capta hasta 20 kHz.
	•	Por eso un CD de música usa 44,1 kHz de muestreo (suficiente para cubrir el rango).

2. Cuantificación (Quantization)
	•	Cada muestra se aproxima a uno de un número finito de niveles.
	•	Cuantos más bits se usen, mayor será la precisión.

Ejemplo:
	•	8 bits → 2⁸ = 256 niveles.
	•	16 bits → 65.536 niveles.

Señal analógica       Muestreo        Cuantificación
   ~~~~                 o o o          ● ● ●
  ~    ~               o   o          ●   ●
 ~      ~             o     o        ●     ●




2.4 Ventajas de digitalizar
	•	Menor degradación: una copia digital es idéntica a la original.
	•	Procesamiento eficiente: algoritmos matemáticos operan sobre valores discretos.
	•	Almacenamiento compacto: se pueden aplicar técnicas de compresión (MP3, JPEG, MP4).
	•	Transmisión confiable: se añaden bits extra para detectar y corregir errores.
	•	Integración universal: todo (texto, audio, imágenes, vídeo) se reduce a bits y se almacena/transmite en los mismos dispositivos.



2.5 Limitaciones y errores
	•	Ruido de cuantificación: el redondeo de muestras introduce un pequeño error.
	•	Resolución limitada: depende del número de bits de cada muestra.
	•	Aliasing: si el muestreo es insuficiente, aparecen distorsiones (ej.: una rueda de cine que parece girar al revés).



2.6 Ejemplos cotidianos
	•	CD de música: 44,1 kHz, 16 bits → calidad transparente para la mayoría de los oyentes.
	•	Fotos digitales: cada píxel se cuantifica con 24 bits (16 millones de colores).
	•	Sensores digitales: un termómetro convierte la temperatura en valores binarios que puedes leer en pantalla.
	•	Streaming: cuando escuchas Spotify, recibes secuencias digitales comprimidas en tiempo real.



2.7 Mini-ejercicios
	1.	Analógico o digital.
a) El vinilo de un disco.
b) Archivo .mp3.
c) Televisión antigua con antena.
d) Netflix en streaming.
	2.	Si un sistema de audio usa 8 bits por muestra, ¿cuántos niveles distintos puede representar cada muestra? ¿Y con 12 bits?
	3.	¿Qué pasaría si grabas una señal de 10 kHz con un muestreo de 15 kHz?



Soluciones rápidas
	1.	a) Analógico · b) Digital · c) Analógico · d) Digital.
	2.	8 bits → 256 niveles · 12 bits → 4096 niveles.
	3.	Violación de Nyquist ⇒ aliasing ⇒ la señal se distorsiona.



2.8 Resumen
	•	El mundo es analógico, pero los ordenadores necesitan traducirlo a digital (0 y 1) para trabajar.
	•	La conversión analógico-digital implica muestrear en el tiempo y cuantificar en niveles.
	•	La calidad depende de la frecuencia de muestreo y la profundidad de bits.
	•	Todo lo que usamos hoy en día (audio, fotos, vídeo, sensores) pasa por este proceso.

