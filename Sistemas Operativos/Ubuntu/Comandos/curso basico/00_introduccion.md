### **Capítulo 1: Introducción a la Terminal de Linux**

#### **1.1 ¿Qué es un Comando en Linux?**

En su esencia, un **comando** es una instrucción textual que se proporciona al sistema operativo a través de una interfaz de línea de comandos (CLI), comúnmente conocida como **terminal** o *shell*. Es el método fundamental para interactuar de forma directa, precisa y programática con el núcleo del sistema.

Desde una perspectiva de la informática, la terminal expone las funcionalidades del sistema operativo de una forma programática, donde cada comando invoca un programa específico diseñado para una tarea. Esta característica la convierte en una herramienta de una potencia y flexibilidad inigualables para la automatización, la precisión y la eficiencia.

Existen dos tipos de comandos:

  * **Comandos Internos**: Son funcionalidades integradas en el propio intérprete de comandos (*shell*). No requieren ejecutar un programa externo. Ejemplos clásicos son `cd` (para cambiar de directorio), `echo` (para imprimir texto) o `exit`.
  * **Comandos Externos**: Son programas ejecutables que residen en el sistema de archivos (generalmente en directorios listados en la variable de entorno `$PATH`). Comandos como `ls` (listar), `cp` (copiar) o `grep` (buscar) son externos.

Puedes determinar el tipo de un comando utilizando `type`:

```bash
type cd   # Salida: cd is a shell builtin
type ls   # Salida: ls is aliased to 'ls --color=auto' (o muestra la ruta /bin/ls)
```

#### **1.2 Estructura de un Comando**

La sintaxis de un comando en Linux sigue una estructura general y predecible: `comando [opciones] [argumentos]`.

  * **Comando**: Es la acción principal a ejecutar (`ls`, `rm`, `mkdir`).
  * **Opciones**: Modifican el comportamiento del comando. Se preceden por uno (`-l`) o dos guiones (`--help`) y pueden agruparse (`-lh`).
  * **Argumentos**: Es la información sobre la que actúa el comando, como un nombre de fichero o una ruta de directorio.

**Ejemplo Analizado**:

```bash
ls -lh /var/log
```

  * **Comando**: `ls`.
  * **Opciones**: `-lh` (`-l` para formato largo, `-h` para tamaño legible).
  * **Argumento**: `/var/log` (el directorio cuyo contenido queremos listar).

-----

#### **1.3 Navegando el Sistema de Archivos: Rutas, Atajos y Comodines**

El sistema de archivos de Linux es una estructura de árbol jerárquica que parte de un único origen: el directorio raíz (`/`). Para localizar cualquier elemento, usamos **rutas**.

##### **1.3.1 Rutas Absolutas y Relativas**

  * **Ruta Absoluta**: Es la dirección completa y unívoca de un fichero o directorio, **comenzando siempre desde la raíz (`/`)**. No importa cuál sea tu ubicación actual, una ruta absoluta siempre apunta al mismo lugar.

      * Ejemplo: `/home/usuario/doctorado/simulaciones`

  * **Ruta Relativa**: Especifica una ubicación en relación con tu **directorio de trabajo actual**. Nunca empieza con `/`.

      * Ejemplo: Si estás en `/home/usuario/doctorado`, la ruta relativa a simulaciones sería simplemente `simulaciones`.

##### **1.3.2 Directorios Especiales: Atajos Esenciales**

Para hacer la navegación más eficiente, el sistema define unos alias o atajos:

  * `/` (Barra): El directorio **raíz**, el origen de todo el sistema de archivos.
  * `~` (Tilde): Representa tu **directorio personal** o *home*. Es un atajo para `/home/tu_usuario`.
  * `.` (Un punto): Representa el **directorio actual**. Es útil para ejecutar scripts (`./mi_script.sh`) o en comandos como `find`.
  * `..` (Dos puntos): Representa el **directorio padre** (el que está un nivel jerárquico por encima).

##### **1.3.3 Comodines (Wildcards): Búsquedas Flexibles**

Los comodines son caracteres especiales que permiten crear patrones para referirse a múltiples ficheros a la vez.

  * `*` (Asterisco): Sustituye **cero o más caracteres**.

      * `ls *.txt`: Lista todos los ficheros que terminen en `.txt`.
      * `rm reporte_*`: Elimina todos los ficheros que comiencen por `reporte_`.

  * `?` (Interrogación): Sustituye **exactamente un carácter**.

      * `ls imagen_0?.jpg`: Listaría `imagen_01.jpg`, `imagen_02.jpg`, pero no `imagen_10.jpg`.

  * `[]` (Corchetes): Representa un **rango o conjunto de caracteres**.

      * `ls archivo[1-3].log`: Listaría `archivo1.log`, `archivo2.log` y `archivo3.log`.
      * `ls [aeiou]*.txt`: Listaría cualquier fichero `.txt` que comience por una vocal minúscula.

-----

#### **1.4 Comandos Fundamentales para Moverse y Manipular Ficheros**

  * `pwd` (Print Working Directory): Muestra la ruta absoluta del directorio donde te encuentras.
  * `ls` (List): Lista el contenido de un directorio.
  * `cd` (Change Directory): Cambia tu directorio de trabajo actual.
  * `mkdir` (Make Directory): Crea nuevos directorios.
  * `touch`: Crea un fichero vacío si no existe o actualiza su fecha de modificación si ya existe.
  * `echo` y Redirección (`>`, `>>`): `echo` imprime texto, y los operadores de redirección envían esa salida a un fichero.
      * `>`: **Sobrescribe** el contenido del fichero.
      * `>>`: **Añade** el contenido al final del fichero.

-----

#### **1.5 ¿Necesitas Ayuda? Cómo Preguntarle a la Terminal**

Nunca necesitarás memorizar todas las opciones. Saber cómo obtener ayuda es una habilidad fundamental.

  * **Opción `--help`**: Ofrece un resumen rápido del propósito, uso y opciones de un comando. Es ideal para una consulta veloz.

    ```bash
    ls --help
    ```

  * **Comando `man` (Manual)**: Abre la página del manual completa y detallada de un comando. Es la fuente de información más exhaustiva. Usa las flechas para navegar y la tecla `q` para salir.

    ```bash
    man ls
    ```

  * **Comando `apropos` y `whatis`**:

      * `apropos <palabra_clave>`: Busca comandos relacionados con una palabra clave. Muy útil si no recuerdas el nombre exacto de un comando.
      * `whatis <comando>`: Muestra una descripción de una sola línea sobre lo que hace un comando.

-----

#### **1.6 Ejercicio Práctico Guiado**

Apliquemos todo lo anterior.

1.  **Ve a tu directorio personal y crea una estructura para el proyecto.**

    ```bash
    cd ~
    mkdir -p doctorado/simulaciones/resultados
    ```

2.  **Navega al directorio más profundo y verifica tu ubicación.**

    ```bash
    cd doctorado/simulaciones/resultados
    pwd
    ```

3.  **Crea varios ficheros de logs usando `touch` y un comodín.**

    ```bash
    # Esto crea log_01.txt, log_02.txt ... log_05.txt
    touch log_0{1..5}.txt
    ```

4.  **Crea un fichero de resumen con contenido usando `echo` y redirección.**

    ```bash
    echo "Resumen del Experimento Inicial" > resumen.md
    echo "Fecha: $(date)" >> resumen.md
    ```

5.  **Lista solo los ficheros de log.**

    ```bash
    ls *.txt
    ```

6.  **Sube al directorio `doctorado` usando `..`.**

    ```bash
    cd ../..
    pwd
    ```

7.  **Desde ahí, lista el contenido de `resultados` usando una ruta relativa.**

    ```bash
    ls simulaciones/resultados
    ```