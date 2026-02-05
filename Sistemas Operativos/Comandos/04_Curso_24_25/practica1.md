# Guía Completa de Navegación y Gestión del Sistema de Archivos Linux


## **Introducción: Entendiendo el Sistema de Archivos**

El sistema de archivos de Linux es una estructura jerárquica en forma de árbol invertido. Todo comienza desde el directorio raíz (`/`) y se ramifica en subdirectorios. Dominar la navegación en este sistema es fundamental para cualquier profesional de sistemas, ya que la línea de comandos ofrece mayor control, velocidad y automatización que las interfaces gráficas. [r-bloggers](https://www.r-bloggers.com/2024/09/navigating-linux-with-pwd-cd-and-ls-a-beginners-guide/)

En este documento aprenderás mediante **repetición práctica** los comandos esenciales para moverte con soltura por el sistema de archivos.

***

## **1. Comandos Fundamentales de Orientación**

### **1.1 pwd - ¿Dónde estoy?**

El comando `pwd` (Print Working Directory) muestra tu ubicación actual en el sistema de archivos. [r-bloggers](https://www.r-bloggers.com/2024/09/navigating-linux-with-pwd-cd-and-ls-a-beginners-guide/)

```bash
$ pwd
/home/usuario
```

**Práctica 1:**
```bash
# Ejecuta esto ahora en tu terminal
pwd
# Anota mentalmente dónde estás
```

### **1.2 ls - ¿Qué hay aquí?**

El comando `ls` lista el contenido del directorio actual. [linuxcommand](https://linuxcommand.org/lc3_lts0020.php)

```bash
# Listar archivos y directorios
$ ls

# Listar con detalles (permisos, tamaño, fecha)
$ ls -l

# Listar incluyendo archivos ocultos
$ ls -a

# Combinar opciones: detalles + ocultos
$ ls -la

# Listar con tamaños legibles (K, M, G)
$ ls -lh
```

**Práctica 2:**
```bash
pwd          # Confirma dónde estás
ls           # Ve qué hay
ls -l        # Ve los detalles
ls -la       # Ve todo, incluso ocultos
```

***

## **2. Rutas Absolutas vs Rutas Relativas**

### **2.1 Rutas Absolutas**

Una ruta absoluta **siempre comienza desde la raíz** (`/`) y especifica la ubicación completa de un archivo o directorio. Son independientes de tu ubicación actual y siempre funcionan igual. [geeksforgeeks](https://www.geeksforgeeks.org/linux-unix/absolute-relative-pathnames-unix/)

**Características:**
- Comienzan con `/`
- Funcionan desde cualquier ubicación
- Son más largas pero inequívocas
- Ideales para scripts y automatización [geeksforgeeks](https://www.geeksforgeeks.org/linux-unix/absolute-relative-pathnames-unix/)

**Ejemplos:**
```bash
/home/usuario/documentos/proyecto
/var/log/syslog
/etc/nginx/nginx.conf
/usr/local/bin
```

### **2.2 Rutas Relativas**

Una ruta relativa **depende de tu directorio actual**. No comienza con `/` y se calcula desde donde te encuentres. [platformstack](https://platformstack.io/posts/absolute-vs-relative-path-in-linux-with-simple-examples/)

**Características:**
- NO comienzan con `/`
- Dependen de tu ubicación actual
- Son más cortas y rápidas de escribir
- Ideales para navegación interactiva [platformstack](https://platformstack.io/posts/absolute-vs-relative-path-in-linux-with-simple-examples/)

**Símbolos especiales:**
- `.` = directorio actual
- `..` = directorio padre (un nivel arriba)
- `~` = directorio home del usuario

**Ejemplos:**
```bash
documentos/proyecto          # Desde tu ubicación actual
./archivo.txt               # En el directorio actual
../carpeta_hermana          # Subir un nivel y entrar en carpeta_hermana
../../etc                   # Subir dos niveles y entrar en etc
```

### **2.3 Comparación Práctica**

Supongamos que estás en `/home/usuario`:

```bash
$ pwd
/home/usuario

# RUTA ABSOLUTA - siempre funciona igual
$ cd /home/usuario/documentos/proyectos

# RUTA RELATIVA - depende de estar en /home/usuario
$ cd documentos/proyectos

# Ambas te llevan al mismo lugar: /home/usuario/documentos/proyectos
```

**Práctica 3:**
```bash
pwd                                    # Anota tu ubicación
cd /tmp                               # Ruta absoluta
pwd                                    # Confirma: estás en /tmp
cd /home                              # Otra ruta absoluta
pwd                                    # Confirma: estás en /home
cd ~                                   # Ruta especial al home
pwd                                    # Confirma: estás en tu home
```

***

## **3. Navegación con cd - Cambiando de Directorio**

### **3.1 Sintaxis Básica**

```bash
cd [destino]
```

### **3.2 Navegación hacia Abajo (Entrando en directorios)**

"Bajar" significa entrar en subdirectorios más profundos en la jerarquía. [ceos3c](https://www.ceos3c.com/linux/linux-directory-navigation-a-complete-guide-to-cd-command/)

```bash
# Con ruta absoluta
$ cd /home/usuario/documentos

# Con ruta relativa
$ pwd
/home/usuario
$ cd documentos              # Entra en documentos
$ pwd
/home/usuario/documentos

# Múltiples niveles de una vez
$ cd /home/usuario/documentos/proyectos/2026/enero
```

**Práctica 4:**
```bash
cd ~                         # Ve al home
pwd                          # Confirma
ls                           # Ve qué hay
cd Documentos               # Entra (ajusta el nombre según tu sistema)
pwd                          # Confirma que "bajaste"
ls                           # Explora
```

### **3.3 Navegación hacia Arriba (Subiendo en la jerarquía)**

"Subir" significa ir al directorio padre. [ceos3c](https://www.ceos3c.com/linux/linux-directory-navigation-a-complete-guide-to-cd-command/)

```bash
# Subir un nivel
$ pwd
/home/usuario/documentos/proyectos
$ cd ..
$ pwd
/home/usuario/documentos

# Subir dos niveles
$ pwd
/home/usuario/documentos/proyectos/2026
$ cd ../..
$ pwd
/home/usuario/documentos

# Subir tres niveles
$ cd ../../..
```

**Práctica 5:**
```bash
cd /usr/local/bin           # Baja profundo con ruta absoluta
pwd                          # Confirma: /usr/local/bin
cd ..                        # Sube un nivel
pwd                          # Ahora: /usr/local
cd ..                        # Sube otro nivel
pwd                          # Ahora: /usr
cd ..                        # Sube al padre
pwd                          # Ahora: /
```

### **3.4 Atajos Esenciales del Comando cd**

| Atajo | Descripción | Ejemplo |
|-------|-------------|---------|
| `cd` o `cd ~` | Volver al directorio home  [ceos3c](https://www.ceos3c.com/linux/linux-directory-navigation-a-complete-guide-to-cd-command/) | `cd` |
| `cd -` | Volver al directorio anterior  [ceos3c](https://www.ceos3c.com/linux/linux-directory-navigation-a-complete-guide-to-cd-command/) | `cd -` |
| `cd ..` | Subir un nivel (directorio padre)  [ceos3c](https://www.ceos3c.com/linux/linux-directory-navigation-a-complete-guide-to-cd-command/) | `cd ..` |
| `cd ../..` | Subir dos niveles | `cd ../..` |
| `cd /` | Ir a la raíz del sistema | `cd /` |
| `cd ~/Documentos` | Ir a Documentos en tu home | `cd ~/Documentos` |

**Práctica 6 - Domina los Atajos:**
```bash
cd /var/log                 # Ve a un directorio
pwd                          # Confirma
cd ~                         # Vuelve al home (atajo 1)
pwd                          # Confirma
cd -                         # Vuelve al anterior (/var/log)
pwd                          # Confirma
cd -                         # Regresa al home de nuevo
pwd                          # Confirma
cd /etc/systemd/system      # Ve a otro lugar
cd                           # Sin argumentos = home
pwd                          # Confirma
```

### **3.5 Navegación Mixta (Subir y Bajar)**

Puedes combinar `..` con nombres de directorios. [ceos3c](https://www.ceos3c.com/linux/linux-directory-navigation-a-complete-guide-to-cd-command/)

```bash
$ pwd
/home/usuario/documentos/proyectos

# Subir un nivel y entrar en "descargas"
$ cd ../descargas
$ pwd
/home/usuario/documentos/descargas

# Subir dos niveles y entrar en otra ruta
$ cd ../../otros_usuario/compartido
```

**Práctica 7:**
```bash
cd ~/Documentos             # Punto de partida
pwd                          # Confirma
mkdir -p carpeta1/subcarpeta1    # Crea estructura (lo veremos después)
mkdir -p carpeta2/subcarpeta2
cd carpeta1/subcarpeta1     # Baja dos niveles
pwd                          # Anota dónde estás
cd ../../carpeta2           # Sube dos, baja uno
pwd                          # Confirma el cambio
cd ../..                     # Vuelve a Documentos
pwd                          # Confirma
```

***

## **4. Creación de Directorios con mkdir**

### **4.1 Crear Directorios Simples**

```bash
# Sintaxis básica
mkdir nombre_directorio

# Ejemplo
$ cd ~
$ mkdir mi_proyecto
$ ls
```

### **4.2 Crear Múltiples Directorios**

```bash
# Crear varios directorios al mismo tiempo
$ mkdir carpeta1 carpeta2 carpeta3
$ ls
```

### **4.3 Crear Estructuras Completas con -p**

La opción `-p` crea directorios padres si no existen (parent). [interserver](https://www.interserver.net/tips/kb/mastering-linux-file-navigation/)

```bash
# Crear toda la jerarquía de una vez
$ mkdir -p proyectos/2026/enero/entregables
$ ls -R proyectos/

# Verificar la estructura
$ cd proyectos/2026/enero/entregables
$ pwd
```

**Práctica 8:**
```bash
cd ~
mkdir practica_terminal
cd practica_terminal
pwd                                      # Confirma ubicación
mkdir dir1 dir2 dir3                    # Crea 3 directorios
ls                                       # Verifica
mkdir -p estructura/nivel2/nivel3/nivel4  # Crea jerarquía
ls -R                                    # Lista recursivamente
cd estructura/nivel2/nivel3/nivel4      # Baja toda la jerarquía
pwd                                      # Confirma dónde estás
cd ~                                     # Vuelve al home
```

***

## **5. Creación de Archivos con touch**

### **5.1 Crear Archivos Vacíos**

```bash
# Sintaxis
touch nombre_archivo

# Ejemplos
$ touch archivo.txt
$ touch documento.md
$ ls -l
```

### **5.2 Crear Múltiples Archivos**

```bash
$ touch archivo1.txt archivo2.txt archivo3.txt
$ ls
```

### **5.3 Crear Archivos en Rutas Específicas**

```bash
# Con ruta relativa
$ touch documentos/nuevo.txt

# Con ruta absoluta
$ touch /tmp/temporal.log

# La carpeta debe existir previamente
```

**Práctica 9:**
```bash
cd ~/practica_terminal
touch readme.md
touch notas.txt informe.doc presentacion.ppt
ls -l                                    # Ve los archivos creados
mkdir documentos
cd documentos
touch doc1.txt doc2.txt doc3.txt
ls
cd ..
touch documentos/doc4.txt               # Ruta relativa
ls documentos/
```

***

## **6. Eliminación de Archivos con rm**

### **6.1 Eliminar Archivos**

```bash
# Sintaxis básica
rm nombre_archivo

# Ejemplo
$ rm archivo.txt

# Eliminar múltiples archivos
$ rm archivo1.txt archivo2.txt

# Forzar eliminación sin confirmación
$ rm -f archivo.txt
```

### **6.2 Confirmación Interactiva**

```bash
# Pedir confirmación antes de eliminar
$ rm -i archivo_importante.txt
rm: remove regular file 'archivo_importante.txt'? y
```

**Práctica 10:**
```bash
cd ~/practica_terminal
ls                                       # Ve qué hay
touch basura1.txt basura2.txt basura3.txt
ls                                       # Confirma creación
rm basura1.txt                          # Elimina uno
ls                                       # Confirma eliminación
rm basura2.txt basura3.txt              # Elimina varios
ls                                       # Confirma
```

***

## **7. Eliminación de Directorios**

### **7.1 Eliminar Directorios Vacíos con rmdir**

```bash
# Solo funciona si el directorio está vacío
$ rmdir directorio_vacio
```

### **7.2 Eliminar Directorios con Contenido con rm -r**

La opción `-r` (recursive) elimina directorios y todo su contenido. [interserver](https://www.interserver.net/tips/kb/mastering-linux-file-navigation/)

```bash
# PRECAUCIÓN: Esto es destructivo
$ rm -r directorio_con_contenido

# Forzar sin preguntar (MUY PELIGROSO)
$ rm -rf directorio/

# Con confirmación (más seguro)
$ rm -ri directorio/
```

**⚠️ ADVERTENCIA:** `rm -rf` puede destruir datos permanentemente. Úsalo con extremo cuidado. [interserver](https://www.interserver.net/tips/kb/mastering-linux-file-navigation/)

**Práctica 11:**
```bash
cd ~/practica_terminal
mkdir temp_vacio
rmdir temp_vacio                        # Elimina directorio vacío
ls                                       # Confirma
mkdir -p temp_lleno/sub1/sub2
touch temp_lleno/archivo.txt
touch temp_lleno/sub1/archivo2.txt
ls -R temp_lleno/                       # Ve la estructura
rm -r temp_lleno                        # Elimina todo recursivamente
ls                                       # Confirma eliminación
```

***

## **8. Tab Completion - Autocompletado**

El autocompletado con Tab es una de las herramientas más potentes para aumentar tu velocidad. [ceos3c](https://www.ceos3c.com/linux/linux-directory-navigation-a-complete-guide-to-cd-command/)

### **8.1 Cómo Funciona**

- Escribe las primeras letras de un archivo/directorio
- Presiona `Tab` una vez: completa si hay coincidencia única
- Presiona `Tab` dos veces: muestra todas las opciones posibles

```bash
# Ejemplo
$ cd ~/Docu[Tab]
# Se completa automáticamente a:
$ cd ~/Documentos/

# Si hay múltiples opciones
$ cd ~/D[Tab][Tab]
Desktop/    Documents/    Downloads/
```

**Práctica 12:**
```bash
cd ~
mkdir -p autocompletado/directorio_muy_largo_para_escribir/subdirectorio
cd auto[Tab]                            # Completa a "autocompletado"
cd dir[Tab]                              # Completa al directorio largo
cd sub[Tab]                              # Completa a "subdirectorio"
pwd                                      # Confirma la ruta completa
cd                                       # Vuelve al home
```

***

## **9. Ejercicios de Integración**

### **Ejercicio 1: Navegación Básica**

```bash
# 1. Ve al home
cd ~
pwd

# 2. Lista el contenido
ls -la

# 3. Ve a /tmp con ruta absoluta
cd /tmp
pwd

# 4. Vuelve al home con atajo
cd
pwd

# 5. Ve a /var/log
cd /var/log
pwd

# 6. Vuelve a la ubicación anterior
cd -
pwd

# 7. Ve a la raíz
cd /
pwd
ls

# 8. Sube... espera, ya estás en la raíz
cd ..
pwd    # Sigues en /

# 9. Vuelve al home
cd ~
```

### **Ejercicio 2: Creación de Estructura de Proyecto**

```bash
# Crea esta estructura:
# proyecto/
#   ├── src/
#   │   ├── main.py
#   │   └── utils.py
#   ├── docs/
#   │   ├── readme.md
#   │   └── manual.pdf
#   └── tests/
#       └── test_main.py

cd ~
mkdir -p proyecto/src
mkdir -p proyecto/docs
mkdir -p proyecto/tests

touch proyecto/src/main.py
touch proyecto/src/utils.py
touch proyecto/docs/readme.md
touch proyecto/docs/manual.pdf
touch proyecto/tests/test_main.py

# Verifica la estructura
ls -R proyecto/

# Navega por ella
cd proyecto
pwd
cd src
pwd
ls
cd ../docs
pwd
ls
cd ../tests
pwd
cd ../..
pwd
```

### **Ejercicio 3: Navegación Compleja**

```bash
cd ~/proyecto/src
pwd                              # Anota: ~/proyecto/src

# Ve a docs usando ruta relativa (subir y bajar)
cd ../docs
pwd                              # Anota: ~/proyecto/docs

# Ve a tests usando ruta relativa
cd ../tests
pwd

# Vuelve a src sin usar cd ..
cd ~/proyecto/src
pwd

# Ahora usa ruta relativa de nuevo
cd ../../proyecto/docs
pwd

# Vuelve al home
cd
```

### **Ejercicio 4: Limpieza Controlada**

```bash
cd ~/proyecto/tests
ls
rm test_main.py
ls

cd ..
pwd                              # Estás en ~/proyecto
ls
rmdir tests                      # Elimina el directorio vacío
ls

cd src
rm main.py utils.py
cd ..
rmdir src
ls

cd docs
ls
cd ..
rm -r docs                       # Elimina directorio con contenido
ls

cd ..
rmdir proyecto                   # Elimina el directorio proyecto
ls
```

***

## **10. Ejercicios de Repetición Intensiva**

### **Bloque A: Repetir 5 veces**

```bash
# Iteración 1
cd ~
mkdir test_A1
cd test_A1
touch file1.txt file2.txt
ls
cd ..
rm -r test_A1

# Iteración 2
cd ~
mkdir test_A2
cd test_A2
touch file1.txt file2.txt
ls
cd ..
rm -r test_A2

# Iteración 3
cd ~
mkdir test_A3
cd test_A3
touch file1.txt file2.txt
ls
cd ..
rm -r test_A3

# Iteración 4
cd ~
mkdir test_A4
cd test_A4
touch file1.txt file2.txt
ls
cd ..
rm -r test_A4

# Iteración 5
cd ~
mkdir test_A5
cd test_A5
touch file1.txt file2.txt
ls
cd ..
rm -r test_A5
```

### **Bloque B: Navegación con .. (Repetir 5 veces)**

```bash
# Iteración 1
cd /usr/local/bin
pwd
cd ../../..
pwd

# Iteración 2
cd /var/log
pwd
cd ../..
pwd

# Iteración 3
cd /etc/systemd/system
pwd
cd ../../..
pwd

# Iteración 4
cd /home
pwd
cd ..
pwd

# Iteración 5
cd /tmp
pwd
cd ..
pwd
```

### **Bloque C: Rutas Absolutas vs Relativas (Repetir 3 veces)**

```bash
# Iteración 1
cd ~
mkdir -p demo/sub1/sub2
cd /home/$USER/demo/sub1/sub2    # Absoluta
pwd
cd ../../..                       # Relativa
pwd
rm -r demo

# Iteración 2
cd ~
mkdir -p demo/sub1/sub2
cd demo/sub1/sub2                 # Relativa
pwd
cd ~                              # Atajo (es ruta absoluta a home)
rm -r demo

# Iteración 3
cd ~
mkdir -p demo/sub1/sub2
cd ~/demo/sub1                    # Absoluta con ~
pwd
cd sub2                           # Relativa
pwd
cd ~
rm -r demo
```

***

## **11. Escenarios Reales del Día a Día**

### **Escenario 1: Organizar Descargas**

```bash
cd ~/Descargas
ls
mkdir -p Documentos Imagenes Videos Software
mv *.pdf Documentos/
mv *.jpg Imagenes/
mv *.png Imagenes/
mv *.mp4 Videos/
ls -l
cd Documentos
ls
cd ../Imagenes
ls
cd ~
```

### **Escenario 2: Revisar Logs del Sistema**

```bash
cd /var/log
ls -lh
cd nginx/              # Si tienes nginx instalado
ls
cd ../apache2/         # O apache
cd ..
cd /var/log
tail -20 syslog        # Ver últimas 20 líneas
cd ~
```

### **Escenario 3: Gestión de Proyecto de Desarrollo**

```bash
cd ~/proyectos
mkdir -p mi_app/{src,tests,docs,config}
cd mi_app
ls
cd src
touch app.py models.py views.py
ls
cd ../tests
touch test_app.py test_models.py
cd ../docs
touch README.md API.md
cd ..
pwd
ls -R
cd ~
```

***

## **12. Consejos Avanzados**

### **12.1 Uso de pushd y popd**

Estos comandos crean una pila de directorios para navegación rápida.

```bash
# Guardar ubicación actual y cambiar
$ cd ~/Documentos
$ pushd /var/log
$ pwd
/var/log

# Volver a la ubicación guardada
$ popd
$ pwd
/home/usuario/Documentos
```

### **12.2 Búsqueda Rápida con find**

```bash
# Encontrar directorios con cierto nombre
$ find ~ -type d -name "proyecto*"

# Encontrar archivos
$ find ~ -type f -name "*.txt"
```

### **12.3 Alias para Navegación**

Agrega estos al archivo `~/.bashrc` o `~/.zshrc`:

```bash
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias ll='ls -lah'
alias la='ls -A'
```

***

## **13. Checklist de Dominio**

Marca cuando puedas hacer cada tarea sin pensar:

- [ ] Uso `pwd` para saber dónde estoy
- [ ] Uso `ls` para ver el contenido
- [ ] Entiendo la diferencia entre rutas absolutas y relativas
- [ ] Puedo usar `cd` con rutas absolutas
- [ ] Puedo usar `cd` con rutas relativas
- [ ] Sé subir directorios con `cd ..`
- [ ] Sé usar `cd ~` para ir al home
- [ ] Sé usar `cd -` para volver al directorio anterior
- [ ] Uso Tab para autocompletar
- [ ] Creo directorios con `mkdir`
- [ ] Creo estructuras completas con `mkdir -p`
- [ ] Creo archivos con `touch`
- [ ] Elimino archivos con `rm`
- [ ] Elimino directorios con `rm -r`
- [ ] Combino navegación (subir y bajar en un comando)
- [ ] Puedo navegar por todo el sistema sin interfaz gráfica

***

## **14. Errores Comunes y Soluciones**

| Error | Causa | Solución |
|-------|-------|----------|
| `No such file or directory` | El path no existe | Verifica con `ls` y `pwd` |
| `Permission denied` | No tienes permisos | Usa `sudo` o cambia permisos |
| `Not a directory` | Intentas usar `cd` en un archivo | Verifica con `ls -l` |
| `Directory not empty` | Usas `rmdir` en directorio con contenido | Usa `rm -r` en su lugar |
| `Command not found` | Error de escritura o comando no instalado | Revisa ortografía |

***

## **15. Práctica Final: Test Completo**

Completa este ejercicio sin mirar la documentación:

```bash
# 1. Ve a tu home


# 2. Crea esta estructura:
#    examen/
#      ejercicio1/
#        solucion.txt
#      ejercicio2/
#        codigo.py
#      ejercicio3/
#        datos.csv


# 3. Navega a ejercicio2


# 4. Vuelve a examen usando ruta relativa


# 5. Ve a ejercicio3 usando ruta relativa


# 6. Crea un archivo nuevo llamado resultados.txt


# 7. Vuelve al home


# 8. Elimina toda la estructura examen/


# 9. Confirma que se eliminó
```

***

**Recuerda:**
- Las rutas absolutas empiezan con `/` y funcionan siempre igual [geeksforgeeks](https://www.geeksforgeeks.org/linux-unix/absolute-relative-pathnames-unix/)
- Las rutas relativas dependen de tu ubicación actual [platformstack](https://platformstack.io/posts/absolute-vs-relative-path-in-linux-with-simple-examples/)
- El autocompletado con Tab es tu mejor aliado [ceos3c](https://www.ceos3c.com/linux/linux-directory-navigation-a-complete-guide-to-cd-command/)
- `pwd` y `ls` son tus herramientas de orientación constante [linuxcommand](https://linuxcommand.org/lc3_lts0020.php)

¡Sigue practicando y dominarás el terminal!