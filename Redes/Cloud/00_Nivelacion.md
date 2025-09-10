## Fundamentos de Sistemas Operativos para Cloud Computing (AWS)

## 1. ¿Qué es un sistema operativo?

Un sistema operativo (SO) es el software fundamental que permite que un computador funcione y nos permite interactuar con él. Es, básicamente, el programa más importante que se ejecuta en un ordenador: sin el sistema operativo, el hardware por sí solo sería inútil. El SO actúa como intermediario entre nosotros (y las aplicaciones) y los componentes físicos de la computadora. Sus funciones básicas incluyen administrar los recursos del hardware (CPU, memoria, dispositivos de entrada/salida, almacenamiento), controlar la ejecución de programas y proveer una interfaz para el usuario ￼. En otras palabras, el sistema operativo se encarga de que todo el hardware y el software trabajen en conjunto de forma coordinada.

Ejemplos comunes de sistemas operativos: En computadores personales son muy conocidos Windows (de Microsoft) y macOS (de Apple), mientras que en servidores y entornos profesionales es muy popular Linux. En dispositivos móviles encontramos sistemas operativos móviles como Android (basado en Linux) o iOS (de Apple). A pesar de sus diferencias de apariencia, todos cumplen el mismo rol esencial: gestionar el hardware y ofrecer una plataforma para que corran las aplicaciones. Por ejemplo, cuando utilizas un navegador web, ese programa en realidad se apoya en servicios que el sistema operativo le brinda (acceso a la red, uso de la pantalla, archivos, etc.).

Relación con el hardware: El sistema operativo se carga al encender la computadora (tras un proceso llamado boot o arranque) y permanece en ejecución gestionando continuamente los recursos. Podemos imaginar el SO como el director de orquesta o administrador del sistema: supervisa qué programa utiliza la CPU en cada momento, qué porción de la memoria ocupa cada aplicación, envía las órdenes adecuadas a la tarjeta de sonido cuando queremos escuchar música, controla el acceso al disco cuando guardamos o abrimos un archivo, etc. Gracias al sistema operativo, los usuarios y programas no tienen que lidiar directamente con los complejos detalles del hardware; el SO traduce nuestras acciones (por ejemplo, hacer clic en un icono o ejecutar un comando) en instrucciones de bajo nivel para el hardware.

En resumen, un sistema operativo proporciona el entorno básico para poder usar un computador. Sin un SO corriendo, no podríamos ni siquiera escribir un documento, navegar por internet o abrir una aplicación, ya que no existiría esa “plataforma” sobre la cual se ejecutan todos los demás programas.

### 2. Tipos de sistemas operativos (en el contexto de la nube)

Existen muchos sistemas operativos, pero en el contexto de servidores cloud (como las instancias en AWS) principalmente veremos variantes de Linux y también opciones de Windows Server. Ambos son sistemas operativos, pero presentan diferencias importantes en su uso práctico en la nube. A continuación, veremos por qué Linux se usa ampliamente en servidores cloud y las comparaciones prácticas entre Linux y Windows al usar AWS.
	•	Linux en servidores cloud: La gran mayoría de servidores en la nube utilizan sistemas operativos basados en Linux. De hecho, por lo general las instancias en la nube vienen preconfiguradas con alguna distribución Linux. ¿Por qué? Varias razones prácticas:
	•	Costo y licencia: Linux es en su mayoría open source (código abierto) y sus distribuciones son gratuitas. No requiere pagar licencias por servidor, a diferencia de Windows. Esto supone ahorros significativos, especialmente cuando se despliegan muchos servidores.
	•	Estabilidad y rendimiento: Linux es reconocido por su alta estabilidad y fiabilidad en entornos de servidor. Puede funcionar por largos períodos sin necesidad de reinicios frecuentes, manejando cargas intensivas de trabajo de forma eficiente. Muchos servidores Linux pueden operar años sin interrupciones, lo cual es ideal para servicios en la nube que deben estar siempre disponibles.
	•	Seguridad: Por diseño y gracias a su activa comunidad, Linux posee una seguridad robusta. Es menos propenso a malware común en entornos de escritorio y las actualizaciones de seguridad son frecuentes. Esto no significa que Linux sea invulnerable, pero en práctica muchos administradores valoran su robustez frente a ataques.
	•	Flexibilidad y personalización: Al ser abierto, Linux permite personalizar prácticamente cualquier aspecto. En la nube esto facilita crear entornos a medida. Además, existen multitud de distribuciones (Debian, Ubuntu, CentOS, Amazon Linux, etc.) para elegir según la necesidad.
	•	Ecosistema y herramientas de servidor: La mayoría de aplicaciones de servidor, herramientas de desarrollo web, bases de datos, etc., fueron concebidas para correr en Linux. Por ejemplo, servidores web populares como Apache o Nginx, lenguajes como PHP, Python, Node.js, entornos de contenedores como Docker y Kubernetes… todo tiene excelente soporte en Linux. Esto hace natural que el entorno cloud “por defecto” sea Linux.
	•	Windows en la nube: Windows Server también se utiliza en AWS (y otros proveedores) cuando se requieren tecnologías específicas de Microsoft (.NET, MS SQL Server, servicios Active Directory, aplicaciones de Windows, etc.). A nivel práctico, Windows Server en la nube tiene ventajas como su interfaz familiar (escritorio gráfico, herramientas GUI) y compatibilidad con software empresarial de Microsoft. Sin embargo, presenta desventajas en este contexto:
	•	Licenciamiento y costo: Ejecutar Windows Server implica costos de licencia. En AWS, usar una AMI de Windows normalmente conlleva un cargo adicional por hora (para cubrir la licencia de Microsoft), mientras que las AMI Linux suelen ser gratuitas en licenciamiento (pagas solo el uso de la instancia). Esto puede encarecer despliegues grandes en Windows.
	•	Consumo de recursos: Windows tiende a requerir más recursos (RAM, almacenamiento) para una instalación básica en comparación con Linux, debido a que incluye entorno gráfico y muchos servicios habilitados por defecto. En instancias de poca potencia esto puede ser una limitante.
	•	Seguridad y actualizaciones: Aunque Windows Server es robusto, tiene un historial de más vulnerabilidades comunes, por lo que requiere una gestión cuidadosa de parches (actualizaciones frecuentes) para mantenerlo seguro. Además, la superficie de ataque suele ser mayor al tener más componentes habilitados. Linux, por su parte, al poderse instalar con lo mínimo necesario, reduce potenciales puertas de entrada.
	•	Curva de aprendizaje en automatización: En entornos cloud es muy común la administración automatizada mediante scripts. Linux está muy orientado a ello (a través de la terminal, bash scripts, etc.), mientras que Windows también lo permite (PowerShell, etc.) pero muchos administradores encuentran más fácil la automatización en Linux debido a su filosofía script-friendly.

¿Por qué entonces no se usa solo Linux? Porque la elección depende de la tarea. Si una empresa tiene aplicaciones diseñadas para Windows (por ejemplo, un sistema hecho en .NET con SQL Server), será más práctico usar Windows Server en la nube. AWS soporta ambas plataformas sin problema. De hecho, al lanzar una instancia EC2 puedes elegir AMIs de Windows Server y conectarte vía Escritorio Remoto (RDP) en lugar de SSH. Sin embargo, en laboratorios básicos de AWS es más común empezar con Linux por simplicidad y para introducir buenas prácticas agnósticas de fabricante.

Linux vs Windows: la experiencia práctica en AWS: En la práctica, para un principiante total, trabajar con un servidor Linux puede parecer menos intuitivo al inicio porque no tiene interfaz gráfica (veremos en la siguiente sección que usaremos la terminal). Windows, en cambio, ofrece un entorno de escritorio familiar. No obstante, aprender Linux a nivel básico no es difícil y brinda mucha flexibilidad. De hecho, la principal barrera de entrada de Linux es la CLI (interfaz de línea de comandos): usuarios acostumbrados a ventanas podrían encontrar desafiante usar comandos de texto. Pero es cuestión de práctica. En este módulo aprenderás esos comandos esenciales de Linux que necesitas para manejarte en AWS. Vale la pena, pues Linux es la opción predominante en la nube por las razones de costo, estabilidad y eficiencia mencionadas.

(En resumen: AWS te permite usar tanto Linux como Windows en tus instancias. Linux es más común por ser gratuito, ligero y ampliamente soportado; Windows se usa cuando se necesita. Como estudiante de cloud, conviene familiarizarse con Linux para sacar el máximo provecho a los laboratorios en AWS.)

### 3. La terminal o consola (interfaz de línea de comandos)

Cuando lanzamos una instancia en AWS (especialmente una instancia Linux), no tendremos un entorno gráfico de escritorio al que conectarnos. A diferencia de usar un PC normal con Windows donde ves ventanas, botones y cursores, en la nube nos conectaremos a servidores que típicamente no tienen GUI (Graphical User Interface) instalada por defecto. Entonces, ¿cómo interactuamos con ellos? Mediante la terminal o consola, es decir, la Interfaz de Línea de Comandos (CLI).

Una terminal es básicamente una pantalla negra (o ventana de texto) donde escribimos comandos y el sistema operativo responde con texto. Es una forma de interactuar con el OS a través de instrucciones escritas en lugar de clicks. Todos los sistemas operativos tienen alguna consola: en Windows existe el Símbolo del Sistema o PowerShell, en Linux y macOS es la terminal Bash u otros shells. En contextos cloud, la terminal es fundamental porque nos da control total usando muy poco ancho de banda y recursos (es solo texto).

¿Por qué es importante la terminal en la nube? Porque, como dijimos, los servidores en AWS generalmente no tienen “escritorio” remoto habilitado (a menos que uses instancias Windows o instales manualmente un entorno gráfico en Linux). Esto se hace por eficiencia y seguridad: un servidor Linux sin entorno gráfico consume menos recursos y tiene menos puertas de ataque. Por tanto, para administrar nuestro servidor en AWS usaremos SSH y una consola (más adelante explicaremos SSH). En esencia, abriremos una terminal local en nuestro PC que nos dará acceso de texto al servidor remoto. A través de esa terminal podremos escribir comandos para navegar por archivos, editar configuraciones, instalar software, arrancar servicios, etc., todo mediante texto.

Al principio puede impresionar o asustar a quienes nunca la usaron (“pantalla negra con letras verdes”). Pero una vez se conocen unos pocos comandos básicos, uno se da cuenta que la terminal no muerde. De hecho, muchos administradores llegan a preferirla por su potencia y rapidez para ciertas tareas. Piensa que con la terminal podemos automatizar tareas con scripts, hacer operaciones en lote, etc., cosas más difíciles de lograr con sólo interfaz gráfica.

Veamos algunos ejemplos básicos de uso de la terminal en Linux, que serán típicos en prácticas de AWS:
	•	Para saber en qué directorio estamos ubicados, usamos pwd (print working directory). Ejemplo:
    
```bash
ec2-user@servidor:~$ pwd  
/home/ec2-user
```
Esto nos mostró la ruta actual (en este caso, el home del usuario ec2-user).

•	Para listar archivos y carpetas en el directorio donde estamos, usamos ls (similar a ver el contenido de una carpeta):
```bash
ec2-user@servidor:~$ ls  
documentos  fotos  script.sh
```

Aquí aparecen tres elementos: dos directorios (documentos, fotos) y un archivo (script.sh).

•	Para cambiar de directorio, usamos cd (change directory). Ejemplo, entrar a la carpeta documentos:
```bash
ec2-user@servidor:~$ cd documentos  
ec2-user@servidor:~/documentos$ 
```
Observa que el prompt (la línea que aparece antes del cursor) ahora muestra que estamos dentro de ~/documentos. El símbolo ~ en Linux representa el home de nuestro usuario.

Muchos comandos tienen opciones. Por ejemplo ls -l muestra la lista en formato detallado (permisos, propietario, fecha, tamaño):
```bash
ec2-user@servidor:~/documentos$ ls -l  
-rw-r--r-- 1 ec2-user ec2-user   1200 Sep 10 12:00 informe.txt  
drwxr-xr-x 2 ec2-user ec2-user   4096 Sep  9 08:30 fotos
```

Aquí vemos información extra, como los permisos -rw-r--r--, el propietario (ec2-user), etc., que luego explicaremos.

Un comando importante es sudo. sudo significa “super user do” (ejecutar como superusuario). En Linux, los usuarios normales no pueden hacer ciertas acciones sensibles (instalar software, abrir puertos privilegiados, modificar archivos de sistema) a menos que usen sudo para elevar privilegios. Por ejemplo, para actualizar la lista de paquetes del sistema, en Ubuntu se haría:

```bash
ec2-user@servidor:~$ sudo apt-get update
```

Tras ingresar este comando, el sistema pedirá la contraseña (si aplica) y luego ejecutará la acción con privilegios administrativos.

Estos son solo algunos comandos, pero con ellos ya puedes navegar por el sistema de archivos (pwd, ls, cd), consultar contenido (por ejemplo, cat archivo.txt mostraría el contenido de un archivo de texto), y ejecutar acciones administrativas con sudo. En AWS, por ejemplo, podrías conectarte por terminal a tu instancia Linux y usar sudo yum install httpd para instalar un servidor web Apache, todo via comandos.

Interfaz gráfica vs línea de comandos: Es importante entender que ambas son formas de enviar instrucciones al OS. Una interfaz gráfica (GUI) traduce clicks y movimientos del ratón en acciones; la CLI nos permite escribir las acciones directamente. Internamente, el SO entiende ambas. De hecho, muchos comandos CLI realizan tareas que también podrías hacer con muchas clicks en una GUI. En entornos cloud, la CLI es reina por su sencillez y control directo. Como dice IBM, la interfaz de usuario puede ser gráfica o una línea de comandos, pero ambas le hablan al sistema operativo en su “idioma”. En AWS trabajaremos mayormente con CLI en nuestras instancias, aunque la plataforma AWS en sí nos ofrece una consola web para manejarlas externamente.

Finalmente, mencionar que AWS ofrece incluso una “Cloud Shell” (una terminal basada en navegador para interactuar con AWS) y su propia CLI de AWS para administrar servicios. Pero no confundamos: Cuando hablamos de la terminal aquí, nos referimos a la terminal del sistema operativo dentro de la instancia. Es decir, usar comandos Linux dentro del servidor. Esto es lo que harás vía SSH. Una vez dominado esto, también podrás explorar la AWS CLI para manejar recursos AWS desde comandos, pero eso es otro tema.

En resumen: la terminal es simplemente una manera de comunicarse con el servidor mediante texto. En AWS, dado que nuestras instancias Linux no tienen entorno gráfico, será nuestra vía principal. No hay que temerle: comandos como ls, cd, pwd, sudo pronto se volverán familiares y nos darán poder para controlar el servidor completamente.

### 1. Conceptos clave de funcionamiento interno del sistema operativo (archivos, usuarios, procesos)

Ahora que sabemos qué es un sistema operativo y que en la nube lo manejaremos vía terminal, conviene entender algunos conceptos internos básicos del OS. No vamos a profundizar en teoría complicada, solo lo necesario para movernos dentro de una instancia Linux con soltura. Los temas clave son: la estructura de archivos, los usuarios y permisos y los procesos/servicios. Estos conceptos te ayudarán a entender qué ves cuando navegas por el sistema de archivos de la instancia, por qué a veces te deniega acceso a algo (tema de permisos) o cómo se gestionan programas corriendo en segundo plano (servicios de sistema).

Estructura de archivos en Linux (sistema de archivos): En Windows estarás acostumbrado a unidades como “C:\” o “D:\” y carpetas como “Documentos” o “Program Files”. Linux (y UNIX en general) tienen una estructura diferente: todo cuelga de un único directorio raíz representado por “/”. Imagínalo como un árbol invertido:
	•	La raíz “/” es la base. Debajo cuelgan varios directorios estándar del sistema. Algunos importantes son:
	•	/home: aquí van los directorios personales de los usuarios. Por ejemplo, el usuario “ec2-user” tendrá su home en /home/ec2-user. Es similar a “Users” en Windows.
	•	/root: es el directorio home del usuario administrador “root” (el superusuario).
	•	/etc: contiene archivos de configuración del sistema (equivale al registro de Windows, pero en archivos de texto y scripts). Por ejemplo, configuración de red, de servicios, contraseñas de usuarios, todo suele residir en /etc.
	•	/bin y /usr/bin: contienen binarios ejecutables básicos del sistema (programas). Comandos como ls, cp, mv viven aquí. /bin es para binarios esenciales y /usr/bin para muchos programas de usuario.
	•	/sbin y /usr/sbin: similares a bin, pero para herramientas administrativas (system binaries). Por ejemplo, shutdown o iptables suelen estar en sbin.
	•	/lib y /usr/lib: librerías compartidas (análogas a archivos .DLL en Windows). Código reutilizable por los programas.
	•	/var: datos variables, como logs del sistema (en /var/log encontrarás archivos de registro), colas de impresión, bases de datos, etc.
	•	/tmp: archivos temporales. Suele limpiarse automáticamente. Sirve para que programas guarden datos temporales.
	•	/dev: archivos especiales para dispositivos. Linux “representa” dispositivos (discos, USB, etc.) como archivos aquí. Por ejemplo, el disco principal podría ser /dev/sda.
	•	/mnt o /media: puntos de montaje para unidades externas (p.ej. si conectas otro volumen o unidad).
	•	/opt: para software “opcional” instalado manualmente (no del gestor de paquetes). Por ejemplo podrías instalar aquí un programa de terceros.
Nota: No necesitas memorizar cada directorio. Con el tiempo recordarás los más usados. Lo importante es saber que en Linux no hay letras de unidad; el árbol empieza en “/”. Si listamos “/” (ls /), veremos muchas de estas carpetas base. Cuando inicies sesión en AWS en tu instancia, probablemente estarás en /home/ec2-user (el home del usuario por defecto). Podrás moverte por el sistema de archivos usando cd /ruta/que/quiero. Por ejemplo cd /var/log te lleva a ver los logs.
Esta estructura unificada hace que todo tenga su lugar. Por convención (FHS: Filesystem Hierarchy Standard) la mayoría de distribuciones mantienen este esquema común, de modo que conocimientos básicos de rutas sirven en cualquier Linux.

Usuarios y permisos básicos: Linux es un sistema multiusuario. Esto significa que puede tener varios usuarios definidos, cada uno con sus archivos y privilegios. En un servidor cloud es común que exista un usuario administrativo (no root) con el que te conectas, y el superusuario root. En AWS, por ejemplo, Amazon Linux usa el usuario ec2-user (Ubuntu usa ubuntu) para login por SSH, y ese usuario puede usar sudo para tareas de administrador.
	•	Usuarios: Cada fichero o proceso en Linux pertenece a un usuario. Puedes listar usuarios definidos en tu sistema mirando el archivo /etc/passwd (¡no hagas esto ahora, es solo informativo!). El usuario más poderoso es root, que tiene control total. Por seguridad, AWS inhabilita el login remoto de root en sus AMIs; por eso entras como ec2-user y luego usas sudo si necesitas privilegios de root. Además de usuarios “humanos”, el sistema tiene usuarios de servicio (por ejemplo, www-data para el servidor web Apache, etc., que sirven para aislar permisos de los servicios).
	•	Grupos: Los usuarios se organizan en grupos. Un grupo es simplemente un conjunto de usuarios, útil para asignar permisos colectivos. Por ejemplo, podría haber un grupo “developers” y darles permiso a ciertos directorios.
	•	Permisos de archivos: En Linux cada archivo o directorio tiene asociados permisos de lectura, escritura y ejecución para 3 categorías: el usuario propietario, el grupo al que pertenece el archivo, y otros (todos los demás). Cuando ejecutamos ls -l, vemos algo como -rw-r--r-- al inicio de la línea. Esto indica los permisos:
	•	-rw-r--r-- se descompone en:
	•	- (guion inicial) significa que es un archivo regular (si fuese d sería directorio).
	•	rw- : permisos del dueño (user) -> read & write (lectura y escritura) pero no ejecución (- en lugar de x).
	•	r-- : permisos del grupo -> solo lectura.
	•	r-- : permisos para otros -> solo lectura.
	•	Así, en este ejemplo el dueño puede leer/escribir, otros solo leer. Si fuera un script, se necesitaría permiso de ejecución (x) para poder ejecutarlo.
Para modificar permisos existe el comando chmod, y para cambiar dueño chown, aunque inicialmente no necesitaremos cambiar muchos permisos en labs básicos, es bueno saber interpretarlos. Un caso típico: creas un script y obtienes “Permiso denegado” al intentar ejecutarlo — probablemente falta dar permiso de ejecución (chmod +x script.sh).
	•	Sudo y privilegios: Ya mencionamos sudo permite ejecutar un comando como superusuario (root) temporalmente, pidiendo tu contraseña. Esto está configurado en AWS de forma que el usuario default (ec2-user/ubuntu) puede usar sudo sin contraseña en muchos casos (depende de la AMI). Intenta siempre operar como usuario normal y solo usar sudo cuando una acción lo requiera (por ejemplo, instalar software, abrir un puerto <1024, reiniciar un servicio del sistema, etc.). Así evitas cambios accidentales graves, ya que root puede hacer cualquier cosa (incluido borrar todo el sistema).

Procesos y servicios: Un proceso es básicamente un programa en ejecución. Cuando ejecutas un comando o inicias un programa, el sistema operativo crea un proceso (o varios). Cada proceso tiene su ID, su propietario (el usuario que lo lanzó), y consume ciertos recursos (CPU, memoria). En sistemas multitarea como Linux, múltiples procesos se ejecutan concurrentemente. El sistema operativo gestiona esto, dando la ilusión de paralelismo incluso en CPUs con pocos núcleos, gracias a que intercala la ejecución muy rápido.
	•	Para ver los procesos corriendo, en Linux existen comandos como ps (muestra procesos) o top (monitor en tiempo real). Por ejemplo ps -ef listaría todos los procesos con detalles, y top te mostraría dinámicamente los procesos que más CPU/memoria consumen.
	•	Notarás que hay procesos del sistema (ejecutados por root o usuarios de servicio) y procesos de usuario (por ejemplo si corres un editor de texto en la terminal, sería un proceso tuyo).

Un tipo especial de proceso es el servicio (en Linux también se les llama daemon o demonio). Un daemon es un programa que corre en segundo plano, sin interacción directa de usuario, generalmente iniciándose junto con el sistema operativo, para ofrecer algún servicio continuo. Por ejemplo, cuando activamos un servidor web Apache en nuestra instancia, se lanza el proceso apache2 (o httpd) como daemon: queda ejecutándose en background escuchando peticiones HTTP. Otros ejemplos: sshd es el demonio que permite conexiones SSH al servidor (arranca al inicio para que puedas conectarte), cron es un demonio que ejecuta tareas programadas, mysqld es la base de datos MySQL corriendo como servicio, etc. Estos procesos habitualmente:
	•	Se inician al arrancar el sistema (o cuando los habilitamos manualmente).
	•	No tienen interfaz gráfica ni suelen requerir input del usuario una vez lanzados.
	•	Corren “por siempre” en segundo plano, realizando su función. Por ejemplo, el demonio web seguirá corriendo y atendiendo páginas hasta que lo detengas o apagues el servidor.
	•	Suelen escribirse logs en /var/log para registrar su actividad o errores en lugar de “hablar” por pantalla.

En Linux moderno, el sistema de administración de servicios más común es systemd. Con comandos como systemctl podemos iniciar, detener, habilitar o deshabilitar servicios. Por ejemplo, sudo systemctl start nginx iniciaría el servicio Nginx (si está instalado), y sudo systemctl enable nginx haría que se inicie automáticamente al arrancar el OS. No profundizaremos en systemd en este nivel inicial, pero conviene saber que existe. Otro sistema más antiguo es SysVinit (comandos service o scripts en /etc/init.d/), pero AWS Linux actuales usan systemd en general.

Lo esencial: procesos = programas corriendo (pueden estar en foreground -ej.: tu sesión de shell- o background), servicios/daemons = procesos en background que brindan funcionalidades del sistema o servidor. Puedes listar servicios con systemctl list-units --type=service (obtendrás muchos, la mayoría iniciados por el sistema).

¿Por qué nos importa? Porque en las prácticas cloud a veces tendrás que iniciar o reiniciar servicios (por ejemplo, después de instalar un servidor de base de datos, habrá que arrancarlo). O verificar si cierto servicio está corriendo (ejemplo: “¿está activo el servicio apache?” puedes hacer systemctl status httpd). Entender que son procesos en segundo plano te ayuda a no verlos como magia: si tu aplicación web “no responde”, quizás el proceso del servidor web se cayó. Puedes revisarlo vía comandos.

Para terminar este bloque, un consejo: No es necesario memorizar todos los comandos ni detalles de procesos y permisos. Es más importante tener la intuición de qué buscar. Por ejemplo, si no puedes editar un archivo en /etc, probablemente es por permisos (solución: usar sudo o cambiar permisos). Si tu servidor web no está accesible, quizás el proceso no esté corriendo (solución: systemctl status/start). Si sale “command not found” es que no estás en el PATH o no está instalado. Estas nociones te permitirán diagnosticar problemas básicos al usar instancias en AWS.

(Resumen: Un sistema Linux organiza sus archivos en un árbol único partiendo de “/”, con carpetas estándar para config, programas, usuarios, etc. Cada archivo/proceso tiene un dueño y permisos que determinan quién puede hacer qué. Los usuarios admin pueden usar sudo para tareas especiales. Los procesos son programas corriendo; algunos se ejecutan como servicios de fondo (daemons) para dar funcionalidades permanentes, como aceptar conexiones SSH o servir páginas web. Conocer esto te ayudará a moverte y solucionar inconvenientes en tu servidor cloud.)

### 5. Virtualización: máquinas virtuales e hipervisores

Pasemos ahora a virtualización, un concepto central en la computación en la nube. De hecho, AWS (y los proveedores cloud en general) se basan fuertemente en virtualización para ofrecer sus servicios.

¿Qué es una máquina virtual (VM)? Es, en esencia, una “computadora simulada por software”. Mediante virtualización, podemos ejecutar múltiples sistemas operativos aislados en una misma máquina física. Cada uno de esos entornos se comporta como si fuera un equipo independiente, ¡pero en realidad comparten el hardware físico subyacente! El componente clave que hace esto posible se llama hipervisor. Un hipervisor es un software especial que gestiona las máquinas virtuales, repartiendo los recursos físicos (CPU, RAM, disco, red) entre ellas. Se le suele llamar también VMM (Virtual Machine Monitor). Piensa en el hipervisor como un árbitro: si tenemos, por ejemplo, 4 VM corriendo en un servidor físico, el hipervisor decide qué VM usa el procesador en cada instante, qué porción de memoria tiene asignada, intercepta las operaciones de las VM hacia los dispositivos físicos, etc. Todo esto dando la ilusión a cada VM de que es la única dueña de la máquina.

Ejemplo cotidiano: Si alguna vez has usado programas como VirtualBox, VMware Workstation o Hyper-V en tu PC para “correr otro sistema operativo” (por ejemplo, instalar Linux dentro de Windows), estabas usando virtualización. En tu Windows actuaba un hipervisor (VirtualBox) que creó un hardware virtual (un “PC virtual”) donde instalaste Linux. Linux no sabe que es virtual: cree que tiene su propio disco, su propia BIOS, etc., cuando en realidad todo es emulado por el hipervisor usando archivos y recursos del Windows anfitrión.

En la nube ocurre lo mismo a gran escala. Amazon EC2 (Elastic Compute Cloud) es básicamente un gigante sistema de virtualización: AWS ejecuta innumerables máquinas virtuales (instancias EC2) sobre un pool de servidores físicos en sus data centers. Cuando lanzas una instancia, en realidad estás “encendiendo” una máquina virtual que corre sobre un servidor físico compartido (con aislamiento, claro, para que tu VM sea segura respecto a otras). La virtualización permite a AWS aprovechar al máximo sus servidores al meter varias instancias en uno solo físico, en lugar de tener uno físico por cliente (lo cual sería muy ineficiente).

Hipervisores tipo 1 vs tipo 2: Existen dos tipos principales de hipervisor:
	•	Hipervisor Tipo 1 (bare metal): Es un hipervisor que se ejecuta directamente sobre el hardware de la máquina. No hay un sistema operativo “anfitrión” convencional; el propio hipervisor actúa como sistema ligero para manejar las VM. Este tipo se utiliza en entornos de servidor/centro de datos. Son muy eficientes y diseñados para producción. Ejemplos: VMware ESXi, Microsoft Hyper-V (cuando corre en un servidor dedicado), Xen y KVM (tecnologías de virtualización open source usadas en muchas nubes).
	•	Hipervisor Tipo 2 (alojado): Este corre encima de un sistema operativo existente. Es decir, primero tienes un OS (ej: tu Windows 10), y luego ejecutas el hipervisor como una aplicación más. Las VM entonces corren como “procesos” dentro de tu OS anfitrión. Son más comunes para uso personal o de prueba, ya que tienen algo más de overhead (tienen que pasar por el OS anfitrión). Ejemplos: VirtualBox, VMware Player/Workstation, Parallels (en Mac).

En AWS y nubes similares, obviamente se emplean hipervisores tipo 1 en los servidores físicos para alojar instancias. AWS históricamente usó el hipervisor Xen; en la actualidad usa una plataforma llamada AWS Nitro, que es un hipervisor muy optimizado (combina software y hardware dedicado) para ofrecer alto rendimiento cercano al metal puro. Pero como usuario de AWS, no tienes que preocuparte de gestionar el hipervisor: eso lo hace Amazon “detrás de bastidores”. Tú solo decides cuántas VM lanzar, de qué tamaño, etc., y AWS ubica esas VM en sus servidores físicos. En definitiva, tu instancia EC2 es una máquina virtual gestionada por el hipervisor de AWS en un host físico compartido.

Vale la pena mencionar que la virtualización es la base de la nube. Permite:
	•	Aislamiento: Cada VM está separada de las demás. Si la tuya se cae o es comprometida, no afecta a otras del mismo host físico.
	•	Elasticidad y escalado: Crear o destruir VMs es cuestión de minutos (o segundos) porque es software. No hay que instalar un servidor físico real cada vez. AWS incluso automatiza esto con escalados automáticos.
	•	Aprovechamiento óptimo: En lugar de tener un servidor físico infrautilizado, se pueden meter varias VM para aprovechar toda la capacidad. Para AWS es crucial maximizar el uso de hardware (y para el usuario, pagar solo por lo que usa, fracción de un servidor si quiere).
	•	Portabilidad: Una VM es esencialmente archivos (imagen de disco, etc.), así que se puede migrar, clonar, hacer snapshots, etc., fácilmente. De hecho, cuando detenemos una instancia AWS y luego la iniciamos, es como encender/apagar una VM – tus datos persisten en un disco virtual.

Técnicamente, las instancias de AWS se categorizan por “tipo” según recursos (t2.micro, t3.medium, m5.large, etc.). Esto define cuántos vCPUs, cuánta RAM, etc., la hipervisor le asignará. Desde tu VM, verás por ejemplo 1 CPU y 1 GB RAM (si es t2.micro), aunque el host físico tenga 36 CPUs y 128 GB RAM compartidos entre varias instancias. El hipervisor se encarga de que cada instancia reciba la fracción prometida. Si excedes (en instancias de tipo burst, hay créditos, etc., pero eso es detalle de AWS).

En resumen, virtualización = tener “computadoras virtuales” corriendo sobre hardware real compartido. Hipervisor = software que hace de intermediario, repartiendo el hardware entre las máquinas virtuales. AWS es un gran sistema de hipervisores bare metal orquestados para que usuarios creen/eliminem VM a demanda. De hecho, AWS define que Amazon EC2 permite escalar en la nube usando hipervisores basados en Xen (en Nitro se mantiene compatibilidad con Xen para instancias antiguas).

(Resumen práctico: Una instancia AWS es una VM. Virtualización hace posible la nube al permitir instancias de muchos clientes en un mismo servidor físico, aisladas. No vemos el hipervisor, pero está ahí (Nitro/Xen en AWS) asignando CPU, memoria, etc. Saber esto nos ayuda a entender que “debajo” de nuestras instancias hay un host físico, y que términos como VM, instancia, máquina virtual, servidor virtual, son equivalentes en este contexto.)

### 6. Contenedores vs máquinas virtuales

En tecnología cloud moderna, seguramente oirás mucho el término contenedores (containers, Docker, Kubernetes, etc.). A veces se confunden con máquinas virtuales, pero no son lo mismo. ¿En qué se diferencian? Aquí daremos una explicación conceptual nivel principiante, sin ahondar en detalles técnicos.

Tanto las máquinas virtuales como los contenedores sirven para aislar entornos de software y empaquetar aplicaciones, pero lo hacen en niveles distintos:
	•	Máquina Virtual (VM): Como vimos, una VM incluye un sistema operativo completo invitado. Cada VM tiene su propio kernel y sistema, sobre un hipervisor. Esto le permite tener múltiples aplicaciones diferentes y simular hardware completo, pero con la penalización de necesitar más recursos (cada VM corre su OS entero). En general, las VM son más pesadas en arranque y consumo, pero también más flexibles en términos de qué pueden ejecutar (cualquier sistema operativo compatible con el hipervisor). Por ejemplo, en un mismo host podrías tener una VM con Linux, otra con Windows, etc. Las VM pueden ejecutar varias aplicaciones robustas a la vez y aislarlas totalmente, a costa de duplicar esfuerzos (cada VM trae su propio OS).
	•	Contenedor: Un contenedor, en cambio, no emula hardware completo. Aprovecha el sistema operativo del host. Podríamos decir que un contenedor es como un “mini-sistema aislado” pero que comparte el kernel del OS host. Un contenedor encapsula una aplicación y todas sus dependencias en un paquete independiente, asegurando que siempre se ejecute igual sin importar el entorno. Pero todos los contenedores sobre un mismo host usan el mismo kernel. Esto los hace mucho más ligeros que las VM: arrancan rápido, consumen menos RAM, y puedes tener muchos contenedores corriendo en una sola máquina OS. Un contenedor típicamente aisla uno o unos pocos procesos (por ejemplo, un contenedor podría ejecutar solo una instancia de una aplicación web). El aislamiento se logra mediante características del propio kernel (namespaces, cgroups en Linux) – en resumen, el motor de contenedores (como Docker) configura que cada contenedor solo vea ciertos recursos (sistema de archivos propio, ciertas interfaces de red, cierta cuota de CPU/RAM) aunque en realidad esté compartiendo el mismo núcleo del OS.

En términos simples: si una VM es un apartamento completo con todos los muebles, un contenedor es una habitación privada en un gran apartamento compartido. Cada contenedor tiene lo necesario para su aplicación, pero el “edificio” (kernel) es común. Esto implica que todos los contenedores en un host Linux deben ser Linux (no puedes ejecutar un contenedor Windows puro en kernel Linux, ni viceversa, porque comparten kernel) ￼. En cambio, en VMs sí podrías mezclar OS distintos en un mismo físico.

¿Por qué el cloud usa contenedores? Porque aportan eficiencia y portabilidad para desplegar aplicaciones:
	•	Son muy ligeros: iniciar un contenedor toma segundos, mientras bootear una VM puede tomar minuto(s). Esto ayuda a escalar aplicaciones rápidamente (p.ej., lanzar 10 contenedores nuevos al subir la carga de una web).
	•	Permiten máxima densidad: en un mismo servidor puedes meter quizás docenas de contenedores (ya que no replican OS entero), donde solo cabrían unas pocas VMs.
	•	Facilitan la portabilidad de aplicaciones: una aplicación empacada en contenedor Docker incluye todo lo que necesita (excepto el kernel). Puedes tomar esa imagen de contenedor y correrla en tu laptop, en un servidor on-premise o en la nube de AWS/Azure/GCP y obtendrás el mismo resultado. “Funciona en mi máquina” deja de ser excusa, porque tu máquina y la del servidor correrán el mismo contenedor.
	•	Encajan con arquitecturas de microservicios: en desarrollo moderno se prefiere dividir aplicaciones en muchos componentes pequeños (microservicios). Los contenedores vienen perfectos para desplegar cada microservicio aislado, pero conviviendo en un host o cluster.
	•	Gestión orquestada: surgen herramientas como Kubernetes para administrar cientos de contenedores (distribuir carga, tolerancia a fallos, etc.). En la nube, Kubernetes y los contenedores son una capa de abstracción que permite desplegar aplicaciones de forma muy eficiente.

AWS y los contenedores: AWS ofrece servicios específicos: por ejemplo ECS (Elastic Container Service) y EKS (Elastic Kubernetes Service) para gestionar contenedores Docker. Además, AWS Fargate permite correr contenedores sin ni siquiera preocuparse de las VM subyacentes. Todo esto para aprovechar la ventaja de contenedores.

¿Reemplazarán a las VM? No exactamente. Cada tecnología tiene su caso de uso. Las máquinas virtuales ofrecen aislamiento completo y pueden ser preferibles para ejecutar aplicaciones monolíticas o antiguas que requieren todo un OS, o entornos mixtos. Los contenedores brillan en nuevas aplicaciones diseñadas para ellos. De hecho, muchas veces los contenedores corren dentro de máquinas virtuales!* (Por ejemplo, en AWS EKS, cada nodo de Kubernetes es una instancia EC2, que luego aloja contenedores). Así que conviene verlos como complementarios. Como señala Red Hat, aunque a veces se piensa que los contenedores reemplazan a los hipervisores, en realidad atienden necesidades diferentes y suelen usarse conjuntamente ￼.

Resumiendo la diferencia principal:
	•	VM: emula una máquina completa, con su sistema operativo. Aislamiento a nivel de hardware virtual. Más pesada en recursos, pero totalmente independiente del host (puede tener distinto OS).
	•	Contenedor: aísla una aplicación a nivel de software dentro del mismo OS host. Comparte kernel, por lo que es más liviano, inicia rápido y consume menos, pero depende del OS base (todos deben usar, por ejemplo, Linux si el host es Linux).

(Ejemplo final para fijar ideas: Imagina que quieres desplegar una aplicación web con base de datos. Con VM podrías crear 2 VM: una con Linux+Apache, otra con Linux+MySQL. Cada una con su OS. Con contenedores, podrías en 1 VM real correr 2 contenedores: uno con Apache (en un contenedor con su Apache y librerías), otro con MySQL (en otro contenedor separado). Ambos comparten el kernel de la VM host. Si necesitas escalar la web, duplicas el contenedor de Apache en la misma VM host o en otra. Así operan muchos servicios cloud modernos.)

### 7. Imágenes del sistema (AMI en AWS)

Al lanzar una instancia nueva en AWS, uno de los pasos críticos es elegir la imagen del sistema que usará. En AWS esto se llama AMI (Amazon Machine Image). Veamos qué significa este concepto.

Una imagen de sistema es básicamente una plantilla pre-configurada de un sistema operativo, posiblemente con software adicional, a partir de la cual se puede crear una máquina nueva. En términos sencillos, es como tener una “fotografía” del disco de una computadora en cierto estado, que puedes clonar para obtener copias idénticas.

En AWS, una AMI proporciona el software necesario para configurar y arrancar una instancia EC2 ￼. Cada AMI incluye:
	•	Un sistema operativo (por ejemplo, Amazon Linux 2, Ubuntu, Windows Server 2019, etc.).
	•	Opcionalmente, software pre-instalado (por ejemplo, hay AMIs con WordPress listo, con Python preconfigurado, con paquetes LAMP, etc., dependiendo del caso).
	•	Configuraciones por defecto (ajustes de seguridad, usuarios iniciales, etc. – por ejemplo la AMI Amazon Linux viene con el usuario ec2-user y ciertas claves preinstaladas).
	•	Información de particionado/volúmenes (mapeo de dispositivos de bloques: qué tamaño de disco tendrá la instancia por defecto al lanzarla, etc.) ￼.

Cuando vas a lanzar una instancia en la consola de AWS, te ofrece elegir una AMI. Tienes varias categorías:
	•	AMI proporcionadas por AWS: Son las “oficiales”, mantenidas por Amazon u OS de base. Por ejemplo “Amazon Linux 2 AMI”, “Ubuntu Server 22.04 LTS”, “Red Hat Enterprise Linux 8”, “Windows Server 2019 Base”, etc. Suelen ser minimalistas (solo el OS básico y utilidades).
	•	AMI de la comunidad o públicas: Imágenes compartidas por otros usuarios o compañías, a veces con software específico. Por ejemplo, puede haber una AMI pública con Apache Kafka ya instalado, lista para usar.
	•	AMI de Marketplace: Imágenes publicadas por proveedores que a veces incluyen software licenciado de pago (por ejemplo, una AMI con SAP, con software de seguridad comercial, etc.). Si eliges estas, AWS te cobrará posiblemente costos de licencia adicionales.
	•	Tus propias AMI: AWS te permite crear una imagen a partir de una instancia que has configurado. Por ejemplo, instalas y configuras un servidor a tu gusto, luego lo “imagenizas” creando una AMI personalizada, para así lanzar múltiples instancias idénticas en el futuro o guardarla de respaldo.

Cada AMI es identificada por un ID (p.ej. ami-0abcdef1234567890) único y está asociada a una región. Debes especificar qué AMI usar al iniciar una instancia ￼. Por ejemplo, en la guía de lanzamiento rápido de AWS, si vas a crear tu primera instancia Linux suele recomendar Amazon Linux 2 (una distribución Linux mantenida por AWS, muy ligera y optimizada para EC2). Si quisieras probar con Windows, elegirías una AMI de Windows Server (observa que entonces la instancia tardará más en arrancar y el proceso de acceso es distinto, vía escritorio remoto).

¿Qué elige el usuario al lanzar una instancia en AWS? Principalmente dos cosas:
	1.	La AMI (imagen), que determina el software/sistema operativo.
	2.	El tipo de instancia, que determina el hardware virtual (tamaño de CPU/RAM, etc.).

Adicionalmente configuras red, almacenamiento, claves SSH, pero la base es AMI + tipo. Por ejemplo, podrías elegir “AMI de Ubuntu 22.04” + “tipo t2.micro”. Eso resultará en una VM con Ubuntu 22.04 corriendo con 1 vCPU, 1 GB RAM. Si en cambio eliges “AMI de Windows Server 2019” + “tipo t2.micro”, será Windows con 1 vCPU/1GB.

Contenido de la AMI: Para aterrizarlo, imagina que una AMI es un archivo enorme que contiene todos los archivos del sistema operativo en un estado listo para arrancar. Cuando lanzas la instancia, AWS básicamente toma ese “molde”, lo copia al volumen de disco provisionado para tu instancia, y luego inicia la VM arrancando desde ahí. Por eso una instancia nueva suele ser idéntica siempre que usemos la misma AMI.

Un detalle: Compatibilidad con tipo de instancia: Algunas AMIs pueden requerir cierto tipo de virtualización o arquitectura. Por ejemplo, hay AMIs para arquitectura x86_64 (la mayoría) y otras para ARM (AWS tiene instancias Graviton ARM). Debes usar una AMI compatible con el tipo de instancia que elijas (AWS filtra esto automáticamente en la interfaz). También hay AMIs HVM o PV (esto era con Xen antigüo), pero hoy casi todas son HVM.

Ejemplos de AMI comunes:
	•	Amazon Linux 2: Distribución Linux basada en Red Hat, mantenida por AWS, con optimizaciones (ya incluye drivers optimizados para AWS, Cloud-init para inicialización, etc.). Es gratuita y suele ser la default para muchos tutoriales AWS.
	•	Ubuntu Server: Muy popular por su comunidad. AMIs oficiales de Canonical para Ubuntu LTS.
	•	Red Hat Enterprise Linux (RHEL): Si la empresa tiene suscripciones, AWS provee AMIs RHEL (con costo de licencia incorporado).
	•	Windows Server: AMIs de Windows Server 2012/2016/2019/2022, etc. Permiten lanzar instancias Windows (que luego accedes vía RDP).
	•	AMI con aplicaciones: Por ejemplo, “WordPress Certified by Bitnami” es una AMI que viene con Ubuntu + WordPress + MySQL preinstalado, lista para usar (útil para demos, aunque en producción quizás prefieras instalar tú mismo).
	•	AMI personalizadas: Si tú configuras un servidor con cierto software y estado, puedes crear tu AMI para replicarlo. Por ejemplo, configuras una instancia con todo tu stack, la conviertes en AMI, y luego desde esa AMI lanzas 5 instancias clones detrás de un balanceador.

Nota sobre instantáneas y AMI: Una AMI incluye referencia a instantáneas de EBS (discos) que tienen la info de los archivos. Cuando la AMI se usa, se crea un nuevo volumen a partir de esas instantáneas para tu instancia.

Relación con virtualización: Podríamos decir que la AMI es al software lo que el tipo de instancia es al hardware virtual. Uno elige ambos para crear la VM completa. Recuerda: AMI = qué va dentro de la máquina; Tipo de instancia = cuánta potencia tendrá la máquina. AWS hace el matching y ¡listo, tu servidor virtual arranca.

(Resumen: Una AMI es una “imagen” de disco de sistema operativo + software. Al lanzar una instancia en AWS debes elegir una AMI, ya sea Linux, Windows u otra. Esto define qué SO tendrás dentro de tu VM. Las AMIs facilitan desplegar servidores rápidamente sin instalar OS manualmente. Si sabes qué AMI usar (ej: Amazon Linux 2 para practicas AWS), en segundos tienes tu servidor listo. Puedes usar AMIs estándar de AWS, de terceros o crear las tuyas. ¡Es como elegir el sistema operativo preinstalado de tu servidor en la nube.)

### 8. Acceso remoto a servidores (SSH y clave privada)

En un entorno cloud, típicamente administramos los servidores de forma remota. No hay monitor, teclado ni ratón conectados a “tu” servidor en AWS; el acceso es a través de la red. Aquí entra en juego SSH (Secure Shell), el protocolo estándar para conexiones remotas seguras a máquinas Linux/Unix. También hablaremos de las claves privadas que AWS utiliza para autenticar estas conexiones, y qué necesitas configurar para lograr acceder exitosamente a tu instancia.

¿Qué es SSH? Secure Shell es un protocolo de comunicación que permite abrir una sesión de terminal en un servidor remoto de forma cifrada (segura). Es decir, usando SSH puedes conectarte desde tu ordenador a la consola de tu instancia en AWS como si estuvieras enfrente de ella. SSH cifra todo el tráfico, de modo que contraseñas o comandos no viajen en texto plano por internet. Para usar SSH necesitas un cliente SSH en tu PC (en Linux/Mac ya existe en la terminal; en Windows puedes usar PowerShell o herramientas como PuTTY). Con SSH te conectarás especificando la IP o nombre DNS de la instancia, un usuario y algún método de autenticación.

Autenticación con clave pública/privada: Existen dos métodos comunes para autenticarse por SSH: contraseña o par de claves. AWS por defecto opta por el sistema de claves porque es más seguro y práctico en despliegues en la nube. ¿Cómo funciona?
	•	Cuando creas/lanza una instancia AWS, se te pide elegir o crear un par de claves (key pair). Este par consiste en una clave pública y una clave privada criptográficas.
	•	AWS coloca automáticamente la clave pública dentro de tu instancia (concretamente, la añade al archivo ~/.ssh/authorized_keys del usuario, p. ej. ec2-user).
	•	Tú debes descargar y guardar la clave privada (.pem) en tu equipo local. Esa clave privada es como “tu identidad secreta” para esa instancia.

Cuando intentas conectar por SSH, tu cliente usa la clave privada para demostrarle al servidor que tienes la pareja de la clave pública que él tiene. Si coincide, acceso concedido sin necesidad de contraseña. En otras palabras, el par de claves es un credencial de seguridad que demuestra tu identidad al conectar ￼. Para instancias Linux, la clave privada te permite iniciar sesión por SSH de forma segura ￼ (en instancias Windows el mismo par se usa para descifrar la contraseña de administrador).

Importante: Guarda bien tu clave privada (.pem); si la pierdes, AWS no tiene copia y no podrás autenticarte (tendrías que recurrir a procedimientos de recuperación más complejos). Y si alguien más obtiene tu .pem, podría acceder a tus instancias – es como una llave maestra secreta ￼. Por eso, nunca la compartas ni la dejes en lugares no seguros. Si necesitas dar acceso a otro colega, lo ideal es que esa persona use su propio par de claves.

Procedimiento típico de acceso por SSH a una instancia AWS:
	1.	Lanzas la instancia eligiendo un par de claves (digamos miClave.pem). Si es la primera vez, AWS te habrá hecho crear uno y descargar el .pem.
	2.	Esperas a que la instancia esté en estado “running” y obtienes su dirección (puede ser una IP pública o un nombre DNS público).
	3.	En tu terminal local, usas un comando del estilo:
```bash
ssh -i /ruta/miClave.pem ec2-user@<IP-o-DNS-de-instancia>
```
Aquí -i indica el archivo de identidad (clave privada), ec2-user@... indica el usuario y host destino.

4.	La primera vez te preguntará si confías en la huella del servidor (tecleas “yes”). Luego, si todo está bien, te dará acceso y verás el prompt de tu instancia Linux.

5.	¡Ya estás dentro! A partir de ahí, cualquier comando que escribas se ejecuta en la instancia remota.

En sistemas Windows, si usas PuTTY, debes convertir el .pem a .ppk (formato PuTTY) con PuTTYgen, luego configurar PuTTY para usar esa clave al conectar a ec2-user@IP. En Windows 10+ puedes habilitar OpenSSH nativo y usar el mismo comando ssh de arriba en PowerShell.

Resumen de lo necesario para acceder a una instancia EC2 Linux:
	•	IP o nombre DNS público de la instancia (que AWS te da). La instancia debe estar en una subnet con internet gateway o con Elastic IP, etc., para ser accesible desde fuera, o tú estar en su misma red (en labs usualmente la ponemos accesible).
	•	Puerto 22 abierto en el firewall de AWS (Security Group) hacia tu IP. (Cuando lanzaste la instancia, seguramente AWS configuró por ti una regla permitiendo SSH desde tu IP actual).
	•	Clave privada (.pem) correspondiente a la clave pública que tiene la instancia. Sin esto, no podrás autenticar (a menos que la instancia estuviera configurada para password login, que no es el caso por defecto en AWS).
	•	Cliente SSH en tu máquina para iniciar la conexión.

Si cumples todo lo anterior, la conexión SSH debe funcionar y verás la terminal remota.

¿Y si la instancia es Windows? El acceso no se hace por SSH (aunque Windows Server 2019 ya puede habilitar OpenSSH, pero tradicionalmente no). En Windows usarías RDP (Remote Desktop Protocol) en el puerto 3389. AWS te proporciona una contraseña (que descifras con la clave privada) para el usuario Administrator, y luego abres la aplicación de “Conexión a Escritorio Remoto” de Windows apuntando a la IP de la instancia. Esto te muestra la interfaz gráfica de ese servidor Windows remoto. Pero en este curso nos centraremos en Linux/SSH.

Volviendo a SSH en Linux, es conveniente mencionar algunas buenas prácticas:
	•	Cambiar la propiedad/permisos de tu archivo .pem para que solo tú puedas leerlo. Por ejemplo, en Linux al descargar miClave.pem, ejecutar chmod 400 miClave.pem para que no sea accesible por otros usuarios del sistema.
	•	Nunca guardar claves privadas en repositorios públicos, ni pasarlas por email sin cifrar, etc.
	•	Opcionalmente, puedes usar un agente SSH (ssh-agent) para no tener que teclear la ruta cada vez, o usar certificados SSH, pero eso es más avanzado.

AWS también tiene una opción llamada Session Manager (parte de AWS Systems Manager) que permite conectarse a instancias sin necesidad de clave SSH, todo vía la consola web o AWS CLI (usando permisos IAM). Es útil en entornos empresariales donde no quieren gestionar claves manualmente. Pero para entender lo esencial, la clave pública/privada es el método tradicional.

(En suma: Para acceder a tu servidor Linux en AWS usaremos SSH, autenticado con un par de claves. AWS guarda la clave pública en la instancia y tú usas la clave privada desde tu equipo. Asegúrate de tener el puerto 22 abierto y utilizar el usuario correcto (p.ej. “ec2-user”). Una vez dentro vía SSH, podrás manejar tu instancia mediante la terminal como si estuvieras local. Esta es la piedra angular de las prácticas en la nube: lanzar instancia, conectarse por SSH, y luego ya puedes instalar software, editar archivos, etc. remotamente.)

### 9. Firewall del sistema operativo (cortafuegos local)

Llegamos al último tema: los firewalls. Ya vimos que AWS tiene su propio firewall a nivel de nube (los Security Groups que controlan qué tráfico entra o sale de la instancia). Pero dentro de la propia instancia también puede haber un firewall activo en el sistema operativo. Si este no está bien configurado, podría bloquear conexiones aunque en AWS hayamos abierto el puerto. Por eso es crucial entender que hay dos capas de firewall: la de AWS y la del sistema operativo, y ambas deben permitir el tráfico para que algo llegue a tu aplicación.

¿Qué es un firewall? Es un sistema (puede ser software o hardware) que filtra paquetes de red según reglas definidas. Básicamente decide qué conexiones o datos dejar pasar y cuáles bloquear, generalmente basado en criterios como dirección IP de origen/destino, puerto utilizado, protocolo, etc. Un firewall puede impedir, por ejemplo, que cualquiera excepto tu IP acceda por SSH, o bloquear todo intento de conectar al puerto 3306 (MySQL) desde fuera por seguridad, etc.

En nuestro contexto, tenemos:
	•	Firewall de AWS (Security Group): Opera antes de que el tráfico llegue a tu instancia. Si aquí no abres el puerto X, ni siquiera llegará nada a tu servidor por ese puerto. AWS Security Groups por defecto permiten todo tráfico saliente y niegan todo entrante salvo lo que especifiques.
	•	Firewall local (sistema operativo): Una vez el tráfico entra a la instancia (gracias a que SG lo permitió), aún puede toparse con el firewall del propio OS. En Linux, el firewall tradicional es iptables (parte del kernel) configurado vía utilidades como ufw (Uncomplicated Firewall) o firewalld. En Windows, está el “Windows Defender Firewall”. Estos hacen la misma función: reglas de permitir/bloquear a nivel del host.

Ejemplo: Supongamos que en AWS abres el puerto 8080 a todo el mundo (en el SG), porque vas a servir una aplicación web en ese puerto. Aun así, clientes no logran conectarse. Revisas en la instancia Linux y descubres que el firewall local (ufw) está activo y por defecto bloquea todas las conexiones entrantes salvo las permitidas. Esto es de hecho el comportamiento predeterminado de ufw: deny incoming, allow outgoing. Si no añadiste regla para 8080, ufw lo bloqueará. La solución sería agregar la regla (sudo ufw allow 8080) y luego los clientes podrán conectar.

Ahora bien, muchas imágenes Linux en AWS vienen con el firewall desactivado por defecto (ej. Amazon Linux no trae ufw, Ubuntu lo trae pero suele estar inactivo inicialmente). Esto se debe a que AWS asume que usarás Security Groups para esa función. Aún así, es buena práctica configurar el firewall de la instancia si vas a abrir muchos puertos o si quieres protección en capas (defense in depth). No está mal tener ambos: SG filtra a gran escala, y el firewall local filtra dentro de la instancia.

Veamos rápidamente cómo manejar el firewall en Linux (ufw), ya que Ubuntu por ejemplo lo usa:
	•	UFW significa Uncomplicated Firewall, es básicamente una interfaz sencilla para iptables.
	•	Para ver si está activo: sudo ufw status. Si dice inactive, no está filtrando nada (todo permitido).
	•	Para permitir algo: sudo ufw allow <servicio/puerto>. Ej: sudo ufw allow ssh abre el 22, sudo ufw allow 80/tcp abre web HTTP.
	•	Para bloquear (aunque por defecto todo está bloqueado a menos que permitas): sudo ufw deny 22 por ejemplo.
	•	Para activar el firewall: sudo ufw enable (¡ojo! haz esto después de permitir SSH, sino te puedes bloquear a ti mismo).
	•	UFW por defecto al habilitar, negará todo entrante no permitido, como decíamos. Por eso, siempre antes de enable, allow ssh desde tu IP o general, para no perder conexión.

En servidores con CentOS/Amazon Linux, existe firewalld o directamente iptables. Los conceptos son iguales: hay un conjunto de reglas que definen qué pasa. Manejar iptables directamente es más complejo (comandos largos), por eso ufw simplifica en Ubuntu.

Firewall de Windows: Si tu instancia es Windows, el Windows Firewall podría bloquear conexiones entrantes. AWS cuando lanza un Windows Server, creo que añade excepciones para RDP y quizás ICMP. Pero si instalas un servicio web en Windows, debes abrirlo también en el firewall de Windows (o desactivarlo en dev, aunque en prod es mejor configurarlo). Eso se hace vía la interfaz gráfica o netsh advfirewall.

¿Cómo saber si es el firewall local causando un problema? Supongamos que tu SG de AWS está bien (puerto abierto), tu app en la instancia está corriendo, pero no responde externamente. Puedes hacer una prueba: desde dentro de la instancia, intenta conectar a su propio puerto (ej curl http://localhost:8080). Si internamente responde, pero externamente no, casi seguro es firewall (local o SG). Ya descartamos SG (lo abriste), entonces probablemente es el OS. Puedes temporariamente desactivar ufw (sudo ufw disable) y probar de fuera de nuevo. Si de pronto funciona, ya sabes que era el firewall local. Entonces re-activalo (sudo ufw enable) y mejor configura las reglas correctamente (sudo ufw allow 8080, etc.).

En entornos AWS, muchos optan por dejar el firewall del OS apagado y controlar todo con Security Groups. Esto es aceptable en nubes bien configuradas. Pero en otros contextos (o por normativa de seguridad), se pueden usar ambos. Para efectos de nuestras prácticas, lo importante es: si abres puerto en AWS y aún así no accedes, piensa en el firewall del sistema operativo como posible causa. Por ejemplo, en Ubuntu, ufw status te mostrará qué está permitido. En Amazon Linux (que no tiene ufw), ver sudo iptables -L te listará las reglas iptables (suelen estar abiertas, exceptuando tal vez ICMP/ping en algunas).

Recapitulando:
	•	Un firewall local permite control granular en la propia máquina (por ejemplo, podrías limitar que solo cierta IP acceda a cierto puerto, similar a SG).
	•	Por defecto, AWS Linux AMIs tienden a no restringir (excepto servicios concretos). Pero Ubuntu sí tiene la herramienta disponible.
	•	Si lo activas, asegúrate de permitir SSH antes, pues de lo contrario te “cortas la rama donde estás sentado” y no podrás reconectar sin consola out-of-band.
	•	La combinación de SG + firewall OS es doble capa de seguridad. Si algo falla, debes revisar ambos.

(Ejemplo final: Configuras un servidor web en tu instancia Ubuntu. Abres el puerto 80 en el Security Group, pero olvidaste que ufw estaba activo y solo permitía SSH. Resultado: nadie puede cargar la página. Solución: sudo ufw allow 80 y listo, el firewall del OS permitirá tráfico web. Moral: siempre revisar el firewall local si los puertos parecen cerrados pese a la configuración cloud correcta.)



Glosario básico
	•	Sistema Operativo (SO): Software fundamental que gestiona el hardware de un computador y ofrece servicios a las aplicaciones. Ejemplos: Windows, Linux, Android.
	•	Servidor: Ordenador (físico o virtual) que provee servicios o recursos a otros (clientes). En la nube, una instancia EC2 actúa como servidor virtual.
	•	Instancia (EC2): Máquina virtual ejecutándose en AWS (Elastic Compute Cloud). Equivale a un servidor virtual que lanzamos, elegimos su tipo (HW virtual) y AMI (OS).
	•	Terminal/Consola (CLI): Interfaz de línea de comandos. Permite al usuario interactuar con el SO escribiendo comandos de texto. Usada en cloud para administrar instancias sin entorno gráfico.
	•	SSH (Secure Shell): Protocolo para conexión segura (cifrada) a una terminal de un sistema remoto. Utilizado para acceder a instancias Linux en AWS de forma remota.
	•	Clave pública/privada (SSH Key Pair): Par de claves criptográficas usado para autenticación SSH sin contraseña. La clave pública se guarda en la instancia; la clave privada la posee el usuario y debe mantenerla secreta ￼. Juntas verifican la identidad del que se conecta.
	•	Usuario root: Usuario administrador principal en sistemas UNIX/Linux, con permisos totales. En AWS, el acceso root remoto suele deshabilitarse por seguridad, usando en su lugar otro usuario con sudo.
	•	Sudo: Comando en Linux para ejecutar acciones como administrador (root) temporalmente. Requiere estar autorizado (usuario en el grupo sudoers). Permite instalar software, modificar config del sistema, etc.
	•	Máquina Virtual (VM): Entorno computacional simulado por software que emula un computador completo. Corre un OS invitado y aplicaciones, aislado de otras VM aunque compartiendo hardware físico.
	•	Hipervisor: Software que habilita la virtualización, permitiendo múltiples VM en un mismo físico. Administra los recursos para cada VM. Tipo 1 corre sobre hardware directo (ej. Xen, Hyper-V); Tipo 2 sobre un OS anfitrión (ej. VirtualBox).
	•	Contenedor: Paquete de software que aísla una aplicación con sus dependencias, sin incluir un OS completo. Varios contenedores comparten el mismo kernel del OS host, manteniendo aislamiento a nivel de proceso. Ejemplo: Docker container.
	•	Docker: Plataforma popular para creación y gestión de contenedores. Usa imágenes (Docker images) para instanciar contenedores portables.
	•	Kubernetes: Sistema de orquestación de contenedores. Gestiona despliegue, escalado y mantenimiento de múltiples contenedores en cluster de servidores.
	•	AMI (Amazon Machine Image): Imagen de máquina de Amazon. Plantilla que contiene un sistema operativo y software para lanzar instancias EC2 ￼. Define el contenido inicial de la instancia (OS, datos en disco). Ej.: “AMI Amazon Linux 2”.
	•	Security Group (SG): Firewall virtual de AWS a nivel de instancia o interfaz de red. Conjunto de reglas que permiten o deniegan tráfico entrante/saliente basado en puertos/protocolos/IPs. Por defecto bloquea todo entrante no autorizado.
	•	Firewall (cortafuegos) del OS: Mecanismo de filtrado de tráfico dentro del sistema operativo. En Linux, típicamente iptables (con ufw o firewalld como interfaz); en Windows, Windows Firewall. Puede bloquear conexiones entrantes si no se configuran reglas, independientemente del SG.
	•	UFW (Uncomplicated FireWall): Herramienta sencilla para gestionar el firewall en Ubuntu y otras distros. Por defecto, viene inactive (inactivo) hasta que se habilita. Si se habilita, su política predeterminada es deny (incoming), requiriendo permitir explícitamente puertos necesarios (ej. ufw allow 22).
	•	Proceso: Instancia en ejecución de un programa en un sistema operativo. Tiene un ID, un propietario, consumo de recursos. Varios procesos pueden correr concurrentemente.
	•	Servicio/Daemon: Proceso en segundo plano que suele iniciarse con el sistema y no tiene interacción directa de usuario (ej.: servidor web, servicio SSH). Proporciona funciones contínuas (escuchar conexiones, ejecutar tareas programadas, etc.). En Linux, muchos se gestionan via systemd (systemctl).


