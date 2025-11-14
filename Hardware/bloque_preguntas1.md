# Bloque 1 de preguntas de Hardware.
## Placa base y buses

**1. Si tuvieras que montar un PC muy compacto pero que tuviera a la vez buena capacidad de expansión, ¿qué factor de forma elegirías y por qué?**
- Un formato micro-ATX (mATX) equilibraría tamaño y capacidad de expansión: más pequeño que ATX pero con varias ranuras de expansión, a diferencia del Mini-ITX que a menudo solo tiene una ranura y limita mucho las opciones de ampliación.

**2. ¿Por qué la robustez de los VRM es determinante al elegir una placa base para CPUs potentes?**
- Una CPU de alto consumo demanda entregas de energía muy estables. Si los VRM son insuficientes, la CPU no rendirá a su máximo potencial, tendrá inestabilidad o incluso daños. Más fases y mejor diseño VRM permiten repartir y enfriar mejor la corriente.

**3. ¿Qué consecuencias tendría instalar una CPU moderna de alto rendimiento en una placa base con VRM básico y sin disipadores?**
- Aunque físicamente sea compatible, la CPU sufriría caídas de voltaje bajo carga, podría sobrecalentarse y se reduciría su vida útil o el sistema sería inestable. Así, el rendimiento real nunca alcanzará el esperado.

**4. ¿Cómo afecta la integración de los "carriles PCIe de la CPU" respecto a los del chipset en el rendimiento de un SSD NVMe ultra rápido?**
- Usar los carriles de la CPU reduce la latencia porque la conexión va directa, sin pasar por el chipset (PCH), que es un "embudo" compartido por otros dispositivos. Los dispositivos conectados al chipset comparten el ancho de banda y pueden sufrir cuellos de botella en uso intensivo.

**5. Si tienes un SSD NVMe Gen4 y dos ranuras M.2 en la placa, una conectada a la CPU (PCIe 4.0 x4) y otra al chipset (PCIe 4.0 x4), ¿dónde lo instalarías para máxima velocidad? ¿Por qué?**
- En la ranura conectada a la CPU: recibiría los datos sin intermediarios ni compartir ancho de banda, minimizando latencia y maximizando transferencia. El chipset añade retrasos y comparte recursos con otros dispositivos.

**6. ¿Para qué situaciones reales resulta crítico saber cuántas líneas PCIe directas ofrece la CPU?**
- Cuando planeas instalar varias GPUs, SSDs NVMe de alto rendimiento o tarjetas de captura profesionales, puedes saturar los carriles de la CPU. Conocer los límites evita cuellos de botella o incompatibilidades.

**7. ¿Por qué los factores de forma pequeños como Mini-ITX no pueden alimentar CPUs de muy alta gama de forma estable?**
- El área limitada implica espacio reducido para VRMs y disipadores grandes. Esto limita la cantidad de fases de potencia y la capacidad de refrigeración, que no sería suficiente para mantener estables CPUs que consumen mucha energía.

**8. Si compras una placa base con solo 4 fases VRM y tu CPU requiere mucha potencia sostenida, ¿qué problemas prácticos puedes encontrar incluso si el sistema "funciona"?**
- Las fases trabajarán al límite, se calentarán mucho y la CPU puede experimentar caídas de rendimiento (throttling) o reinicios bajo carga intensa por falta de energía estable.

**9. ¿Por qué un profesional que busca un equipo para edición de vídeo elegiría un chipset de gama alta (ej. Z790/X670E) y no de gama media (B760/B650)?**
- Porque tendrá más líneas PCIe, más puertos USB de alta velocidad, soporte completo para overclocking y mayor capacidad de expansión para tarjetas de captura y almacenamiento ultrarrápido, fundamentales en edición profesional.

**10. Explica el razonamiento de por qué el formato ATX suele ser el estándar para PCs de alto rendimiento y servidores domésticos.**
- Permite instalar múltiples tarjetas de expansión, RAM y sistemas de refrigeración robustos. Su tamaño facilita disipadores grandes y VRMs de calidad, otorgando estabilidad y flexibilidad para ampliaciones futuras.

## CPU y RAM

**11. Si el cuello de botella de tu PC es el acceso a memoria y no la potencia "pura" de la CPU, ¿por qué puede ser preferible invertir en RAM más rápida o en arquitectura Dual Channel?**
- Porque una CPU rápida solo es útil si recibe los datos a tiempo. Una RAM lenta obliga a la CPU a esperar, desaprovechando su potencial. El Dual Channel dobla el ancho de banda disponible para memoria y reduce los atascos.

**12. Supón que tienes un procesador con 8 núcleos pero solo ejecutas programas de ofimática y navegación web. ¿Qué limitación percibirás y por qué?**
- La mayoría de programas de ese tipo solo usan uno o dos núcleos, por lo que el "exceso" de núcleos no se aprovecha. Tendrás capacidad sobrante, pero la mejora perceptible la marcará la velocidad/turbo de un solo núcleo y la agilidad de acceso a disco/RAM.

**13. ¿Por qué la arquitectura basada en chiplets en CPUs actuales (AMD, Apple) mejora la eficiencia de fabricación y el rendimiento?**
- Fabricar varios chips pequeños (chiplets) reduce costos y fallos de producción respecto a hacer un único chip grande. Además, cada chiplet puede fabricarse en el proceso más adecuado (uno en 4 nm, otro en 6 nm), optimizando coste y funcionalidades.

**14. Si comparas dos CPUs con igual número de núcleos pero una tiene 96MB de L3 y la otra 12MB, ¿cómo influirá esto en tareas como edición de vídeo o gaming pesado?**
- Una L3 más grande permite guardar más datos "calientes", minimizando el acceso a RAM lenta. En gaming y edición, donde se repiten muchos accesos a los mismos datos, la mayor caché reduce la latencia y mejora el rendimiento.

**15. ¿Cómo puede una NPU integrada en el chip ser una ventaja competitiva si quieres desarrollar aplicaciones con IA en local?**
- La NPU está optimizada para operaciones de inteligencia artificial y aprendizaje automático, lo que permite ejecutar tareas de IA (como reconocimiento de voz, imagen o asistentes) de modo rápido y eficiente, descargando a la CPU y ahorrando energía.

**16. ¿Por qué sistemas con RAM DDR5 y CPU moderna suelen ser preferibles pensando en largo plazo, aunque sean ahora más caras?**
- DDR5 tiene mayor ancho de banda y eficiencia energética, soporta módulos mayores y duplicación de subcanales. Garantiza compatibilidad con futuras actualizaciones y mejor rendimiento con gráficas integradas (iGPU) y cargas multicore.

**17. Imagina que tienes 32GB de RAM pero mala configuración de canales (todo en un solo canal). ¿Qué impacto tendrá para tareas gráficas con iGPU y por qué?**
- Las iGPU usan la RAM como VRAM. Si está en Single Channel, el ancho de banda se reduce mucho, provocando limitaciones de velocidad gráfica y caída de FPS en juegos y edición, pese a tener mucha RAM.

**18. Si montas un procesador Intel de 14ª generación en LGA1700 y quieres hacer overclocking, ¿por qué la elección del chipset importa más que la calidad de la placa en sí?**
- Porque solo los chipsets de gama alta (Z790) habilitan el overclocking de CPU. Aunque la placa tenga buen VRM, si su chipset (ej. B760) no lo permite, la BIOS no dejará modificar los parámetros principales y no aprovecharás el potencial extra del chip.

**19. Razona por qué elegir una CPU con una iGPU decente puede ser inteligente incluso para PCs de escritorio que posteriormente recibirán GPU dedicada.**
- Permite usar el PC mientras esperas la gráfica, reduce problemas iniciales de compatibilidad y limita el impacto si la GPU dedicada falla. Además, facilita diagnosis de averías y consume menos energía para tareas habituales.

**20. Si una empresa quiere PCs rápidos y duraderos para ofimática, ¿por qué priorizar frecuencias turbo estables y buena caché L3 en la CPU en vez de núcleos extra?**
- Ofimática rara vez paraleliza tareas. El rendimiento "fluido" depende de la agilidad de un solo núcleo y la disponibilidad rápida de datos frecuentes, por lo que la frecuencia alta (turbo) y la caché L3 serán lo más determinante.

## Almacenamiento

**21. Razona por qué un SSD NVMe basado en protocolo PCIe es mucho más ágil que un SSD SATA, incluso cuando ambos usan tecnología flash NAND.**
- El bus PCIe tiene mucho mayor ancho de banda y menor latencia que SATA. Además, el protocolo NVMe está diseñado para aprovechar el paralelismo interno de la flash NAND, gestionando cientos de miles de colas de datos, frente a la única de SATA/AHCI.

**22. Si tienes la opción entre dos SSD NVMe: uno conecta por PCIe a la CPU y otro por el chipset, ¿cuándo notarás más la diferencia?**
- En cargas muy intensivas o simultáneas (muchas transferencias, bases de datos, edición de vídeo pesada). El SSD conectado a la CPU mantendrá menor latencia y no competirá por el bus con otros dispositivos, mientras el que depende del chipset puede sufrir atascos si otros puertos (USB, SATA) están siendo usados al mismo tiempo.

**23. Explica cómo la evolución de SATA/PATA a PCIe/NVMe ha permitido que el almacenamiento deje de ser el mayor cuello de botella en los PCs modernos.**
- SATA (y antes PATA) era una interfaz lenta y un protocolo poco paralelo, útil para discos mecánicos. PCIe/NVMe multiplica el ancho de banda y reduce la latencia porque conecta los SSDs directamente a la CPU, eliminando intermediarios y explotando la arquitectura flash.

**24. Cuando elegirías todavía un HDD clásico para un nuevo sistema actual, pese a las ventajas del SSD. Razona tu respuesta.**
- Para almacenar grandes volúmenes de datos "fríos" (archivos raramente usados, copias de seguridad, vídeos, fotos). Los HDDs ofrecen coste por terabyte imbatible. Para el sistema y tareas activas siempre debe usarse SSD.

**25. Si tu SSD NVMe funciona a velocidades anormalmente bajas, ¿qué posibles causas relacionadas con la placa base deberías investigar?**
- Si el SSD está conectado a una ranura solo cableada para SATA, si comparte bus con muchos otros dispositivos (chipset saturado), versión del firmware, o si el disipador no está bien instalado, pues el thermal throttling puede reducir la velocidad. Igualmente, comprobar el soporte del bus PCIe: Gen3, Gen4, Gen5…

**26. ¿Por qué en la práctica un HDD rara vez alcanza su ancho de banda máximo teórico durante el uso normal?**
- El acceso es principalmente aleatorio, implicando muchos movimientos de los cabezales y esperas de rotación, lo que reduce el rendimiento real respecto al óptimo de transferencias secuenciales grandes en el borde externo del plato.

**27. Imagina que quieres aprovechar al máximo la vida útil de un SSD QLC. ¿Qué estrategias razonadas aplicarías?**
- Limitar la escritura repetitiva (descargas, archivos temporales, swap), dejar activado TRIM, activar el "overprovisioning" si el SSD lo permite, y mantenerlo siempre con espacio libre para facilitar la gestión de celdas usadas y la nivelación de desgaste.

**28. ¿Por qué la diferencia entre SLC, TLC, QLC o PLC en un SSD importa para ciertas aplicaciones y es irrelevante en otras?**
- SLC es más duradero y rápido pero caro; QLC almacena más datos pero soporta menos ciclos de escritura. En servidores de bases de datos (muchas escrituras) usar QLC es riesgoso. Para almacenamiento en frío (copias de seguridad, uso ocasional) el bajo coste de QLC supera el problema de poca durabilidad.

**29. Piensa en una situación donde un SSD "sin caché de DRAM" (DRAM-less) se comportará peor que uno con ella. Razona el porqué.**
- Cuando se accede mucho y simultáneamente a pequeños archivos, el SSD DRAM-less tarda más en encontrar y gestionar los bloques de datos, porque carece de un mapa de ubicación ultrarrápido. Notarás mucho lag en instalaciones y en sistemas multitarea intensos.

**30. Explica por qué la protección contra sobrevoltajes de una fuente de alimentación no solo protege a la propia fuente sino a todos los componentes del PC.**
- Si entra un pico de voltaje, la protección detiene la alimentación antes de que el exceso destruya placas, CPU, RAM, GPU y SSDs. Sin protección, el sobrevoltaje puede causar cortocircuitos y daños fatales e irreparables.

## Pruebas de razonamiento real sobre configuraciones

**31. Si configuras un PC para juegos con presupuesto limitado, ¿por qué puede ser racional ahorrar en CPU/placa y gastar más en GPU?**
- Los juegos modernos dependen sobre todo de la potencia de la GPU. Una CPU decente bastará para no generar cuello de botella, pero invertir más en GPU maximiza los FPS y el detalle gráfico. Es lógica de equilibrio coste-beneficio.

**32. Un cliente pide un PC para edición de vídeo profesional 4K. Entre elegir 64GB de RAM a velocidad base o 32GB de RAM rápida en Dual Channel, ¿qué opción puede ser preferible y por qué?**
- Si el software utiliza mucho "caché" de RAM y trabaja con archivos muy grandes, prioriza cantidad. Si el flujo de trabajo es multitarea y los datos son menos voluminosos pero accedidos en pequeños bloques, prioriza velocidad y doble canal.

**33. En una pequeña empresa, ¿por qué podría preferirse un SSD SATA en vez de NVMe para los PCs de norma?**
- Un SSD SATA ya es infinitamente más rápido que un HDD para tareas de ofimática y supone menor coste, mayor compatibilidad y menor calor. El NVMe aporta ventajas, pero en varios PCs estándar, el coste extra no está justificado.

**34. ¿Qué razonamiento justifica el uso de fuentes de alimentación "full-modular" en un entorno profesional de mantenimiento de PCs?**
- Facilitan la gestión de cables, reducen tiempo de instalación/reparación, mejoran el flujo de aire y permiten cambiar rápidamente el cableado si hay fallos o se personaliza el equipo.

**35. Si se plantea actualizar un portátil de RAM DDR3 a DDR5, ¿qué aspectos razonados demostrarían la inviabilidad de la actualización?**
- Los zócalos físicos y los voltajes no son compatibles. La placa base y el controlador de memoria de la CPU solo aceptan el estándar para el que fueron diseñados. No se trata solo de encajar el módulo; el sistema no lo reconoce ni puede usarlo.

**36. Si el fabricante de tu placa publica una actualización de firmware que "mejora la compatibilidad de RAM", ¿por qué puede ser conveniente actualizarlo antes de ampliar la memoria?**
- Un firmware antiguo puede no reconocer nuevos módulos o perfiles XMP modernos. Actualizar permite usar RAM más rápida/eficiente, evitando problemas de arranque o inestabilidad tras la ampliación.

**37. ¿Por qué los equipos para uso constante en servidores priorizan fuentes de "alta eficiencia" con certificación Gold o superior, aunque sean más caras?**
- Porque a largo plazo ahorran en consumo y generan menos calor, lo que reduce averías, gasto energético en refrigeración y bajas inesperadas. El retorno de la inversión se ve a lo largo del tiempo y la fiabilidad es crítica.

**38. Si te dan a elegir entre una fuente de alimentación con varios raíles +12V o solo uno pero de la misma potencia total, ¿cuándo preferirías la de único raíl y por qué?**
- Para equipos con GPUs muy potentes y alto consumo, un único raíl elimina el riesgo de sobrecargar uno solo de los raíles múltiples. Así, toda la potencia está disponible para cualquier componente que la necesite.

**39. Un disco duro antiguo hace un "clic" repetitivo y no arranca. ¿Por qué un técnico avispado sospecharía un head crash y cómo evitaría que el desastre empeore?**
- El "clic" suele indicar que el cabezal intenta reutilizar la posición pero encuentra fallos físicos (head crash). Apagar inmediatamente el equipo para evitar que los residuos del daño físico se propaguen y buscar recuperación profesional.

**40. Un cliente quiere conectar un SSD SATA moderno a una placa antigua solo con PATA/IDE. Explica de forma razonada por qué no funcionará y qué alternativas existen.**
- Los conectores y protocolos son incompatibles: los SATA utilizan conexiones y comunicaciones diferentes a las de los antiguos PATA. La única opción es usar un adaptador activo (con conversor de señal), aunque esta solución suele limitar el rendimiento.

## Razonamiento aplicado a la evaluación técnica y auditoría

**41. Si, tras ejecutar un benchmark de CPU, la temperatura máxima reportada supera la especificación del fabricante, ¿por qué es racional posponer cualquier ampliación hasta mejorar la refrigeración actual?**
- Una CPU que trabaja al límite térmico sufrirá "thermal throttling" y acortará su vida útil. Una ampliación sin solventar el problema solo agravaría la situación y podría dañar componentes costosos.

**42. En una auditoría de hardware, descubres que un PC de oficina tiene la RAM configurada fuera de Dual Channel. El usuario se queja de lentitud al abrir varios documentos a la vez. ¿Por qué sospechas que esa es la causa y cómo lo solucionarías?**
- Sin Dual Channel, el ancho de banda se reduce a la mitad, por lo que el acceso simultáneo a varios archivos es mucho más lento. Solución: instalar los módulos en los zócalos recomendados por el fabricante para activar Dual Channel.

**43. Analizando el "inventario" de un equipo con CPU compatible hasta Ryzen 7 5800X3D, descubres que el uso principal es modelado 3D. ¿Por qué sugerir esa CPU en vez de más RAM, incluso si hay solo 16GB?**
- Para modelado 3D, el rendimiento puro del procesador y la gran caché L3 mejoran la gestión de escenas complejas y el renderizado. Si el trabajo no suele llegar al tope de RAM, invertir en mejor CPU ofrece más ganancia.

**44. Si en el análisis decides ampliar de SSD SATA a NVMe, ¿qué consideraciones hardware y software deberás tener en cuenta antes del cambio?**
- Comprobar que la placa soporta NVMe por PCIe, qué ranura es la ideal, si puedes migrar/instalar el sistema operativo ahí y si necesitas disipadores para evitar el "thermal throttling" típico de los SSDs NVMe rápidos.

**45. Has evaluado la fuente de alimentación y ves que no tiene protección OVP, SCP u OTP. ¿Por qué recomendarías cambiar de fuente aunque la actual funcione?**
- La seguridad de los componentes es prioritaria. Ante cualquier pico de tensión, cortocircuito o sobrecalentamiento, la fuente sin protecciones puede destruir placas, discos, CPU y GPU en una sola avería.

**46. Si detectas que la RAM instalada es mayor que la soportada por el sistema operativo (ej. 32GB en Windows 10 Home 32 bits), ¿cómo razonarías el abordaje del problema?**
- Un SO de 32 bits sólo puede usar hasta 4GB de RAM, así que aunque haya más instalada, el resto es invisible y desaprovechado. La única solución real es actualizar a un SO de 64 bit.

**47. Tras medir el rendimiento (IOPS) de dos SSDs NVMe en diferentes ranuras, uno tiene la mitad de IOPS que el otro. ¿Por qué podrías deducir un problema de configuración de líneas PCIe?**
- Es posible que la segunda ranura esté conectada al chipset, comparta bus con otros dispositivos o esté limitada a una generación anterior de PCIe (Gen3 vs Gen4). Revisar la documentación y configurar correctamente las ranuras es clave.

**48. Si un PC antiguo da errores al intentar instalar Windows 11 por "falta de soporte UEFI", ¿por qué este requisito no es trivial?**
- UEFI reemplaza BIOS para soportar discos de más de 2.2TB, seguridad de arranque (Secure Boot), y nuevas tecnologías de memoria. Sin UEFI, no solo es imposible instalar Windows 11, sino que el sistema es menos seguro y compatible.

**49. ¿Cómo justificarías ante un cliente que, aunque un HDD tiene "más terabytes", el SSD es irrenunciable como unidad de sistema?**
- El HDD no puede competir en velocidad de arranque, apertura de programas ni fluidez general. El SSD garantiza experiencia ágil y moderna; el HDD debe usarse solo como almacén de datos secundarios.



[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/138042210/b5efe66f-3e80-47f6-9a52-c3d117876e5b/01_PlacaBase.pdf)
[2](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/138042210/7b6ed538-1281-4291-86d9-ca69460afc6c/03_EsquemaResumenCPU_RAM.pdf)
[3](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/138042210/52c1fb5c-ecff-41eb-9460-ecac2349e297/04_SistemasDeAlmacenamiento.pdf)
[4](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/138042210/11074aad-1db1-40fb-86dd-c5c94a73fc71/FuentesDeAlimentacion.pdf)
[5](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/138042210/e10c9cc7-fcbf-4374-b837-8bdfe84970d9/EjerciciosDeHardwarev2.pdf)
[6](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/138042210/86bc268a-eed4-4173-a3a6-7915cb96fd5e/02_Ram_CPU.pdf)