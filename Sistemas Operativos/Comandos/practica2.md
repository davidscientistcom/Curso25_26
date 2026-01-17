# Guía Completa de Navegación y Gestión del Sistema de Archivos Linux

## **PRÁCTICA 2: Permisos, Búsqueda, Tuberías y Redirecciones**

***

## **Introducción: Elevando tu Nivel**

En la Práctica 1 dominaste la navegación básica del sistema de archivos. Ahora aprenderás a **controlar quién puede hacer qué** con tus archivos, a **encontrar información rápidamente** y a **combinar comandos** para crear flujos de trabajo potentes. Estos son los comandos que separan a un usuario casual de un administrador de sistemas profesional. [digitalocean](https://www.digitalocean.com/community/tutorials/how-to-set-permissions-linux)

**Recuerda:** En cada ejercicio seguirás practicando `cd`, `pwd`, `ls`, `mkdir`, `touch` y `rm` de la Práctica 1. La repetición es la clave del dominio. [baeldung](https://www.baeldung.com/linux/grep-pipe-search-term)

***

## **1. Sistema de Permisos en Linux**

### **1.1 Entendiendo ls -l**

Cuando ejecutas `ls -l`, ves información crítica sobre permisos: [redhat](https://www.redhat.com/en/blog/linux-file-permissions-explained)

```bash
$ ls -l archivo.txt
-rw-r--r-- 1 usuario grupo 1234 Jan 15 10:30 archivo.txt
```

**Desglose:**
```
-rw-r--r--  1  usuario  grupo  1234  Jan 15 10:30  archivo.txt
│││││││││││  │    │       │      │       │           │
│││││││││││  │    │       │      │       │           └─ Nombre
│││││││││││  │    │       │      │       └─ Fecha modificación
│││││││││││  │    │       │      └─ Tamaño (bytes)
│││││││││││  │    │       └─ Grupo propietario
│││││││││││  │    └─ Usuario propietario
│││││││││││  └─ Número de enlaces
│└┴┴└┴┴└┴┴─ Permisos (explicados abajo)
└─ Tipo: - (archivo), d (directorio), l (enlace)
```

### **1.2 Los Tres Niveles de Permisos**

Los permisos se dividen en **tres grupos de tres caracteres**: [digitalocean](https://www.digitalocean.com/community/tutorials/how-to-set-permissions-linux)

```
-rw-r--r--
 │  │  │
 │  │  └─ Others (otros usuarios)
 │  └─ Group (grupo propietario)
 └─ User/Owner (propietario)
```

Cada grupo tiene **tres permisos posibles**: [linuxconcept](https://linuxconcept.com/tools/chmod-explainer-tool)

| Símbolo | Permiso | Valor Numérico | Significado en Archivo | Significado en Directorio |
|---------|---------|----------------|------------------------|---------------------------|
| `r` | Read | 4 | Leer contenido  [linuxconcept](https://linuxconcept.com/tools/chmod-explainer-tool) | Listar archivos (`ls`)  [digitalocean](https://www.digitalocean.com/community/tutorials/how-to-set-permissions-linux) |
| `w` | Write | 2 | Modificar/eliminar  [linuxconcept](https://linuxconcept.com/tools/chmod-explainer-tool) | Crear/eliminar archivos  [digitalocean](https://www.digitalocean.com/community/tutorials/how-to-set-permissions-linux) |
| `x` | Execute | 1 | Ejecutar como programa  [linuxconcept](https://linuxconcept.com/tools/chmod-explainer-tool) | Entrar con `cd`  [digitalocean](https://www.digitalocean.com/community/tutorials/how-to-set-permissions-linux) |
| `-` | Sin permiso | 0 | Sin acceso  [linuxconcept](https://linuxconcept.com/tools/chmod-explainer-tool) | Sin acceso  [digitalocean](https://www.digitalocean.com/community/tutorials/how-to-set-permissions-linux) |

**Práctica 1:**
```bash
cd ~
mkdir practica2
cd practica2
touch archivo_prueba.txt
ls -l archivo_prueba.txt        # Observa los permisos
pwd                              # Confirma ubicación
```

***

## **2. chmod - Cambiar Permisos**

### **2.1 Modo Simbólico (Letras)**

**Sintaxis:** `chmod [quien][operación][permiso] archivo` [dohost](https://dohost.us/index.php/2025/07/23/changing-permissions-the-chmod-command-symbolic-and-numeric-modes/)

**Componentes:**
- **Quien:** `u` (user/owner), `g` (group), `o` (others), `a` (all) [dohost](https://dohost.us/index.php/2025/07/23/changing-permissions-the-chmod-command-symbolic-and-numeric-modes/)
- **Operación:** `+` (añadir), `-` (quitar), `=` (establecer exacto) [dohost](https://dohost.us/index.php/2025/07/23/changing-permissions-the-chmod-command-symbolic-and-numeric-modes/)
- **Permiso:** `r` (read), `w` (write), `x` (execute) [dohost](https://dohost.us/index.php/2025/07/23/changing-permissions-the-chmod-command-symbolic-and-numeric-modes/)

**Ejemplos básicos:**
```bash
# Añadir permiso de ejecución al propietario
$ chmod u+x script.sh

# Quitar permiso de escritura al grupo
$ chmod g-w archivo.txt

# Añadir lectura a otros
$ chmod o+r documento.txt

# Dar todos los permisos al propietario
$ chmod u+rwx programa.py

# Quitar todos los permisos a otros
$ chmod o-rwx secreto.txt

# Establecer permisos exactos para el propietario
$ chmod u=rw archivo.txt        # Solo lectura y escritura, sin ejecución
```

**Práctica 2:**
```bash
cd ~/practica2
touch script1.sh
ls -l script1.sh                 # Observa: -rw-r--r--
chmod u+x script1.sh            # Añade ejecución al propietario
ls -l script1.sh                 # Ahora: -rwxr--r--
chmod g+x script1.sh            # Añade ejecución al grupo
ls -l script1.sh                 # Ahora: -rwxr-xr--
chmod o-r script1.sh            # Quita lectura a otros
ls -l script1.sh                 # Ahora: -rwxr-x---
chmod a-x script1.sh            # Quita ejecución a todos
ls -l script1.sh                 # Ahora: -rw-r-----
```

### **2.2 Modo Numérico (Octales)**

Los permisos se representan con **tres dígitos** donde cada uno es la suma de: [theserverside](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/how-permissions-chmod-with-numbers-command-explained-777-rwx-unix)
- **4** = lectura (r)
- **2** = escritura (w)
- **1** = ejecución (x)

**Cálculo:**
```
rwx = 4+2+1 = 7
rw- = 4+2+0 = 6
r-x = 4+0+1 = 5
r-- = 4+0+0 = 4
-wx = 0+2+1 = 3
-w- = 0+2+0 = 2
--x = 0+0+1 = 1
--- = 0+0+0 = 0
```

**Permisos comunes:**
```bash
# 755: rwxr-xr-x (común para scripts/ejecutables)
$ chmod 755 script.sh

# 644: rw-r--r-- (común para archivos de texto)
$ chmod 644 documento.txt

# 700: rwx------ (solo el propietario tiene acceso total)
$ chmod 700 privado.sh

# 777: rwxrwxrwx (todos los permisos a todos - PELIGROSO)
$ chmod 777 archivo.txt

# 600: rw------- (solo propietario lee y escribe)
$ chmod 600 config_secreta.conf
```

**Práctica 3:**
```bash
cd ~/practica2
touch archivo1.txt archivo2.txt archivo3.txt
ls -l                            # Observa permisos por defecto
chmod 755 archivo1.txt
chmod 644 archivo2.txt
chmod 600 archivo3.txt
ls -l                            # Compara las diferencias
chmod 777 archivo1.txt
ls -l archivo1.txt               # Verifica: rwxrwxrwx
chmod 000 archivo1.txt
ls -l archivo1.txt               # Verifica: ---------
chmod 644 archivo1.txt           # Restaura permisos normales
ls -l
```

### **2.3 chmod Recursivo**

Para cambiar permisos de directorios y todo su contenido: [geeksforgeeks](https://www.geeksforgeeks.org/linux-unix/chmod-command-linux/)

```bash
# Cambiar permisos recursivamente
$ chmod -R 755 directorio/

# Útil para estructuras de proyectos
$ chmod -R u+w proyecto/        # Dar escritura al propietario en todo
```

**Práctica 4:**
```bash
cd ~/practica2
mkdir -p proyecto/{src,docs,tests}
touch proyecto/src/main.py
touch proyecto/docs/readme.md
touch proyecto/tests/test.py
ls -lR proyecto/                 # Observa permisos actuales
chmod -R 755 proyecto/          # Cambia todo recursivamente
ls -lR proyecto/                 # Verifica cambios
chmod -R u=rw,g=r,o=r proyecto/ # Modo simbólico recursivo
ls -lR proyecto/
```

***

## **3. chown - Cambiar Propietario**

### **3.1 Sintaxis Básica**

**NOTA:** Generalmente necesitas `sudo` para cambiar propietarios. [geeksforgeeks](https://www.geeksforgeeks.org/linux-unix/chown-command-in-linux-with-examples/)

```bash
# Cambiar solo usuario propietario
$ sudo chown nuevo_usuario archivo.txt

# Cambiar usuario y grupo
$ sudo chown nuevo_usuario:nuevo_grupo archivo.txt

# Cambiar solo grupo (alternativa: chgrp)
$ sudo chown :nuevo_grupo archivo.txt
$ sudo chgrp nuevo_grupo archivo.txt
```

**Práctica 5:**
```bash
cd ~/practica2
touch test_owner.txt
ls -l test_owner.txt             # Anota el propietario actual
# NOTA: Los siguientes comandos requieren sudo
# Si estás en tu propio sistema, puedes probar:
sudo chown root:root test_owner.txt
ls -l test_owner.txt             # Ahora es de root
sudo chown $USER:$USER test_owner.txt
ls -l test_owner.txt             # De vuelta a ti
```

### **3.2 chown Recursivo**

```bash
# Cambiar propietario de directorio y contenido
$ sudo chown -R usuario:grupo directorio/

# Ejemplo real: transferir propiedad de proyecto web
$ sudo chown -R www-data:www-data /var/www/html/
```

**Práctica 6:**
```bash
cd ~/practica2
mkdir -p ownership_test/sub1/sub2
touch ownership_test/file1.txt
touch ownership_test/sub1/file2.txt
ls -lR ownership_test/
# Cambiar propietario recursivamente (requiere sudo)
# sudo chown -R root:root ownership_test/
# ls -lR ownership_test/
```

***

## **4. Visualización de Archivos**

### **4.1 cat - Concatenar y Mostrar**

```bash
# Mostrar contenido completo
$ cat archivo.txt

# Mostrar múltiples archivos
$ cat archivo1.txt archivo2.txt

# Mostrar con números de línea
$ cat -n archivo.txt

# Crear archivo rápidamente (Ctrl+D para terminar)
$ cat > nuevo_archivo.txt
Escribe el contenido
Línea 2
[Ctrl+D]
```

**Práctica 7:**
```bash
cd ~/practica2
cat > lista_tareas.txt
- Aprender chmod
- Dominar grep
- Practicar find
[Presiona Ctrl+D]
cat lista_tareas.txt             # Muestra contenido
cat -n lista_tareas.txt          # Con números de línea
```

### **4.2 head - Primeras Líneas**

```bash
# Mostrar primeras 10 líneas (por defecto)
$ head archivo.txt

# Mostrar primeras N líneas
$ head -n 5 archivo.txt
$ head -5 archivo.txt            # Sintaxis corta
```

### **4.3 tail - Últimas Líneas**

```bash
# Mostrar últimas 10 líneas (por defecto)
$ tail archivo.txt

# Mostrar últimas N líneas
$ tail -n 20 archivo.txt

# Seguir archivo en tiempo real (ESENCIAL para logs)
$ tail -f /var/log/syslog
```

**Práctica 8:**
```bash
cd ~/practica2
cat > numeros.txt
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
[Ctrl+D]
head numeros.txt                 # Primeras 10
head -n 3 numeros.txt           # Primeras 3
tail numeros.txt                 # Últimas 10
tail -n 3 numeros.txt           # Últimas 3
cat -n numeros.txt               # Todo con números de línea
```

### **4.4 less - Visualización Paginada**

```bash
# Abrir archivo para navegación interactiva
$ less archivo_largo.txt

# Controles dentro de less:
# Espacio    - Siguiente página
# b          - Página anterior
# /patron    - Buscar patrón
# n          - Siguiente coincidencia
# q          - Salir
```

**Práctica 9:**
```bash
cd ~/practica2
# Crear archivo largo para practicar less
seq 1 100 > numeros_largo.txt
less numeros_largo.txt
# Dentro de less:
# - Presiona Espacio varias veces
# - Presiona 'b' para retroceder
# - Escribe /50 y presiona Enter (busca "50")
# - Presiona 'q' para salir
```

***

## **5. grep - Búsqueda de Patrones en Texto**

### **5.1 Uso Básico**

```bash
# Buscar palabra en archivo
$ grep "palabra" archivo.txt

# Ignorar mayúsculas/minúsculas
$ grep -i "palabra" archivo.txt

# Mostrar número de línea
$ grep -n "palabra" archivo.txt

# Buscar recursivamente en directorios
$ grep -r "patrón" directorio/

# Invertir búsqueda (líneas que NO contienen el patrón)
$ grep -v "palabra" archivo.txt
```

**Práctica 10:**
```bash
cd ~/practica2
cat > usuarios.txt
Juan Perez admin
Maria Garcia usuario
Pedro Lopez admin
Ana Martinez usuario
Luis Rodriguez admin
[Ctrl+D]
grep "admin" usuarios.txt        # Busca "admin"
grep -n "admin" usuarios.txt     # Con números de línea
grep -i "MARIA" usuarios.txt     # Insensible a mayúsculas
grep -v "admin" usuarios.txt     # Líneas SIN "admin"
grep -c "admin" usuarios.txt     # Cuenta ocurrencias
```

### **5.2 Expresiones Regulares Básicas**

```bash
# Líneas que empiezan con patrón
$ grep "^palabra" archivo.txt

# Líneas que terminan con patrón
$ grep "palabra$" archivo.txt

# Buscar palabras completas
$ grep -w "palabra" archivo.txt

# Buscar múltiples patrones
$ grep -e "patron1" -e "patron2" archivo.txt
$ grep -E "patron1|patron2" archivo.txt
```

**Práctica 11:**
```bash
cd ~/practica2
cat > logs.txt
ERROR: conexión fallida
INFO: sistema iniciado
ERROR: archivo no encontrado
WARNING: memoria baja
INFO: usuario logueado
ERROR: timeout en la red
[Ctrl+D]
grep "^ERROR" logs.txt           # Líneas que empiezan con ERROR
grep "ERROR$" logs.txt           # No hay coincidencias
grep "iniciado$" logs.txt        # Líneas que terminan con "iniciado"
grep -E "ERROR|WARNING" logs.txt # ERROR o WARNING
grep -v "^INFO" logs.txt         # Excluir líneas que empiezan con INFO
```

### **5.3 grep con Contexto**

```bash
# Mostrar N líneas después de la coincidencia
$ grep -A 2 "patrón" archivo.txt

# Mostrar N líneas antes de la coincidencia
$ grep -B 2 "patrón" archivo.txt

# Mostrar N líneas antes y después
$ grep -C 2 "patrón" archivo.txt
```

**Práctica 12:**
```bash
cd ~/practica2
cat > codigo.txt
linea 1
linea 2
linea 3 con BUG
linea 4
linea 5
linea 6
linea 7 con BUG
linea 8
linea 9
[Ctrl+D]
grep "BUG" codigo.txt            # Solo líneas con BUG
grep -A 1 "BUG" codigo.txt       # BUG + 1 línea después
grep -B 1 "BUG" codigo.txt       # BUG + 1 línea antes
grep -C 1 "BUG" codigo.txt       # BUG + 1 antes y 1 después
```

***

## **6. find - Búsqueda de Archivos y Directorios**

### **6.1 Búsqueda por Nombre**

```bash
# Buscar por nombre exacto
$ find /ruta -name "archivo.txt"

# Buscar con patrón (case-sensitive)
$ find . -name "*.txt"

# Buscar ignorando mayúsculas/minúsculas
$ find . -iname "*.TXT"

# Buscar solo directorios
$ find . -type d -name "proyecto*"

# Buscar solo archivos
$ find . -type f -name "*.py"
```

**Práctica 13:**
```bash
cd ~/practica2
mkdir -p busqueda/{dir1,dir2,dir3}
touch busqueda/archivo1.txt
touch busqueda/archivo2.log
touch busqueda/dir1/script.sh
touch busqueda/dir2/documento.txt
touch busqueda/dir3/data.csv
cd busqueda
pwd                              # Confirma ubicación
find . -name "*.txt"            # Todos los .txt
find . -type f                   # Todos los archivos
find . -type d                   # Todos los directorios
find . -name "dir*"             # Directorios que empiezan con "dir"
cd ..
```

### **6.2 Búsqueda por Tamaño**

```bash
# Archivos mayores de 100MB
$ find . -size +100M

# Archivos menores de 10KB
$ find . -size -10k

# Archivos exactamente de 1GB
$ find . -size 1G

# Unidades: c (bytes), k (KB), M (MB), G (GB)
```

**Práctica 14:**
```bash
cd ~/practica2
# Crear archivos de diferentes tamaños
dd if=/dev/zero of=small.txt bs=1K count=1    # 1KB
dd if=/dev/zero of=medium.txt bs=1M count=1   # 1MB
dd if=/dev/zero of=large.txt bs=1M count=10   # 10MB
ls -lh *.txt                     # Ver tamaños
find . -name "*.txt" -size +500k # Archivos .txt mayores de 500KB
find . -name "*.txt" -size -2M   # Archivos .txt menores de 2MB
```

### **6.3 Búsqueda por Tiempo**

```bash
# Modificados en las últimas 24 horas
$ find . -mtime -1

# Modificados hace más de 7 días
$ find . -mtime +7

# Modificados hace exactamente 2 días
$ find . -mtime 2

# Accedidos recientemente
$ find . -atime -1
```

### **6.4 Excluir Directorios**

```bash
# Excluir directorio específico
$ find . -name "*.js" -not -path "*/node_modules/*"

# Excluir múltiples patrones
$ find . -type f -not -path "*/.*" -not -path "*/node_modules/*"
```

**Práctica 15:**
```bash
cd ~/practica2
mkdir -p proyecto/{src,tests,node_modules,build}
touch proyecto/src/app.js
touch proyecto/tests/test.js
touch proyecto/node_modules/library.js
touch proyecto/build/output.js
find proyecto/ -name "*.js"      # Todos los .js
find proyecto/ -name "*.js" -not -path "*/node_modules/*"  # Excluir node_modules
find proyecto/ -name "*.js" -not -path "*/build/*"         # Excluir build
```

### **6.5 Ejecutar Comandos con find**

```bash
# Ejecutar comando en cada resultado
$ find . -name "*.log" -exec rm {} \;

# Con confirmación
$ find . -name "*.tmp" -ok rm {} \;

# Listar detalles
$ find . -name "*.txt" -exec ls -l {} \;
```

**Práctica 16:**
```bash
cd ~/practica2
mkdir temp_files
cd temp_files
touch file1.tmp file2.tmp file3.tmp archivo.txt
ls
find . -name "*.tmp"            # Encuentra archivos .tmp
find . -name "*.tmp" -exec ls -l {} \;  # Lista detalles
# find . -name "*.tmp" -exec rm {} \;    # Eliminaría todos los .tmp
cd ..
```

***

## **7. Tuberías (Pipes) - Encadenando Comandos**

Las tuberías (`|`) conectan la salida de un comando con la entrada de otro  [freecodecamp](https://www.freecodecamp.org/news/linux-terminal-piping-and-redirection-guide/).

### **7.1 Concepto Básico**

```bash
# Sintaxis
comando1 | comando2 | comando3

# La salida de comando1 va a comando2
# La salida de comando2 va a comando3
```

### **7.2 Ejemplos Prácticos**

```bash
# Contar líneas que contienen "ERROR"
$ grep "ERROR" log.txt | wc -l

# Listar archivos y buscar uno específico
$ ls -la | grep "documento"

# Ver procesos de un usuario específico
$ ps aux | grep "usuario"

# Directorios ordenados por nombre
$ ls -l | grep "^d" | sort

# Últimas líneas de un log que contienen "WARNING"
$ tail -100 /var/log/syslog | grep "WARNING"
```

**Práctica 17:**
```bash
cd ~/practica2
cat > servidor.log
2026-01-15 10:00:00 INFO Server started
2026-01-15 10:01:00 ERROR Connection failed
2026-01-15 10:02:00 INFO User logged in
2026-01-15 10:03:00 WARNING Low memory
2026-01-15 10:04:00 ERROR Disk full
2026-01-15 10:05:00 INFO Backup completed
2026-01-15 10:06:00 ERROR Network timeout
[Ctrl+D]
cat servidor.log                 # Muestra todo
cat servidor.log | grep "ERROR" # Solo errores
cat servidor.log | grep "ERROR" | wc -l  # Cuenta errores
cat servidor.log | grep -v "INFO"        # Excluye INFO
cat servidor.log | grep "ERROR" | head -2  # Primeros 2 errores
```

### **7.3 Combinaciones Avanzadas**

```bash
# Encontrar archivos grandes y mostrar con detalles
$ find . -size +1M | xargs ls -lh

# Buscar procesos y ordenar por uso de memoria
$ ps aux | grep python | sort -k 4 -nr

# Contar archivos por extensión
$ find . -type f | grep -o '\.[^.]*$' | sort | uniq -c

# Ver usuarios únicos en un log
$ cat access.log | cut -d' ' -f1 | sort | uniq
```

**Práctica 18:**
```bash
cd ~/practica2
# Crear múltiples archivos para practicar
mkdir pipe_practice
cd pipe_practice
touch {archivo1,archivo2,archivo3}.txt
touch {script1,script2}.sh
touch {data1,data2}.csv
ls                               # Lista todo
ls | grep "txt"                 # Solo .txt
ls | grep "sh"                  # Solo .sh
ls | wc -l                      # Cuenta archivos
ls -l | grep "^-"              # Solo archivos (no directorios)
cd ..
```

***

## **8. Redirecciones - Controlando Entrada/Salida**

### **8.1 Redirección de Salida**

```bash
# Sobrescribir archivo (cuidado, borra contenido previo)
$ comando > archivo.txt

# Añadir al final del archivo
$ comando >> archivo.txt

# Ejemplos
$ echo "Hola mundo" > saludo.txt
$ echo "Nueva línea" >> saludo.txt
$ ls -la > listado.txt
```

**Práctica 19:**
```bash
cd ~/practica2
echo "Primera línea" > salida.txt
cat salida.txt                   # Muestra: Primera línea
echo "Segunda línea" > salida.txt
cat salida.txt                   # Muestra: Segunda línea (sobrescrito!)
echo "Tercera línea" >> salida.txt
cat salida.txt                   # Muestra: Segunda y Tercera
ls -la > directorio.txt
cat directorio.txt               # Contenido del directorio guardado
```

### **8.2 Redirección de Entrada**

```bash
# Leer entrada desde archivo
$ comando < archivo_entrada.txt

# Ejemplo: contar palabras desde archivo
$ wc -w < texto.txt
```

**Práctica 20:**
```bash
cd ~/practica2
cat > palabras.txt
uno dos tres
cuatro cinco seis
siete ocho nueve
[Ctrl+D]
wc -w palabras.txt              # Cuenta palabras (muestra nombre)
wc -w < palabras.txt            # Cuenta palabras (solo número)
```

### **8.3 Redirección de Errores**

```bash
# Redirigir solo errores (stderr)
$ comando 2> errores.txt

# Redirigir salida estándar y errores a archivos diferentes
$ comando > salida.txt 2> errores.txt

# Redirigir todo (salida y errores) al mismo archivo
$ comando &> todo.txt
$ comando > todo.txt 2>&1       # Alternativa

# Descartar errores
$ comando 2> /dev/null
```

**Práctica 21:**
```bash
cd ~/practica2
# Comando que genera salida normal
ls -la > salida_ok.txt
cat salida_ok.txt
# Comando que genera error
ls /directorio_inexistente 2> error.txt
cat error.txt                    # Muestra el mensaje de error
# Combinar salida y error
ls -la /directorio_inexistente &> completo.txt
cat completo.txt
```

***

## **9. Ejercicios de Integración: Práctica 1 + Práctica 2**

### **Ejercicio 1: Gestión Completa de Proyecto**

```bash
# 1. Navegación básica (Práctica 1)
cd ~
pwd
mkdir -p proyectos/webapp
cd proyectos/webapp
pwd

# 2. Crear estructura
mkdir -p {src,config,logs,backups}
touch src/app.py src/models.py
touch config/settings.conf
touch logs/app.log

# 3. Permisos (Práctica 2)
chmod 755 src/app.py            # Ejecutable
chmod 644 config/settings.conf  # Solo lectura para grupo/otros
chmod 700 logs                  # Solo propietario accede a logs
ls -la

# 4. Añadir contenido
cat > logs/app.log
2026-01-15 ERROR Database connection failed
2026-01-15 INFO Application started
2026-01-15 WARNING Memory usage high
2026-01-15 ERROR Timeout in API call
[Ctrl+D]

# 5. Búsqueda
grep "ERROR" logs/app.log
grep "ERROR" logs/app.log > logs/solo_errores.txt
cat logs/solo_errores.txt

# 6. Navegar y verificar
cd ..
find webapp/ -name "*.py"
find webapp/ -type d
cd ~
```

### **Ejercicio 2: Análisis de Logs**

```bash
# Preparación
cd ~/practica2
mkdir log_analysis
cd log_analysis

# Crear log simulado
cat > access.log
192.168.1.10 GET /home 200
192.168.1.11 POST /login 401
192.168.1.10 GET /profile 200
192.168.1.12 GET /admin 403
192.168.1.11 POST /login 200
192.168.1.13 GET /home 200
192.168.1.10 GET /logout 200
[Ctrl+D]

# Análisis con tuberías y redirecciones
cat access.log | grep "200" > exitosos.txt
cat access.log | grep -v "200" > fallidos.txt
cat access.log | grep "200" | wc -l > contador_exitos.txt

# Verificar resultados
echo "=== Accesos exitosos ==="
cat exitosos.txt
echo "=== Accesos fallidos ==="
cat fallidos.txt
echo "=== Total de éxitos ==="
cat contador_exitos.txt

cd ~
```

### **Ejercicio 3: Limpieza de Sistema**

```bash
cd ~/practica2
mkdir limpieza_sistema
cd limpieza_sistema

# Crear archivos de diferentes tipos
touch documento{1..5}.txt
touch temporal{1..3}.tmp
touch backup{1..4}.bak
mkdir -p antiguos/viejos

# Listar todo
ls -la

# Encontrar y listar archivos temporales
find . -name "*.tmp"
find . -name "*.tmp" > archivos_tmp.txt
cat archivos_tmp.txt

# Encontrar archivos de backup
find . -name "*.bak" -exec ls -lh {} \;

# Contar cada tipo
echo "Archivos .txt: $(find . -name '*.txt' | wc -l)"
echo "Archivos .tmp: $(find . -name '*.tmp' | wc -l)"
echo "Archivos .bak: $(find . -name '*.bak' | wc -l)"

cd ~
```

***

## **10. Ejercicios de Repetición Intensiva**

### **Bloque A: chmod Repetitivo (5 veces)**

```bash
# Iteración 1
cd ~/practica2
touch chmod_test1.txt
ls -l chmod_test1.txt
chmod 755 chmod_test1.txt
ls -l chmod_test1.txt
chmod 644 chmod_test1.txt
ls -l chmod_test1.txt
rm chmod_test1.txt

# Iteración 2
touch chmod_test2.txt
ls -l chmod_test2.txt
chmod u+x chmod_test2.txt
ls -l chmod_test2.txt
chmod g-r chmod_test2.txt
ls -l chmod_test2.txt
rm chmod_test2.txt

# Iteración 3
touch chmod_test3.txt
ls -l chmod_test3.txt
chmod 700 chmod_test3.txt
ls -l chmod_test3.txt
chmod 777 chmod_test3.txt
ls -l chmod_test3.txt
rm chmod_test3.txt

# Iteración 4
touch chmod_test4.sh
chmod 755 chmod_test4.sh
ls -l chmod_test4.sh
chmod u=rwx,g=rx,o=rx chmod_test4.sh
ls -l chmod_test4.sh
rm chmod_test4.sh

# Iteración 5
touch chmod_test5.conf
chmod 600 chmod_test5.conf
ls -l chmod_test5.conf
chmod u=rw,g=,o= chmod_test5.conf
ls -l chmod_test5.conf
rm chmod_test5.conf
```

### **Bloque B: grep + pipes (5 veces)**

```bash
cd ~/practica2

# Iteración 1
cat > test1.txt
ERROR: fallo en sistema
INFO: todo correcto
ERROR: problema detectado
[Ctrl+D]
cat test1.txt | grep "ERROR"
cat test1.txt | grep "ERROR" | wc -l
rm test1.txt

# Iteración 2
cat > test2.txt
usuario admin juan
usuario normal maria
usuario admin pedro
[Ctrl+D]
grep "admin" test2.txt
grep "admin" test2.txt | wc -l
rm test2.txt

# Iteración 3
cat > test3.txt
linea 1
linea 2 con MATCH
linea 3
linea 4 con MATCH
linea 5
[Ctrl+D]
grep "MATCH" test3.txt
grep "MATCH" test3.txt > matches.txt
cat matches.txt
rm test3.txt matches.txt

# Iteración 4
echo "palabra palabra palabra" > test4.txt
cat test4.txt | grep -o "palabra" | wc -l
rm test4.txt

# Iteración 5
ls -la | grep "^d"
ls -la | grep "practica"
ls -la | grep "txt$"
```

### **Bloque C: find + Práctica 1 (5 veces)**

```bash
# Iteración 1
cd ~/practica2
mkdir find_test1
cd find_test1
touch archivo{1..5}.txt
find . -name "*.txt"
find . -name "*.txt" | wc -l
cd ..
rm -r find_test1

# Iteración 2
mkdir find_test2
cd find_test2
touch {a,b,c}.py
touch {x,y,z}.sh
find . -name "*.py"
find . -name "*.sh"
cd ..
rm -r find_test2

# Iteración 3
mkdir -p find_test3/{sub1,sub2}
touch find_test3/file1.txt
touch find_test3/sub1/file2.txt
touch find_test3/sub2/file3.txt
find find_test3/ -name "*.txt"
find find_test3/ -type f
rm -r find_test3

# Iteración 4
mkdir find_test4
cd find_test4
touch importante.txt
touch borrar.tmp
find . -name "*.txt"
find . -name "*.tmp"
cd ..
rm -r find_test4

# Iteración 5
mkdir -p find_test5/profundo/muy/profundo
touch find_test5/archivo.txt
touch find_test5/profundo/muy/profundo/oculto.txt
find find_test5/ -name "*.txt"
rm -r find_test5
```

***

## **11. Escenarios Reales del Mundo Profesional**

### **Escenario 1: Preparar Script para Producción**

```bash
cd ~
mkdir -p produccion/scripts
cd produccion/scripts

# Crear script de deployment
cat > deploy.sh
#!/bin/bash
echo "Iniciando deployment..."
echo "Conectando a servidor..."
echo "Desplegando aplicación..."
[Ctrl+D]

# Configurar permisos correctos
chmod 750 deploy.sh             # Ejecutable, grupo puede leer
ls -l deploy.sh

# Crear archivo de configuración sensible
cat > database.conf
DB_HOST=localhost
DB_USER=admin
DB_PASS=secret123
[Ctrl+D]

# Proteger archivo de configuración
chmod 600 database.conf         # Solo propietario
ls -l database.conf

cd ~
```

### **Escenario 2: Análisis de Logs de Servidor Web**

```bash
cd ~/practica2
mkdir web_logs
cd web_logs

# Simular log de Apache/Nginx
cat > access.log
192.168.1.100 - - [15/Jan/2026:10:00:00] "GET /index.html HTTP/1.1" 200 1234
192.168.1.101 - - [15/Jan/2026:10:01:00] "GET /api/users HTTP/1.1" 404 0
192.168.1.102 - - [15/Jan/2026:10:02:00] "POST /login HTTP/1.1" 200 567
192.168.1.100 - - [15/Jan/2026:10:03:00] "GET /admin HTTP/1.1" 403 0
192.168.1.103 - - [15/Jan/2026:10:04:00] "GET /index.html HTTP/1.1" 200 1234
192.168.1.101 - - [15/Jan/2026:10:05:00] "GET /api/data HTTP/1.1" 500 0
[Ctrl+D]

# Análisis de errores
grep " 404 " access.log > errores_404.txt
grep " 500 " access.log > errores_500.txt
grep -E " (404|500) " access.log > todos_errores.txt

# Contar peticiones exitosas
grep " 200 " access.log | wc -l > peticiones_exitosas.txt

# Extraer IPs únicas (simplificado)
grep "192.168" access.log | cut -d' ' -f1 | sort | uniq > ips_unicas.txt

# Mostrar resultados
echo "=== Errores 404 ==="
cat errores_404.txt
echo "=== Errores 500 ==="
cat errores_500.txt
echo "=== Total exitosas ==="
cat peticiones_exitosas.txt
echo "=== IPs únicas ==="
cat ips_unicas.txt

cd ~
```

### **Escenario 3: Auditoría de Permisos**

```bash
cd ~/practica2
mkdir auditoria_permisos
cd auditoria_permisos

# Crear estructura de archivos
mkdir -p publico privado compartido
touch publico/readme.txt
touch privado/passwords.txt
touch compartido/proyecto.txt

# Configurar permisos apropiados
chmod 755 publico
chmod 644 publico/readme.txt

chmod 700 privado
chmod 600 privado/passwords.txt

chmod 775 compartido
chmod 664 compartido/proyecto.txt

# Auditar permisos
echo "=== AUDITORÍA DE PERMISOS ===" > auditoria.txt
ls -lR >> auditoria.txt

# Verificar archivos con permisos muy abiertos (simulado)
find . -type f -perm -002 > archivos_escritura_global.txt

# Mostrar resultados
cat auditoria.txt
echo "=== Archivos con escritura global ==="
cat archivos_escritura_global.txt

cd ~
```

### **Escenario 4: Búsqueda y Limpieza de Archivos Grandes**

```bash
cd ~/practica2
mkdir limpieza_espacio
cd limpieza_espacio

# Crear archivos de prueba de diferentes tamaños
dd if=/dev/zero of=archivo_5mb.dat bs=1M count=5 2>/dev/null
dd if=/dev/zero of=archivo_15mb.dat bs=1M count=15 2>/dev/null
dd if=/dev/zero of=archivo_pequeno.txt bs=1K count=10 2>/dev/null

# Buscar archivos grandes (mayores de 10MB)
find . -type f -size +10M

# Listar archivos grandes con detalles
find . -type f -size +10M -exec ls -lh {} \; > archivos_grandes.txt
cat archivos_grandes.txt

# Buscar todos los archivos y mostrar tamaños
find . -type f -exec ls -lh {} \; | grep -v "^d"

# Limpiar archivos grandes (simulación - comentado)
# find . -type f -size +10M -exec rm {} \;

cd ~
```

***

## **12. Comandos Adicionales Útiles**

### **12.1 wc - Contar**

```bash
# Contar líneas, palabras, caracteres
$ wc archivo.txt

# Solo líneas
$ wc -l archivo.txt

# Solo palabras
$ wc -w archivo.txt

# Solo caracteres
$ wc -c archivo.txt
```

**Práctica:**
```bash
cd ~/practica2
cat > contar.txt
una dos tres
cuatro cinco
seis
[Ctrl+D]
wc contar.txt                    # Todo
wc -l contar.txt                 # Líneas
wc -w contar.txt                 # Palabras
wc -c contar.txt                 # Caracteres
```

### **12.2 sort - Ordenar**

```bash
# Ordenar alfabéticamente
$ sort archivo.txt

# Ordenar en reversa
$ sort -r archivo.txt

# Ordenar numéricamente
$ sort -n numeros.txt

# Ordenar y eliminar duplicados
$ sort -u archivo.txt
```

**Práctica:**
```bash
cd ~/practica2
cat > desordenado.txt
zebra
apple
mango
banana
[Ctrl+D]
sort desordenado.txt
sort -r desordenado.txt
cat > numeros_desordenados.txt
10
5
20
3
15
[Ctrl+D]
sort numeros_desordenados.txt    # Alfabético (incorrecto para números)
sort -n numeros_desordenados.txt # Numérico (correcto)
```

### **12.3 uniq - Eliminar Duplicados**

```bash
# Eliminar líneas duplicadas consecutivas
$ uniq archivo.txt

# Contar ocurrencias
$ uniq -c archivo.txt

# Mostrar solo duplicados
$ uniq -d archivo.txt

# Nota: Generalmente se usa con sort
$ sort archivo.txt | uniq
```

**Práctica:**
```bash
cd ~/practica2
cat > duplicados.txt
manzana
naranja
manzana
pera
naranja
manzana
[Ctrl+D]
sort duplicados.txt | uniq       # Elimina duplicados
sort duplicados.txt | uniq -c    # Cuenta ocurrencias
```

***

## **13. Ejercicio Final Integrador**

```bash
# EJERCICIO COMPLETO: Sistema de Gestión de Logs

# 1. Preparación (Práctica 1)
cd ~
mkdir -p sistema_logs/raw sistema_logs/processed sistema_logs/reports
cd sistema_logs
pwd

# 2. Crear logs simulados
cat > raw/app.log
2026-01-15 10:00:00 INFO Application started
2026-01-15 10:01:23 ERROR Database connection failed
2026-01-15 10:02:45 WARNING Memory usage at 85%
2026-01-15 10:03:12 INFO User john logged in
2026-01-15 10:04:56 ERROR File not found: config.xml
2026-01-15 10:05:34 INFO Processing batch job
2026-01-15 10:06:21 ERROR Network timeout
2026-01-15 10:07:09 WARNING Disk space low
2026-01-15 10:08:45 INFO Backup completed
2026-01-15 10:09:12 ERROR Authentication failed for user admin
[Ctrl+D]

# 3. Permisos correctos (Práctica 2)
chmod 644 raw/app.log
chmod 755 processed
chmod 755 reports
ls -la raw/

# 4. Procesar logs con grep y pipes
grep "ERROR" raw/app.log > processed/errors.log
grep "WARNING" raw/app.log > processed/warnings.log
grep "INFO" raw/app.log > processed/info.log

# 5. Generar reportes
echo "=== REPORTE DE ANÁLISIS DE LOGS ===" > reports/resumen.txt
echo "" >> reports/resumen.txt
echo "Total de líneas: $(wc -l < raw/app.log)" >> reports/resumen.txt
echo "Total de errores: $(wc -l < processed/errors.log)" >> reports/resumen.txt
echo "Total de warnings: $(wc -l < processed/warnings.log)" >> reports/resumen.txt
echo "Total de info: $(wc -l < processed/info.log)" >> reports/resumen.txt
echo "" >> reports/resumen.txt
echo "=== ERRORES DETECTADOS ===" >> reports/resumen.txt
cat processed/errors.log >> reports/resumen.txt

# 6. Ver reporte final
cat reports/resumen.txt

# 7. Búsqueda avanzada
find . -name "*.log"
find . -name "*.log" -exec wc -l {} \;

# 8. Limpiar archivos temporales (simulado)
# find . -name "*.tmp" -exec rm {} \;

cd ~
```

***

## **14. Checklist de Dominio - Práctica 2**

Marca cuando domines cada concepto:

**Permisos:**
- [ ] Interpreto correctamente `ls -l`
- [ ] Entiendo rwx para usuario/grupo/otros
- [ ] Uso `chmod` en modo simbólico (u+x, g-w, etc.)
- [ ] Uso `chmod` en modo numérico (755, 644, etc.)
- [ ] Calculo permisos numéricos mentalmente
- [ ] Uso `chmod -R` para directorios recursivos
- [ ] Entiendo `chown` y cuándo necesito `sudo`

**Visualización:**
- [ ] Uso `cat` para ver archivos completos
- [ ] Uso `head` y `tail` para ver partes de archivos
- [ ] Conozco `tail -f` para logs en tiempo real
- [ ] Uso `less` para navegar archivos largos

**Búsqueda:**
- [ ] Busco patrones con `grep`
- [ ] Uso `grep -i`, `-n`, `-v`, `-r`
- [ ] Uso expresiones regulares básicas (^, $)
- [ ] Uso `grep -A`, `-B`, `-C` para contexto
- [ ] Busco archivos con `find` por nombre
- [ ] Busco con `find` por tipo y tamaño
- [ ] Excluyo directorios en `find`

**Tuberías y Redirecciones:**
- [ ] Encadeno comandos con `|`
- [ ] Redirijo salida con `>` y `>>`
- [ ] Entiendo la diferencia entre `>` y `>>`
- [ ] Redirijo entrada con `<`
- [ ] Manejo errores con `2>`
- [ ] Uso `&>` para redirigir todo

**Integración:**
- [ ] Combino Práctica 1 y 2 fluidamente
- [ ] Creo flujos de trabajo complejos
- [ ] Resuelvo problemas reales de sistema

***

## **15. Errores Comunes y Soluciones - Práctica 2**

| Error | Causa | Solución |
|-------|-------|----------|
| `Permission denied` con `chmod` | Intentas cambiar permisos de archivos ajenos | Usa `sudo` si tienes privilegios  [digitalocean](https://www.digitalocean.com/community/tutorials/how-to-set-permissions-linux) |
| `chmod: invalid mode` | Sintaxis incorrecta | Revisa: `chmod 755` o `chmod u+x`  [dohost](https://dohost.us/index.php/2025/07/23/changing-permissions-the-chmod-command-symbolic-and-numeric-modes/) |
| `grep: command not found` | grep no instalado (raro) | Instala: `sudo apt install grep` |
| `>` borra mi archivo | Usaste `>` en lugar de `>>` | `>` sobrescribe, `>>` añade  [freecodecamp](https://www.freecodecamp.org/news/linux-terminal-piping-and-redirection-guide/) |
| `find` muy lento | Buscando en todo el sistema | Limita la búsqueda: `find /ruta/específica` |
| No veo cambios en `chmod` | No refrescaste `ls -l` | Ejecuta `ls -l` nuevamente |

***

## **16. Tips Profesionales**

### **Permisos Estándar por Tipo de Archivo**

```bash
# Scripts ejecutables
chmod 755 script.sh              # rwxr-xr-x

# Archivos de configuración
chmod 644 config.conf            # rw-r--r--

# Archivos sensibles (passwords, keys)
chmod 600 secret.key             # rw-------

# Directorios compartidos
chmod 775 compartido/            # rwxrwxr-x

# Directorios privados
chmod 700 privado/               # rwx------
```

### **Alias Útiles para .bashrc / .zshrc**

```bash
alias ll='ls -lah'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
```

### **Búsqueda Rápida de Archivos Recientes**

```bash
# Archivos modificados hoy
find . -type f -mtime 0

# Archivos modificados en la última hora
find . -type f -mmin -60
```

***

En la **Práctica 3** añadiremos gestión de procesos, análisis de disco, enlaces simbólicos y compresión de archivos, siempre practicando todo lo aprendido en Práctica 1 y 2. [baeldung](https://www.baeldung.com/linux/grep-pipe-search-term)

¡Sigue practicando y dominarás el terminal como un profesional!