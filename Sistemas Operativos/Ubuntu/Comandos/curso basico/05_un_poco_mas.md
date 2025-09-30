

### 1. Visualización y Análisis de Contenido de Ficheros

Hemos visto cómo crear ficheros (`touch`, `echo >`), pero una de las tareas más comunes es **inspeccionar su contenido**.

  * **`cat` (Concatenate)**: Muestra el contenido completo de uno o más ficheros en la salida estándar (la terminal). Es ideal para ficheros cortos.

    ```bash
    # Ver el contenido de un fichero de configuración
    cat /etc/hostname
    ```

  * **`less` (Less is more)**: Es un visor de ficheros interactivo. Permite navegar por ficheros largos hacia adelante y hacia atrás usando las flechas, buscar texto con `/` y salir con `q`. Es mucho más práctico que `cat` para ficheros de log o código fuente.

    ```bash
    # Explorar un log del sistema de forma interactiva
    less /var/log/syslog
    ```

  * **`head` y `tail`**: Muestran las primeras (`head`) o las últimas (`tail`) líneas de un fichero. Son extremadamente útiles para ver el inicio de un fichero de configuración o los últimos eventos de un log en tiempo real.

    ```bash
    # Ver las primeras 10 líneas de un fichero
    head un_fichero_largo.csv

    # Ver las últimas 5 líneas de un log y seguir viendo las nuevas que lleguen
    tail -n 5 -f /var/log/syslog
    ```

-----

### \#\# 2. Búsqueda y Filtrado de Texto con `grep`

El comando `grep` (Global Regular Expression Print) es posiblemente una de las herramientas más potentes de la terminal. Permite buscar patrones de texto dentro de ficheros o en la salida de otros comandos. Es el "bisturí" para encontrar información.

  * **Buscar texto en un fichero**:

    ```bash
    # Encontrar todas las líneas que contienen la palabra "error" en un log
    grep "error" /var/log/syslog
    ```

  * **Filtrar la salida de otro comando (usando un pipeline, que explicaremos a continuación)**:

    ```bash
    # Listar todos los procesos en ejecución y mostrar solo los relacionados con python
    ps aux | grep "python"
    ```

-----

### \#\# 3. El Poder de las Tuberías (Pipelines `|`)

Este es un concepto transformador. Una **tubería**, representada por el carácter `|`, conecta la **salida estándar (`stdout`)** de un comando con la **entrada estándar (`stdin`)** del siguiente. Esto permite encadenar comandos simples para crear flujos de trabajo complejos y potentes sin necesidad de ficheros intermedios.

  * **Concepto**: `comando1 | comando2 | comando3`

      * La salida de `comando1` se convierte en la entrada de `comando2`.
      * La salida de `comando2` se convierte en la entrada de `comando3`.

  * **Ejemplo Práctico**: Obtener los 5 procesos que más CPU consumen.

    ```bash
    # 1. ps aux: Lista todos los procesos
    # 2. sort -nrk 3: Ordena la salida numéricamente (-n), en orden inverso (-r), por la tercera columna (-k 3), que es la de %CPU.
    # 3. head -5: Muestra solo las primeras 5 líneas del resultado ordenado.
    ps aux | sort -nrk 3 | head -5
    ```

-----

### \#\# 4. Comandos de Gestión del Sistema y Monitorización

Para un uso práctico, es vital saber qué está ocurriendo en el sistema.

  * **`df` (Disk Free)**: Muestra el uso del espacio en disco de los sistemas de ficheros montados. La opción `-h` (`human-readable`) es casi obligatoria para entender la salida.

    ```bash
    # Ver el espacio libre en todos los discos de forma legible
    df -h
    ```

  * **`du` (Disk Usage)**: Muestra el espacio en disco usado por un fichero o directorio. También se suele usar con `-h`.

    ```bash
    # Ver cuánto ocupa la carpeta 'proyecto_empresarial' y sus subdirectorios
    du -h /proyecto_empresarial
    ```

  * **`ps` (Process Status)** y **`kill`**: `ps` muestra una "fotografía" de los procesos que se están ejecutando en ese instante. `kill` permite enviar señales a los procesos, normalmente para terminarlos.

    ```bash
    # Ver todos mis procesos en ejecución
    ps u

    # Forzar la detención de un proceso con PID (Process ID) 1234
    kill -9 1234
    ```

  * **`top` (o el más moderno `htop`)**: Ofrece una vista en tiempo real y dinámica de los procesos y el consumo de recursos del sistema (CPU, memoria). Es el monitor de actividad por excelencia.

    ```bash
    top
    ```

-----

### \#\# 5. Compresión y Archivado con `tar`

Es una tarea muy común agrupar múltiples ficheros y directorios en un único fichero (`.tar`) y, opcionalmente, comprimirlo (`.tar.gz` o `.tgz`).

  * **`tar` (Tape Archive)**: Es la herramienta estándar para esto. Su sintaxis puede parecer compleja, pero las combinaciones más comunes son fáciles de recordar:

      * **`c`**: **C**rear un archivo.
      * **`x`**: **E**xtraer de un archivo.
      * **`v`**: **V**erboso (muestra los ficheros mientras opera).
      * **`f`**: **F**ichero (indica que el siguiente argumento es el nombre del archivo).
      * **`z`**: Comprimir/descomprimir con **g(z)ip**.

  * **Ejemplos**:

    ```bash
    # Comprimir la carpeta 'proyecto_A' en un fichero llamado 'backup.tar.gz'
    tar -czvf backup.tar.gz /home/techsolutions/proyectos/proyecto_A

    # Descomprimir el fichero en el directorio actual
    tar -xzvf backup.tar.gz
    ```