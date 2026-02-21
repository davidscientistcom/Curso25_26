## BLOQUE 1 — Historia de las Redes Neuronales

**1. ¿Cuándo y quiénes propusieron el primer modelo matemático de neurona artificial?**
En 1943, Warren McCulloch y Walter Pitts propusieron el primer modelo matemático de neuronas artificiales, inspirado en el funcionamiento del cerebro humano y basado en la lógica. 

**2. ¿Quién desarrolló el perceptrón y en qué año?**
Frank Rosenblatt desarrolló el perceptrón en 1958, como una neurona artificial capaz de realizar tareas de clasificación aprendiendo a ajustar sus pesos. 

**3. ¿Cuál era la limitación fundamental del perceptrón original de Rosenblatt?**
Solo podía resolver problemas linealmente separables. Si los datos no podían dividirse con una línea (o hiperplano), el perceptrón era incapaz de encontrar una solución. 

**4. ¿Qué publicaron Minsky y Papert en 1969 y qué consecuencias tuvo?**
Publicaron el libro *Perceptrons*, donde demostraban que el perceptrón no podía resolver problemas complejos como el XOR. Esto provocó una pausa en la investigación conocida como el "invierno de las redes neuronales". 

**5. ¿Qué es el "invierno de las redes neuronales"?**
Es la etapa de los años 70 en que la investigación en redes neuronales quedó prácticamente paralizada tras las críticas de Minsky y Papert, y el foco de la IA se desvió hacia sistemas basados en reglas. 

**6. ¿Cuáles son las tres partes principales de una neurona biológica?**
Las dendritas (reciben señales de otras neuronas), el soma (procesa las señales y dispara el impulso si superan un umbral) y el axón (transmite el impulso hacia otras neuronas). 

**7. ¿Cómo emula el perceptrón el funcionamiento de una neurona biológica?**
Las dendritas equivalen a las entradas, el soma al cálculo de la suma ponderada, y el axón a la salida. Si la suma supera el umbral, la neurona artificial "dispara" produciendo una salida de 1. 

**8. ¿Qué es un problema linealmente separable?**
Es aquel en que las clases de datos pueden dividirse mediante una línea recta (en 2D) o un hiperplano (en N dimensiones). Las compuertas AND y OR son ejemplos de problemas linealmente separables. 

**9. ¿Qué es un problema no linealmente separable?**
Es aquel en que no existe ninguna línea o plano capaz de separar correctamente las clases. El ejemplo clásico es la compuerta XOR. 

**10. ¿Cuál es la fórmula matemática general del perceptrón?**
\[ y = f\left(\sum_{i=1}^{n} w_i x_i + b\right) \]
Donde \(x_i\) son las entradas, \(w_i\) los pesos, \(b\) el bias y \(f\) la función de activación. 



## BLOQUE 2 — El Perceptrón Simple

**11. ¿Qué es la suma ponderada en el perceptrón?**
Es la combinación lineal de las entradas multiplicadas por sus pesos, más el bias:
\[ z = w_1 x_1 + w_2 x_2 + \ldots + w_n x_n + b \]
Es el valor que se pasa a la función de activación para producir la salida. 

**12. ¿Qué es el bias y por qué es importante?**
El bias es un valor constante que desplaza el umbral de activación. Sin él, la frontera de decisión estaría forzada a pasar por el origen, lo que limitaría la capacidad de clasificación del modelo. Equivale a una entrada adicional de valor 1 con peso \(w_0\). 

**13. ¿Qué es la función de activación escalón (Heaviside)?**
Es la función que convierte la suma ponderada en una salida binaria:
\[ f(z) = \begin{cases} 1 & \text{si } z > 0 \\ 0 & \text{si } z \leq 0 \end{cases} \]
Determina si la neurona "se activa" o no. 

**14. ¿En qué consiste la regla de aprendizaje del perceptrón?**
Consiste en ajustar los pesos cuando hay error entre la salida obtenida y la deseada:
\[ w_i = w_i + \eta \cdot (y_{\text{deseado}} - y_{\text{obtenido}}) \cdot x_i \]
Si la predicción es correcta, los pesos no cambian. 

**15. ¿Qué es la tasa de aprendizaje (η)?**
Es un hiperparámetro que controla la magnitud de los ajustes de los pesos. Si es muy alta, el entrenamiento es inestable; si es muy baja, la convergencia es muy lenta. 

**16. ¿Qué garantiza el teorema de convergencia del perceptrón?**
Que si los datos son linealmente separables, el algoritmo del perceptrón encontrará una solución correcta en un número finito de iteraciones. 

**17. ¿Cuáles son los criterios de parada del entrenamiento del perceptrón?**
1. Error cero (clasifica correctamente todos los ejemplos).
2. Número máximo de iteraciones alcanzado.
3. Cambios insignificantes en los pesos entre iteraciones. 

**18. ¿Qué tipo de aprendizaje usa el perceptrón?**
Aprendizaje supervisado, ya que se entrena con ejemplos etiquetados (entradas con su salida deseada conocida). 

**19. ¿Qué hace la compuerta lógica AND?**
Devuelve 1 solo cuando ambas entradas son 1; en cualquier otro caso devuelve 0. Es un problema linealmente separable que el perceptrón puede resolver. 

**20. ¿Qué hace la compuerta lógica OR?**
Devuelve 1 si al menos una de las dos entradas es 1. También es linealmente separable y puede resolverse con un perceptrón simple. 

**21. ¿Por qué el perceptrón simple no puede resolver la compuerta XOR?**
Porque el XOR no es linealmente separable: no existe ninguna línea recta que separe correctamente los casos verdaderos de los falsos. El perceptrón solo puede trazar fronteras lineales. 

**22. ¿Por qué es crucial normalizar los datos de entrada del perceptrón?**
Porque si las características tienen magnitudes muy diferentes, el proceso de aprendizaje puede ser más difícil e inestable, ya que los pesos se ajustarán de forma desproporcionada. 

**23. ¿En qué caso el perceptrón NO ajusta sus pesos?**
Cuando la predicción coincide con la salida deseada, es decir, cuando el error es cero. El ajuste de pesos solo ocurre cuando hay error. 

**24. ¿Qué ocurre si la entrada \(x_i\) es 0 durante el ajuste de pesos?**
El peso correspondiente no se modifica, ya que el ajuste es \(\Delta w_i = \eta \cdot \text{error} \cdot x_i = 0\). Esto se puede verificar en el notebook de código. 

**25. ¿Para qué tipo de tareas es adecuado el perceptrón simple?**
Exclusivamente para tareas de clasificación binaria con datos linealmente separables. Para problemas no lineales se necesitan redes más complejas como el MLP. 



##  BLOQUE 3 — El Perceptrón Multicapa (MLP)

**26. ¿Qué es el Perceptrón Multicapa (MLP)?**
Es una extensión del perceptrón simple que incorpora una o más capas ocultas entre la capa de entrada y la de salida, permitiendo aprender relaciones no lineales complejas. 

**27. ¿Cuáles son las tres capas de un MLP?**
1. **Capa de entrada**: recibe los datos; cada nodo representa una característica.
2. **Capas ocultas**: procesan y transforman los datos de forma no lineal.
3. **Capa de salida**: genera la predicción final. 

**28. ¿Qué es la arquitectura "totalmente conectada" del MLP?**
Significa que cada neurona de una capa está conectada con todas las neuronas de la capa siguiente, formando una red densa sin omisiones. 

**29. ¿Cuántas neuronas tiene la capa de salida según el tipo de problema?**
Una neurona para problemas de regresión o clasificación binaria; múltiples neuronas para problemas de clasificación multiclase. 

**30. ¿Qué es la propagación hacia adelante (forward propagation)?**
Es el proceso de calcular las salidas de cada neurona desde la capa de entrada hasta la de salida. Para cada capa \(l\) se calcula:
\[ z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}, \quad a^{(l)} = f(z^{(l)}) \]  

**31. ¿Por qué las funciones de activación son necesarias en el MLP?**
Introducen no linealidad en la red. Sin ellas, el MLP sería equivalente a un simple perceptrón lineal, incapaz de aprender relaciones complejas. 

**32. ¿Cuál es la fórmula de la función sigmoide y cuándo es útil?**
\[ \sigma(z) = \frac{1}{1 + e^{-z}} \]
Produce salidas en el rango (0, 1), útiles para interpretar probabilidades. Tiene el inconveniente del vanishing gradient en redes profundas. 

**33. ¿Qué es la función tanh y en qué se diferencia de la sigmoide?**
\[ \tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}} \]
Produce salidas en (−1, 1), está centrada en cero y tiene gradientes más fuertes que la sigmoide, aunque también sufre vanishing gradient. 

**34. ¿Qué es ReLU y cuál es su ventaja principal?**
ReLU (Rectified Linear Unit): \(\text{ReLU}(z) = \max(0, z)\). Es simple, computacionalmente eficiente y mitiga el problema del vanishing gradient. Su desventaja: neuronas que siempre reciben entrada negativa pueden "morir". 

**35. ¿Qué es el problema del gradiente difuminado (vanishing gradient)?**
Ocurre en redes profundas cuando los gradientes se vuelven tan pequeños durante el backpropagation que los pesos de las capas iniciales casi no se actualizan, dificultando el aprendizaje. 

**36. ¿Por qué el MLP sí puede resolver el problema XOR?**
Porque las capas ocultas con funciones de activación no lineales permiten transformar el espacio de entrada en uno donde los datos sí son linealmente separables. 

**37. ¿Cuántas neuronas necesita el MLP para resolver el XOR según el ejemplo?**
2 neuronas de entrada, 2 neuronas en la capa oculta (con activación sigmoide) y 1 neurona de salida. 

**38. ¿Qué es el descenso por gradiente?**
Es el algoritmo de optimización que ajusta iterativamente los pesos y biases del MLP en la dirección que minimiza la función de pérdida, usando los gradientes calculados mediante backpropagation. 

**39. ¿Qué es el backpropagation?**
Es la técnica que calcula eficientemente los gradientes de la función de pérdida respecto a cada peso de la red, propagando el error desde la capa de salida hacia las capas anteriores. 

**40. ¿Cómo se obtienen los pesos finales en un MLP real (no en un ejemplo preajustado)?**
Se obtienen a través del entrenamiento: el MLP comienza con pesos aleatorios y los ajusta iterativamente usando backpropagation y descenso por gradiente hasta minimizar el error. 



##  BLOQUE 4 — Código del Perceptrón (Notebook)

**41. ¿En cuántas épocas convergió el perceptrón para la compuerta AND en el notebook?**
El perceptrón para la compuerta AND convergió en la **época 10**, alcanzando error total cero. 

**42. ¿Qué observamos en el entrenamiento del perceptrón para XOR según el notebook?**
El error nunca llega a cero; el perceptrón oscila constantemente con errores de 3 o 4 en cada época, confirmando que el XOR no es resoluble con un perceptrón simple. 

**43. ¿Qué hace la función `funcion_activacion(suma_ponderada)` en el código?**
Implementa la función escalón: retorna 1 si la suma ponderada es positiva, y 0 en cualquier otro caso. 

**44. ¿Cómo se calcula el ajuste de un peso en el código del perceptrón?**
Mediante la fórmula: `Δw_i = η * error * x_i`, donde `η` es la tasa de aprendizaje (0.1), `error` es la diferencia entre la salida deseada y la obtenida, y `x_i` la entrada correspondiente. 

**45. ¿Qué parámetros iniciales aleatorios usa el perceptrón en el código?**
Los pesos se inicializan con valores aleatorios en el rango `[-1, 1]` usando `random.uniform(-1, 1)`, y el bias también se inicializa aleatoriamente en el mismo rango. 



##  BLOQUE 5 — Big Data: Unidad 1

**46. ¿Qué es Big Data?**
Se refiere a conjuntos de datos cuyo tamaño, velocidad de generación o complejidad superan la capacidad de las herramientas tradicionales de procesamiento. Implica la necesidad de nuevos paradigmas, arquitecturas y perfiles profesionales. 

**47. ¿Qué es la Pirámide DIKW?**
Es un modelo jerárquico con cuatro niveles: **Datos** (hechos crudos sin contexto), **Información** (datos organizados con contexto), **Conocimiento** (interpretación de patrones) y **Sabiduría** (conocimiento aplicado para tomar decisiones óptimas). 

**48. ¿Cuáles son las 5 Vs del Big Data?**
1. **Volumen** (cantidad de datos)
2. **Velocidad** (ritmo de generación)
3. **Variedad** (diversidad de tipos)
4. **Veracidad** (calidad y fiabilidad)
5. **Valor** (utilidad para el negocio) 

**49. ¿Qué es el Volumen en Big Data? Da un ejemplo.**
Se refiere a la inmensa cantidad de datos generados. Ejemplo: Walmart importa más de 2,5 petabytes de datos por hora desde sus más de 10.500 tiendas en 24 países. 

**50. ¿Qué es la Velocidad en Big Data? Da un ejemplo.**
Es el ritmo al que se generan y deben procesarse los datos. Ejemplo: los sistemas de detección de fraude con tarjetas analizan millones de transacciones en milisegundos para bloquear compras fraudulentas. 

**51. ¿Qué es la Variedad en Big Data y cuáles son sus tres categorías de datos?**
Describe la diversidad de formatos. Las categorías son:
- **Estructurados**: tablas, bases de datos relacionales.
- **No estructurados**: texto libre, imágenes, vídeos.
- **Semiestructurados**: JSON, XML. 

**52. ¿Qué es la Veracidad en Big Data?**
Se refiere a la calidad, precisión y fiabilidad de los datos. Los datos reales son "sucios": contienen errores, sesgos, valores ausentes e inconsistencias que pueden llevar a decisiones incorrectas. 

**53. ¿Qué es el Valor en Big Data?**
Es la capacidad de transformar los datos en conocimientos accionables que generen beneficio tangible. Ejemplo: el sistema de recomendación de Netflix ahorra más de 1.000 millones de dólares al año en retención de clientes. 

**54. ¿Cuáles son las fases del ciclo de vida de los datos?**
1. Generación y captura
2. Ingesta y almacenamiento
3. Procesamiento (ETL/ELT)
4. Análisis
5. Visualización y consumo
6. Gobernanza, ética y destrucción 

**55. ¿Qué diferencia hay entre ingesta por lotes (batch) y en tiempo real (streaming)?**
La ingesta batch recopila y procesa datos en grandes bloques a intervalos programados; la streaming procesa los datos continuamente a medida que se generan, en tiempo real. 

**56. ¿Qué es un Data Warehouse?**
Es un sistema centralizado optimizado para datos estructurados y limpios. Usa esquema en la escritura (schema-on-write) y ETL. Es ideal para Business Intelligence, informes corporativos y análisis histórico. 

**57. ¿Qué es un Data Lake?**
Es un repositorio masivo de bajo coste que almacena datos en su formato nativo (estructurados, semiestructurados y no estructurados). Usa esquema en la lectura (schema-on-read) y ELT. Ideal para ciencia de datos exploratoria y machine learning. 

**58. ¿Qué es un Data Lakehouse?**
Es una arquitectura híbrida que combina la flexibilidad del Data Lake con las capacidades de gestión y transacciones ACID del Data Warehouse, sirviendo como plataforma única para BI, IA y machine learning. 

**59. ¿Qué es Apache Hadoop y cuáles son sus tres componentes principales?**
Es un framework open source para almacenamiento y procesamiento distribuido de grandes volúmenes de datos usando commodity hardware. Sus componentes son:
- **HDFS**: sistema de archivos distribuido.
- **MapReduce**: paradigma de procesamiento por lotes.
- **YARN**: gestor de recursos del clúster. 

**60. ¿Qué es HDFS y cómo garantiza la tolerancia a fallos?**
HDFS (Hadoop Distributed File System) divide los archivos en bloques (de 128 MB típicamente) y los replica en múltiples DataNodes (por defecto, 3 réplicas). El NameNode gestiona los metadatos. 

**61. ¿Cuáles son las limitaciones de MapReduce?**
- Dependencia intensiva del disco (alto I/O entre fases).
- Solo apto para procesamiento batch, no streaming.
- Muy ineficiente para algoritmos iterativos (como los de ML).
- Alta complejidad de programación con código repetitivo. 

**62. ¿Qué es Apache Spark y en qué supera a MapReduce?**
Es un motor de procesamiento distribuido que procesa los datos en memoria RAM, evitando el costoso I/O de disco. Puede ser hasta 100 veces más rápido que MapReduce y soporta batch, streaming, SQL y machine learning en un único framework unificado. 

**63. ¿Qué es ETL y qué es ELT?**
- **ETL** (Extract, Transform, Load): transforma los datos antes de cargarlos. Garantiza alta calidad pero es más rígido y lento. Típico de Data Warehouses.
- **ELT** (Extract, Load, Transform): carga primero los datos crudos y los transforma cuando se necesitan. Más flexible y rápido para la ingesta. Típico de Data Lakes. 

**64. ¿Qué es la Pirámide DIKW y cómo se relaciona con los roles del equipo de datos?**
El paso de Dato a Información es el dominio del Ingeniero de Datos; de Información a Conocimiento, del Analista y Científico de Datos; y el salto a Sabiduría es la responsabilidad de los líderes empresariales asesorados por el equipo. 

**65. ¿Qué es DataOps?**
Es un enfoque que aplica principios de DevOps al mundo de los datos, enfatizando la automatización, monitorización y bucles de retroalimentación continuos para acelerar la entrega de valor desde el dato crudo. 



##  BLOQUE 6— Fundamentos de Ciberseguridad

**66. ¿Qué es la ciberseguridad?**
Es la práctica de proteger sistemas, redes y programas de ataques digitales que tienen como objetivo acceder, cambiar o destruir información sensible, extorsionar a usuarios o interrumpir procesos de negocio. 

**67. ¿Cuáles son los tres pilares fundamentales de la seguridad de la información (tríada CIA)?**
1. **Confidencialidad**: solo usuarios autorizados acceden a la información.
2. **Integridad**: los datos no son alterados sin autorización.
3. **Disponibilidad**: la información es accesible cuando se necesita. 

**68. ¿Qué es el malware?**
Es software malicioso diseñado para dañar, explotar o comprometer sistemas. Incluye virus, troyanos, spyware y, como caso especial, el ransomware. 

**69. ¿Qué es el ransomware?**
Es un tipo de malware que cifra los archivos de la víctima y exige un rescate económico para restaurar el acceso a los datos. Es una de las amenazas más impactantes en la actualidad. 

**70. ¿Qué es el phishing?**
Es una técnica de ingeniería social que engaña a los usuarios mediante correos, mensajes o sitios web falsos para robar credenciales, datos bancarios u otra información sensible. 

**71.  ¿Qué es un ataque DDoS?**
DDoS (Distributed Denial of Service) consiste en saturar un sistema o servidor con tráfico masivo procedente de múltiples fuentes para dejarlo inoperativo e inaccesible para usuarios legítimos. 

**72.  ¿Qué es el modelo Zero Trust?**
Es un modelo de seguridad basado en el principio "Nunca confíes, siempre verifica": ningún usuario, dispositivo o sistema es considerado confiable por defecto, independientemente de si está dentro o fuera de la red corporativa. 

**73.  ¿Qué es la autenticación multifactor (MFA)?**
Es un mecanismo que requiere múltiples formas de verificación para acceder a un sistema: algo que sabes (contraseña, PIN), algo que tienes (token, móvil) y algo que eres (huella, rostro, iris). 

**74.  ¿Qué es la regla 3-2-1 de copias de seguridad?**
Consiste en mantener 3 copias de los datos, almacenadas en 2 tipos de medios diferentes, con 1 copia ubicada fuera de las instalaciones (offsite) para protección ante desastres. 

**75.  ¿Qué son SIEM y SOC?**
- **SIEM** (Security Information and Event Management): sistema que recopila y analiza eventos de seguridad en tiempo real para detectar amenazas.
- **SOC** (Security Operations Center): centro operativo de seguridad donde equipos especializados monitorizan y responden a incidentes. 


> 📌 **Total: 70 preguntas y respuestas** (con 5 bonus adicionales) cubriendo todos los archivos: Historia de RNs, Perceptrón Simple, Código del Perceptrón, Perceptrón Multicapa, Big Data Unidad 1  y Fundamentos de Ciberseguridad. Puedes pedir que amplíe algún bloque, reformule las preguntas, o genere un quiz interactivo con estas preguntas. 
>
> Aquí tienes las **20 preguntas y respuestas adicionales de Ciberseguridad**, con numeración continuada desde el bloque anterior:



## BLOQUE 6 — Ciberseguridad (Ampliación)

**76. ¿Cuál es la nueva frontera del cibercrimen en 2026 según los materiales?**
Las plataformas de mensajería instantánea se han convertido en el principal vector de infección, ya que los atacantes las usan para distribuir malware, enlaces maliciosos y ataques de ingeniería social a gran escala. 

**77. ¿Qué son los deepfakes y por qué son una amenaza de ciberseguridad?**
Los deepfakes son contenidos audiovisuales falsos hiperrealistas creados mediante inteligencia artificial. Representan una amenaza porque pueden usarse para suplantar identidades, difundir desinformación, realizar fraudes y manipular a las víctimas en ataques dirigidos. 

**78. ¿Por qué se considera la identidad como la superficie de ataque dominante en 2026?**
Porque los atacantes priorizan el compromiso de credenciales de usuarios para moverse dentro de los sistemas sin necesidad de explotar vulnerabilidades técnicas complejas. El control de una identidad da acceso directo a recursos críticos. 

**79. ¿Qué es un ataque APT (Advanced Persistent Threat)?**
Son ataques prolongados y sigilosos llevados a cabo por grupos organizados, a menudo patrocinados por estados. Su objetivo es infiltrarse en sistemas de alto valor durante un largo periodo de tiempo sin ser detectados, para espionaje, sabotaje o robo de información. 

**80. ¿Qué es un ataque a la cadena de suministro (supply chain attack)?**
Consiste en comprometer a un proveedor o software de terceros de confianza para, a través de él, infectar simultáneamente a múltiples organizaciones que usan ese producto o servicio. El atacante entra por una puerta lateral ya validada. 

**81. ¿Por qué IoT y OT son superficies de ataque en expansión exponencial?**
Los dispositivos IoT (Internet de las Cosas) y OT (Tecnología Operacional) proliferan rápidamente pero suelen carecer de medidas de seguridad robustas, actualizaciones frecuentes y monitorización adecuada, convirtiéndose en puntos de entrada vulnerables para los atacantes. 

**82. ¿Qué es la ingeniería social en el contexto de la ciberseguridad?**
Es la manipulación psicológica de personas para que revelen información confidencial, ejecuten acciones perjudiciales o proporcionen acceso no autorizado a sistemas. No ataca la tecnología, sino el factor humano, que es el eslabón más débil. 

**83. ¿Qué son las vulnerabilidades de software y por qué son peligrosas?**
Son errores o debilidades en el código de una aplicación o sistema que pueden ser explotados por atacantes para tomar el control, robar datos o interrumpir servicios. Si no se parchean, permanecen abiertas indefinidamente. 

**84. ¿Qué riesgo representan las redes WiFi públicas sin cifrado?**
Son una puerta abierta para que los atacantes intercepten las comunicaciones (ataque man-in-the-middle), capturando credenciales, datos bancarios y cualquier información transmitida en texto claro entre el usuario y los servidores. 

**85. ¿Por qué no actualizar el software es considerado negligencia en ciberseguridad?**
Porque los parches de seguridad cierran vulnerabilidades conocidas. Un sistema desactualizado mantiene abiertas puertas que los atacantes ya conocen y pueden explotar de forma automatizada, sin necesidad de técnicas avanzadas. 

**86. ¿Qué es la defensa en profundidad (defensa en múltiples capas)?**
Es una estrategia de seguridad que consiste en implementar múltiples capas de controles y defensas (técnicas, físicas y humanas) de forma que si una capa falla, las siguientes contengan el ataque y limiten el daño. 

**87. ¿Qué es un firewall y cuál es su función?**
Es una barrera de seguridad que filtra el tráfico de red entrante y saliente según reglas predefinidas. Actúa como primer nivel de defensa, bloqueando comunicaciones no autorizadas entre redes de diferente nivel de confianza. 

**88. ¿En qué consiste el cifrado de información?**
Es el proceso de transformar datos legibles en un formato ilegible (texto cifrado) mediante algoritmos matemáticos, de modo que solo quien posea la clave correcta pueda descifrarlos y acceder a la información original. 

**89. ¿Qué son los sistemas IDS e IPS?**
- **IDS** (Intrusion Detection System): detecta actividades sospechosas o intrusiones en la red y genera alertas.
- **IPS** (Intrusion Prevention System): además de detectar, actúa de forma automática para bloquear o neutralizar la amenaza en tiempo real. 

**90. ¿Cuáles son los tres factores de autenticación en la MFA y a qué corresponden?**
1. **Algo que sabes**: contraseña o PIN.
2. **Algo que tienes**: token, móvil o tarjeta.
3. **Algo que eres**: huella dactilar, reconocimiento facial o iris (biometría). 

**91. ¿Cómo está transformando la IA a la ciberseguridad en 2026?**
La IA agéntica autónoma representa una revolución tanto para la defensa (detección automática de amenazas, respuesta en tiempo real) como para el ataque (automatización de intrusiones, generación de phishing personalizado y deepfakes). 

**92. ¿Qué es la segmentación de red y para qué sirve?**
Consiste en dividir la red corporativa en zonas aisladas (segmentos). Si un atacante compromete un segmento, la segmentación limita su movimiento lateral, impidiendo que se propague libremente por toda la infraestructura. 

**93. ¿Cuál es el principal desafío humano de la ciberseguridad a nivel mundial en 2026?**
Existe una brecha de talento crítica: hay millones de posiciones de ciberseguridad sin cubrir a nivel mundial, lo que deja a muchas organizaciones sin el personal especializado necesario para defender sus sistemas. 

**94. ¿Qué desafío regulatorio enfrentan las organizaciones en materia de ciberseguridad en 2026?**
Las regulaciones son cada vez más estrictas y costosas, obligando a las empresas a cumplir normativas de protección de datos, privacidad y reporte de incidentes, bajo pena de sanciones económicas significativas. 

**95. ¿Por qué se dice que "la ciberseguridad no es un destino, es un viaje continuo"?**
Porque las amenazas evolucionan constantemente y los atacantes siempre buscan nuevas técnicas y vectores de ataque. No existe un estado de seguridad permanente; la defensa requiere actualización, formación y adaptación continua. 

