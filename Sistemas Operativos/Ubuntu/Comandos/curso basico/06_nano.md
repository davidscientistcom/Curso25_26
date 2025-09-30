### 6. Edición de Ficheros en la Terminal con `nano`

Un editor de texto que se ejecuta directamente en la terminal es una herramienta indispensable. `nano` es un editor ligero, intuitivo y presente en la mayoría de las distribuciones de Linux, lo que lo convierte en la opción ideal para ediciones rápidas de ficheros de configuración, scripts o notas.

#### **6.1 Operaciones Básicas: Abrir, Guardar y Salir**

La sintaxis para abrir un fichero es simple. Si el fichero no existe, `nano` lo creará al momento de guardarlo.

```bash
# Abrir (o crear) un script de Python
nano mi_script.py
```

Una vez dentro de `nano`, verás una interfaz de texto simple. En la parte inferior, se muestra una leyenda con los comandos más comunes. El símbolo `^` representa la tecla **Ctrl**.

  * **Guardar el fichero**: Presiona `Ctrl + O` ("Write **O**ut"). `nano` te pedirá confirmar el nombre del fichero en la parte inferior. Simplemente presiona **Enter**.
  * **Salir de `nano`**: Presiona `Ctrl + X` ("E**x**it"). Si has realizado cambios sin guardar, `nano` te preguntará si deseas hacerlo. Pulsa `Y` (Yes) para guardar, `N` (No) para descartar los cambios, o `Ctrl + C` para cancelar y volver al editor.

-----

#### **6.2 Navegación y Edición Esencial**

  * **Mover el cursor**: Puedes usar las **teclas de flecha** para moverte por el documento de forma intuitiva.
  * **Cortar, Copiar y Pegar**:
      * **Cortar una línea entera**: Sitúa el cursor en la línea que quieres cortar y presiona `Ctrl + K` (**K**ill). La línea desaparecerá, pero quedará guardada en el portapapeles de `nano`.
      * **Pegar texto**: Mueve el cursor a la posición deseada y presiona `Ctrl + U` (**U**ncut) para pegar el texto que cortaste previamente.
      * **Copiar una línea entera**: La forma más sencilla es usar la combinación de cortar y pegar. Presiona `Ctrl + K` para cortar la línea y `Ctrl + U` para pegarla de nuevo en su sitio. Ahora la línea está en el portapapeles y puedes pegarla en otro lugar con `Ctrl + U`.
      * **Copiar una selección de texto**:
        1.  Mueve el cursor al inicio del texto que quieres copiar.
        2.  Presiona `Alt + A` para marcar el inicio de la selección (**Set Mark**).
        3.  Usa las flechas para extender la selección.
        4.  Presiona `Alt + 6` para copiar el texto seleccionado al portapapeles.
        5.  Pega el texto con `Ctrl + U`.

-----

#### **6.3 Búsqueda y Reemplazo de Texto**

Estas son funcionalidades cruciales cuando trabajas con ficheros grandes.

  * **Buscar una palabra (`Where is`)**:

    1.  Presiona `Ctrl + W`.
    2.  Escribe el término que quieres buscar en el menú inferior y presiona **Enter**.
    3.  El cursor saltará a la primera coincidencia.
    4.  Para encontrar la siguiente coincidencia, simplemente presiona `Alt + W`.

  * **Buscar y Reemplazar (`Replace`)**:

    1.  Presiona `Ctrl + \` (en algunos teclados, puede ser `Alt + R`).
    2.  `nano` te pedirá el término a buscar ("Search (to replace)"). Escríbelo y presiona **Enter**.
    3.  Luego, te pedirá el texto por el que lo quieres reemplazar ("Replace with"). Escríbelo y presiona **Enter**.
    4.  `nano` se detendrá en la primera coincidencia y te preguntará qué hacer:
          * Pulsa `Y` para reemplazar esta única coincidencia.
          * Pulsa `N` para saltar esta coincidencia y buscar la siguiente.
          * Pulsa `A` para reemplazar **todas** las coincidencias en el fichero de una sola vez.
          * Pulsa `Ctrl + C` para cancelar la operación de reemplazo.

-----

#### **6.4 Funcionalidades Avanzadas 🚀**

  * **Ir a una línea específica**: Si estás depurando un script y un error te indica una línea concreta (p. ej., "error on line 42"), puedes saltar directamente a ella. Presiona `Ctrl + _` (guion bajo), escribe el número de la línea y presiona **Enter**.
  * **Mostrar números de línea**: Para ver los números de línea constantemente, puedes presionar `Alt + N`. También puedes iniciarlo con `nano -l mi_fichero.txt` o configurarlo de forma permanente (ver abajo).
  * **Justificar un párrafo**: `Alt + J` justifica el párrafo donde se encuentra el cursor.
  * **Configuración permanente con `.nanorc`**: Puedes personalizar el comportamiento de `nano` creando un fichero de configuración en tu directorio personal llamado `.nanorc`.
    ```bash
    # Abre el fichero de configuración de nano
    nano ~/.nanorc
    ```
    Dentro de este fichero, puedes añadir opciones útiles:
    ```nanorc
    # Muestra los números de línea a la izquierda
    set linenumbers

    # Habilita el uso del ratón para posicionar el cursor
    set mouse

    # Convierte los tabuladores en 4 espacios (esencial para Python)
    set tabsize 4
    set tabstospaces
    ```
    Guarda el fichero (`Ctrl + O`, **Enter**, `Ctrl + X`) y la próxima vez que abras `nano`, estas opciones estarán activas.

-----

#### **Tabla de Comandos de `nano` (Hoja de Referencia)**

| Acción | Atajo de Teclado | Descripción |
| :--- | :--- | :--- |
| **Gestión de Ficheros** | | |
| Guardar | `Ctrl + O` | Guarda los cambios actuales en el fichero. |
| Salir | `Ctrl + X` | Cierra el editor. |
| **Edición** | | |
| Cortar línea | `Ctrl + K` | Corta la línea actual al portapapeles. |
| Pegar | `Ctrl + U` | Pega el contenido del portapapeles. |
| Copiar Selección | `Alt + 6` | Copia el texto seleccionado (previamente marcado con `Alt + A`). |
| Deshacer | `Alt + U` | Deshace la última acción. |
| Rehacer | `Alt + E` | Rehace la última acción deshecha. |
| **Navegación y Búsqueda**| | |
| Buscar | `Ctrl + W` | Busca un término en el texto. |
| Buscar Siguiente | `Alt + W` | Salta a la siguiente ocurrencia de la búsqueda. |
| Reemplazar | `Ctrl + \` | Busca y reemplaza un término. |
| Ir a Línea/Columna | `Ctrl + _` | Salta a un número de línea y columna específico. |