Representación de la Información — 10. Representación del vídeo



10.1 ¿Qué es un vídeo digital?

Un vídeo digital combina dos elementos principales:
	1.	Imágenes (fotogramas): son secuencias de imágenes bitmap que se muestran una tras otra.
	2.	Sonido: es un flujo de audio digital sincronizado con los fotogramas.

La sensación de movimiento aparece porque el ojo humano percibe como continuo cualquier cambio que ocurra a más de unas 16 imágenes por segundo.

En la práctica:
	•	Cine → 24 FPS.
	•	TV europea (PAL) → 25 FPS.
	•	TV americana (NTSC) → 30 FPS.
	•	Vídeo moderno (gaming, streaming) → 60 FPS o más.



10.2 Resolución y calidad de imagen en vídeo

El vídeo hereda las características de las imágenes: resolución y profundidad de color.

Ejemplos de resoluciones comunes:
	•	SD (Standard Definition): 720×576.
	•	HD (High Definition): 1280×720.
	•	Full HD: 1920×1080.
	•	4K (UHD): 3840×2160.
	•	8K: 7680×4320.

A mayor resolución y FPS, mayor será el volumen de datos.



10.3 Tamaño de un vídeo sin comprimir

El tamaño de un vídeo se calcula como:

\text{Tamaño} = \text{Ancho} \times \text{Alto} \times \text{Bits por píxel} \times \text{FPS} \times \text{Duración (segundos)}

Ejemplo:
Vídeo Full HD (1920×1080), 24 bits, 30 FPS, 1 minuto:

1920 \times 1080 \times 24 \times 30 \times 60 / 8 \approx 10,7 \; \text{GB}

Esto explica por qué es imprescindible la compresión en vídeo digital.



10.4 Compresión de vídeo

El vídeo se comprime para reducir tamaño, usando algoritmos llamados codecs (coder-decoder).

Tipos de compresión:
	•	Intra-frame: cada fotograma se comprime como si fuera una imagen independiente (ej.: MJPEG).
	•	Inter-frame: se aprovechan las similitudes entre fotogramas consecutivos; solo se guardan las diferencias.
Ejemplo: en una escena estática, la mayor parte de los píxeles no cambia.

Codecs más usados:
	•	MPEG-2: TV digital y DVD.
	•	H.264/AVC: estándar actual en streaming, Blu-Ray, YouTube.
	•	H.265/HEVC: sucesor de H.264, más eficiente (4K, 8K).
	•	VP9 / AV1: alternativas abiertas usadas en YouTube y Netflix.



10.5 Contenedores de vídeo

El vídeo y el audio se empaquetan en un contenedor que sincroniza los flujos.
El contenedor no define cómo se comprime, sino cómo se organizan los datos.

Ejemplos:
	•	.MP4 (MPEG-4 Part 14).
	•	.AVI (Audio Video Interleave, clásico de Windows).
	•	.MKV (Matroska, muy flexible).
	•	.MOV (QuickTime, Apple).



10.6 Streaming y transmisión

Hoy en día, la mayoría del vídeo se consume en streaming, no descargado.
Esto implica:
	•	Transmisión por partes: no hace falta descargar todo para empezar a reproducir.
	•	Adaptación dinámica: la calidad se ajusta según la velocidad de conexión (ej.: YouTube cambia entre 480p, 720p, 1080p…).
	•	Protocolos específicos: HLS (Apple), DASH (MPEG).



10.7 Limitaciones y retos
	•	Compresión excesiva: produce artefactos visibles (bloques, desenfoque).
	•	Alto consumo de ancho de banda: especialmente en 4K/8K.
	•	Sincronización audio-vídeo: imprescindible para que no haya “desfase labial”.
	•	Compatibilidad de codecs: no todos los dispositivos reproducen todos los formatos.



10.8 Ejemplos cotidianos
	•	Una película Blu-Ray (1080p, 2 horas) ocupa ~25 GB.
	•	La misma película en streaming (Netflix, H.264, 1080p) ocupa ~5 GB.
	•	Un clip de TikTok de 30 segundos en 720p comprimido apenas ocupa 3 MB.



10.9 Analogía para alumnos

Piensa en el vídeo como un flipbook (libro de dibujos animados):
	•	Cada página = un fotograma (imagen).
	•	Pasar rápido las páginas = FPS.
	•	Añadir un narrador = la pista de audio.
	•	Comprimir = en lugar de dibujar toda la página cada vez, dibujas solo lo que cambia.



10.10 Mini-ejercicios
	1.	Calcula cuánto ocuparía 1 segundo de vídeo 800×600, 24 bits, 25 FPS sin compresión.
	2.	¿Qué codec se usa típicamente para YouTube en 1080p?
	3.	¿Por qué es inviable guardar películas sin compresión?
	4.	¿Qué diferencia hay entre un codec y un contenedor?



Soluciones rápidas
	1.	800×600×24×25/8 ≈ 36 MB.
	2.	H.264/AVC (también VP9 en algunos casos).
	3.	Porque ocuparían decenas de GB por minuto, imposible de transmitir.
	4.	Codec = cómo se comprime; contenedor = cómo se organiza el audio/vídeo juntos.



10.11 Resumen
	•	Un vídeo digital es una secuencia de imágenes (fotogramas) más una pista de audio.
	•	La calidad depende de resolución, FPS y profundidad de color.
	•	El tamaño sin comprimir es enorme → se usan codecs (H.264, H.265, VP9).
	•	Los contenedores (.mp4, .avi, .mkv) organizan los flujos.
	•	El streaming permite consumir vídeo en tiempo real, adaptando la calidad.
