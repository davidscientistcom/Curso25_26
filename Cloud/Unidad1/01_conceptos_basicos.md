# Capítulo 1. Introducción a la informática en la nube y AWS

## 1. Introducción a la informática en la nube

### 1.1 Definición

La **informática en la nube** (cloud computing) es un modelo de consumo de recursos tecnológicos que permite a los usuarios acceder a servicios de computación, almacenamiento, bases de datos, redes o aplicaciones directamente a través de Internet. Estos servicios se ofrecen bajo demanda y se facturan mediante un modelo de **pago por uso**, lo que significa que solo se paga por los recursos efectivamente utilizados.

Un ejemplo cotidiano puede ayudarnos a entenderlo: cuando usamos **Netflix** no compramos un servidor ni un sistema de almacenamiento para guardar las películas, simplemente accedemos al catálogo bajo demanda pagando una cuota. Del mismo modo, cuando una empresa utiliza la nube, no compra servidores físicos: consume potencia de cálculo, almacenamiento y otros servicios de forma flexible y escalable.

### 1.2 Infraestructura como software

En los modelos tradicionales, la **infraestructura se concibe como hardware**. Esto significa comprar servidores físicos, instalarlos en un CPD (Centro de Proceso de Datos), garantizar su refrigeración, seguridad física, suministro eléctrico, así como el personal encargado de gestionarlos. Todo ello implica:

* Una **inversión de capital inicial elevada**.
* **Largos ciclos de adquisición** de hardware (semanas o meses desde que se planifica hasta que llega el servidor).
* La necesidad de **prever la capacidad máxima** que se cree que la empresa necesitará en el futuro.

En contraposición, la nube permite ver la **infraestructura como software**. En lugar de depender de un servidor físico que hemos comprado, podemos crear servidores virtuales en minutos, crecer o reducir su capacidad según la carga de trabajo, y eliminar la infraestructura cuando ya no la necesitamos. Esto transforma la gestión de TI en algo mucho más **ágil, flexible y rentable**.

### 1.3 Comparación entre modelos

**Modelo tradicional (infraestructura como hardware):**

* Requiere espacio físico y personal.
* Altos costes iniciales.
* Riesgo de infrautilizar o sobrecargar la infraestructura.
* Escalabilidad lenta (semanas o meses para añadir recursos).

**Modelo en la nube (infraestructura como software):**

* Los recursos se despliegan en minutos.
* Escalabilidad casi inmediata.
* Pago únicamente por los recursos usados.
* Se eliminan muchas tareas pesadas: mantenimiento físico, parches de hardware, sustitución de piezas.

## 2. Modelos de servicio en la nube

Los servicios en la nube se agrupan en tres grandes modelos, que difieren en el nivel de control que tiene el cliente:

### 2.1 IaaS (Infrastructure as a Service)

La nube proporciona recursos básicos: máquinas virtuales, almacenamiento y redes. El cliente se encarga de instalar y gestionar el sistema operativo, las bases de datos y las aplicaciones.

**Ejemplo:** Amazon EC2 permite crear instancias de servidor con las características que necesitemos (CPU, memoria, disco). Nosotros decidimos qué sistema operativo instalar y cómo configurarlo.

### 2.2 PaaS (Platform as a Service)

Aquí el proveedor ofrece una plataforma lista para desplegar aplicaciones, sin que el cliente deba preocuparse por el sistema operativo o la infraestructura subyacente.

**Ejemplo:** AWS Elastic Beanstalk permite subir el código de una aplicación y la plataforma se encarga de desplegarla, escalarla y mantenerla.

### 2.3 SaaS (Software as a Service)

En este modelo, el cliente consume directamente aplicaciones completas que funcionan en la nube.

**Ejemplo:** Gmail o Microsoft 365. El usuario simplemente accede y utiliza el software, sin necesidad de instalar nada ni gestionar servidores.

### 2.4 Comparativa de control

* En **IaaS** el cliente tiene el mayor control sobre los recursos.
* En **PaaS** el control se reduce, pero aumenta la comodidad.
* En **SaaS** el control es mínimo, pero también lo es la carga de gestión.

## 3. Modelos de implementación de la nube

No todas las organizaciones consumen la nube de la misma manera. Existen distintos enfoques:

* **Nube pública**: servicios compartidos por muchos clientes, gestionados por un proveedor como AWS. Es el modelo más flexible y económico.
* **Nube privada**: la infraestructura está dedicada a una sola organización, ofreciendo más control y seguridad. Puede estar alojada en las instalaciones de la empresa o en un centro de datos externo.
* **Nube híbrida**: combina elementos de nube pública y privada, permitiendo mover cargas de trabajo entre ambos entornos según las necesidades.

## 4. Ventajas de la informática en la nube

### 4.1 Cambio de gastos de capital a gastos variables

En lugar de invertir millones en servidores y CPDs, se paga solo por lo que se consume mes a mes. Esto reduce riesgos financieros.

### 4.2 Economías de escala

Proveedores como AWS compran hardware y energía en volúmenes enormes, consiguiendo precios que ninguna empresa individual podría alcanzar. Estos ahorros se trasladan al cliente.

### 4.3 Evitar estimaciones de capacidad

Ya no es necesario calcular con antelación la demanda futura. Si el tráfico de una web se multiplica de repente, la nube permite escalar los recursos en minutos.

### 4.4 Aumento de la velocidad y agilidad

Un servidor físico puede tardar semanas en estar disponible. En la nube, un servidor virtual se levanta en cuestión de minutos.

### 4.5 Reducción de costes en mantenimiento de centros de datos

Se elimina la necesidad de gestionar instalaciones físicas, personal de seguridad, electricidad o refrigeración.

### 4.6 Escala global en minutos

Con la nube, una empresa puede desplegar recursos en distintas regiones del mundo casi al instante. Esto permite ofrecer servicios más rápidos a clientes internacionales.

## 5. Introducción a Amazon Web Services (AWS)

### 5.1 Qué es AWS

AWS es la plataforma de servicios en la nube más utilizada a nivel mundial. Ofrece cientos de servicios organizados en categorías como cómputo, almacenamiento, bases de datos, redes, seguridad, análisis o inteligencia artificial. Sus principios básicos son:

* **Acceso bajo demanda**: se puede crear infraestructura en cualquier momento.
* **Pago por uso**: no hay inversión inicial, se paga solo por lo consumido.
* **Servicios integrados**: diseñados para funcionar de forma conjunta.

### 5.2 Categorías de servicios principales

Algunos ejemplos son:

* **Cómputo**: Amazon EC2, AWS Lambda.
* **Almacenamiento**: Amazon S3, Amazon EBS.
* **Bases de datos**: Amazon RDS, DynamoDB.
* **Redes y entrega de contenido**: VPC, Route 53, CloudFront.
* **Seguridad**: IAM, AWS Shield.
* **Monitorización y administración**: CloudWatch, CloudTrail.

### 5.3 Formas de interactuar con AWS

* **Consola de administración**: interfaz gráfica accesible por navegador.
* **CLI (Command Line Interface)**: permite gestionar AWS mediante comandos y scripts.
* **SDKs**: facilitan el uso de AWS desde lenguajes de programación como Python, Java o C#.

## 6. Marco de adopción de la nube de AWS (CAF)

El **Cloud Adoption Framework (CAF)** de AWS ayuda a las organizaciones a migrar a la nube teniendo en cuenta todos los aspectos, no solo los técnicos. Se organiza en seis perspectivas:

1. **Negocios**: asegurar que la inversión en TI aporta resultados medibles al negocio.
2. **Personal**: formación técnica y adaptación de roles para aprovechar la nube.
3. **Gobernanza**: procesos y habilidades para alinear TI con los objetivos empresariales.
4. **Plataforma**: definición de la arquitectura técnica de destino.
5. **Seguridad**: cumplimiento de los objetivos de seguridad de la organización.
6. **Operaciones**: cómo se gestionarán las operaciones del día a día en la nube.

Cada perspectiva tiene un conjunto de capacidades que deben desarrollarse para una adopción eficaz.

## 7. Conclusión del módulo

En este capítulo hemos aprendido:

* Qué es la informática en la nube y cómo cambia la gestión de recursos TI.
* Las diferencias entre infraestructura tradicional y en la nube.
* Los modelos de servicio (IaaS, PaaS, SaaS) y de implementación (pública, privada, híbrida).
* Las seis ventajas fundamentales de la nube.
* Qué es AWS, qué servicios ofrece y cómo interactuar con ellos.
* Cómo el marco CAF estructura la adopción de la nube en seis perspectivas clave.

Este conocimiento proporciona la base para explorar servicios específicos de AWS en los siguientes capítulos.
