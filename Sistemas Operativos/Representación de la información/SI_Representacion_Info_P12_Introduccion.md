Representación de la Información — 9. Representación del sonido



9.1 El sonido en el mundo físico

El sonido es una onda mecánica que se produce por variaciones de presión en el aire.
Cuando hablamos o tocamos un instrumento, las moléculas de aire vibran y esa vibración se transmite hasta nuestros oídos.
	•	Frecuencia (Hz): número de vibraciones por segundo. Define el tono (grave/agudo).
	•	Voz humana: 85 Hz a 255 Hz aprox.
	•	Oído humano: de 20 Hz a 20.000 Hz.
	•	Amplitud: altura de la onda, que percibimos como volumen.



9.2 De lo analógico a lo digital: muestreo

Un micrófono transforma la onda de presión en una señal eléctrica analógica. Para almacenarla en un ordenador, hay que digitalizarla mediante un convertidor analógico-digital (ADC).

Proceso de muestreo
	•	Se toman muestras de la señal a intervalos regulares de tiempo.
	•	La frecuencia de muestreo se mide en Hz (muestras por segundo).
	•	Según el teorema de Nyquist, hay que muestrear al menos al doble de la frecuencia máxima de la señal para representarla correctamente.

Ejemplo:
	•	Audio de CD: frecuencia máxima ≈ 20 kHz.
	•	Muestreo = 44,1 kHz (suficiente para cubrir el rango del oído humano).



9.3 Cuantificación

Cada muestra se redondea a uno de un número finito de valores. Esto depende de la profundidad de bits:
	•	8 bits → 256 niveles posibles.
	•	16 bits → 65.536 niveles posibles.
	•	24 bits → 16,7 millones de niveles posibles.

Ejemplo:
	•	Audio de CD: 44,1 kHz de muestreo × 16 bits por muestra × 2 canales (estéreo).
	•	Resultado: ~1,4 Mbps de datos → unos 10 MB por minuto de audio sin compresión.



9.4 Representación en la práctica

PCM (Pulse Code Modulation)
	•	Forma más simple: cada muestra se guarda tal cual.
	•	Usada en WAV y en audio de CD.
	•	Calidad alta, pero ocupa mucho espacio.

Compresión con pérdida
	•	Ejemplo: MP3, AAC, OGG.
	•	Eliminan información poco perceptible al oído humano.
	•	Reducen el tamaño drásticamente, a costa de una pérdida de fidelidad.

Compresión sin pérdida
	•	Ejemplo: FLAC, ALAC.
	•	Reducen tamaño sin eliminar información.
	•	Útiles para archivado de música de alta calidad.



9.5 Canales y sonido estéreo
	•	Mono: un solo canal.
	•	Estéreo: dos canales (izquierda/derecha).
	•	Surround (5.1, 7.1, Dolby Atmos): varios canales para sonido envolvente.

Cada canal se digitaliza por separado, aumentando el tamaño total de los datos.



9.6 Limitaciones y problemas
	•	Aliasing: si el muestreo es insuficiente, aparecen distorsiones (ej.: un tono alto que parece más bajo).
	•	Ruido de cuantificación: pequeñas diferencias por el redondeo de las muestras.
	•	Compresión excesiva: en MP3 de baja calidad aparecen artefactos (“sonido metálico”).



9.7 Ejemplos cotidianos
	•	Un CD de música almacena 74 minutos de audio en PCM sin compresión.
	•	Spotify y YouTube usan compresión (OGG, AAC) para reducir el tamaño y poder transmitir por internet.
	•	Un archivo WAV de 3 minutos ≈ 30 MB. El mismo en MP3 de 128 kbps ≈ 3 MB.



9.8 Analogía para entenderlo

Imagina que el sonido es como dibujar una curva en un papel.
	•	El muestreo serían los puntos que marcas en la curva (cuantos más, más fiel es la copia).
	•	La cuantificación sería limitar cuántas alturas puedes marcar (si solo tienes una regla con divisiones grandes, perderás detalle).



9.9 Mini-ejercicios
	1.	Si grabas audio a 8 kHz con 8 bits en mono, ¿cuánto ocupará 1 segundo de grabación?
	2.	¿Por qué el estándar de CD usa 44,1 kHz y no 20 kHz exactos?
	3.	Explica la diferencia entre un archivo WAV y un MP3.
	4.	¿Qué ocurre si intentas muestrear una señal de 30 kHz con 40 kHz?



Soluciones rápidas
	1.	8.000 muestras × 8 bits = 64.000 bits = 8 KB.
	2.	Para evitar aliasing: 44,1 kHz cubre holgadamente el rango del oído humano (20 kHz).
	3.	WAV = sin compresión (PCM), ocupa más. MP3 = comprimido con pérdida, ocupa menos.
	4.	No cumple Nyquist (se necesitarían ≥ 60 kHz). Resultado: aliasing → el sonido se distorsiona.



9.10 Resumen
	•	El sonido es una onda analógica que se digitaliza con muestreo (tiempo) y cuantificación (amplitud).
	•	La calidad depende de la frecuencia de muestreo y la profundidad de bits.
	•	Formatos como WAV/PCM guardan todo, mientras que MP3/AAC comprimen con pérdida.
	•	Hoy en día, casi todo el audio que escuchamos pasa por este proceso de digitalización y compresión.
