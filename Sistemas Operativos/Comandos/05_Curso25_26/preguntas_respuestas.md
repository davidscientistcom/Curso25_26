He leído todo el material. Ahora genero la batería completa de 100 preguntas y respuestas. 


# 📚 Batería de 100 Preguntas y Respuestas — Linux CLI

Basada en tus materiales de prácticas: navegación, permisos, búsqueda, tuberías, procesos, disco, compresión y gestión de usuarios.



## 🟢 NIVEL BÁSICO — 50 preguntas



**P1. ¿Qué comando muestra en qué directorio te encuentras actualmente?**

> `pwd` (Print Working Directory). Siempre que te pierdas, escribe `pwd` y verás la ruta completa desde la raíz. Ejemplo de salida: `/home/usuario` 


**P2. ¿Para qué sirve el comando `ls`?**

> Lista el contenido del directorio actual. Sin opciones muestra los nombres; con `-l` muestra detalles como permisos, propietario, tamaño y fecha de modificación. 


**P3. ¿Qué diferencia hay entre `ls -a` y `ls -l`?**

> `-a` muestra **todos** los archivos incluyendo los ocultos (los que empiezan por `.`). `-l` muestra el contenido en **formato largo** con detalles. Puedes combinarlos con `ls -la` para ver ambas cosas a la vez. 


**P4. ¿Cómo te mueves al directorio `/tmp`?**

> Con `cd /tmp`. Esto usa una **ruta absoluta** (empieza en `/`) y funciona desde cualquier lugar del sistema. 


**P5. ¿Qué hace `cd ..`?**

> Sube un nivel en la jerarquía de directorios: va al **directorio padre**. Si estás en `/home/usuario/documentos`, te llevará a `/home/usuario`. 


**P6. ¿Cómo vuelves al directorio home del usuario de forma rápida?**

> Con `cd ~` o simplemente `cd` sin argumentos. El símbolo `~` siempre representa el directorio personal del usuario actual. 


**P7. ¿Para qué sirve `cd -`?**

> Vuelve al **último directorio visitado**. Es muy útil para alternar entre dos carpetas. Si estabas en `/var/log` y te fuiste al home, `cd -` te regresa a `/var/log`. 


**P8. ¿Qué es una ruta absoluta? Da un ejemplo.**

> Es la dirección completa de un archivo desde la raíz `/`. Siempre empieza con `/` y funciona desde cualquier lugar. Ejemplo: `/home/usuario/documentos/informe.txt` 


**P9. ¿Qué es una ruta relativa? Da un ejemplo.**

> Es la ubicación de un archivo **en relación al directorio actual**. No empieza con `/`. Ejemplo: si estás en `/home/usuario`, puedes usar `documentos/informe.txt` en lugar de la ruta absoluta completa. 


**P10. ¿Qué representan `.` y `..` en una ruta?**

> `.` representa el **directorio actual** y `..` representa el **directorio padre** (un nivel arriba). Se usan en rutas relativas: `cd ../otro_directorio` sube un nivel y entra en `otro_directorio`. 


**P11. ¿Cómo creates un directorio llamado `proyectos`?**

> Con `mkdir proyectos`. El comando `mkdir` (make directory) crea el directorio en la ubicación actual. 


**P12. ¿Qué opción de `mkdir` permite crear directorios padre que no existen?**

> La opción `-p` (parent). Por ejemplo, `mkdir -p proyectos/2026/enero` crea los tres niveles de una sola vez aunque ninguno exista. 


**P13. ¿Cómo creas varios directorios a la vez?**

> Listándolos separados por espacios: `mkdir carpeta1 carpeta2 carpeta3`. También puedes usar expansión de llaves: `mkdir carpeta{1..3}` para crear `carpeta1`, `carpeta2` y `carpeta3`. 


**P14. ¿Para qué sirve el comando `touch`?**

> Crea un archivo vacío si no existe, o actualiza la fecha de modificación si ya existe. Ejemplo: `touch notas.txt` crea el archivo `notas.txt` vacío. 


**P15. ¿Cómo creas tres archivos de texto vacíos con un solo comando?**

> `touch archivo1.txt archivo2.txt archivo3.txt`. O usando expansión: `touch archivo{1..3}.txt` 


**P16. ¿Qué hace `rm archivo.txt`?**

> Elimina el archivo `archivo.txt` de forma permanente. En Linux, `rm` **no manda archivos a la papelera**, los borra directamente. 


**P17. ¿Por qué es útil `rm -i`?**

> Porque pide **confirmación** antes de eliminar cada archivo. Es más seguro que `rm` directo cuando no estás seguro de qué eliminas. El sistema pregunta `remove 'archivo.txt'? y/n`. 


**P18. ¿Cómo eliminas un directorio que ya está vacío?**

> Con `rmdir nombre_directorio`. Solo funciona si el directorio está completamente vacío; si tiene contenido, da error. 


**P19. ¿Cómo eliminas un directorio con todo su contenido dentro?**

> Con `rm -r nombre_directorio`. La `-r` significa recursivo y elimina el directorio y todo lo que hay dentro. Con `rm -rf` además fuerza la eliminación sin preguntar (¡úsalo con mucho cuidado!). 


**P20. ¿Qué muestra `ls -lh`?**

> Lista los archivos en formato largo con tamaños **legibles para humanos** (Human-readable): muestra KB, MB, GB en lugar de bytes crudos. Ejemplo: `4.0K` en lugar de `4096`. 


**P21. ¿Cómo subes dos niveles de directorio de una sola vez?**

> Con `cd ../..`. Cada `..` sube un nivel y se encadenan con `/`. Puedes subir tres niveles con `cd ../../..`. 


**P22. ¿Qué hace `echo "Hola Mundo"`?**

> Imprime el texto `Hola Mundo` en la terminal. `echo` se usa para mostrar texto, variables y también para escribir contenido en archivos con redirecciones. 


**P23. ¿Cómo ves el valor de la variable de entorno `$HOME`?**

> Con `echo $HOME`. Muestra la ruta del directorio home del usuario actual, generalmente `/home/nombreusuario`. 


**P24. ¿Qué hace el operador `>` en `ls > salida.txt`?**

> **Redirige** la salida del comando `ls` al archivo `salida.txt`. Si el archivo ya existe, **lo sobrescribe** completamente. Si no existe, lo crea. 


**P25. ¿Qué diferencia hay entre `>` y `>>`?**

> `>` sobrescribe el archivo (borra el contenido anterior). `>>` **añade** el nuevo contenido al final del archivo sin borrar lo que ya había. Ejemplo: `echo "línea" >> log.txt` siempre añade. 


**P26. ¿Qué hace `cat archivo.txt`?**

> Muestra el contenido completo del archivo en la terminal. También puede concatenar varios archivos: `cat archivo1.txt archivo2.txt` los muestra seguidos. 


**P27. ¿Qué hace `cat -n archivo.txt`?**

> Muestra el contenido del archivo con **números de línea** delante de cada una. Muy útil para referenciar líneas concretas al programar o depurar scripts. 


**P28. ¿Para qué sirve `head archivo.txt`?**

> Muestra las **primeras 10 líneas** del archivo por defecto. Con `-n` puedes especificar cuántas: `head -n 5 archivo.txt` muestra las 5 primeras líneas. 


**P29. ¿Para qué sirve `tail archivo.txt`?**

> Muestra las **últimas 10 líneas** del archivo. Muy usado para revisar logs recientes. Con `tail -f` además sigue el archivo en tiempo real mostrando nuevas líneas según se añaden. 


**P30. ¿Qué es el autocompletado con Tab y para qué sirve?**

> Al pulsar `Tab` el terminal completa automáticamente el nombre de archivos o directorios. Si hay varias opciones, pulsas `Tab` dos veces para verlas todas. Evita errores de escritura y acelera mucho el trabajo. 


**P31. ¿Qué hace `grep "error" archivo.log`?**

> Busca y muestra todas las líneas del archivo que contienen la palabra `error`. Es sensible a mayúsculas por defecto. 


**P32. ¿Qué opción de `grep` ignora mayúsculas y minúsculas?**

> `-i` (insensitive). Con `grep -i "error" archivo.log` encuentra tanto `error`, `Error`, `ERROR` y cualquier combinación. 


**P33. ¿Cómo cuento cuántas veces aparece una palabra en un archivo con `grep`?**

> Con la opción `-c` (count): `grep -c "error" archivo.log` devuelve un número entero con el total de líneas que contienen la palabra. 


**P34. ¿Para qué sirve `grep -v`?**

> Invierte la búsqueda: muestra las líneas que **NO** contienen el patrón. `grep -v "INFO" archivo.log` muestra todo excepto las líneas de información. 


**P35. ¿Qué hace `grep -n`?**

> Muestra el **número de línea** junto a cada coincidencia. Muy útil para localizar exactamente dónde está un patrón en un archivo largo: `grep -n "BUG" codigo.py`. 


**P36. ¿Qué hace el comodín `*` en `ls *.txt`?**

> El asterisco `*` representa **cualquier número de caracteres**. `ls *.txt` lista todos los archivos del directorio actual que terminen en `.txt`. 


**P37. ¿Qué diferencia hay entre `*` y `?` como comodines?**

> `*` sustituye **cero o más** caracteres. `?` sustituye exactamente **un solo** carácter. `archivo?.txt` coincide con `archivo1.txt` pero no con `archivo12.txt`. 


**P38. ¿Qué hace `ls archivo[1-3].txt`?**

> Los corchetes `[]` permiten especificar un rango o conjunto de caracteres. Esto lista `archivo1.txt`, `archivo2.txt` y `archivo3.txt` pero no `archivo4.txt`. 


**P39. ¿Cómo listas recursivamente todo el contenido de un directorio y sus subdirectorios?**

> Con `ls -R`. Muestra el contenido del directorio actual y de todos los subdirectorios de forma recursiva, nivel por nivel. 


**P40. ¿Qué hace `ls -t`?**

> Ordena los archivos por **fecha de modificación**, mostrando los más recientes primero. Muy útil para ver qué archivos se han modificado recientemente. 


**P41. ¿Qué información muestra `ls -l` al principio de cada línea?**

> Los **permisos**: 10 caracteres. El primero indica el tipo (`-` archivo, `d` directorio, `l` enlace). Los siguientes 9 son tres grupos de `rwx` (lectura, escritura, ejecución) para propietario, grupo y otros. 


**P42. ¿Qué significa `chmod` y para qué se usa?**

> `chmod` (Change Mode) modifica los **permisos** de acceso a archivos y directorios: quién puede leer, escribir o ejecutar un archivo. 


**P43. ¿Cuánto vale cada permiso en formato numérico?**

> Lectura (r) = **4**, escritura (w) = **2**, ejecución (x) = **1**. Se suman para obtener el valor de cada grupo: `rwx` = 7, `rw-` = 6, `r-x` = 5, `r--` = 4. 


**P44. ¿Qué permisos da `chmod 644 archivo.txt`?**

> Propietario: `rw-` (6 = leer + escribir). Grupo: `r--` (4 = solo leer). Otros: `r--` (4 = solo leer). Es el permiso estándar para archivos de texto normales. 


**P45. ¿Qué hace `chmod u+x script.sh`?**

> Añade (`+`) permiso de ejecución (`x`) al propietario (`u` de *user*). Sin este permiso, no puedes ejecutar un script de shell aunque seas el dueño. 


**P46. ¿Qué hace `chmod o-w archivo.txt`?**

> Quita (`-`) el permiso de escritura (`w`) a los otros usuarios (`o` de *others*): cualquiera que no sea el propietario ni del grupo no podrá modificar el archivo. 


**P47. ¿Qué hace `chown usuario archivo.txt`?**

> Cambia el **propietario** del archivo al usuario indicado. Generalmente requiere `sudo`. Con `chown usuario:grupo` puedes cambiar propietario y grupo a la vez. 


**P48. ¿Cómo ves los procesos que están corriendo actualmente?**

> Con `ps` para ver solo tus procesos o `ps aux` para ver **todos los procesos del sistema** con detalle (usuario, PID, % CPU, % memoria, etc.). 


**P49. ¿Qué información muestra `df -h`?**

> Muestra el **espacio libre y usado** en cada partición del sistema de archivos, en formato legible para humanos (KB, MB, GB). Útil para saber si el disco se está llenando. 


**P50. ¿Para qué sirve `wc -l archivo.txt`?**

> Cuenta el número de **líneas** del archivo. `wc` (word count) también tiene `-w` para palabras y `-c` para caracteres. Muy usado en combinación con tuberías: `grep "error" log.txt | wc -l`.  


## 🟡 NIVEL MEDIO — 30 preguntas



**P51. ¿Cómo combinas una tubería `|` con `grep` para filtrar la salida de `ps aux`?**

> `ps aux | grep bash` muestra solo los procesos que contienen la palabra `bash`. El operador `|` (pipe) pasa la salida de un comando como entrada del siguiente.  


**P52. ¿Qué hace `cat servidor.log | grep "ERROR" | wc -l`?**

> Es una cadena de tuberías: `cat` muestra el log, `grep` filtra las líneas con "ERROR" y `wc -l` **cuenta** cuántas hay. Resultado: un número entero con el total de errores. 


**P53. ¿Cómo guardas en un archivo el listado detallado de un directorio?**

> `ls -la > listado.txt`. La redirección `>` envía la salida del comando al archivo en lugar de a la pantalla. Si quieres añadir sin borrar, usa `ls -la >> listado.txt`. 


**P54. ¿Qué hace `grep "^ERROR" logs.txt`?**

> El `^` en una expresión regular indica **inicio de línea**. Este comando busca solo las líneas que **empiezan** exactamente con `ERROR`, no las que contienen ERROR en cualquier posición. 


**P55. ¿Qué hace `grep "iniciado$" logs.txt`?**

> El `$` indica **final de línea**. Encuentra las líneas que **terminan** con la palabra `iniciado`. Es una expresión regular básica muy útil para filtrar logs. 


**P56. ¿Cómo buscas un archivo llamado `main.py` dentro de toda tu carpeta home?**

> `find ~ -name "main.py"`. El comando `find` busca de forma recursiva. `~` indica que empiece desde el home, `-name` especifica el nombre exacto. 


**P57. ¿Cómo buscas todos los archivos `.txt` en el directorio actual y sus subdirectorios?**

> `find . -name "*.txt"`. El punto `.` indica el directorio actual, y el comodín `*` en el nombre permite cualquier nombre con extensión `.txt`. 


**P58. ¿Cómo buscas solo directorios (no archivos) con `find`?**

> `find . -type d`. La opción `-type d` filtra solo directorios. Para archivos regulares se usa `-type f`. Ejemplo: `find ~ -type d -name "proyecto*"` busca directorios que empiezan por "proyecto". 


**P59. ¿Cómo buscas archivos mayores de 10 MB con `find`?**

> `find . -size +10M`. El `+` significa "mayor que". Las unidades son: `c` (bytes), `k` (KB), `M` (MB), `G` (GB). Para menor que: `find . -size -10M`. 


**P60. ¿Cómo excluyes el directorio `node_modules` en una búsqueda con `find`?**

> `find . -name "*.js" -not -path "*/node_modules/*"`. La opción `-not -path` excluye los resultados cuya ruta coincida con el patrón dado. 


**P61. ¿Qué hace `find . -name "*.log" -exec rm {} \;`?**

> Encuentra todos los archivos `.log` en el directorio actual y ejecuta `rm` en cada uno. `{}` es un placeholder que se reemplaza con cada resultado. El `\;` termina el comando `-exec`. 


**P62. ¿Qué hace `chmod -R 755 directorio/`?**

> Cambia los permisos de forma **recursiva** (`-R`): aplica `755` al directorio y a todos los archivos y subdirectorios que contiene. Útil para configurar proyectos completos. 


**P63. ¿Qué significa el permiso `chmod 755`?**

> Propietario: `rwx` (7). Grupo: `r-x` (5). Otros: `r-x` (5). Es el permiso estándar para **scripts ejecutables y directorios**: el dueño puede modificar, todos pueden leer y ejecutar/entrar. 


**P64. ¿Qué significa el permiso `chmod 700`?**

> Propietario: `rwx` (7). Grupo: `---` (0). Otros: `---` (0). Solo el propietario tiene acceso total. Nadie más puede ni siquiera leer el archivo. Ideal para scripts privados. 


**P65. ¿Qué hace `grep -A 2 "BUG" codigo.txt`?**

> Muestra cada línea que contiene "BUG" más las **2 líneas después** (A de *After*). También existe `-B 2` (Before) y `-C 2` (Context, que muestra antes y después). 


**P66. ¿Cómo buscas múltiples patrones con `grep`?**

> Con `-E` y el operador `|`: `grep -E "ERROR|WARNING" logs.txt`. O con la opción `-e` repetida: `grep -e "ERROR" -e "WARNING" logs.txt`. Ambas formas son equivalentes.  


**P67. ¿Qué hace `sort archivo.txt`?**

> Ordena las líneas del archivo **alfabéticamente**. Con `-r` ordena en reversa, con `-n` ordena numéricamente (importante para números: sin `-n`, el 10 va antes del 2). 


**P68. ¿Qué hace `sort | uniq` y cuándo se usa?**

> `sort` ordena las líneas (necesario para que `uniq` funcione) y `uniq` elimina las **líneas duplicadas consecutivas**. Juntos eliminan todos los duplicados de un archivo o salida. 


**P69. ¿Qué hace `du -sh directorio/`?**

> Muestra el **tamaño total** que ocupa el directorio en disco, en formato legible. `-s` (summary) muestra solo el total, sin desglosar subdirectorios. `-h` lo hace legible (KB, MB, GB). 


**P70. ¿Cómo ves qué subdirectorios son los más grandes dentro de tu home?**

> `du -h --max-depth=1 ~ | sort -hr`. Muestra el uso de cada subdirectorio del primer nivel ordenado de mayor a menor. Ideal para encontrar qué carpeta ocupa más espacio.  


**P71. ¿Qué hace `tail -f /var/log/syslog`?**

> Sigue el archivo en tiempo real, mostrando nuevas líneas según se añaden. La `-f` (follow) es esencial para monitorizar logs de sistemas o aplicaciones en producción. 


**P72. ¿Cómo creas un enlace simbólico a un directorio?**

> `ln -s /ruta/directorio_original nombre_enlace`. El enlace simbólico actúa como un acceso directo: si el original se borra, el enlace queda roto (a diferencia de los enlaces duros). 


**P73. ¿Qué diferencia hay entre un enlace simbólico y un enlace duro?**

> El enlace **simbólico** apunta al *nombre* del archivo (se rompe si se borra el original). El enlace **duro** apunta al mismo *inode* (bloque de datos): si se borra el original, el enlace duro sigue funcionando porque ambos comparten los datos. 


**P74. ¿Cómo creas un archivo comprimido `.tar.gz` de un directorio?**

> `tar -czvf archivo.tar.gz directorio/`. Flags: `-c` (crear), `-z` (compresión gzip), `-v` (verbose, muestra archivos), `-f` (nombre del archivo). Es el formato más usado en Linux. 


**P75. ¿Cómo extraes un archivo `.tar.gz`?**

> `tar -xzvf archivo.tar.gz`. Cambia `-c` (create) por `-x` (extract). Para extraer en un directorio específico: `tar -xzvf archivo.tar.gz -C /ruta/destino/`. 


**P76. ¿Cómo ves el contenido de un `.tar.gz` sin extraerlo?**

> `tar -tvf archivo.tar.gz`. La opción `-t` (list) lista el contenido del archivo comprimido sin descomprimirlo. Muy útil para verificar qué hay dentro antes de extraer. 


**P77. ¿Qué hace `kill -9 1234`?**

> Envía la señal `KILL` (señal 9) al proceso con PID 1234, forzando su **terminación inmediata**. A diferencia de `kill 1234` (señal TERM), el proceso no puede ignorarla ni limpiar recursos antes de morir. 


**P78. ¿Cómo creates un usuario en Linux y lo asignas a un grupo?**

> `sudo useradd -m -g nombre_grupo -s /bin/bash nombre_usuario`. `-m` crea la carpeta home, `-g` asigna el grupo principal, `-s` define el shell. Luego `sudo passwd nombre_usuario` para poner contraseña. 


**P79. ¿Cómo añades un usuario a un grupo secundario sin quitarlo de los actuales?**

> `sudo usermod -aG nombre_grupo nombre_usuario`. La opción `-a` (append) es crucial: sin ella, el usuario se quedaría **solo** en el nuevo grupo, perdiendo los anteriores. 


**P80. ¿Cómo compruebas a qué grupos pertenece un usuario?**

> Con `id nombre_usuario` (muestra UID, GID y todos los grupos) o con `groups nombre_usuario` (solo lista los nombres de los grupos). 


## 🔴 NIVEL COMPLEJO — 20 preguntas



**P81. ¿Cómo creas una estructura de directorios completa de proyecto con un solo comando?**

> `mkdir -p proyecto/{src,docs,tests,config}`. Las llaves `{}` con la opción `-p` permiten crear múltiples subdirectorios en paralelo. Equivale a cuatro comandos `mkdir` en uno. 


**P82. Explica qué hace esta cadena: `ps aux | grep python | sort -k 4 -nr`**

> `ps aux` lista todos los procesos; `grep python` filtra solo los que contienen "python"; `sort -k 4 -nr` ordena por la columna 4 (% de memoria) de forma numérica (`-n`) y en reversa (`-r`), dejando los que más memoria consumen arriba. 


**P83. ¿Qué hace `find . -name "*.tmp" -exec rm {} \;` y cuál es su riesgo?**

> Busca todos los archivos `.tmp` en el directorio actual y los **elimina directamente**. El riesgo es que `rm` no pregunta confirmación. Para mayor seguridad usa `-ok` en lugar de `-exec`, que pide confirmación por cada archivo. 


**P84. ¿Cómo harías un backup comprimido con la fecha actual en el nombre?**

> `tar -czvf backup_$(date +%Y%m%d).tar.gz directorio/`. La sustitución de comandos `$()` inserta el resultado de `date +%Y%m%d` (ej: `20260221`) en el nombre del archivo resultante. 


**P85. Explica qué permisos da `chmod 770` y en qué escenario es apropiado.**

> Propietario: `rwx` (7), Grupo: `rwx` (7), Otros: `---` (0). Es ideal para **carpetas departamentales**: los miembros del grupo tienen acceso total, pero nadie fuera del grupo puede ni siquiera listar el contenido. Se usa en entornos multiusuario como servidores corporativos. 


**P86. ¿Cómo configuras una carpeta para que todos puedan leer pero solo el propietario pueda escribir?**

> `chmod 755 directorio`. El propietario tiene `rwx` (7), grupo y otros tienen `r-x` (5): pueden leer y entrar al directorio, pero no crear ni borrar archivos dentro. 


**P87. ¿Cómo encontrarías todos los archivos con permisos de escritura para cualquier usuario (`o+w`) en un directorio?**

> `find . -type f -perm -002`. El `-perm -002` busca archivos donde el bit de escritura para "otros" (`002`) está activo. Es una auditoría de seguridad básica. 


**P88. Explica cómo funciona un script de rotación de logs usando las herramientas aprendidas.**

> El script usa `tar -czvf` para comprimir los logs actuales con fecha en el nombre, `>` o `>` vacío para limpiar los logs activos, y `find -mtime +30 -exec rm {}` para eliminar archivos comprimidos más antiguos de 30 días. Este patrón es estándar en administración de sistemas. 


**P89. ¿Cómo rediriges los errores de un comando a un archivo separado?**

> Con `2>`: `ls /directorio_inexistente 2> errores.txt`. El descriptor `2` es `stderr` (errores estándar). Para capturar tanto salida normal como errores: `comando > salida.txt 2> errores.txt` o `comando &> todo.txt`. 


**P90. ¿Cómo extraerías las IPs únicas de un log de acceso web?**

> `cat access.log | cut -d' ' -f1 | sort | uniq > ips_unicas.txt`. `cut -d' ' -f1` extrae el primer campo (la IP), `sort` las ordena (necesario para `uniq`) y `uniq` elimina duplicados.  


**P91. ¿Cómo creas un script ejecutable de shell y lo ejecutas correctamente?**

> 1) Crea el archivo: `cat > script.sh` con el shebang `#!/bin/bash`. 2) Dale permisos: `chmod +x script.sh`. 3) Ejecútalo: `./script.sh` (el `./` indica que está en el directorio actual). Sin `./`, el sistema no lo encontrará a menos que esté en el `$PATH`. 


**P92. ¿Cómo añades un directorio al PATH de forma permanente?**

> Añades `export PATH=$PATH:/tu/nuevo/directorio` al archivo `~/.bashrc` (para bash) o `~/.zshrc` (para zsh). Luego ejecutas `source ~/.bashrc` para aplicar los cambios sin reiniciar el terminal. 


**P93. Explica la diferencia entre `kill`, `killall` y `pkill`.**

> `kill PID` termina un proceso por su **número de proceso**. `killall nombre` termina todos los procesos con ese **nombre exacto** (ej: `killall firefox`). `pkill patron` termina procesos cuyo nombre **coincida con un patrón** (más flexible). Los tres envían SIGTERM por defecto; con `-9` envían SIGKILL. 


**P94. ¿Cómo implementarías un sistema de deployment con enlaces simbólicos?**

> Se mantienen múltiples versiones en `releases/v1.0`, `releases/v2.0`, etc. El directorio `current` es un enlace simbólico: `ln -s releases/v1.0 current`. Para actualizar, simplemente se cambia el enlace: `rm current && ln -s releases/v2.0 current`. Así el rollback es instantáneo. 


**P95. ¿Qué hace `grep -r "clave_secreta" /etc` y en qué caso es útil?**

> Busca la cadena `clave_secreta` de forma recursiva en todos los archivos de `/etc`. Es útil en **auditorías de seguridad** para detectar contraseñas en claro dentro de archivos de configuración del sistema. 


**P96. ¿Cómo crearías un reporte del sistema combinando varios comandos en un solo script?**

> Usando `echo` y `>>` para ir añadiendo secciones al reporte:
> ```bash
> echo "=== DISCO ===" > reporte.txt
> df -h >> reporte.txt
> echo "=== PROCESOS ===" >> reporte.txt
> ps aux --sort=-%cpu | head -10 >> reporte.txt
> echo "=== MEMORIA ===" >> reporte.txt
> free -h >> reporte.txt
> ```
> Cada `>>` añade sin borrar lo anterior. 


**P97. ¿Cómo configurarías permisos en un entorno multiusuario tipo empresa con departamentos aislados?**

> 1) Crea grupos por departamento: `groupadd informatica`. 2) Crea usuarios asignándolos a su grupo: `useradd -m -g informatica usuario`. 3) Crea carpetas departamentales: `mkdir /empresa/informatica`. 4) Asigna propietario y grupo: `chown root:informatica /empresa/informatica`. 5) Aplica `chmod 770` para que solo el grupo acceda. El `jefe` se añade a todos los grupos con `usermod -aG`. 


**P98. ¿Qué hace `du -ah | sort -hr | head -10` y cómo lo interpretas?**

> `du -ah` lista todos los archivos y directorios con su tamaño. `sort -hr` los ordena por tamaño de mayor a menor en formato legible. `head -10` muestra solo los 10 primeros. El resultado es la lista de los **10 elementos más pesados** del disco, perfecta para diagnóstico de espacio. 


**P99. ¿Cómo automatizarías la búsqueda y compresión de logs antiguos con un solo one-liner?**

> `find /var/log -name "*.log" -mtime +7 -exec gzip {} \;`. Busca archivos `.log` modificados hace más de 7 días y comprime cada uno con `gzip`. En producción se suele combinar con `cron` para que se ejecute automáticamente cada noche. 


**P100. ¿Cómo escribirías un script completo que verifique si los grupos, usuarios, carpetas y permisos de una práctica están correctamente configurados?**

> El script usaría `grep -q "^grupo:" /etc/group` para verificar grupos, `id usuario &>/dev/null` para usuarios, `[ -d /ruta/carpeta ]` para carpetas, y `stat -c "%a" /ruta` para comparar permisos numéricos con los esperados. Para cada comprobación imprime `✓` (éxito) o `✗` (fallo), como el script `verificar.sh` de la práctica de TechCorp. 

