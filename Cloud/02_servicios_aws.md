# Anexo A. Servicios de AWS por categoría (explicados y comparados)

Este anexo desarrolla, con lenguaje claro y orientado a 2.º de DAM, los principales servicios de AWS por categorías. La idea es que, al leer cada entrada, sepas **qué es**, **para qué sirve**, y **en qué se diferencia** de servicios cercanos.

> Nota: AWS tiene decenas de servicios. Aquí priorizamos los **más importantes** para fundamentos y laboratorios. Donde proceda, añadimos alternativas cercanas para entender diferencias.



## 1) Cómputo

### Amazon EC2 (Elastic Compute Cloud)

* **Qué es:** Servidores virtuales (instancias) en la nube con control total del SO.
* **Para qué sirve:** Hospedar aplicaciones, APIs, bases de datos autogestionadas, servidores de juegos, etc.
* **Diferencias clave:** Máximo control y flexibilidad, pero también más responsabilidad (parcheo, escalado, alta disponibilidad). A diferencia de **Lambda** (sin servidores) o **Beanstalk** (plataforma gestionada), en EC2 tú gestionas casi todo.

### Amazon EC2 Auto Scaling

* **Qué es:** Servicio que **añade o quita** instancias EC2 automáticamente según métricas (CPU, peticiones…).
* **Para qué sirve:** Mantener rendimiento y optimizar costes en picos/valleys de carga.
* **Diferencias clave:** Suele combinarse con **Elastic Load Balancing** para repartir tráfico.

### Elastic Load Balancing (ALB / NLB / GWLB)

* **Qué es:** Balanceadores de carga gestionados.
* **Para qué sirve:** Repartir tráfico entre múltiples instancias/servicios para alta disponibilidad.
* **Diferencias clave:**

  * **ALB (Application LB):** capa 7 (HTTP/HTTPS), rutas por URL/host, ideal para apps web y microservicios.
  * **NLB (Network LB):** capa 4 (TCP/UDP), ultra rendimiento y baja latencia.
  * **GWLB (Gateway LB):** integra appliances de seguridad/terceros como si fueran un gateway.

### AWS Lambda

* **Qué es:** *Serverless compute*. Ejecuta **funciones** bajo demanda sin gestionar servidores.
* **Para qué sirve:** Backends event-driven, APIs ligeras, procesado de eventos de S3/Kinesis, cron jobs.
* **Diferencias clave:** Pagas por **tiempo de ejecución** y **número de invocaciones**. No gestionas servidores ni escalado. Frente a EC2, es más simple para cargas irregulares o event-driven; menos adecuado para procesos de larga duración o requerimientos especiales del SO.

### AWS Elastic Beanstalk

* **Qué es:** Plataforma gestionada para desplegar apps (Java, .NET, Node.js, Python…).
* **Para qué sirve:** Subes código y Beanstalk orquesta EC2, balanceo, Auto Scaling, logs.
* **Diferencias clave:** Abstrae detalles de infraestructura. Más control que **Lambda**, menos que **EC2** “a pelo”. Útil para equipos que quieren simplicidad sin perder visibilidad de instancias.

### Contenedores: Amazon ECS / Amazon EKS / AWS Fargate / Amazon ECR

* **Amazon ECS (Elastic Container Service):** Orquestación de contenedores **propietaria de AWS**; más sencilla si te quedas en el ecosistema AWS.
* **Amazon EKS (Elastic Kubernetes Service):** Kubernetes **gestionado**; para quien ya apuesta por K8s estándar.
* **AWS Fargate:** **Ejecución sin servidores** para ECS/EKS; no gestionas nodos, solo tareas/pods.
* **Amazon ECR (Elastic Container Registry):** Registro de imágenes de contenedor, privado y gestionado.
* **Diferencias clave:** ECS (simplicidad AWS) vs EKS (estándar K8s). Fargate evita administrar instancias. ECR es el repositorio de imágenes.

### AWS Batch

* **Qué es:** Gestión de **trabajos por lotes** (batch) a gran escala.
* **Para qué sirve:** Render, análisis científico, ETL batch, simulaciones.
* **Diferencias clave:** Optimiza colas, colas de cómputo y coste sin que tengas que programar el escalado a bajo nivel.

### Amazon Lightsail (mención)

* **Qué es:** VPS simplificado con plantillas para blogs, sitios web pequeños, pilas LAMP/WordPress.
* **Para qué sirve:** Proyectos sencillos, educativos o pruebas.
* **Diferencias clave:** Más simple que EC2, pero menos flexible.



## 2) Almacenamiento

### Amazon S3 (Simple Storage Service)

* **Qué es:** **Almacenamiento de objetos** (no de archivos ni de bloques) altamente duradero.
* **Para qué sirve:** Almacenar archivos estáticos, copias de seguridad, datos para análisis, assets web.
* **Diferencias clave:** No es un sistema de archivos POSIX. Ideal para **grandes volúmenes** y acceso vía API/HTTP. Clases de almacenamiento (Standard, IA, One Zone-IA, Intelligent-Tiering, Glacier, Deep Archive) para ajustar **coste vs. acceso**.

### Amazon EBS (Elastic Block Store)

* **Qué es:** **Almacenamiento en bloques** para adjuntar a instancias EC2 (volúmenes).
* **Para qué sirve:** Discos del SO o datos que requieren **baja latencia** y acceso en bloque.
* **Diferencias clave:** Persiste más allá del ciclo de la instancia si el volumen no se borra al terminar. No se comparte entre instancias simultáneamente (salvo casos Multi-Attach con io2). Comparar con S3 (objetos) y EFS (archivos compartidos).

### Amazon EFS (Elastic File System)

* **Qué es:** **Sistema de archivos** NFS **compartido** y elástico.
* **Para qué sirve:** Varios servidores accediendo a los mismos archivos (web servers, CMS, home dirs, ML).
* **Diferencias clave:** Comparte archivos entre múltiples instancias; pago por almacenamiento usado; elástico. Frente a EBS (bloque, por instancia) y S3 (objetos, vía API).

### Amazon FSx (familia)

* **FSx for Windows File Server:** SMB nativo para cargas Windows (Active Directory, ACLs).
* **FSx for Lustre:** Alto rendimiento para HPC y ML. Integra con S3.
* **FSx for NetApp ONTAP:** Funcionalidades avanzadas de ONTAP (snapshots, clones, multiprotocolo NFS/SMB).
* **FSx for OpenZFS:** Rendimiento y snapshots tipo ZFS.

### S3 Glacier / S3 Glacier Deep Archive

* **Qué es:** Clases de S3 para **archivo** y **retención** a largo plazo a **muy bajo coste**.
* **Para qué sirve:** Backups, históricos, cumplimiento.
* **Diferencias clave:** Tiempos de recuperación más altos (minutos a horas) según clase.

### AWS Storage Gateway (mención)

* **Qué es:** Conecta on-premises con S3/FSx (File/Volume/Tape Gateway).
* **Para qué sirve:** Migraciones, backup y extensión de almacenamiento al cloud desde CPD.

### AWS Backup (mención)

* **Qué es:** Orquestación centralizada de **copias de seguridad** para S3, EBS, RDS, EFS, DynamoDB, etc.



## 3) Bases de datos

### Amazon RDS (Relational Database Service)

* **Qué es:** Servicio **gestionado** para BD relacionales: **MySQL, PostgreSQL, MariaDB, Oracle, SQL Server**.
* **Para qué sirve:** Apps transaccionales tradicionales (OLTP) sin tener que administrar parches, backups o replicas a bajo nivel.
* **Diferencias clave:** Gestionado por AWS; tú eliges motor. Escalado vertical fácil; replicación y Multi-AZ.

### Amazon Aurora

* **Qué es:** Motor relacional compatible con **MySQL** y **PostgreSQL** desarrollado por AWS con mejoras de rendimiento y alta disponibilidad.
* **Para qué sirve:** Sustituir MySQL/PostgreSQL gestionados con mejores **rendimiento/HA**.
* **Diferencias clave:** Arquitectura separa cómputo y almacenamiento con replicación automática; suele ser más rápido que RDS estándar.

### Amazon DynamoDB

* **Qué es:** Base de datos **NoSQL** clave-valor y documentos, **completamente gestionada**, latencia milisegundos de un dígito.
* **Para qué sirve:** Apps con altísima escala, catálogos, sesiones, IoT, gaming, carritos.
* **Diferencias clave:** Escala automática, sin servidores; modelo de acceso por particiones (**diseño de claves** es crítico). Diferente paradigma que SQL.

### Amazon Redshift

* **Qué es:** **Data warehouse** columnar, orientado a **analítica** (OLAP) a gran escala.
* **Para qué sirve:** BI, informes, agregación de grandes volúmenes, consultas complejas.
* **Diferencias clave:** Optimizado para consultas analíticas; no para transacciones OLTP.

### Amazon ElastiCache / MemoryDB for Redis

* **ElastiCache:** Caches gestionadas **Redis** o **Memcached** para acelerar lecturas.
* **MemoryDB for Redis:** Base de datos en memoria compatible con Redis con persistencia sólida.
* **Diferencias clave:** ElastiCache se usa como **caché**; MemoryDB como **base de datos en memoria** primaria con durabilidad más fuerte.

### Otras BBDD gestionadas (mención)

* **Amazon Neptune:** grafos (Property Graph y RDF) para relaciones complejas.
* **Amazon DocumentDB:** compatible con API de MongoDB.
* **Amazon Timestream:** series temporales (IoT, métricas).
* **Amazon Keyspaces:** compatible con Cassandra (NoSQL columnar).
* **Amazon QLDB:** ledger inmutable con verificación criptográfica.



## 4) Redes y entrega de contenido

### Amazon VPC (Virtual Private Cloud)

* **Qué es:** Red virtual **aislada** donde colocas subredes, tablas de rutas, **security groups** y **NACLs**.
* **Para qué sirve:** Definir topología de red, segmentación, control de tráfico entre recursos.
* **Diferencias clave:** Componentes básicos:

  * **Subnets** (públicas/privadas),
  * **Internet Gateway** (salida a Internet),
  * **NAT Gateway/Instance** (salida a Internet desde subredes privadas),
  * **Route Tables**, **Security Groups** (estadoful) y **NACLs** (stateless).

### Amazon Route 53

* **Qué es:** Servicio **DNS** gestionado y **health checks**.
* **Para qué sirve:** Resolver nombres de dominio, routing por latencia/geolocalización/fallos.
* **Diferencias clave:** Integra con registros de AWS y soporta **traffic policies** avanzadas.

### Amazon CloudFront

* **Qué es:** **CDN** global.
* **Para qué sirve:** Distribuir contenido estático/dinámico a baja latencia desde ubicaciones perimetrales.
* **Diferencias clave:** Integra con S3, EC2, ALB y **Lambda\@Edge** para lógica en el borde.

### AWS Global Accelerator (mención)

* **Qué es:** Acelera tráfico TCP/UDP con **Anycast** y red global de AWS.
* **Para qué sirve:** Mejorar disponibilidad y latencia de aplicaciones globales.
* **Diferencias clave:** No es CDN; optimiza el **routing** de red para tu app.

### Conectividad híbrida

* **AWS Site-to-Site VPN:** túneles cifrados por Internet entre tu CPD y VPC.
* **AWS Direct Connect:** enlace dedicado de red, menor latencia y más estabilidad.
* **AWS Transit Gateway:** enrutamiento centralizado entre múltiples VPCs y on-prem.
* **VPC Peering / AWS PrivateLink:** conectividad punto a punto (peering) o publicación privada de servicios (PrivateLink) sin exposición pública.



## 5) Seguridad, identidad y conformidad

### AWS IAM (Identity and Access Management)

* **Qué es:** Control de **identidades** (usuarios, roles) y **permisos** mediante políticas.
* **Para qué sirve:** Conceder a personas/recursos el acceso mínimo necesario (**principio de menor privilegio**).

### IAM Identity Center (antes AWS SSO)

* **Qué es:** Gestión centralizada de acceso y **SSO** a múltiples cuentas y aplicaciones.
* **Para qué sirve:** Acceso federado y asignación de permisos basada en roles a escala de organización.

### Amazon Cognito

* **Qué es:** Autenticación/registro de **usuarios finales** (de tu aplicación), con federación social y MFA.
* **Para qué sirve:** Añadir login de usuarios a apps sin construir un backend de identidad propio.

### AWS Organizations / AWS Control Tower

* **Organizations:** Agrupa y gobierna **múltiples cuentas** con **SCPs** (políticas a nivel org).
* **Control Tower:** *Landing zone* con buenas prácticas, cuentas y guardrails preconfigurados.

### AWS KMS / AWS CloudHSM / AWS Certificate Manager / Secrets Manager / SSM Parameter Store

* **KMS:** Gestión de **claves** y **cifrado** integrado con la mayoría de servicios.
* **CloudHSM:** Módulos de seguridad hardware dedicados.
* **ACM:** Emisión/gestión de **certificados TLS** para tus dominios/ALB/CloudFront.
* **Secrets Manager:** Guarda y **rota** credenciales/API keys.
* **SSM Parameter Store:** Parámetros/configuración (incluye valores cifrados). Más simple que Secrets Manager.

### Protección y visibilidad

* **AWS WAF:** Firewall de aplicaciones web (bloquea SQLi, XSS, bots, reglas gestionadas).
* **AWS Shield:** Protección **DDoS** (Standard/Advanced).
* **Firewall Manager:** Política centralizada de WAF/Shield/Security Groups a nivel organización.
* **Amazon GuardDuty:** Detección de **amenazas** (anomalías) basada en logs/telemetría.
* **Amazon Inspector:** **Vulnerabilidades** en instancias/containers y desviaciones de buenas prácticas.
* **Amazon Macie:** Descubre **datos sensibles** (PII) en S3.
* **AWS Security Hub:** Panel unificado de hallazgos de seguridad (agrega WAF, GuardDuty, Inspector, etc.).
* **AWS Artifact:** Documentación de **cumplimiento** y auditoría (informes SOC/ISO/PCI…).



## 6) Monitorización y administración

### Amazon CloudWatch

* **Qué es:** **Métricas**, **logs** y **alarmas**. Incluye dashboards, eventos programados (EventBridge) y perfiles de aplicación (X-Ray se integra para trazas).
* **Para qué sirve:** Observar rendimiento de recursos y aplicaciones.
* **Diferencias clave:** CloudWatch = telemetría y alertas; no es auditoría de API.

### AWS CloudTrail

* **Qué es:** **Auditoría** de llamadas a la **API** de AWS (quién hizo qué y cuándo).
* **Para qué sirve:** Cumplimiento, forense, trazabilidad de cambios.
* **Diferencias clave:** CloudTrail registra acciones; CloudWatch mide y alerta.

### AWS Config

* **Qué es:** Inventario de recursos, **historial de configuración** y reglas de conformidad.
* **Para qué sirve:** Detectar **drift** y evaluar cumplimiento (p. ej., “todos los buckets S3 deben cifrarse”).

### AWS Systems Manager (SSM)

* **Qué es:** Suite para operar recursos: **Session Manager** (acceso sin SSH), **Patch Manager**, **Automation**, **Run Command**, **Inventory**, **Parameter Store**.
* **Para qué sirve:** Operaciones seguras a escala, sin abrir puertos ni gestionar salt servers.

### Otras herramientas útiles

* **AWS Trusted Advisor:** Recomendaciones de coste, seguridad y rendimiento.
* **AWS Well-Architected Tool:** Revisión frente a los 6 pilares de buenas prácticas.
* **AWS Service Catalog:** Catálogo interno de plantillas aprobadas.
* **AWS Backup:** Copias de seguridad centralizadas (mencionado arriba en almacenamiento).
* **AWS Health Dashboard:** Eventos y avisos que te afectan como cliente.



## 7) Guía rápida de elección (resumen práctico)

* **Quiero un servidor con control total:** EC2 (+ ALB + Auto Scaling según necesidad).
* **Quiero ejecutar funciones sin servidores:** Lambda.
* **Quiero desplegar código sin pelearme con la infraestructura:** Elastic Beanstalk.
* **Uso contenedores y quiero simplicidad AWS:** ECS (+ Fargate si no quiero gestionar nodos).
* **Uso Kubernetes estándar:** EKS (y opcionalmente Fargate).
* **Necesito almacenamiento barato y masivo para archivos:** S3 (elige clase según acceso).
* **Necesito el disco del servidor (bloque):** EBS.
* **Necesito compartir un sistema de archivos entre varias instancias:** EFS (o FSx según caso Windows/HPC/ONTAP/ZFS).
* **Quiero SQL gestionado:** RDS (o Aurora para más rendimiento/HA).
* **Quiero NoSQL sin servidores y a gran escala:** DynamoDB.
* **Analítica a gran escala/BI:** Redshift.
* **Red privada en AWS:** VPC (subredes + IGW/NAT + SG/NACL + rutas).
* **DNS y routing avanzado:** Route 53.
* **Distribuir contenido globalmente:** CloudFront (y Lambda\@Edge si necesito lógica en borde).
* **Identidades y permisos en AWS:** IAM (e IAM Identity Center para SSO multi-cuenta).
* **Identidades de usuarios finales de mi app:** Cognito.
* **Auditar quién hace qué:** CloudTrail.
* **Métricas/logs/alertas:** CloudWatch.
* **Cumplimiento y drift:** AWS Config.



## 8) Recomendaciones para laboratorio

1. **Empieza por VPC**: crea subredes pública/privada, IGW y NAT; practica security groups y NACLs.
2. **Despliega una app web** en **EC2** con **ALB** y **Auto Scaling**. Guarda estáticos en **S3**.
3. Añade **CloudWatch** (métricas/alarms) y **CloudTrail** (auditoría). Revisa **Config** con una regla básica de cifrado en S3.
4. Repite el backend con **Lambda + API Gateway** para comparar con EC2/Beanstalk.
5. Practica **RDS** (MySQL) y **DynamoDB** en dos ejercicios distintos para entender SQL vs NoSQL.



### Cierre

Este anexo debe servir como *mapa mental operativo*: identifica el **servicio adecuado** en cada categoría y entiende **por qué** elegir uno u otro. Si necesitas añadimos diagramas simples o casos guiados por pasos en un anexo adicional.
