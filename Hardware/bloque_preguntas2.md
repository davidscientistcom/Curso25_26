# Bloque 2 De preguntas de Hardware.


**1. Si al montar un nuevo PC buscas el máximo silencio posible, ¿por qué deberías fijarte en el formato y la cantidad de ventiladores que admite la caja de la placa base?**  
Cuantos más ventiladores grandes puedes instalar y menor restricción tenga el flujo de aire de la caja, más despacio pueden girar para la misma refrigeración. Menos RPM significa menos ruido, por lo que una caja con muchas opciones te deja optimizar silencio y temperaturas.

**2. ¿Por qué no es recomendable usar placas base OEM (de grandes marcas ensambladoras) para proyectos de upgrades serios o overclocking?**  
Las placas OEM suelen estar diseñadas para el coste y la estabilidad básica, con escasa personalización, VRMs sencillos y BIOS muy limitadas, lo que te restringe las posibilidades de mejora y control.

**3. Si tienes una placa base antigua sin soporte UEFI, ¿cómo afecta eso a la compatibilidad con discos modernos y sistemas operativos recientes?**  
Sin UEFI, tu placa no podrá arrancar sistemas desde discos de más de 2,2TB ni aprovechar ciertas protecciones de arranque seguro, dificultando el uso de hardware o sistemas modernos como Windows 11.

**4. ¿Por qué puede haber pérdida de rendimiento al instalar dos módulos de RAM de distinta velocidad en una placa base?**  
El sistema ajusta la velocidad al del módulo más lento para garantizar la estabilidad, desaprovechando la velocidad potencial del módulo más rápido.

**5. Diferencia, con razones, entre las salidas de vídeo DisplayPort y HDMI, y cuándo priorizar una u otra.**  
DisplayPort soporta mayor ancho de banda y más monitores en una sola conexión; HDMI es más extendido en televisores y soporta audio de retorno (ARC). Para monitores de PC con altas tasas de refresco, mejor DisplayPort; para TVs o dispositivos multimedia, HDMI.

**6. Una fuente de alimentación de baja calidad puede dañar componentes aun si funciona “temporalmente”. Razona por qué.**  
Las fuentes de baja calidad tienen malas protecciones contra picos eléctricos y rizado de tensión, factores que pueden degradar placas, RAM, SSD y CPU a largo plazo, aunque el sistema arranque aparente “normal”.

**7. ¿Por qué los sistemas modernos ya no usan tanto los puertos PS/2 para teclados y ratones?**  
USB es más universal, soporta más dispositivos y permite conexión/desconexión en caliente, algo que PS/2 sólo tolera si el PC está apagado. Así, la estandarización, flexibilidad y migración al USB es lógica.

**8. ¿Para qué situaciones resulta relevante conocer la diferencia entre cable SATA y SATA Express?**  
SATA Express permite mayor ancho de banda y compatibilidad con dispositivos PCIe, esencial cuando se busca aprovechar SSDs de alto rendimiento en placas que lo permiten.

**9. Si al instalar una tarjeta gráfica el PC no da video pero todo parece conectado, ¿por qué revisar la fuente de alimentación no es sólo un trámite?**  
Las GPUs modernas pueden exigir mucha potencia instantánea. Si la fuente es insuficiente, incluso siendo “nueva”, puede no entregar los amperios necesarios, bloqueando compeltamente el arranque de la GPU sin quemarse.

**10. Si tienes un PC que arranca muy lento aunque tiene un SSD nuevo, ¿por qué comprobar la configuración de arranque en BIOS/UEFI es clave?**  
Quizás arranca primero desde otro disco duro viejo o la secuencia de arranque es incorrecta. Así, tarda revisando varios discos hasta dar con el correcto, lo que puede descuadrar cualquier mejora esperada con el SSD.

***

**11. ¿Por qué las memorias ECC se eligen en servidores y no tanto en PCs domésticos?**  
ECC corrige errores de bit, imprescindible en sistemas donde la corrupción de un dato sería catastrófica (bancos, hospitales), mientras que en PC la prioridad suele ser rendimiento y coste, donde la tasa de fallos es asumible.

**12. Si tu CPU y RAM soportan overclock pero la placa base es básica, ¿razona por qué puedes no conseguir ningún aumento de frecuencia?**  
El VRM podría no aguantar más voltaje, la BIOS bloquea cambios en multiplicadores o voltajes, y los perfiles XMP pueden no funcionar por limitaciones del diseño básico de la placa.

**13. Si compras un SSD externo para copias rápidas de mucho volumen, ¿por qué puede ser un error usar puertos USB frontales de la caja?**  
Esos puertos suelen estar limitados por su cableado (2.0 o 3.0 pero con menos pines activos), lo que puede capar la velocidad real. Usar siempre los traseros, soldadados directamente a la placa, garantiza máximas velocidades.

**14. ¿Por qué elegirías un portátil con ranuras SO-DIMM accesibles para la RAM si prevés ampliaciones?**  
Algunos portátiles tienen RAM soldada, lo que impide cualquier mejora futura. Con SO-DIMM accesibles puedes ampliar memoria fácilmente, alargando la vida útil y el rendimiento del equipo.

**15. ¿Por qué las APU modernas pueden sustituir a una CPU+GPU básica en muchos entornos?**  
Las APU (CPU con gráfica integrada potente) permiten ahorrar energía, reducir costes y complicaciones de compatibilidad y son suficientes para la mayoría de oficinas, aulas y multimedia ligera.

**16. Si el ventilador de la CPU gira pero sigue subiendo la temperatura, ¿por qué revisar la pasta térmica y el montaje tiene lógica?**  
La pasta podría estar seca o mal aplicada, o el disipador no estar bien sujeto: se crea una separación entre CPU y disipador y la transferencia de calor falla, aunque el ventilador esté operativo.

**17. ¿Por qué a veces el máximo de RAM oficialmente soportado por una placa difiere del que es posible usar extraoficialmente?**  
Los fabricantes suelen homologar sólo módulos que han probado pero la placa puede detectar y usar más capacidad si los chips/módulos cumplen el estándar eléctrico y lógico, aunque no se garantice esa estabilidad.

**18. Si tienes que elegir entre dos discos duros mecánicos, uno con 7200 rpm y otro con 5400 rpm, ¿qué factores prácticos afectan realmente a la elección?**  
Un disco de 7200 rpm es más rápido en lecturas/escrituras pero más ruidoso y calienta más; uno de 5400 rpm es más adecuado para almacenamiento masivo poco usado (menos ruido, más vida), pero más lento.

**19. ¿Por qué es fundamental tener memorias USB o SD de marcas fiables, especialmente para guardar fotos o documentos importantes?**  
Las memorias baratas a menudo usan chips reciclados o de baja calidad, lo que eleva el riesgo de corrupción o pérdida de datos. Una marca reconocida ofrece garantías de fiabilidad y soporte.

**20. Si una placa base sólo comparte una ranura PCIe x16 para GPU con una x4 para SSD NVMe, ¿por qué puede haber conflicto de rendimiento en juegos o edición de vídeo?**  
Si ambas ranuras comparten líneas PCIe, el ancho de banda se reparte. Al usar GPU y SSD intensamente, pueden saturarse y la transferencia de datos (FPS o escritura/lectura) disminuirá.

***

**21. Si un usuario busca aumentar la autonomía de un portátil, ¿por qué razón la sustitución del HDD por un SSD marca la diferencia aunque ambos sean “almacenamiento”?**  
El SSD requiere menos energía ya que no tiene partes móviles y accede a los datos casi instantáneamente, lo que reduce tanto el consumo eléctrico global como los tiempos de acceso (más tiempo en suspensión).

**22. ¿Por qué es racional limpiar periódicamente el interior del PC y especialmente disipadores y ventiladores?**  
El polvo actúa como un aislante térmico y limita el flujo de aire, lo que puede subir la temperatura, forzar los ventiladores y reducir la vida útil de los componentes por sobrecalentamiento.

**23. ¿Qué ventaja puede aportar instalar una tarjeta de red dedicada (PCIe) frente a una integrada en placa?**  
Las tarjetas dedicadas suelen ofrecer mayor rendimiento, opciones avanzadas (Wake on LAN, VLAN) y menor uso de recursos del sistema (CPU y RAM), mejorando la conectividad en ambientes exigentes.

**24. Razona cuándo NO tiene sentido invertir en una fuente de alimentación con certificación Platinum para un PC de oficina estándar.**  
El consumo global será bajo y el ahorro en la factura eléctrica mínimo, haciendo que la relación coste-beneficio no compense frente a una Gold o Bronze.

**25. ¿Por qué reinstalar el sistema operativo desde cero tras cambiar de HDD a SSD y no solo clonar el disco?**  
La clonación puede arrastrar sectores dañados, configuraciones antiguas y drivers de HDD; una instalación limpia optimiza Arranque, TRIM y el uso del SSD para un rendimiento real y estabilidad.

**26. Si tienes una microSD mal reconocida en el PC pero sí en el móvil, ¿qué aspecto técnico podrías investigar antes de formatearla?**  
Algunos lectores no soportan sistemas de archivos grandes (exFAT, NTFS). Podrías comprobar el sistema de archivos y cambiar a FAT32 si la compatibilidad lo requiere.

**27. ¿Por qué las BIOS/UEFI traen opciones para “deshabilitar” la gráfica integrada al poner una dedicada?**  
Desactivando la iGPU, se liberan recursos y se reduce el consumo, evitando posibles conflictos de drivers o errores en el arranque BIOS/UEFI.

**28. ¿Para qué se sigue usando memoria ROM en dispositivos actuales si la RAM es mucho más rápida y barata?**  
La ROM es no volátil y protege el contenido de modificaciones accidentales. Es ideal para almacenar firmware básico que debe estar siempre disponible y libre de corrupción (ejemplo: BIOS, routers, impresoras).

**29. ¿Por qué es relevante conocer la diferencia entre GiB, GB y TB al instalar discos?**  
Por precisión: GB usa múltiplos de 1000, GiB usa múltiplos de 1024. Los sistemas operativos suelen medir en GiB, lo que puede llevar a confusiones sobre el espacio disponible vs. nominal del fabricante.

**30. La presencia de puertos USB-C en una placa base, ¿en qué casos prácticos puede influir tu elección de hardware?**  
El USB-C soporta alta velocidad, carga rápida y reversibilidad. Si tienes periféricos modernos (discos externos, smartphones, monitores portátiles), preferir USB-C te permite aprovechar todo su potencial.

***

**31. Si la CPU de tu portátil baja drásticamente la frecuencia bajo carga media, ¿qué deducción razonada harías antes de cambiarla?**  
Probablemente hay thermal throttling: el sistema baja la frecuencia a la fuerza para evitar sobrecalentamiento. Sería más lógico limpiar ventiladores o cambiar la pasta térmica antes de pensar en cambiar la CPU.

**32. ¿Por qué mover módulos de RAM a las ranuras “iguales de color” en la placa puede tener impacto en el rendimiento?**  
Esas ranuras suelen ser para activar el Dual (o Quad) Channel según el esquema de la placa. Si los módulos no están alineados, el sistema no aprovechará el mayor ancho de banda disponible.

**33. En placas base actuales, ¿por qué algunos puertos SATA dejan de funcionar si usas determinadas ranuras M.2 NVMe?**  
Comparten rutas físicas de conexiones, no pueden estar activos a la vez por limitaciones de líneas internas. Hay que consultar siempre el manual para evitar perder funcionalidad sin querer.

**34. ¿Por qué muchas placas ofrecen cabezales para ventiladores de CPU, chasis y AIO por separado?**  
Permite controlar la velocidad de cada uno de forma independiente según temperatura y posición, optimizando refrigeración y nivel de ruido.

**35. ¿Por qué un USB típico (A o C) puede estar limitado a baja velocidad aunque sea “3.0”?**  
Cables y conectores internos de baja calidad, uso de hubs intermedios o falta de soporte de pines completos pueden reducir la velocidad real aunque el estándar sea superior.

**36. ¿Por qué interesa conocer si la RAM es unificada cuando eliges un portátil o consola de nueva generación?**  
La RAM unificada es accesible tanto para la CPU como para la GPU, eliminando esperas y cuellos de botella en tareas que requieren acceso conjunto (gráficos, IA, multitarea).

**37. ¿Por qué en la práctica rara vez se alcanza el “ancho de banda máximo” teórico de los buses/interconexiones (SATA, PCIe, USB)?**  
El rendimiento real se ve afectado por latencias, colas de espera, calidad del cableado y el firmware, entre otros factores, imposibilitando usar todo el potencial simultáneo sostenido.

**38. ¿Por qué muchas veces los teclados USB pueden dejar de funcionar en la BIOS, pero sí en Windows?**  
Algunas placas requieren opciones de “USB legacy” en BIOS para soportar periféricos USB antes de que el SO cargue sus drivers completos.

**39. ¿Por qué las CPUs actuales integran cada vez más funciones (gráfica, memoria, I/O) en el propio paquete en vez de usar “chipsets” externos?**  
Reduce latencia, consumo y costes de fabricación. Al minimizar el trayecto de datos, se gana eficiencia y velocidad global.

**40. En un SSD NVMe, ¿por qué la refrigeración activa (disipador con ventilador propio) puede ser relevante en rendimiento real?**  
La memoria NAND y el controlador generan calor bajo uso intensivo; si se sobrecalientan, se activa el thermal throttling y baja la velocidad bruscamente.

***

**41. Si una placa base tiene WiFi integrado pero resulta lento comparado con un adaptador USB externo moderno, ¿qué evaluarías de forma razonada?**  
Puede tratarse de un chip WiFi antiguo (2.4 GHz solo) o limitado en antenas/MIMO. Un adaptador externo moderno puede tener mejores estándares y más antenas, dando mejor velocidad y estabilidad.

**42. ¿Por qué en hardware empresarial se usaban placas con doble BIOS?**  
Si una actualización fallaba, podía arrancar con la secundaria, garantizando recuperación rápida en entornos críticos considerando que el riesgo de corrupción de firmware es inasumible profesionalmente.

**43. ¿Por qué muchas fuentes de alimentación traen conectores modulares?**  
Permite usar sólo los cables necesarios, mejorando el flujo de aire, reduciendo el lío de cables y facilitando reemplazos en caso de fallo o futura ampliación.

**44. En una placa base moderna, ¿por qué decidir entre usar ranuras DIMM o SODIMM puede dictar el tipo de caja y formato global del PC?**  
DIMM es para PCs de escritorio, grandes y fácilmente ampliables. SODIMM va en portátiles/Mini-PCs, es más compacto pero ofrece menos opciones de refrigeración y velocidad.

**45. ¿Por qué una estación de trabajo debería utilizar RAID 1 para los discos en vez de RAID 0 en la mayoría de casos empresariales?**  
RAID 1 duplica los datos en dos discos, garantizando redundancia y seguridad. RAID 0 solo suma velocidad pero aumenta el peligro de perder todos los datos si falla un disco.

**46. Si un servidor soporta hot-swap de discos, ¿qué ventaja competitiva ofrece frente a uno que no lo tiene?**  
Permite cambiar discos sin apagar el sistema, manteniendo disponibilidad y reduciendo tiempos de inactividad en empresas.

**47. ¿Por qué puede ser mejor optar por un SSD TLC bien refrigerado que por un QLC más barato en ordenadores exigentes?**  
El TLC tiene más ciclos de escritura y mayor rendimiento sostenido; el QLC pierde velocidad con uso intensivo y resiste menos escrituras antes de deteriorarse.

**48. Cuando conectas un disco duro antiguo con muchos errores de sectores, ¿por qué es mejor sacar antes una imagen bit a bit que copiar sólo archivos?**  
Una imagen permite rescatar datos aunque el sistema de archivos esté dañado; copiar solo archivos puede omitir partes recuperables y obviar los errores más importantes.

**49. ¿Por qué el consumo energético de un componente puede afectar a la estabilidad global del sistema aunque la suma total esté dentro del límite de la fuente?**  
Picos de consumo instantáneo en un componente (GPU, CPU) pueden sobrepasar lo que puede entregar un solo raíl, aunque la suma de vatios no lo haga, causando reinicios o apagones inesperados.

**50. Por qué conviene razonar cada decisión de hardware no solo mirando las “hojas técnicas” sino también la compatibilidad, el uso final y la evolución de necesidades.**  
Las especificaciones teóricas no reflejan limitaciones del mundo real (compatibilidad, recambios, escalabilidad, soporte técnico). Entender todo el ecosistema y el caso de uso asegura una compra eficaz y duradera.

[1](https://es.educaplay.com/recursos-educativos/2457724-preguntas_sobre_hardware.html)
[2](https://www.tinglado.net/?id=tests-sobre-componentes-del-pc&page=1)
[3](https://cibertest.com/test-examen/45/hardware)
[4](https://www.cerebriti.com/juegos-de-tecnologia/preguntas-de-hardware-y-software)
[5](https://www.vervecopilot.com/es/preguntas-de-entrevista/las-30-preguntas-de-entrevista-de-hardware-m%C3%A1s-comunes-que-debes-preparar)
[6](https://wayground.com/admin/quiz/67f466e058e2d407d743ba81/quiz-sobre-hardware-y-componentes-de-un-ordenador)
[7](https://es.scribd.com/document/615280065/Test-Repaso-Tema-1-Resuelto)
[8](https://www.youtube.com/watch?v=wKNHmd2zyUc)
[9](http://avfer.blogspot.com/2015/12/test-sobre-componentes-del-pc.html)
[10](https://www.goconqr.com/es/cuestionario/6082985/test-la-computadora-y-sus-partes)