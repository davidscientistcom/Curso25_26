Representación de la Información — 8. Representación de imágenes

8.1 ¿Qué es una imagen digital?

Una imagen digital es una representación numérica de una imagen visual. Puede almacenarse de dos maneras principales:
	•	Como una matriz de píxeles (mapa de bits o bitmap).
	•	Como un conjunto de fórmulas geométricas (vectorial).

Ambos métodos tienen ventajas e inconvenientes, y se usan en distintos contextos.



8.2 Imágenes de mapa de bits (bitmap o raster)

Una imagen de mapa de bits se representa como una rejilla de píxeles.
Cada píxel tiene un valor de color, que se guarda en binario.
	•	Resolución: número de píxeles en ancho y alto.
	•	Profundidad de color: número de bits que definen el color de cada píxel.
	•	Tamaño: proporcional a resolución × profundidad de color.

Ejemplo:
Una imagen de 1024×768 a 24 bits ocupa ~2,25 MB sin compresión.

Ventajas:
	•	Reproduce fotos con gran detalle.
	•	Adecuado para imágenes con muchos matices (fotografía, vídeo).

Inconvenientes:
	•	Escalarla (ampliarla) provoca pérdida de calidad (efecto pixelado).
	•	Archivos grandes si no se usa compresión.

Formatos típicos:
	•	BMP, PNG, JPEG, GIF, TIFF.



8.3 Imágenes vectoriales

Una imagen vectorial se representa mediante objetos geométricos definidos matemáticamente:
	•	Puntos.
	•	Líneas.
	•	Curvas.
	•	Polígonos.

Cada objeto tiene atributos como color de relleno, trazo, grosor.

Ejemplo:
Un círculo se guarda como “centro (x,y), radio r, color azul”, no como millones de píxeles.

Ventajas:
	•	Se pueden escalar infinitamente sin perder calidad (perfectas para logotipos).
	•	Archivos muy ligeros para gráficos simples.
	•	Fáciles de editar en programas de diseño.

Inconvenientes:
	•	No sirven para representar fotos reales (serían demasiado complejas).
	•	Necesitan rasterizarse (convertirse en mapa de bits) para mostrarse en pantallas o impresoras.

Formatos típicos:
	•	SVG (Scalable Vector Graphics).
	•	EPS, PDF, AI (Adobe Illustrator).



8.4 Profundidad de color en mapas de bits

La profundidad de color indica el número de bits usados por píxel:
	•	1 bit: blanco y negro.
	•	8 bits: 256 colores (o grises).
	•	24 bits: 16,7 millones de colores (RGB verdadero).
	•	32 bits: 24 bits de color + 8 bits de transparencia (alfa).

Ejemplo:
Un píxel en 24 bits se codifica como tres bytes:
	•	Rojo (0–255).
	•	Verde (0–255).
	•	Azul (0–255).



8.5 Compresión de imágenes bitmap

Sin pérdida:
	•	PNG, BMP, TIFF (sin compresión).
	•	Conservan todos los datos.

Con pérdida:
	•	JPEG.
	•	Reducen tamaño eliminando información perceptualmente menos relevante.



8.6 Tamaño de una imagen bitmap

\text{Tamaño} = \text{Ancho} \times \text{Alto} \times \frac{\text{Bits por píxel}}{8}

Ejemplo: Imagen 1920×1080, 24 bits:
1920 \times 1080 \times 24 / 8 \approx 6,22 \; \text{MB}



8.7 Comparativa bitmap vs vectorial

Característica	Bitmap	Vectorial
Representación	Matriz de píxeles	Fórmulas geométricas
Calidad al escalar	Pierde calidad (pixelado)	Escala infinita sin pérdida
Tamaño de archivo	Grande (dependiente resolución)	Pequeño (dependiente complejidad)
Uso típico	Fotos, capturas, vídeos	Logos, iconos, ilustraciones
Formatos comunes	BMP, JPEG, PNG, GIF, TIFF	SVG, PDF, EPS, AI




8.8 Ejemplos cotidianos
	•	Una foto de vacaciones → mapa de bits (JPEG/PNG).
	•	El logotipo de una empresa → vectorial (SVG/AI).
	•	Al escalar una foto pequeña en Paint → se ve pixelada.
	•	Al escalar un logo vectorial en Illustrator → se ve perfecto.



8.9 Mini-ejercicios
	1.	¿Qué tipo de imagen usarías para:
a) Un logotipo en la web.
b) Una foto en un álbum digital.
c) Un icono de aplicación que debe verse bien en cualquier tamaño.
	2.	Calcula el tamaño de una imagen de 800×600 a 8 bits por píxel.
	3.	¿Qué pasa si amplías una imagen bitmap al doble de su tamaño?



Soluciones rápidas
	1.	a) Vectorial (SVG) · b) Bitmap (JPEG/PNG) · c) Vectorial (SVG).
	2.	800×600×8/8 = 480.000 bytes ≈ 468 KB.
	3.	Se pixelará, porque no se pueden inventar píxeles nuevos con detalle.



8.10 Resumen
	•	Bitmap (raster): imágenes como matriz de píxeles, ideales para fotos, pero pesadas y con pixelado al escalar.
	•	Vectoriales: imágenes definidas matemáticamente, ideales para gráficos escalables como logos.
	•	En la práctica:
	•	Fotos → bitmap (JPEG/PNG).
	•	Logos e ilustraciones → vectorial (SVG/AI/PDF).

