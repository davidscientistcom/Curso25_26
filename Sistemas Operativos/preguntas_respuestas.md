# 100 preguntas y respuestas para obtener un 10 en la unidad de sistemas informáticos (DAM)

***

**1. ¿Qué es un sistema informático?**  
Un sistema informático reúne hardware, software y usuarios para procesar y gestionar la información.

**2. ¿De qué consta el hardware de un ordenador? Da ejemplos.**  
El hardware incluye componentes físicos: CPU, memoria, placa base, disco duro, teclado, pantalla.

**3. ¿Qué es el software? Da ejemplos.**  
El software son los programas y datos que permiten al hardware funcionar: sistemas operativos, ofimática, navegadores web.

**4. Explica cómo conviertes 45 de decimal a binario mediante la tabla de potencias.**  
Busca la mayor potencia de 2 menor o igual que 45 (32). Pon un 1 y resta (45-32=13). Siguiente potencia, 16 (no cabe, 0), 8 (cabe, 1, 13-8=5), 4 (cabe, 1, 5-4=1), 2 (no cabe, 0), 1 (cabe, 1, 1-1=0). Binario: 101101.

**5. Convierte el binario 100111 a decimal, explicando el método.**  
Coloca las potencias de 2 bajo cada cifra, de derecha a izquierda (1,2,4,8,16,32). Suma solo potencias donde hay 1: 32+4+2+1=39.

**6. ¿Cómo conviertes 78 a hexadecimal usando el método de divisiones sucesivas?**  
Divide 78 entre 16: 78/16=4 y resto 14. 14 en hexadecimal es "E". Resultado: 4E.

**7. Convierte el hexadecimal A7 a decimal paso a paso.**  
A=10, 7=7. Multiplica cada cifra por su potencia de 16: (10x16) + 7 = 160 + 7 = 167.

**8. ¿Cómo conviertes 11010110 a hexadecimal usando la agrupación de 4 bits?**  
Agrupa: 1101 (D) - 0110 (6). Así 11010110 binario es D6 hexadecimal.

**9. Explica cómo se representa el texto "A" en binario según la codificación ASCII.**  
"A" tiene valor decimal 65. En binario: 01000001.

**10. ¿Por qué los ordenadores usan el sistema binario y no el decimal directamente?**  
Por la simplicidad eléctrica; sólo hay que distinguir dos niveles, lo que hace el hardware más fiable y sencillo.

***

**11. Explica la diferencia fundamental entre sistema operativo monousuario y multiusuario. Da ejemplo.**  
Monousuario: solo una sesión activa, ejemplo: MS-DOS. Multiusuario: permite varias sesiones simultáneas, ejemplo: GNU/Linux.

**12. ¿Qué caracteriza a un sistema operativo de tipo monoproceso y multiproceso?**  
Monoproceso sólo ejecuta una tarea a la vez (MS-DOS), multiproceso puede ejecutar varias simultáneamente (Windows, Linux).

**13. ¿Qué permite la multitarea en los sistemas operativos actuales?**  
Simular la ejecución simultánea de múltiples programas, intercalando tiempo de CPU entre procesos.

**14. Explica cómo funciona la planificación FIFO en sistemas operativos.**  
El primer proceso en llegar a la cola de preparados se ejecuta primero; no se interrumpe hasta acabar (como una cola física).

**15. ¿Cómo funciona la planificación por trabajos más cortos primero (SJF)?**  
Se ejecuta siempre el proceso más corto disponible, aunque llegue después que otros, buscando eficiencia en el tiempo total.

***

**16. ¿Cuál es la diferencia entre sistema operativo de monoprocesador y multiprocesador?**  
Monoprocesador maneja un único procesador, multiprocesador gestiona varios y reparte tareas entre ellos.

**17. ¿Por qué existen sistemas operativos distribuidos? ¿Para qué se usan?**  
Para repartir la gestión y uso de recursos entre diferentes computadoras conectadas, como sistemas de red avanzados.

**18. Explica el concepto de máquina virtual en informática.**  
Una máquina virtual simula un hardware completo, permitiendo ejecutar varios sistemas operativos en el mismo equipo.

**19. Enumera dos ejemplos de sistemas operativos con microkernel y di la ventaja de la estructura microkernel.**  
MINIX y QNX; ventaja: más seguridad y tolerancia a fallos porque separa funciones esenciales en núcleos independientes.

**20. Explica el modelo de capas en sistemas operativos.**  
Cada capa únicamente interactúa con la inferior; así se simplifican cambios y errores, mejorando mantenimiento.

***

**21. ¿Qué contiene el bloque de control de procesos (PCB) en sistemas operativos?**  
Contiene identificador, estado, información de planificación y recursos del proceso que necesita el SO para gestionarlo.

**22. ¿Qué estados puede tener un proceso dentro del sistema operativo?**  
Listo/preparado, ejecutando, bloqueado y terminado/muerto.

**23. Explica de forma sencilla la transición de estados de un proceso.**  
Un proceso pasa a listo si está listo para ejecutarse, a ejecutando cuando avanza, a bloqueado si espera recursos, y termina si finaliza.

**24. ¿Qué hace el planificador de procesos (CPU Scheduler)?**  
Decide qué proceso pasa de la cola de preparados a ejecución según el algoritmo escogido (FIFO, SJF, Round Robin...)

**25. ¿Para qué sirve el comando 'ps -efl' en Linux?**  
Permite ver la lista detallada de procesos actuales, con sus estados y estadísticas de uso de recursos.

***

**26. ¿Qué es un núcleo (kernel) en el contexto de sistemas operativos?**  
Es la parte central que gestiona la memoria, procesos y comunicación entre software y hardware.

**27. ¿Qué ventajas aporta el uso de software libre en una empresa?**  
Permite modificar, distribuir y usar programas sin coste, fomentando el aprendizaje y adaptabilidad.

**28. ¿Por qué es recomendable personalizar la instalación de software en el ordenador?**  
Para optimizar el uso de recursos instalando sólo lo necesario y evitando programas inútiles.

**29. ¿En qué consiste la instalación avanzada de un programa?**  
Permite elegir componentes y configuraciones específicas, personalizando la aplicación para el usuario experto.

**30. ¿Cómo influye el tipo de sistema operativo en la gestión de periféricos?**  
Un SO bien diseñado facilita el reconocimiento, gestión y actualización de drivers para periféricos y hardware nuevo.

***

**31. Explica cómo se representa el número -27 en complemento a 2 (8 bits).**  
27 binario es 00011011; se invierten los bits: 11100100; se suma 1: 11100101.

**32. ¿Por qué la suma 0.1+0.2 en muchos lenguajes de programación no da exactamente 0.3?**  
Porque algunos números decimales no se pueden representar exactos en binario, lo que genera un pequeño error de redondeo.

**33. ¿Cómo se representa el número 0 en complemento a 2? ¿Por qué es útil esa propiedad?**  
Con todos los bits a 0. Es útil porque sólo hay una representación posible, simplificando la lógica del hardware.

**34. ¿Para qué sirve la mantisa en la representación de coma flotante?**  
La mantisa guarda los dígitos significativos del número normalizado, permitiendo precisión en los cálculos.

**35. ¿Qué significa exponente en exceso-127 en IEEE 754? Explica con ejemplo.**  
El exponente real se almacena sumándole 127; si el exponente es 3, se guarda como 130 (127+3).

***

**36. ¿Por qué es importante la normalización de números en coma flotante?**  
Permite representar números de manera única, maximizando la precisión de la mantisa y simplificando la lógica binaria.

**37. Da un ejemplo de error por codificación de texto en archivos y cómo se produce.**  
Abrir un archivo UTF-8 con Notepad usando ISO-8859-1: aparecen símbolos extraños en vez de ñ o acentos.

**38. ¿Cuál es la diferencia principal entre imagen rasterizada y vectorial?**  
Rasterizada tiene píxeles fijos; vectorial usa fórmulas matemáticas, escalable sin perder calidad.

**39. ¿Por qué las imágenes vectoriales no pierden nitidez al ampliarlas?**  
Porque se redibujan usando fórmulas, no dependen de la resolución original.

**40. ¿En qué casos es mejor usar imágenes rasterizadas en vez de vectoriales?**  
Para fotografías o imágenes con mucha textura y detalle, donde la representación por fórmulas sería inviable.

***

**41. ¿Cómo se representa el sonido digital en el ordenador?**  
Como una secuencia de muestras discretas, cada una con un valor binario, dependiendo de la frecuencia y profundidad de bits.

**42. ¿Qué determina la calidad (fidelidad) de un archivo de audio digital?**  
La frecuencia de muestreo y la profundidad de bits: más muestras y más bits proporcionan mayor calidad.

**43. ¿Por qué un archivo comprimido (jpg, mp3) es más pequeño que uno sin comprimir?**  
Porque elimina datos redundantes y menos perceptibles para ahorrar espacio manteniendo la calidad aceptable.

**44. Explica qué es un códec de vídeo y para qué sirve.**  
Es el algoritmo que codifica y decodifica la señal para reducir su tamaño y hacerla gestionable.

**45. ¿Cuál es la diferencia entre códec y contenedor en vídeo digital? Da ejemplo.**  
El códec define cómo comprimir el vídeo (H.264), el contenedor (mp4, mkv) organiza y almacena múltiples flujos en un solo archivo.

***

**46. ¿Por qué es útil la memoria caché en el sistema?**  
Acelera el acceso a datos repetidos o cercanos, disminuyendo el tiempo de espera del procesador.

**47. Explica por qué el bus de datos es esencial en la arquitectura del ordenador.**  
Permite que los distintos componentes (CPU, memoria, periféricos) se comuniquen rápidamente.

**48. ¿Cómo ayuda el sistema operativo en la gestión de errores y fallos?**  
Registra, maneja y recupera fallos del hardware y software, manteniendo la estabilidad y seguridad del sistema.

**49. ¿Para qué sirven los drivers en los sistemas operativos?**  
Traducen las órdenes de software a acciones concretas de hardware, permitiendo usar impresoras o tarjetas gráficas.

**50. ¿Qué diferencia hay entre software de sistema y software de aplicación? Da ejemplo de cada uno.**  
Software de sistema es el SO (Windows, Linux). De aplicación: Word, Photoshop, navegadores.

***

**51. ¿Qué significa que la memoria RAM es volátil?**  
Pierde su contenido al apagar el ordenador; sólo almacena datos temporalmente durante la ejecución.

**52. ¿Por qué es necesario tener sistemas de respaldo y copias de seguridad?**  
Para evitar la pérdida de datos irreversibles ante fallos, robos o errores humanos.

**53. ¿Cuándo utilizarías una máquina virtual en tu trabajo como programador?**  
Cuando necesitas probar software en distintos SO, aislar proyectos y garantizar ambiente controlado.

**54. ¿Qué información puedes obtener con el comando 'ipconfig' o 'ifconfig'?**  
Datos de configuración de red: dirección IP, máscara de subred, puerta de enlace, estado de interfaces.

**55. ¿En qué consiste el modelo cliente-servidor en informática?**  
El cliente solicita servicios y el servidor los provee en una red; permite compartir recursos y ejecutar tareas distribuidas.

***

**56. ¿Cómo afectan los fallos de hardware a los sistemas informáticos?**  
Pueden detener procesos, corromper datos o causar pérdida de información; el SO debe detectar y minimizar los efectos.

**57. ¿Qué diferencia hay entre almacenamiento primario y secundario?**  
Primario (RAM) es rápido pero volátil; secundario (disco duro, SSD) es permanente y tiene mayor capacidad.

**58. Explica la utilidad de particionar un disco duro.**  
Aísla y organiza el espacio en discos virtuales para instalar varios sistemas y proteger datos.

**59. ¿Qué ventajas aporta la virtualización a la administración de sistemas?**  
Permite ejecutar varios entornos independientes, optimizar recursos y recuperar sistemas rápidamente tras fallos.

**60. Da un ejemplo de sistema operativo que soporte multiprocesador.**  
GNU/Linux o Windows 10 pueden distribuir procesos entre varios procesadores físicos.

***

**61. ¿Por qué es importante entender la representación de los datos en binario para programar?**  
Porque la manipulación de bits es esencial para el rendimiento, seguridad y gestión eficaz de la información.

**62. Explica cómo sería el proceso para convertir 102 decimal a binario siguiendo la tabla de potencias.**  
102 - 64=38 (1 en 2⁶). 32 cabe, 38 - 32=6 (1 en 2⁵). 16 no cabe, 0. 8 no cabe, 0. 4 cabe, 6-4=2 (1 en 2²). 2 cabe, 2-2=0 (1 en 2¹). 1 no cabe (0). Binario: 1100110.

**63. ¿Cómo conviertes el binario 10111010 a decimal paso a paso?**  
128+32+16+8+2=186 (sumando las posiciones con 1 en el binario).

**64. Explica cómo obtienes el binario de 217 usando la tabla de potencias.**  
217-128=89 (1 en 2⁷). 64 cabe, 89-64=25 (1 en 2⁶). 32 no cabe, 0. 16 cabe, 25-16=9 (1 en 2⁴). 8 cabe, 9-8=1 (1 en 2³). 4 no cabe, 0. 2 no cabe, 0. 1 cabe, 1-1=0 (1 en 2⁰). Binario: 11011001.

**65. Convierte el hexadecimal 1AF a binario con explicación.**  
1=0001, A=1010, F=1111. Resultado: 000110101111.

***

**66. ¿Por qué los sistemas operativos modernos incluyen gestión avanzada de usuarios?**  
Para proteger información, segmentar derechos de acceso y permitir operaciones simultáneas sin conflictos.

**67. ¿Qué significa tener permisos de ejecución en un archivo de sistema?**  
Define si un usuario puede lanzar el archivo como programa; sin permiso no se puede iniciar.

**68. ¿Cómo se asegura la seguridad en el acceso a archivos y carpetas?**  
Con permisos granulares (lectura/escritura/ejecución) y propietarios; sólo quien tiene permisos adecuados puede acceder o modificar.

**69. ¿Qué diferencias hay entre los tipos de particiones: primaria, extendida y lógica?**  
Primarias pueden arrancar SO; extendida es un contenedor para varias lógicas; lógicas amplían el número de “unidades” usables.

**70. ¿Para qué se usa el sistema de archivos? Da ejemplo.**  
Organiza y controla cómo se almacenan y recuperan datos (ext4 en Linux, NTFS en Windows).

***

**71. ¿Por qué la actualización regular del sistema operativo es una práctica recomendada?**  
Corrige vulnerabilidades, mejora rendimiento y compatibilidad con hardware actual.

**72. ¿Qué puedes hacer si al abrir un archivo aparecen caracteres extraños?**  
Cambiar la codificación al abrir el archivo (UTF-8, ISO-8859-1, etc.) o re-guardar con la codificación correcta.

**73. ¿Cuál es el objetivo principal del gestor de memoria en el SO?**  
Optimizar el uso de la memoria RAM, asignando y liberando espacios según las necesidades de los programas.

**74. ¿Qué problema puede generar un mal uso de la memoria RAM por el software?**  
Ralentización, fallos, cierre inesperado de programas o incluso bloqueo total del equipo.

**75. Da ejemplo de cómo el sistema operativo gestiona los dispositivos externos (plug & play).**  
Microsoft Windows instala el driver adecuado al conectar una impresora y la deja lista para usar automáticamente.

***

**76. ¿Por qué es útil la segmentación de procesos en la multitarea?**  
Evita que procesos interfieran entre sí, gestionando de forma eficiente los recursos y tiempos de CPU.

**77. ¿En qué consiste el sistema de prioridades en la planificación de procesos?**  
Procesos con prioridad alta reciben más tiempo o recursos; los menos importantes esperan más para ser ejecutados.

**78. ¿Por qué el sistema operativo utiliza algoritmos como Round Robin?**  
Para repartir equitativamente el tiempo de CPU entre procesos, evitando bloqueos y manteniendo la multitarea.

**79. ¿Qué problema puede presentar el uso excesivo de la CPU por un proceso?**  
Ralentiza el resto del sistema y puede bloquear la respuesta incluso al usuario u otros programas.

**80. ¿Para qué sirve la monitorización de procesos y recursos en sistemas de servidores?**  
Permite prevenir errores, anticipar cuellos de botella y tomar decisiones rápidas ante sobrecargas.

***

**81. Explica la diferencia clave entre software propietario y libre.**  
Propietario requiere licencia y no se puede modificar; el libre es editable, redistribuible y normalmente gratuito.

**82. ¿Qué significa que un sistema operativo se organise en capas?**  
Cada capa depende sólo de la inferior, separando funciones como interfaz de usuario, gestión de recursos y núcleo.

**83. ¿Cómo influye la arquitectura microkernel en la fiabilidad de los sistemas?**  
Divide el SO en componentes mínimos, evitando que un fallo afecte a todo el sistema.

**84. Da ejemplo de uso de máquina virtual en una empresa.**  
Probar aplicaciones en Windows y Linux dentro de un mismo equipo físico, sin riesgo de errores en el sistema real.

**85. ¿Qué ventaja ofrece el modelo cliente-servidor ante software monolítico?**  
Permite escalabilidad, mantenimiento y actualización individual de los servicios, mejorando la eficiencia.

***

**86. ¿Qué diferencia hay entre dirección IP pública y privada?**  
La IP pública identifica en Internet; la privada sólo dentro de la red interna (LAN).

**87. ¿Por qué es importante configurar adecuadamente la máscara de subred en una red local?**  
Para definir el rango de dispositivos que pueden comunicarse directamente.

**88. ¿En qué consiste NAT y para qué se usa en redes?**  
Traduce direcciones IP internas a externas para compartir la conexión de red y mejorar la seguridad.

**89. ¿Por qué los sistemas operativos permiten la autenticación de usuarios?**  
Para proteger recursos y mantener la privacidad/control de datos en entornos compartidos.

**90. ¿Cómo protege el SO a los procesos de los ataques de software malicioso?**  
Establece privilegios, espacios de memoria independientes y monitoriza accesos sospechosos.

***

**91. ¿Por qué es vital saber distinguir entre bits y bytes en programacion?**  
Porque las capacidades y el trabajo con datos dependen de saber si tratas con 8 bits (1 byte), 16 bits, etc.

**92. Explica cómo obtendrías la representación binaria de una imagen de 2x2 píxeles en blanco y negro.**  
Cada píxel es 1 bit: 00 para arriba, 11 para abajo; combinación de estos bits da el archivo de imagen.

**93. ¿Cómo puedes identificar un archivo ejecutable en Windows y en Linux?**  
Por extensión (.exe en Windows); por permiso de ejecución y encabezado binario en Linux.

**94. ¿Por qué un programador debería entender el funcionamiento de los algoritmos de planificación de procesos?**  
Para escribir software eficiente, optimizar el uso de recursos y evitar bloqueos y esperas innecesarias.

**95. Haz paso a paso la conversión de 255 a hexadecimal.**  
255/16=15 y resto 15; 15=F. Por lo tanto, FF lejos.

***

**96. Explica, dando un ejemplo, cómo la información de los procesos se almacena en la tabla de bloques de control.**  
Cada entrada almacena el PID (ID de proceso), estado, recursos asignados. Ejemplo: PID=124, estado=preparado, 16MB RAM.

**97. ¿Por qué se dice que FIFO puede bloquear procesos cortos?**  
Porque si llega un proceso largo antes, los cortos deben esperar hasta que acabe el primero.

**98. ¿Cuál es el objetivo de los algoritmos de planificación modernos?**  
Maximizar la eficiencia y minimizar la espera total de todos los procesos activos.

**99. ¿Qué ventaja aporta separar la gestión de procesos y la de memoria en el SO?**  
Permite organizar recursos y proteger datos, evitando que procesos accedan a memoria de otros.

**100. ¿Por qué la comprensión de estos conceptos es clave para aprobar y ser útil en la empresa?**  
Porque garantizan que sabes convertir, interpretar y manejar datos, gestionar sistemas operativos y resolver problemas reales.


[1](https://www.studocu.com/es/document/ilerna/sistemas-informaticos/test-uf1-110-preguntas-corregido/54606531)
[2](https://www.youtube.com/watch?v=1xsnH0rPRCY)
[3](https://discoduroderoer.es/tareas-1-sistemas-informaticos-dam-daw-e-learning-resueltas/)
[4](https://es.scribd.com/document/821428524/DAM-Examen-Tema-4-Sistemas-Informaticos)
[5](https://www.studocu.com/es/document/instituto-de-educacion-secundaria-fernando-wirtz-suarez/tecnologias-de-la-informacion-y-la-comunicacion-ii/dam-si01-software-de-un-sistema-informatico/112487643)
[6](https://fr.scribd.com/document/615028293/Examen-1%C2%BA-DAM-B-Solucionado)
[7](https://github.com/Qv1ko/DAM)
[8](https://www.daypo.com/sistemas-informaticos-preguntas-libro.html)
[9](https://www.daypo.com/dam-1-sistemas-informaticos-t1.html)
[10](https://www.youtube.com/watch?v=oiJPsxvvrLI)