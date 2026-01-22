Introducción: Dominando la Administración Avanzada

Has llegado a la Práctica 3, donde consolidarás todo lo aprendido en las Prácticas 1 y 2 mientras dominas herramientas profesionales de administración de sistemas. Aprenderás a gestionar procesos en ejecución, analizar uso de disco, trabajar con enlaces simbólicos, comprimir archivos y automatizar tareas.​

Recuerda: Seguirás practicando navegación (cd, pwd, ls), permisos (chmod, chown), búsqueda (grep, find) y tuberías de las prácticas anteriores.​
1. Gestión de Procesos
1.1 ps - Listar Procesos

El comando ps muestra información sobre los procesos en ejecución.​

bash
# Ver procesos del usuario actual
$ ps

# Ver todos los procesos del sistema
$ ps aux

# Ver procesos en formato jerárquico (árbol)
$ ps auxf

# Ver procesos de un usuario específico
$ ps -u nombre_usuario

# Ver procesos por PID (Process ID)
$ ps -p 1234

Salida de ps aux explicada:

text
USER    PID  %CPU %MEM    VSZ   RSS TTY   STAT START   TIME COMMAND
juan    1234  2.5  1.2 123456 45678 pts/0 S    10:30   0:15 firefox
│       │     │    │     │      │    │     │     │      │    │
│       │     │    │     │      │    │     │     │      │    └─ Comando
│       │     │    │     │      │    │     │     │      └─ Tiempo CPU
│       │     │    │     │      │    │     │     └─ Hora inicio
│       │     │    │     │      │    │     └─ Estado (S=sleeping, R=running)
│       │     │    │     │      │    └─ Terminal
│       │     │    │     │      └─ Memoria física (KB)
│       │     │    │     └─ Memoria virtual (KB)
│       │     │    └─ % Memoria
│       │     └─ % CPU
│       └─ ID del proceso
└─ Usuario propietario

Práctica 1:

bash
cd ~
mkdir practica3
cd practica3
pwd                              # Confirma ubicación
ps                               # Tus procesos
ps aux | head -20               # Primeros 20 procesos del sistema
ps aux | grep $USER             # Solo tus procesos
ps aux | grep bash              # Procesos bash
ps aux > procesos_actuales.txt  # Guardar en archivo
cat procesos_actuales.txt | wc -l  # Contar procesos

1.2 top - Monitor en Tiempo Real

top muestra procesos en tiempo real con actualización automática.​

bash
# Ejecutar top
$ top

# Comandos dentro de top:
# q       - Salir
# k       - Matar proceso (pide PID)
# P       - Ordenar por CPU
# M       - Ordenar por memoria
# h       - Ayuda
# 1       - Mostrar todos los CPUs
# Espacio - Refrescar manualmente

Práctica 2:

bash
# Abre una terminal y ejecuta:
top

# Dentro de top:
# 1. Presiona 'P' para ordenar por CPU
# 2. Presiona 'M' para ordenar por memoria
# 3. Presiona '1' para ver todos los CPUs
# 4. Presiona 'h' para ver ayuda
# 5. Presiona 'q' para salir

# Ejecutar top con opciones
top -n 1 -b > top_snapshot.txt   # Una iteración, modo batch
cat top_snapshot.txt | head -20

1.3 htop - Monitor Mejorado

htop es una versión más visual y amigable de top.​

bash
# Instalar htop (si no está instalado)
$ sudo apt install htop         # Debian/Ubuntu
$ sudo yum install htop          # RHEL/CentOS

# Ejecutar htop
$ htop

# Controles en htop:
# F2       - Configuración
# F3       - Buscar proceso
# F4       - Filtrar procesos
# F5       - Vista de árbol
# F9       - Matar proceso
# F10/q    - Salir
# Flechas  - Navegar
# Espacio  - Marcar proceso

Práctica 3:

bash
cd ~/practica3
# Si tienes htop instalado
htop -u $USER                    # Solo tus procesos

# Crear archivo de información del sistema
echo "=== REPORTE DEL SISTEMA ===" > sistema_info.txt
echo "Fecha: $(date)" >> sistema_info.txt
echo "" >> sistema_info.txt
echo "Usuario: $USER" >> sistema_info.txt
echo "Total de procesos: $(ps aux | wc -l)" >> sistema_info.txt
echo "" >> sistema_info.txt
echo "=== TOP 10 PROCESOS POR CPU ===" >> sistema_info.txt
ps aux --sort=-%cpu | head -11 >> sistema_info.txt

cat sistema_info.txt

1.4 kill - Terminar Procesos

bash
# Terminar proceso por PID (señal TERM - suave)
$ kill 1234

# Forzar terminación (señal KILL - inmediata)
$ kill -9 1234
$ kill -KILL 1234

# Terminar por nombre de proceso
$ killall firefox
$ pkill chrome

Práctica 4:

bash
cd ~/practica3
# Crear un proceso de larga duración
sleep 300 &                      # & ejecuta en segundo plano
echo "PID del proceso: $!"
ps aux | grep sleep

# Ver tu proceso
jobs                             # Trabajos en segundo plano
ps aux | grep sleep | grep -v grep

# Terminar el proceso
# Anota el PID del sleep y ejecuta:
# kill [PID]
# O directamente:
killall sleep

# Verificar que terminó
ps aux | grep sleep | grep -v grep

2. Análisis de Uso de Disco
2.1 df - Espacio en Sistemas de Archivos

df (disk free) muestra el espacio disponible en particiones montadas.​

bash
# Información básica
$ df

# Formato legible por humanos
$ df -h

# Mostrar tipo de sistema de archivos
$ df -hT

# Información de inodos
$ df -i

# Mostrar solo particiones locales (excluir montajes remotos)
$ df -hl

Práctica 5:

bash
cd ~/practica3
df                               # Vista básica
df -h                            # Legible
df -h > espacio_disco.txt
cat espacio_disco.txt

# Filtrar solo particiones importantes
df -h | grep "^/dev"            # Solo dispositivos físicos
df -h | grep "/$"               # Solo partición raíz

# Guardar reporte completo
echo "=== REPORTE DE ESPACIO EN DISCO ===" > reporte_disco.txt
echo "Fecha: $(date)" >> reporte_disco.txt
echo "" >> reporte_disco.txt
df -h >> reporte_disco.txt
cat reporte_disco.txt

2.2 du - Uso de Disco por Directorio

du (disk usage) calcula el espacio usado por archivos y directorios.​

bash
# Uso del directorio actual
$ du

# Formato legible
$ du -h

# Resumen (solo total)
$ du -sh directorio/

# Resumen de cada subdirectorio de primer nivel
$ du -h --max-depth=1 directorio/

# Mostrar todos los archivos y directorios
$ du -ah directorio/

# Ordenar por tamaño
$ du -h directorio/ | sort -hr

Práctica 6:

bash
cd ~/practica3
mkdir espacio_test
cd espacio_test

# Crear archivos de diferentes tamaños
dd if=/dev/zero of=archivo1.dat bs=1M count=5 2>/dev/null
dd if=/dev/zero of=archivo2.dat bs=1M count=10 2>/dev/null
dd if=/dev/zero of=archivo3.dat bs=1M count=15 2>/dev/null
mkdir subdir1
dd if=/dev/zero of=subdir1/grande.dat bs=1M count=20 2>/dev/null

# Analizar uso
du -h                            # Todo en formato legible
du -sh .                         # Resumen total
du -h --max-depth=1             # Solo primer nivel
du -ah | sort -hr               # Ordenado por tamaño

# Encontrar archivos grandes
du -ah | sort -hr | head -5 > top5_archivos.txt
cat top5_archivos.txt

cd ..

2.3 Combinando df y du

bash
# Ver particiones con poco espacio
$ df -h | grep -E "9[0-9]%|100%"

# Encontrar los 10 directorios más grandes
$ du -h /home/$USER | sort -hr | head -10

# Análisis completo del home
$ du -h --max-depth=1 ~ | sort -hr

Práctica 7:

bash
cd ~/practica3
# Análisis completo del espacio
echo "=== ANÁLISIS DE ESPACIO COMPLETO ===" > analisis_completo.txt
echo "" >> analisis_completo.txt
echo "== Particiones ==" >> analisis_completo.txt
df -h >> analisis_completo.txt
echo "" >> analisis_completo.txt
echo "== Uso en directorio actual ==" >> analisis_completo.txt
du -h --max-depth=1 . >> analisis_completo.txt

cat analisis_completo.txt

3. Enlaces Simbólicos y Duros
3.1 Diferencia entre Enlaces Duros y Simbólicos

Enlaces Duros (Hard Links):

    Apuntan directamente al mismo inode​

    No pueden cruzar sistemas de archivos

    No pueden enlazar directorios

    Si se borra el original, el enlace sigue funcionando​

Enlaces Simbólicos (Symbolic/Soft Links):

    Apuntan al nombre del archivo original​

    Pueden cruzar sistemas de archivos

    Pueden enlazar directorios​

    Si se borra el original, el enlace se rompe​

3.2 ln - Crear Enlaces

bash
# Crear enlace simbólico
$ ln -s archivo_original enlace_simbolico
$ ln -s /ruta/completa/archivo enlace

# Crear enlace duro
$ ln archivo_original enlace_duro

# Ver enlaces con detalles
$ ls -li                         # Muestra inodes

Práctica 8:

bash
cd ~/practica3
mkdir enlaces_test
cd enlaces_test

# Crear archivo original
echo "Contenido original" > original.txt
cat original.txt
ls -li original.txt              # Anota el inode

# Crear enlace simbólico
ln -s original.txt enlace_simbolico.txt
ls -li                           # Compara inodes
cat enlace_simbolico.txt        # Funciona igual

# Crear enlace duro
ln original.txt enlace_duro.txt
ls -li                           # Mismo inode que original!
cat enlace_duro.txt

# Modificar mediante enlace
echo "Nueva línea" >> enlace_simbolico.txt
cat original.txt                 # Se modificó el original
cat enlace_duro.txt             # También muestra el cambio

# Ver claramente los enlaces
ls -lh

3.3 Probando la Diferencia

Práctica 9:

bash
cd ~/practica3/enlaces_test

# Crear nuevo archivo y enlaces
echo "Prueba de borrado" > prueba.txt
ln -s prueba.txt enlace_sim.txt
ln prueba.txt enlace_hard.txt

ls -li
cat enlace_sim.txt
cat enlace_hard.txt

# Borrar original
rm prueba.txt
ls -li

# Intentar leer enlaces
cat enlace_sim.txt              # ERROR: broken link
cat enlace_hard.txt             # FUNCIONA: enlace duro sobrevive!

cd ..

3.4 Usos Prácticos de Enlaces Simbólicos

Práctica 10:

bash
cd ~/practica3
mkdir proyectos
mkdir proyectos/proyecto_actual_v2.5

# En lugar de navegar a ruta larga, crear atajo
ln -s proyectos/proyecto_actual_v2.5 proyecto
ls -lh

# Ahora puedes acceder fácilmente
cd proyecto
pwd                              # Ruta real
cd ..

# Enlace a directorio de logs
# ln -s /var/log logs_sistema
# cd logs_sistema

# Crear versión nueva y cambiar enlace
mkdir proyectos/proyecto_actual_v3.0
rm proyecto                      # Eliminar enlace viejo
ln -s proyectos/proyecto_actual_v3.0 proyecto
ls -lh proyecto

4. Compresión y Archivado
4.1 tar - Archivador

tar agrupa múltiples archivos en uno solo (tape archive).​

bash
# Crear archivo tar (sin comprimir)
$ tar -cvf archivo.tar directorio/

# Crear tar con compresión gzip (.tar.gz o .tgz)
$ tar -czvf archivo.tar.gz directorio/

# Crear tar con compresión bzip2 (.tar.bz2)
$ tar -cjvf archivo.tar.bz2 directorio/

# Extraer archivo tar
$ tar -xvf archivo.tar

# Extraer tar.gz
$ tar -xzvf archivo.tar.gz

# Ver contenido sin extraer
$ tar -tvf archivo.tar

# Extraer en directorio específico
$ tar -xzvf archivo.tar.gz -C /ruta/destino/

Flags explicados:

    -c: Create (crear)​

    -x: eXtract (extraer)​

    -v: Verbose (mostrar archivos)​

    -f: File (especificar nombre de archivo)​

    -z: gZip compression​

    -j: bZip2 compression

    -t: lisT (ver contenido)

Práctica 11:

bash
cd ~/practica3
mkdir proyecto_backup
cd proyecto_backup

# Crear estructura de proyecto
mkdir -p proyecto/{src,docs,config}
echo "print('Hola')" > proyecto/src/main.py
echo "# README" > proyecto/docs/readme.md
echo "DB_HOST=localhost" > proyecto/config/app.conf

ls -R proyecto/

# Crear archivo tar sin comprimir
tar -cvf proyecto.tar proyecto/
ls -lh proyecto.tar

# Crear tar con gzip (más usado)
tar -czvf proyecto.tar.gz proyecto/
ls -lh proyecto.tar.gz           # Comparar tamaño

# Ver contenido sin extraer
tar -tvf proyecto.tar.gz

# Crear tar con bzip2 (más compresión)
tar -cjvf proyecto.tar.bz2 proyecto/
ls -lh *.tar*                    # Comparar todos los tamaños

cd ..

4.2 Extraer y Manipular Archivos tar

Práctica 12:

bash
cd ~/practica3
mkdir extraccion_test
cd extraccion_test

# Copiar archivo comprimido
cp ../proyecto_backup/proyecto.tar.gz .
ls -lh

# Extraer
tar -xzvf proyecto.tar.gz
ls -lh
ls -R proyecto/

# Modificar algo
echo "nueva_linea" >> proyecto/src/main.py
cat proyecto/src/main.py

# Crear nuevo backup con fecha
tar -czvf proyecto_backup_$(date +%Y%m%d).tar.gz proyecto/
ls -lh

cd ..

4.3 gzip y gunzip - Compresión Individual

bash
# Comprimir archivo (reemplaza original)
$ gzip archivo.txt               # Crea archivo.txt.gz

# Comprimir manteniendo original
$ gzip -k archivo.txt

# Descomprimir
$ gunzip archivo.txt.gz
$ gzip -d archivo.txt.gz         # Alternativa

# Ver contenido comprimido sin descomprimir
$ zcat archivo.txt.gz
$ zless archivo.txt.gz           # Visualización paginada

Práctica 13:

bash
cd ~/practica3
mkdir compresion_test
cd compresion_test

# Crear archivo grande
seq 1 100000 > numeros.txt
ls -lh numeros.txt

# Comprimir
gzip -k numeros.txt              # -k mantiene original
ls -lh                           # Compara tamaños

# Ver comprimido sin descomprimir
zcat numeros.txt.gz | head -10
zcat numeros.txt.gz | tail -10

# Descomprimir
gunzip numeros.txt.gz
ls -lh

cd ..

5. Descarga de Archivos
5.1 wget - Descarga Robusta

wget descarga archivos de Internet.​

bash
# Descargar archivo
$ wget https://ejemplo.com/archivo.zip

# Descargar con nombre específico
$ wget -O nuevo_nombre.zip https://ejemplo.com/archivo.zip

# Descargar en directorio específico
$ wget -P /ruta/destino https://ejemplo.com/archivo.zip

# Continuar descarga interrumpida
$ wget -c https://ejemplo.com/archivo_grande.iso

# Descargar recursivamente un sitio (con límite)
$ wget -r -l 2 https://ejemplo.com

# Descargar en segundo plano
$ wget -b https://ejemplo.com/archivo.zip

Práctica 14:

bash
cd ~/practica3
mkdir descargas_test
cd descargas_test

# Descargar archivo de prueba (ejemplo real)
wget https://www.kernel.org/pub/linux/kernel/README

ls -lh
cat README

# Descargar con nombre específico
wget -O kernel_readme.txt https://www.kernel.org/pub/linux/kernel/README
ls -lh

cd ..

5.2 curl - Cliente HTTP Versátil

curl es más flexible para APIs y peticiones HTTP.​

bash
# Descargar archivo (necesita -O)
$ curl -O https://ejemplo.com/archivo.zip

# Descargar con nombre específico
$ curl -o nuevo_nombre.zip https://ejemplo.com/archivo.zip

# Seguir redirecciones
$ curl -L -O https://ejemplo.com/archivo.zip

# Ver solo headers
$ curl -I https://ejemplo.com

# Descargar múltiples archivos
$ curl -O https://ejemplo.com/file1.txt -O https://ejemplo.com/file2.txt

Práctica 15:

bash
cd ~/practica3/descargas_test

# Descargar con curl
curl -O https://www.kernel.org/pub/linux/kernel/README
mv README README_curl

# Ver headers de una web
curl -I https://www.google.com > headers_google.txt
cat headers_google.txt

# Comparar wget vs curl
echo "Ambos archivos descargados:"
ls -lh README* kernel_readme.txt

cd ..

6. Variables de Entorno y PATH
6.1 Ver Variables de Entorno

bash
# Ver todas las variables de entorno
$ env
$ printenv

# Ver variable específica
$ echo $PATH
$ echo $HOME
$ echo $USER
$ echo $SHELL

# Ver PATH formateado
$ echo $PATH | tr ':' '\n'

Práctica 16:

bash
cd ~/practica3
# Explorar variables de entorno
echo "Usuario: $USER" > variables_entorno.txt
echo "Home: $HOME" >> variables_entorno.txt
echo "Shell: $SHELL" >> variables_entorno.txt
echo "PATH: $PATH" >> variables_entorno.txt
echo "" >> variables_entorno.txt
echo "=== PATH FORMATEADO ===" >> variables_entorno.txt
echo $PATH | tr ':' '\n' >> variables_entorno.txt

cat variables_entorno.txt

6.2 Crear y Exportar Variables

bash
# Crear variable local (solo en shell actual)
$ MI_VARIABLE="valor"
$ echo $MI_VARIABLE

# Exportar variable (disponible para procesos hijos)
$ export MI_VARIABLE="valor"
$ export PATH=$PATH:/nueva/ruta

# Ver si una variable está exportada
$ printenv MI_VARIABLE

Práctica 17:

bash
cd ~/practica3
# Crear variable temporal
MI_NOMBRE="Juan"
echo "Hola, $MI_NOMBRE"

# Crear variable con ruta
MI_DIRECTORIO="$HOME/practica3"
echo "Directorio de trabajo: $MI_DIRECTORIO"
cd $MI_DIRECTORIO
pwd

# Variable temporal solo existe en esta sesión
# Se perderá al cerrar terminal

6.3 Modificar PATH Permanentemente

bash
# Añadir al final de ~/.bashrc o ~/.bash_profile
$ echo 'export PATH=$PATH:$HOME/mis_scripts' >> ~/.bashrc

# Aplicar cambios sin reiniciar
$ source ~/.bashrc

# O para zsh:
$ echo 'export PATH=$PATH:$HOME/mis_scripts' >> ~/.zshrc
$ source ~/.zshrc

Práctica 18:

bash
cd ~/practica3
mkdir mis_scripts
cd mis_scripts

# Crear script ejecutable
cat > hola.sh << 'EOF'
#!/bin/bash
echo "¡Hola desde mi script personalizado!"
echo "Fecha: $(date)"
EOF

chmod +x hola.sh
./hola.sh                        # Ejecutar con ./

# Para ejecutarlo desde cualquier lugar:
# Opción 1: Añadir al PATH (comentado para no modificar tu sistema)
# echo 'export PATH=$PATH:$HOME/practica3/mis_scripts' >> ~/.bashrc
# source ~/.bashrc
# hola.sh  # Funcionaría sin ./

cd ..

7. Ejercicios de Integración: Prácticas 1 + 2 + 3
Ejercicio 1: Análisis Completo del Sistema

bash
# 1. Preparación (Práctica 1)
cd ~
mkdir sistema_completo
cd sistema_completo
pwd

# 2. Crear script de análisis
cat > analisis_sistema.sh << 'EOF'
#!/bin/bash
echo "================================"
echo "REPORTE COMPLETO DEL SISTEMA"
echo "================================"
echo ""
echo "Fecha: $(date)"
echo "Usuario: $USER"
echo "Hostname: $(hostname)"
echo ""
echo "=== USO DE DISCO ==="
df -h | grep "^/dev"
echo ""
echo "=== PROCESOS ACTIVOS ==="
ps aux | wc -l
echo ""
echo "=== TOP 5 PROCESOS POR CPU ==="
ps aux --sort=-%cpu | head -6
echo ""
echo "=== ESPACIO EN HOME ==="
du -sh ~
echo ""
echo "================================"
EOF

# 3. Dar permisos (Práctica 2)
chmod 755 analisis_sistema.sh
ls -l analisis_sistema.sh

# 4. Ejecutar
./analisis_sistema.sh > reporte_$(date +%Y%m%d_%H%M%S).txt

# 5. Ver resultado
ls -lh
cat reporte_*.txt

# 6. Comprimir reporte (Práctica 3)
tar -czvf reportes_sistema.tar.gz reporte_*.txt
ls -lh *.tar.gz

cd ~

Ejercicio 2: Backup Inteligente de Proyecto

bash
cd ~
mkdir proyecto_web
cd proyecto_web

# 1. Crear estructura de proyecto (Práctica 1)
mkdir -p web/{html,css,js,images}
mkdir -p logs
mkdir -p backups

# 2. Crear archivos
echo "<html><body>Hola Mundo</body></html>" > web/html/index.html
echo "body { color: blue; }" > web/css/style.css
echo "console.log('App iniciada');" > web/js/app.js

# 3. Crear logs simulados
cat > logs/access.log << 'EOF'
192.168.1.1 GET /index.html 200
192.168.1.2 GET /style.css 200
192.168.1.3 GET /app.js 200
192.168.1.1 POST /api/login 401
192.168.1.4 GET /index.html 200
EOF

# 4. Configurar permisos (Práctica 2)
chmod 755 web/html web/css web/js
chmod 644 web/html/* web/css/* web/js/*
chmod 700 logs
chmod 600 logs/access.log

ls -lR

# 5. Analizar logs (Práctica 2)
grep "200" logs/access.log > logs/exitosos.log
grep "401" logs/access.log > logs/errores.log
wc -l logs/*.log

# 6. Crear backup con fecha (Práctica 3)
FECHA=$(date +%Y%m%d_%H%M%S)
tar -czvf backups/proyecto_web_$FECHA.tar.gz web/ logs/
ls -lh backups/

# 7. Análisis de espacio
du -sh web/
du -sh logs/
du -sh backups/
du -h --max-depth=1 .

# 8. Crear enlace simbólico al último backup
cd backups
ln -sf proyecto_web_$FECHA.tar.gz ultimo_backup.tar.gz
ls -lh
cd ..

# 9. Generar reporte completo
cat > reporte_proyecto.txt << EOF
=== REPORTE DEL PROYECTO WEB ===
Fecha: $(date)

=== Estructura de archivos ===
$(find web/ -type f | wc -l) archivos en web/

=== Logs procesados ===
Accesos exitosos: $(wc -l < logs/exitosos.log)
Errores: $(wc -l < logs/errores.log)

=== Espacio utilizado ===
$(du -sh .)

=== Backups disponibles ===
$(ls -lh backups/)
EOF

cat reporte_proyecto.txt

cd ~

Ejercicio 3: Monitoreo y Limpieza del Sistema

bash
cd ~
mkdir monitor_sistema
cd monitor_sistema

# 1. Script de monitoreo
cat > monitor.sh << 'EOF'
#!/bin/bash

FECHA=$(date +%Y%m%d_%H%M%S)
ARCHIVO="monitor_$FECHA.log"

echo "=== MONITOREO DEL SISTEMA ===" > $ARCHIVO
echo "Fecha: $(date)" >> $ARCHIVO
echo "" >> $ARCHIVO

echo "=== ESPACIO EN DISCO ===" >> $ARCHIVO
df -h >> $ARCHIVO
echo "" >> $ARCHIVO

echo "=== USO DE MEMORIA ===" >> $ARCHIVO
free -h >> $ARCHIVO
echo "" >> $ARCHIVO

echo "=== PROCESOS POR USUARIO ===" >> $ARCHIVO
ps aux | awk '{print $1}' | sort | uniq -c | sort -nr >> $ARCHIVO
echo "" >> $ARCHIVO

echo "=== DIRECTORIOS GRANDES EN HOME ===" >> $ARCHIVO
du -h ~ --max-depth=1 2>/dev/null | sort -hr | head -10 >> $ARCHIVO
echo "" >> $ARCHIVO

echo "Monitor guardado en $ARCHIVO"
EOF

chmod +x monitor.sh
./monitor.sh
ls -lh

# 2. Script de limpieza
cat > limpieza.sh << 'EOF'
#!/bin/bash

echo "=== SCRIPT DE LIMPIEZA ==="
echo "Buscando archivos temporales..."

# Buscar archivos .tmp
TEMP_FILES=$(find ~ -name "*.tmp" 2>/dev/null | wc -l)
echo "Archivos .tmp encontrados: $TEMP_FILES"

# Buscar archivos .log antiguos (simulado)
OLD_LOGS=$(find ~ -name "*.log" -mtime +30 2>/dev/null | wc -l)
echo "Logs antiguos (>30 días): $OLD_LOGS"

# Buscar archivos grandes (>100MB)
BIG_FILES=$(find ~ -type f -size +100M 2>/dev/null | wc -l)
echo "Archivos grandes (>100MB): $BIG_FILES"

echo "Limpieza completa. Revisar manualmente antes de eliminar."
EOF

chmod +x limpieza.sh
./limpieza.sh

# 3. Comprimir logs antiguos
mkdir -p logs_viejos
touch logs_viejos/old1.log logs_viejos/old2.log
tar -czvf logs_archivo_$(date +%Y%m).tar.gz logs_viejos/
ls -lh

# 4. Crear enlace para acceso rápido
ln -s $PWD/monitor.sh ~/monitor_rapido
ls -l ~/monitor_rapido

cd ~

8. Ejercicios de Repetición Intensiva
Bloque A: tar + compresión (5 veces)

bash
cd ~/practica3

# Iteración 1
mkdir test1
touch test1/file{1..5}.txt
tar -czvf test1.tar.gz test1/
ls -lh test1.tar.gz
rm -rf test1 test1.tar.gz

# Iteración 2
mkdir test2
touch test2/archivo{1..3}.log
tar -czvf test2.tar.gz test2/
tar -tvf test2.tar.gz
rm -rf test2 test2.tar.gz

# Iteración 3
mkdir test3
echo "contenido" > test3/data.txt
tar -czvf test3.tar.gz test3/
tar -xzvf test3.tar.gz
rm -rf test3 test3.tar.gz

# Iteración 4
mkdir -p test4/{a,b,c}
touch test4/a/file1.txt test4/b/file2.txt
tar -czvf test4.tar.gz test4/
ls -lh test4.tar.gz
rm -rf test4 test4.tar.gz

# Iteración 5
mkdir test5
seq 1 1000 > test5/numbers.txt
tar -czvf test5.tar.gz test5/
tar -xzvf test5.tar.gz -C /tmp/
rm -rf test5 test5.tar.gz

Bloque B: Enlaces simbólicos (5 veces)

bash
cd ~/practica3

# Iteración 1
echo "original1" > orig1.txt
ln -s orig1.txt link1.txt
cat link1.txt
rm orig1.txt link1.txt

# Iteración 2
mkdir dir2
ln -s dir2 linkdir2
ls -ld linkdir2
rm -rf dir2 linkdir2

# Iteración 3
echo "data3" > orig3.txt
ln -s orig3.txt link3.txt
ls -li orig3.txt link3.txt
rm orig3.txt link3.txt

# Iteración 4
mkdir -p path/to/deep/dir
ln -s path/to/deep/dir shortcut4
cd shortcut4
pwd -P
cd ~/practica3
rm -rf path shortcut4

# Iteración 5
echo "test5" > file5.txt
ln -s file5.txt alias5.txt
cat alias5.txt
rm file5.txt
cat alias5.txt  # Error: broken link
rm alias5.txt

Bloque C: Integración completa (3 veces)

bash
# Iteración 1
cd ~/practica3
mkdir integracion1
cd integracion1
mkdir datos
echo "info" > datos/archivo.txt
chmod 644 datos/archivo.txt
ls -l datos/
tar -czvf backup1.tar.gz datos/
ls -lh
find . -name "*.tar.gz"
cd ..
rm -rf integracion1

# Iteración 2
cd ~/practica3
mkdir integracion2
cd integracion2
touch file{1..5}.log
ls | grep "log$" | wc -l
tar -czvf logs.tar.gz *.log
du -sh logs.tar.gz
cd ..
rm -rf integracion2

# Iteración 3
cd ~/practica3
mkdir integracion3
cd integracion3
echo "data" > original.dat
ln -s original.dat link.dat
chmod 600 original.dat
ls -l
tar -czvf complete.tar.gz *
ls -lh complete.tar.gz
cd ..
rm -rf integracion3

9. Escenarios Profesionales Avanzados
Escenario 1: Rotación de Logs Automatizada

bash
cd ~
mkdir log_rotation_system
cd log_rotation_system

# 1. Crear estructura
mkdir -p {current_logs,archived_logs,scripts}

# 2. Simular logs
cat > current_logs/app.log << EOF
2026-01-15 10:00:00 INFO Application started
2026-01-15 10:01:00 ERROR Connection timeout
2026-01-15 10:02:00 WARNING Memory high
EOF

cat > current_logs/access.log << EOF
192.168.1.1 GET / 200
192.168.1.2 POST /api 201
192.168.1.3 GET /admin 403
EOF

# 3. Script de rotación
cat > scripts/rotate_logs.sh << 'EOF'
#!/bin/bash

FECHA=$(date +%Y%m%d)
LOG_DIR="current_logs"
ARCHIVE_DIR="archived_logs"

echo "Iniciando rotación de logs..."

# Comprimir logs actuales
tar -czvf $ARCHIVE_DIR/logs_$FECHA.tar.gz $LOG_DIR/*.log

# Limpiar logs actuales
> $LOG_DIR/app.log
> $LOG_DIR/access.log

echo "Logs rotados y archivados en $ARCHIVE_DIR/logs_$FECHA.tar.gz"

# Eliminar archivos de más de 30 días (simulado)
find $ARCHIVE_DIR -name "*.tar.gz" -mtime +30 -exec rm {} \;

echo "Rotación completada"
EOF

chmod +x scripts/rotate_logs.sh

# 4. Ejecutar rotación
./scripts/rotate_logs.sh

# 5. Verificar
ls -lh archived_logs/
ls -lh current_logs/

cd ~

Escenario 2: Sistema de Deployment

bash
cd ~
mkdir deployment_system
cd deployment_system

# 1. Estructura
mkdir -p {releases,current,backups,scripts}

# 2. Simular release
mkdir releases/v1.0
echo "App v1.0" > releases/v1.0/app.py
echo "Config v1.0" > releases/v1.0/config.ini

# 3. Script de deployment
cat > scripts/deploy.sh << 'EOF'
#!/bin/bash

VERSION=$1
if [ -z "$VERSION" ]; then
    echo "Uso: ./deploy.sh <version>"
    exit 1
fi

RELEASE_DIR="releases/$VERSION"
CURRENT_DIR="current"
BACKUP_DIR="backups"

# Verificar que existe la release
if [ ! -d "$RELEASE_DIR" ]; then
    echo "ERROR: Release $VERSION no encontrada"
    exit 1
fi

echo "Desplegando versión $VERSION..."

# Backup de versión actual si existe
if [ -d "$CURRENT_DIR" ]; then
    echo "Creando backup..."
    BACKUP_FILE="$BACKUP_DIR/backup_$(date +%Y%m%d_%H%M%S).tar.gz"
    tar -czf $BACKUP_FILE $CURRENT_DIR/
    echo "Backup guardado: $BACKUP_FILE"
fi

# Remover enlace actual
rm -f $CURRENT_DIR

# Crear enlace simbólico a nueva versión
ln -s $RELEASE_DIR $CURRENT_DIR

echo "Deployment completado"
echo "Versión activa: $(ls -l $CURRENT_DIR)"
EOF

chmod +x scripts/deploy.sh

# 4. Ejecutar deployment
./scripts/deploy.sh v1.0

# 5. Verificar
ls -lh current
cat current/app.py

# 6. Nueva release
mkdir releases/v2.0
echo "App v2.0 - Nueva funcionalidad" > releases/v2.0/app.py
echo "Config v2.0" > releases/v2.0/config.ini

# 7. Deployment de v2.0
./scripts/deploy.sh v2.0
cat current/app.py

# 8. Ver backups
ls -lh backups/

cd ~

Escenario 3: Monitoreo de Recursos

bash
cd ~
mkdir resource_monitor
cd resource_monitor

# Script completo de monitoreo
cat > monitor_resources.sh << 'EOF'
#!/bin/bash

REPORT_FILE="resource_report_$(date +%Y%m%d_%H%M%S).txt"
ALERT_THRESHOLD=80

echo "==================================" > $REPORT_FILE
echo "REPORTE DE RECURSOS DEL SISTEMA" >> $REPORT_FILE
echo "==================================" >> $REPORT_FILE
echo "Fecha: $(date)" >> $REPORT_FILE
echo "" >> $REPORT_FILE

# Uso de disco
echo "=== USO DE DISCO ===" >> $REPORT_FILE
df -h | grep "^/dev" >> $REPORT_FILE
echo "" >> $REPORT_FILE

# Alertas de disco
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
if [ $DISK_USAGE -gt $ALERT_THRESHOLD ]; then
    echo "⚠️  ALERTA: Disco al ${DISK_USAGE}%" >> $REPORT_FILE
fi
echo "" >> $REPORT_FILE

# Memoria
echo "=== USO DE MEMORIA ===" >> $REPORT_FILE
free -h >> $REPORT_FILE
echo "" >> $REPORT_FILE

# Top procesos por CPU
echo "=== TOP 10 PROCESOS (CPU) ===" >> $REPORT_FILE
ps aux --sort=-%cpu | head -11 >> $REPORT_FILE
echo "" >> $REPORT_FILE

# Top procesos por Memoria
echo "=== TOP 10 PROCESOS (MEM) ===" >> $REPORT_FILE
ps aux --sort=-%mem | head -11 >> $REPORT_FILE
echo "" >> $REPORT_FILE

# Directorios grandes
echo "=== TOP DIRECTORIOS EN /home ===" >> $REPORT_FILE
du -h /home/$USER --max-depth=1 2>/dev/null | sort -hr | head -10 >> $REPORT_FILE
echo "" >> $REPORT_FILE

echo "==================================" >> $REPORT_FILE
echo "Reporte completado: $REPORT_FILE" >> $REPORT_FILE

# Comprimir reportes antiguos
find . -name "resource_report_*.txt" -mtime +7 -exec gzip {} \;

echo "Reporte generado: $REPORT_FILE"
cat $REPORT_FILE
EOF

chmod +x monitor_resources.sh
./monitor_resources.sh

ls -lh

cd ~

10. Checklist de Dominio - Práctica 3

Marca cuando domines cada concepto:

Gestión de Procesos:

    Listo procesos con ps

    Interpreto la salida de ps aux

    Uso top para monitoreo en tiempo real

    Navego y uso htop eficientemente

    Termino procesos con kill y killall

Análisis de Disco:

    Verifico espacio disponible con df -h

    Analizo uso de directorios con du

    Encuentro archivos grandes con du y sort

    Combino df y du para análisis completo

Enlaces:

    Entiendo la diferencia entre enlaces duros y simbólicos

    Creo enlaces simbólicos con ln -s

    Creo enlaces duros con ln

    Uso enlaces para crear atajos útiles

Compresión:

    Creo archivos tar con tar -cvf

    Comprimo con gzip usando tar -czvf

    Extraigo archivos tar con tar -xvf

    Listo contenido sin extraer con tar -tvf

    Comprimo archivos individuales con gzip

Descargas:

    Descargo archivos con wget

    Descargo archivos con curl

    Entiendo las diferencias entre wget y curl

Variables y Automatización:

    Visualizo variables de entorno con echo $VAR

    Creo variables temporales

    Exporto variables con export

    Entiendo y modifico $PATH

    Creo scripts bash básicos

Integración:

    Combino comandos de Práctica 1, 2 y 3

    Creo scripts automatizados complejos

    Resuelvo problemas reales de administración

11. Comandos Adicionales Útiles
11.1 time - Medir Tiempo de Ejecución

bash
# Medir cuánto tarda un comando
$ time ls -lR /

# Medir script
$ time ./mi_script.sh

11.2 watch - Ejecutar Comando Repetidamente

bash
# Ejecutar cada 2 segundos (por defecto)
$ watch df -h

# Ejecutar cada 5 segundos
$ watch -n 5 'ps aux | grep python'

# Resaltar diferencias
$ watch -d free -h

Práctica:

bash
cd ~/practica3
# Ver espacio actualizándose
watch -n 2 'du -sh .'
# Presiona Ctrl+C para salir

11.3 alias - Crear Atajos

bash
# Crear alias temporal
$ alias ll='ls -lah'
$ alias update='sudo apt update && sudo apt upgrade'

# Ver todos los alias
$ alias

# Hacer permanente (añadir a ~/.bashrc)
$ echo "alias ll='ls -lah'" >> ~/.bashrc

12. Proyecto Final Integrador

bash
# SISTEMA COMPLETO DE GESTIÓN DE PROYECTOS

cd ~
mkdir proyecto_final
cd proyecto_final

# 1. Estructura completa (Práctica 1)
mkdir -p {proyectos,backups,logs,scripts,temp}
mkdir -p proyectos/{web_app,mobile_app}

# 2. Crear archivos de proyecto
echo "Web App v1.0" > proyectos/web_app/app.py
echo "Mobile App v1.0" > proyectos/mobile_app/main.dart

# 3. Configurar permisos (Práctica 2)
chmod 755 proyectos/web_app proyectos/mobile_app
chmod 644 proyectos/web_app/* proyectos/mobile_app/*
find proyectos/ -type f -ls

# 4. Crear logs simulados
cat > logs/activity.log << EOF
2026-01-16 10:00:00 INFO Sistema iniciado
2026-01-16 10:15:00 INFO Backup completado
2026-01-16 10:30:00 ERROR Falló conexión
2026-01-16 10:45:00 INFO Proyecto actualizado
2026-01-16 11:00:00 WARNING Espacio bajo
EOF

# 5. Análisis de logs (Práctica 2)
grep "ERROR" logs/activity.log > logs/errors.log
grep "INFO" logs/activity.log > logs/info.log
grep "WARNING" logs/activity.log > logs/warnings.log
wc -l logs/*.log

# 6. Script de backup completo (Práctica 3)
cat > scripts/backup_completo.sh << 'EOF'
#!/bin/bash

FECHA=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="backups"

echo "=== BACKUP COMPLETO ==="
echo "Fecha: $(date)"

# Backup de proyectos
tar -czvf $BACKUP_DIR/proyectos_$FECHA.tar.gz proyectos/
echo "✓ Proyectos respaldados"

# Backup de logs
tar -czvf $BACKUP_DIR/logs_$FECHA.tar.gz logs/
echo "✓ Logs respaldados"

# Crear enlace al último backup
cd $BACKUP_DIR
ln -sf proyectos_$FECHA.tar.gz ultimo_backup.tar.gz
cd ..

# Reporte
echo "=== REPORTE DE BACKUP ===" > backups/reporte_$FECHA.txt
echo "Fecha: $(date)" >> backups/reporte_$FECHA.txt
echo "Archivos respaldados:" >> backups/reporte_$FECHA.txt
echo "- proyectos_$FECHA.tar.gz ($(ls -lh $BACKUP_DIR/proyectos_$FECHA.tar.gz | awk '{print $5}'))" >> backups/reporte_$FECHA.txt
echo "- logs_$FECHA.tar.gz ($(ls -lh $BACKUP_DIR/logs_$FECHA.tar.gz | awk '{print $5}'))" >> backups/reporte_$FECHA.txt

# Limpiar backups antiguos (>30 días)
find $BACKUP_DIR -name "*.tar.gz" -mtime +30 -exec rm {} \;

echo "Backup completado: backups/proyectos_$FECHA.tar.gz"
EOF

chmod +x scripts/backup_completo.sh

# 7. Ejecutar backup
./scripts/backup_completo.sh

# 8. Verificar todo
ls -lh backups/
cat backups/reporte_*.txt

# 9. Análisis de recursos
df -h . > analisis_sistema.txt
du -sh * >> analisis_sistema.txt
ps aux | wc -l >> analisis_sistema.txt

# 10. Reporte final
cat > REPORTE_FINAL.txt << EOF
===========================================
PROYECTO FINAL - SISTEMA DE GESTIÓN
===========================================
Fecha: $(date)
Usuario: $USER

=== ESTRUCTURA ===
$(find . -type d | wc -l) directorios
$(find . -type f | wc -l) archivos

=== ESPACIO UTILIZADO ===
$(du -sh .)

=== BACKUPS DISPONIBLES ===
$(ls -lh backups/ | grep "tar.gz" | wc -l) backups

=== LOGS PROCESADOS ===
Errores: $(wc -l < logs/errors.log)
Información: $(wc -l < logs/info.log)
Advertencias: $(wc -l < logs/warnings.log)

=== SCRIPTS DISPONIBLES ===
$(ls scripts/)

===========================================
Proyecto completado exitosamente
===========================================
EOF

cat REPORTE_FINAL.txt

cd ~

Conclusión

¡Felicidades! Has completado las tres prácticas de administración de sistemas Linux. Ahora dominas: