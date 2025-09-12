Representación de la Información — 2. De lo Analógico a lo Digital

Objetivo: comprender qué son las señales analógicas y digitales, cómo funciona la conversión analógico-digital (ADC) y por qué los ordenadores trabajan exclusivamente con señales digitales.



2.1 Señales analógicas

Una señal analógica es aquella que puede tomar infinitos valores dentro de un rango. Ejemplo clásico: la voz humana.
	•	Cuando hablas, el aire vibra creando ondas continuas de presión.
	•	Si mides esa presión con un micrófono, obtienes una señal eléctrica que también varía de forma continua en el tiempo.

Características:
	•	Amplitud variable (puede valer, por ejemplo, 0.735 V en un instante).
	•	Tiempo continuo: entre dos puntos siempre hay infinitos valores intermedios.
	•	Son sensibles al ruido y a la degradación.



2.2 Señales digitales

Una señal digital solo puede tomar un número finito de valores, normalmente dos: bajo (0) y alto (1).

Ejemplo: un pulsador que activa un LED. Está apagado (0) o encendido (1), sin estados intermedios válidos.

Tiempo →      ┌───┐       ┌───┐
Nivel alto    │   │       │   │
              │   │       │   │
Nivel bajo ───┘   └───────┘   └───

Características:
	•	Valores discretos (ej.: 0 V = “0”, 5 V = “1”).
	•	Mucho más resistentes al ruido: si la señal es 4.7 V, sigue interpretándose como “1”.
	•	Más fáciles de procesar, guardar y transmitir.



2.3 Conversión analógico-digital (ADC)

El convertidor analógico-digital (ADC) es el dispositivo que traduce una señal analógica a digital. Su funcionamiento se basa en dos pasos:
	1.	Muestreo (Sampling): medimos la señal en instantes de tiempo regulares.
	•	Ejemplo: 44.100 veces por segundo en un CD de música (44.1 kHz).
	•	Regla de Nyquist: para representar bien una señal, hay que muestrearla al menos al doble de su frecuencia máxima.
	2.	Cuantificación (Quantization): cada muestra se aproxima a uno de N niveles posibles.
	•	Ejemplo: si usamos 8 bits → 2⁸ = 256 niveles de amplitud.
	•	Si usamos 16 bits → 65.536 niveles (más precisión, más memoria).

Señal analógica       Muestreo        Cuantificación
   ~~~~                 o o o          ● ● ●
  ~    ~               o   o          ●   ●
 ~      ~             o     o        ●     ●




2.4 Ventajas de digitalizar
	•	Menor degradación: copiar un archivo digital no cambia los bits.
	•	Procesamiento eficiente: algoritmos matemáticos y lógicos funcionan mejor con valores discretos.
	•	Almacenamiento compacto: se pueden comprimir (MP3, JPEG).
	•	Transmisión confiable: se añaden técnicas de detección y corrección de errores.
	•	Integración universal: todo (texto, audio, imágenes, vídeo) puede transformarse en bits y almacenarse/transmitirse en el mismo medio.



2.5 Limitaciones y errores
	•	Ruido de cuantificación: al redondear valores analógicos a niveles digitales, siempre hay un pequeño error.
	•	Resolución limitada: depende del número de bits por muestra.
	•	Aliasing: si el muestreo es insuficiente, aparecen distorsiones (ejemplo: rueda de cine que parece girar al revés).



2.6 Ejemplos cotidianos
	•	CD de música: muestreo a 44.1 kHz, 16 bits por muestra → calidad aceptable para el oído humano.
	•	Fotos digitales: cada píxel es una cuantificación de color en 24 bits (16 millones de colores).
	•	Sensores de temperatura: un termómetro digital convierte la señal analógica en números binarios que puedes leer en pantalla.



2.7 Mini-ejercicios
	1.	Analógico o digital.
a) El vinilo de un disco.
b) Archivo .mp3.
c) Televisión antigua con antena.
d) Netflix en streaming.
	2.	Si un sistema de audio usa 8 bits por muestra, ¿cuántos niveles distintos puede representar cada muestra? ¿Y con 12 bits?
	3.	¿Qué pasaría si grabas una señal de 10 kHz con un muestreo de 15 kHz?



Soluciones rápidas
	1.	a) Analógico · b) Digital · c) Analógico · d) Digital
	2.	8 bits → 256 niveles · 12 bits → 4096 niveles
	3.	Violación de Nyquist ⇒ aliasing ⇒ la señal se distorsiona



2.8 Resumen
	•	El mundo es analógico, pero los ordenadores necesitan digitalizar para trabajar con bits (0/1).
	•	La conversión analógico-digital implica muestrear en el tiempo y cuantificar en niveles.
	•	La calidad depende de la frecuencia de muestreo y de la profundidad de bits.
	•	Todo lo que usamos hoy en día (audio, fotos, vídeo, sensores) pasa por este proceso.

