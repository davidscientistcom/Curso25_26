# Git & GitHub: Tutorial Práctico Profesional

De commits básicos a flujos de trabajo enterprise - Aprende haciendo

## Objetivos de Aprendizaje

Al finalizar este tutorial serás capaz de:

- Entender cómo funciona Git internamente
- Resolver conflictos complejos con confianza
- Dominar rebase y merge (y saber cuándo usar cada uno)
- Recuperarte de cualquier error con Git
- Implementar flujos de trabajo profesionales (Git Flow, trunk-based)
- Usar GitHub de forma profesional (PRs, reviews, actions)
- Debuggear problemas en repositorios grandes

***

# PARTE 1: FUNDAMENTOS Y CONFIGURACIÓN

## 1.1 Instalación de Git

### Windows

**Opción 1: Git for Windows (Recomendado)**

1. Descarga el instalador desde https://git-scm.com/download/win
2. Ejecuta el instalador
3. Configuración recomendada durante la instalación:
   - Editor: Selecciona tu editor preferido (VS Code, Notepad++, Vim)
   - PATH: "Git from the command line and also from 3rd-party software"
   - Line endings: "Checkout Windows-style, commit Unix-style line endings"
   - Terminal: "Use MinTTY"

4. Verifica la instalación abriendo PowerShell o CMD:

```bash
git --version
```

Deberías ver algo como: `git version 2.43.0.windows.1`

**Opción 2: Windows Subsystem for Linux (WSL)**

Si usas WSL, sigue las instrucciones de Linux más abajo. [kinsta](https://kinsta.com/blog/install-git/)

### macOS

**Opción 1: Homebrew (Recomendado)**

```bash
brew install git
```

**Opción 2: Xcode Command Line Tools**

```bash
xcode-select --install
```

**Opción 3: Instalador oficial**

Descarga desde https://git-scm.com/download/mac

Verifica la instalación:

```bash
git --version
```

### Linux

**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install git
```

**Fedora:**

```bash
sudo dnf install git
```

**Arch Linux:**

```bash
sudo pacman -S git
```

Verifica la instalación:

```bash
git --version
```

***

## 1.2 Configuración Inicial Obligatoria

Antes de hacer tu primer commit, Git necesita saber quién eres. Esta información se incluirá en cada commit que hagas. [github](https://github.com/git-guides/install-git)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"
```

**Importante:** Usa el mismo email que usarás en GitHub/GitLab si planeas trabajar con repositorios remotos.

### Configurar el Editor

Git abrirá un editor de texto para mensajes de commit y otras operaciones. Configura tu editor preferido:

**VS Code:**
```bash
git config --global core.editor "code --wait"
```

**Vim:**
```bash
git config --global core.editor "vim"
```

**Nano:**
```bash
git config --global core.editor "nano"
```

**Notepad++ (Windows):**
```bash
git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"
```

### Configuración de Line Endings

Los sistemas operativos manejan los saltos de línea de forma diferente. Para evitar problemas en equipos colaborativos:

**Linux/macOS:**
```bash
git config --global core.autocrlf input
```

**Windows:**
```bash
git config --global core.autocrlf true
```

### Configuración del Comportamiento de Pull

Para evitar warnings molestos:

```bash
git config --global pull.rebase false
```

### Habilitar Colores

Para mejor legibilidad en la terminal:

```bash
git config --global color.ui auto
```

### Verificar tu Configuración

```bash
git config --list
```

O para ver valores específicos:

```bash
git config user.name
git config user.email
```

### EJERCICIO 1: Configuración Inicial

**Objetivo:** Configurar Git correctamente en tu sistema.

**Pasos:**

1. Verifica que Git está instalado con `git --version`
2. Configura tu nombre y email
3. Configura tu editor preferido
4. Configura line endings según tu sistema operativo
5. Verifica toda tu configuración con `git config --list`
6. Comprueba valores específicos con `git config user.name` y `git config user.email`

**Resultado esperado:**

Deberías poder ejecutar `git config --list` y ver al menos:

```
user.name=Tu Nombre
user.email=tu.email@ejemplo.com
core.editor=code --wait
core.autocrlf=input (o true en Windows)
color.ui=auto
pull.rebase=false
```

***

## 1.3 Cómo Funciona Git Internamente

Antes de empezar a usar Git, es crucial entender cómo funciona por dentro. Esta comprensión te ayudará a resolver problemas y a usar Git con confianza.

### Git es una Base de Datos de Contenido

Git no almacena diferencias entre archivos (como SVN o CVS). En su lugar, Git almacena snapshots completos de tu proyecto en cada commit. Para hacer esto eficiente, usa cuatro tipos de objetos. [gist.github](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13)

### Los Cuatro Tipos de Objetos Git

#### 1. Blob (Binary Large Object)

Un blob almacena el contenido de un archivo. Solo el contenido, sin nombre ni metadata.

Ejemplo:
- Archivo: `README.md` con contenido "Hola Git"
- Git crea: Blob con hash `abc123` que contiene "Hola Git"

#### 2. Tree (Árbol)

Un tree representa un directorio. Contiene:
- Referencias a blobs (archivos)
- Referencias a otros trees (subdirectorios)
- Nombres de archivos
- Permisos de archivos

Ejemplo:
```
Tree raíz
├── blob abc123 (README.md)
├── blob def456 (main.py)
└── tree xyz789 (src/)
    └── blob ghi012 (utils.py)
```

#### 3. Commit

Un commit es un snapshot completo de tu proyecto en un momento específico. Contiene:
- Referencia a un tree (el estado del proyecto)
- Referencia al commit padre (excepto el primer commit)
- Autor y fecha
- Mensaje de commit

#### 4. Tag

Un tag es una etiqueta permanente que apunta a un commit específico. Se usa para marcar releases (v1.0.0, v2.0.0, etc.).

### Visualización de Objetos

Cuando haces un commit, Git crea esta estructura:

```
COMMIT abc123
├── Tree def456 (directorio raíz)
│   ├── Blob 111111 (README.md)
│   ├── Blob 222222 (main.py)
│   └── Tree 333333 (src/)
│       └── Blob 444444 (utils.py)
├── Parent: xyz789 (commit anterior)
├── Author: David <david@example.com>
└── Message: "feat: add utils module"
```

### EJERCICIO 2: Explorar Objetos Git

**Objetivo:** Ver cómo Git almacena información internamente.

**Pasos:**

1. Crea un directorio de prueba:

```bash
mkdir git-internals-test
cd git-internals-test
git init
```

2. Crea un archivo simple:

```bash
echo "Hola Git" > prueba.txt
```

3. Añade el archivo al staging area:

```bash
git add prueba.txt
```

4. Verifica que Git creó un blob:

```bash
git hash-object prueba.txt
```

Esto te dará un hash como `8d0e41234f24b6da002d962a26c2495ea16a425f`

5. Examina el objeto blob:

```bash
git cat-file -t 8d0e41234f24b6da002d962a26c2495ea16a425f
```

Salida: `blob`

```bash
git cat-file -p 8d0e41234f24b6da002d962a26c2495ea16a425f
```

Salida: `Hola Git`

6. Crea un commit:

```bash
git commit -m "primer commit"
```

7. Examina el objeto commit:

```bash
git cat-file -t HEAD
```

Salida: `commit`

```bash
git cat-file -p HEAD
```

Salida similar a:
```
tree 4b825dc642cb6eb9a060e54bf8d69288fbee4904
author Tu Nombre <tu.email@ejemplo.com> 1737572400 +0100
committer Tu Nombre <tu.email@ejemplo.com> 1737572400 +0100

primer commit
```

8. Examina el tree del commit:

```bash
git cat-file -p HEAD^{tree}
```

Salida similar a:
```
100644 blob 8d0e41234f24b6da002d962a26c2495ea16a425f    prueba.txt
```

**Resultado esperado:**

Deberías entender que:
- Git almacena el contenido en blobs
- Los trees organizan blobs en estructuras de directorios
- Los commits apuntan a trees y contienen metadata
- Todo se identifica por hashes SHA-1

***

## 1.4 Las Tres Áreas de Git

Git tiene tres áreas principales donde los archivos pueden residir:

### 1. Working Directory (Directorio de Trabajo)

Es tu carpeta de proyecto donde editas archivos. Los archivos aquí pueden estar en cualquier estado.

### 2. Staging Area (Área de Preparación o Index)

Un área intermedia donde preparas los cambios que irán en el próximo commit. También se llama "index".

### 3. Repository (Repositorio o .git directory)

Donde Git almacena permanentemente los commits. Está en el directorio `.git/`.

### Flujo de Trabajo

```
Working Directory  →  Staging Area  →  Repository
     (edit)          (git add)       (git commit)
```

Ejemplo visual:

```
┌─────────────────┐
│ Working Dir     │  ← Editas archivos aquí
│                 │
│ file.txt (mod)  │
└─────────────────┘
        │
        │ git add file.txt
        ▼
┌─────────────────┐
│ Staging Area    │  ← Preparas cambios aquí
│                 │
│ file.txt        │
└─────────────────┘
        │
        │ git commit -m "mensaje"
        ▼
┌─────────────────┐
│ Repository      │  ← Commits permanentes aquí
│                 │
│ commit abc123   │
└─────────────────┘
```

***

## 1.5 Los Cuatro Estados de un Archivo

Un archivo en tu proyecto Git puede estar en uno de estos cuatro estados:

### 1. Untracked (No rastreado)

Git no sabe que existe. Archivos nuevos que nunca se han añadido con `git add`.

### 2. Unmodified (Sin modificar)

El archivo está en el repositorio y no ha cambiado desde el último commit.

### 3. Modified (Modificado)

El archivo ha cambiado en el working directory pero no está en staging.

### 4. Staged (Preparado)

El archivo está en staging area, listo para el próximo commit.

### Diagrama de Transiciones

```
Untracked ──(git add)──→ Staged
                            │
                     (git commit)
                            │
                            ▼
                        Unmodified
                            │
                      (edit file)
                            │
                            ▼
                        Modified
                            │
                       (git add)
                            │
                            ▼
                        Staged
```

**Importante:** Un archivo puede estar staged Y modified al mismo tiempo. Esto sucede cuando:
1. Modificas un archivo
2. Haces `git add` (ahora está staged)
3. Modificas el archivo de nuevo (la versión en staging es diferente a la del working directory)

### EJERCICIO 3: Estados de Archivos

**Objetivo:** Experimentar con los cuatro estados de archivos.

**Pasos:**

1. Crea un nuevo repositorio:

```bash
mkdir estados-test
cd estados-test
git init
```

2. Crea un archivo nuevo:

```bash
echo "Línea 1" > archivo.txt
```

3. Verifica el estado (debería ser Untracked):

```bash
git status
```

Salida esperada:
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	archivo.txt

nothing added to commit but untracked files present (use "git add" to track)
```

4. Añade el archivo al staging area:

```bash
git add archivo.txt
```

5. Verifica el estado (debería ser Staged):

```bash
git status
```

Salida esperada:
```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   archivo.txt
```

6. Haz el primer commit:

```bash
git commit -m "agregar archivo.txt"
```

7. Verifica el estado (debería estar limpio):

```bash
git status
```

Salida esperada:
```
On branch main
nothing to commit, working tree clean
```

Ahora el archivo está Unmodified.

8. Modifica el archivo:

```bash
echo "Línea 2" >> archivo.txt
```

9. Verifica el estado (debería ser Modified):

```bash
git status
```

Salida esperada:
```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   archivo.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

10. Añade los cambios al staging:

```bash
git add archivo.txt
```

11. Modifica el archivo de nuevo (antes de commitear):

```bash
echo "Línea 3" >> archivo.txt
```

12. Verifica el estado (el archivo está Staged Y Modified):

```bash
git status
```

Salida esperada:
```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   archivo.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   archivo.txt
```

13. Ver las diferencias:

```bash
# Ver cambios en working directory vs staging
git diff archivo.txt

# Ver cambios en staging vs último commit
git diff --staged archivo.txt
```

**Resultado esperado:**

Deberías entender:
- Cómo un archivo pasa por los cuatro estados
- Que `git status` muestra el estado actual de archivos
- Que un archivo puede estar staged y modified simultáneamente
- La diferencia entre `git diff` y `git diff --staged`

***

## Checkpoint: Parte 1

Antes de continuar, verifica que puedes:

- Instalar y configurar Git en tu sistema operativo
- Explicar qué es un blob, tree, commit y tag
- Describir las tres áreas de Git (working directory, staging area, repository)
- Identificar los cuatro estados de un archivo (untracked, unmodified, modified, staged)
- Usar `git status` para ver el estado actual
- Entender la diferencia entre `git diff` y `git diff --staged`
- Explorar objetos Git internos con `git cat-file`

Si no te sientes cómodo con alguno de estos conceptos, repasa la sección correspondiente antes de continuar.

***

# PARTE 2: OPERACIONES BÁSICAS

## 2.1 Crear tu Primer Repositorio

Hay dos formas de obtener un repositorio Git:

1. Inicializar uno nuevo en un directorio existente
2. Clonar un repositorio existente (lo veremos en la Parte 3)

### Inicializar un Repositorio Nuevo

```bash
# Navega al directorio de tu proyecto
cd mi-proyecto

# Inicializa Git
git init
```

Esto crea un subdirectorio `.git/` que contiene toda la estructura necesaria del repositorio.

### EJERCICIO 4: Crear un Proyecto desde Cero

**Objetivo:** Crear un proyecto nuevo, inicializar Git y hacer tu primer commit.

**Pasos:**

1. Crea un directorio para tu proyecto:

```bash
mkdir calculadora-python
cd calculadora-python
```

2. Inicializa el repositorio:

```bash
git init
```

3. Verifica que se creó el directorio `.git`:

```bash
ls -la
```

Deberías ver un directorio `.git/`

4. Crea un archivo README:

```bash
cat > README.md << 'EOF'
# Calculadora Python

Proyecto de práctica para aprender Git.

## Descripción

Una calculadora simple implementada en Python.

## Características

- Operaciones básicas (suma, resta, multiplicación, división)
- Interfaz de línea de comandos
EOF
```

5. Verifica el estado:

```bash
git status
```

6. Añade el archivo al staging:

```bash
git add README.md
```

7. Verifica el estado de nuevo:

```bash
git status
```

8. Haz tu primer commit:

```bash
git commit -m "docs: agregar README inicial"
```

9. Verifica el historial:

```bash
git log
```

**Resultado esperado:**

Deberías ver un commit en el historial con tu mensaje, autor y fecha.

***

## 2.2 El Ciclo Básico: Add y Commit

El flujo de trabajo básico en Git es:

1. Editar archivos en tu working directory
2. Añadir cambios al staging area con `git add`
3. Crear un commit con `git commit`

### git add: Añadir al Staging Area

```bash
# Añadir un archivo específico
git add archivo.txt

# Añadir múltiples archivos
git add archivo1.txt archivo2.txt

# Añadir todos los archivos modificados
git add .

# Añadir todos los archivos de cierto tipo
git add *.py

# Añadir archivos de un directorio
git add src/
```

### git commit: Crear un Commit

```bash
# Commit con mensaje en línea
git commit -m "mensaje descriptivo"

# Commit abriendo el editor para mensaje largo
git commit

# Commit saltando staging (solo archivos ya rastreados)
git commit -a -m "mensaje"
# o
git commit -am "mensaje"
```

### Mensajes de Commit Efectivos

Un buen mensaje de commit sigue esta estructura:

```
tipo: descripción corta (máximo 50 caracteres)

Cuerpo opcional explicando QUÉ y POR QUÉ (no cómo).
Separado por una línea en blanco.
Envuelve líneas en ~72 caracteres.
```

**Tipos comunes (Conventional Commits):** [dev](https://dev.to/itxshakil/commit-like-a-pro-a-beginners-guide-to-conventional-commits-34c3)

- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `docs`: Cambios en documentación
- `style`: Formato, puntos y comas, etc (no cambia lógica)
- `refactor`: Refactorización de código
- `test`: Añadir o modificar tests
- `chore`: Tareas de mantenimiento, configuración

**Ejemplos buenos:**

```bash
git commit -m "feat: agregar función de suma en calculadora"
git commit -m "fix: corregir división por cero"
git commit -m "docs: actualizar guía de instalación"
git commit -m "refactor: simplificar lógica de validación"
```

**Ejemplos malos:**

```bash
git commit -m "cambios"
git commit -m "fix"
git commit -m "wip"
git commit -m "actualizando cosas"
```

### EJERCICIO 5: Flujo Add-Commit

**Objetivo:** Practicar el ciclo básico de add y commit.

**Contexto:** Continuamos con el proyecto calculadora-python del ejercicio anterior.

**Pasos:**

1. Navega al directorio del proyecto:

```bash
cd calculadora-python
```

2. Crea la estructura básica del proyecto:

```bash
cat > calculadora.py << 'EOF'
class Calculadora:
    """Calculadora básica con operaciones aritméticas"""
    
    def __init__(self):
        self.resultado = 0
    
    def limpiar(self):
        """Reinicia el resultado a cero"""
        self.resultado = 0
        return self.resultado

if __name__ == "__main__":
    calc = Calculadora()
    print("Calculadora inicializada")
    print(f"Resultado inicial: {calc.resultado}")
EOF
```

3. Verifica el estado:

```bash
git status
```

4. Añade y commitea el archivo:

```bash
git add calculadora.py
git commit -m "feat: crear clase Calculadora base"
```

5. Añade la función de suma:

```bash
cat >> calculadora.py << 'EOF'
    
    def sumar(self, a, b):
        """Suma dos números"""
        self.resultado = a + b
        return self.resultado
EOF
```

6. Verifica qué cambió:

```bash
git diff calculadora.py
```

7. Añade y commitea:

```bash
git add calculadora.py
git commit -m "feat: implementar operación de suma"
```

8. Añade la función de resta:

```bash
cat >> calculadora.py << 'EOF'
    
    def restar(self, a, b):
        """Resta dos números"""
        self.resultado = a - b
        return self.resultado
EOF
```

9. Commitea usando el shortcut:

```bash
git commit -am "feat: implementar operación de resta"
```

10. Verifica el historial:

```bash
git log --oneline
```

**Resultado esperado:**

Deberías ver tres commits:
```
abc1234 feat: implementar operación de resta
def5678 feat: implementar operación de suma
ghi9012 feat: crear clase Calculadora base
jkl3456 docs: agregar README inicial
```

***

## 2.3 Visualizar el Historial con git log

`git log` es fundamental para entender el historial de tu proyecto.

### Comandos Básicos

```bash
# Log estándar (verboso)
git log

# Log compacto (una línea por commit)
git log --oneline

# Log con gráfico de branches
git log --oneline --graph

# Log de todos los branches
git log --oneline --graph --all

# Últimos N commits
git log -3

# Log con estadísticas de cambios
git log --stat

# Log con diff completo
git log -p
```

### Filtrar el Historial

```bash
# Commits desde cierta fecha
git log --since="2026-01-01"
git log --since="2 weeks ago"
git log --since="yesterday"

# Commits hasta cierta fecha
git log --until="2026-01-20"

# Commits de cierto autor
git log --author="David"

# Buscar en mensajes de commit
git log --grep="feat"
git log --grep="fix"

# Historial de un archivo específico
git log -- calculadora.py

# Commits que modificaron cierta función
git log -S "def sumar"
```

### Formato Personalizado

```bash
# Formato personalizado
git log --pretty=format:"%h - %an, %ar : %s"

# Componentes del formato:
# %h  = hash abreviado
# %H  = hash completo
# %an = nombre del autor
# %ae = email del autor
# %ad = fecha del autor
# %ar = fecha relativa
# %s  = mensaje
```

### EJERCICIO 6: Explorar el Historial

**Objetivo:** Familiarizarte con las diferentes formas de ver el historial.

**Pasos:**

1. En tu proyecto calculadora-python, ve el log completo:

```bash
git log
```

2. Ve el log en formato compacto:

```bash
git log --oneline
```

3. Ve estadísticas de cada commit:

```bash
git log --stat
```

4. Ve los cambios completos del último commit:

```bash
git log -1 -p
```

5. Busca commits con la palabra "suma":

```bash
git log --grep="suma"
```

6. Ve el historial del archivo calculadora.py:

```bash
git log -- calculadora.py
```

7. Crea un formato personalizado:

```bash
git log --pretty=format:"%h - %an (%ar): %s" --graph
```

**Resultado esperado:**

Deberías poder navegar el historial de diferentes formas y encontrar información específica sobre commits.

***

## 2.4 Ver Cambios con git diff

`git diff` muestra diferencias entre diferentes estados de tu proyecto.

### Tipos de Diff

```bash
# Cambios en working directory (no staged)
git diff

# Cambios en staging area (staged pero no committed)
git diff --staged
# o
git diff --cached

# Cambios entre dos commits
git diff commit1 commit2

# Cambios entre branches
git diff main feature-branch

# Solo nombres de archivos modificados
git diff --name-only

# Estadísticas de cambios
git diff --stat

# Diff de un archivo específico
git diff archivo.txt
```

### Leer un Diff

Ejemplo de salida de `git diff`:

```diff
diff --git a/calculadora.py b/calculadora.py
index abc1234..def5678 100644
--- a/calculadora.py
+++ b/calculadora.py
@@ -8,3 +8,8 @@ class Calculadora:
         """Reinicia el resultado a cero"""
         self.resultado = 0
         return self.resultado
+
+    def sumar(self, a, b):
+        """Suma dos números"""
+        self.resultado = a + b
+        return self.resultado
```

Interpretación:
- `---` líneas del archivo original
- `+++` líneas del archivo nuevo
- `@@` ubicación del cambio
- Líneas con `+` fueron añadidas
- Líneas con `-` fueron eliminadas
- Líneas sin prefijo no cambiaron (contexto)

### EJERCICIO 7: Trabajar con Diferencias

**Objetivo:** Entender cómo usar git diff en diferentes situaciones.

**Pasos:**

1. En calculadora-python, modifica el archivo sin hacer add:

```bash
cat >> calculadora.py << 'EOF'
    
    def multiplicar(self, a, b):
        """Multiplica dos números"""
        self.resultado = a * b
        return self.resultado
EOF
```

2. Ve los cambios en working directory:

```bash
git diff
```

3. Añade los cambios al staging:

```bash
git add calculadora.py
```

4. Intenta ver git diff de nuevo:

```bash
git diff
```

No deberías ver nada porque los cambios ya están staged.

5. Ve los cambios staged:

```bash
git diff --staged
```

6. Modifica el archivo de nuevo:

```bash
echo "" >> calculadora.py
echo "# TODO: agregar validación de entrada" >> calculadora.py
```

7. Ve ambas diferencias:

```bash
# Cambios no staged
git diff

# Cambios staged
git diff --staged
```

8. Commitea solo los cambios staged:

```bash
git commit -m "feat: implementar operación de multiplicación"
```

9. Ve la diferencia entre los últimos dos commits:

```bash
git diff HEAD~1 HEAD
```

10. Ve solo los nombres de archivos que cambiaron:

```bash
git diff HEAD~1 HEAD --name-only
```

**Resultado esperado:**

Deberías entender:
- La diferencia entre `git diff` y `git diff --staged`
- Cómo leer un diff
- Cómo comparar commits específicos
- Que puedes tener cambios staged y unstaged simultáneamente

***
## 2.5 Deshacer Cambios

Una de las habilidades más importantes en Git es saber cómo deshacer cambios. Git ofrece varias formas según el estado de tus archivos.

### Descartar Cambios en Working Directory

Si modificaste un archivo pero no lo has añadido al staging, puedes descartarlo:

```bash
# Descartar cambios en un archivo específico
git restore archivo.txt

# Método antiguo (también funciona)
git checkout -- archivo.txt

# Descartar cambios en todos los archivos
git restore .
```

**Advertencia:** Esto es destructivo. Los cambios se pierden permanentemente.

### Quitar Archivos del Staging Area

Si añadiste un archivo al staging pero quieres quitarlo (sin perder los cambios):

```bash
# Quitar archivo específico del staging
git restore --staged archivo.txt

# Método antiguo (también funciona)
git reset HEAD archivo.txt

# Quitar todos los archivos del staging
git restore --staged .
```

Los cambios permanecen en el working directory, solo se quitan del staging.

### Modificar el Último Commit

Si olvidaste incluir algo en el último commit o quieres cambiar el mensaje:

```bash
# Cambiar solo el mensaje del último commit
git commit --amend -m "nuevo mensaje"

# Añadir archivos al último commit
git add archivo_olvidado.txt
git commit --amend --no-edit

# Cambiar mensaje Y archivos (abre editor)
git add archivo.txt
git commit --amend
```

**Advertencia:** Solo usa `--amend` en commits que no hayas pusheado. Si ya están en el repositorio remoto, modificarlos causará problemas.

### Deshacer Commits

```bash
# Deshacer último commit pero mantener cambios en staging
git reset --soft HEAD~1

# Deshacer último commit, cambios vuelven a working directory
git reset HEAD~1
# o
git reset --mixed HEAD~1

# Deshacer último commit Y descartar todos los cambios (peligroso)
git reset --hard HEAD~1

# Deshacer N commits
git reset --soft HEAD~3
```

**Tipos de reset:**

- `--soft`: Mueve HEAD pero mantiene staging y working directory
- `--mixed` (default): Mueve HEAD, limpia staging, mantiene working directory
- `--hard`: Mueve HEAD, limpia staging Y working directory (destructivo)

### Visualización de Reset

```
Antes:
HEAD -> C3 -> C2 -> C1
Staging: cambios listos
Working: cambios sin añadir

git reset --soft HEAD~1:
HEAD -> C2 -> C1
Staging: C3 + cambios anteriores
Working: cambios sin añadir

git reset --mixed HEAD~1:
HEAD -> C2 -> C1
Staging: vacío
Working: C3 + todos los cambios

git reset --hard HEAD~1:
HEAD -> C2 -> C1
Staging: vacío
Working: vacío (todo se pierde)
```

### EJERCICIO 8: Deshacer Cambios

**Objetivo:** Practicar diferentes formas de deshacer cambios.

**Parte A: Descartar cambios en working directory**

1. Modifica calculadora.py:

```bash
echo "# Cambio temporal que no queremos" >> calculadora.py
```

2. Verifica que cambió:

```bash
git diff
```

3. Descarta el cambio:

```bash
git restore calculadora.py
```

4. Verifica que el cambio desapareció:

```bash
git diff
```

**Parte B: Quitar del staging**

1. Crea un archivo temporal:

```bash
echo "archivo temporal" > temp.txt
```

2. Añádelo al staging:

```bash
git add temp.txt
```

3. Verifica el estado:

```bash
git status
```

4. Quítalo del staging:

```bash
git restore --staged temp.txt
```

5. Verifica que sigue en working directory:

```bash
git status
ls
```

6. Elimina el archivo:

```bash
rm temp.txt
```

**Parte C: Modificar el último commit**

1. Añade la función de división:

```bash
cat >> calculadora.py << 'EOF'
    
    def dividir(self, a, b):
        """Divide dos números"""
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        self.resultado = a / b
        return self.resultado
EOF
```

2. Commitea:

```bash
git add calculadora.py
git commit -m "feat: implementar división"
```

3. Te das cuenta que olvidaste actualizar el README. Añade información:

```bash
cat >> README.md << 'EOF'

## Uso

```python
from calculadora import Calculadora

calc = Calculadora()
print(calc.sumar(5, 3))      # 8
print(calc.restar(10, 4))    # 6
print(calc.multiplicar(3, 4)) # 12
print(calc.dividir(10, 2))   # 5.0
```
EOF
```

4. Añade el README al último commit:

```bash
git add README.md
git commit --amend --no-edit
```

5. Verifica que el commit incluye ambos archivos:

```bash
git show --stat
```

**Parte D: Deshacer commits**

1. Crea dos commits rápidos:

```bash
echo "# Comentario 1" >> calculadora.py
git commit -am "comentario 1"

echo "# Comentario 2" >> calculadora.py
git commit -am "comentario 2"
```

2. Ve el historial:

```bash
git log --oneline -5
```

3. Deshaz el último commit con soft reset:

```bash
git reset --soft HEAD~1
```

4. Verifica el estado:

```bash
git status
```

Los cambios del commit deberían estar en staging.

5. Ve el historial:

```bash
git log --oneline -5
```

El último commit debería haber desaparecido.

6. Commitea de nuevo con mejor mensaje:

```bash
git commit -m "docs: agregar comentarios explicativos"
```

7. Crea otro commit de prueba:

```bash
echo "# Comentario temporal" >> calculadora.py
git commit -am "commit temporal"
```

8. Deshazlo con reset mixed:

```bash
git reset HEAD~1
```

9. Verifica que los cambios están en working directory:

```bash
git status
git diff
```

10. Descarta los cambios:

```bash
git restore calculadora.py
```

**Resultado esperado:**

Deberías poder:
- Descartar cambios en working directory con `git restore`
- Quitar archivos del staging con `git restore --staged`
- Modificar el último commit con `git commit --amend`
- Deshacer commits con `git reset` en sus diferentes modos
- Entender la diferencia entre `--soft`, `--mixed` y `--hard`

***

## 2.6 Trabajar con .gitignore

El archivo `.gitignore` especifica qué archivos Git debe ignorar intencionalmente.

### Por Qué Usar .gitignore

Hay archivos que no deberías versionar:

- Archivos generados (compilados, builds)
- Dependencias (node_modules/, venv/)
- Archivos del sistema operativo (.DS_Store, Thumbs.db)
- Archivos de configuración local (.env, config.local)
- Archivos temporales (*.log, *.tmp)
- Credenciales y secretos

### Sintaxis de .gitignore

```bash
# Ignorar archivo específico
secreto.txt

# Ignorar todos los archivos de cierto tipo
*.log
*.tmp

# Ignorar directorio completo
node_modules/
__pycache__/

# Ignorar archivos en directorio específico (no subdirectorios)
/logs/*.log

# Ignorar archivos en cualquier directorio
**/temp/

# NO ignorar archivo específico (excepción)
!importante.log

# Ignorar todos los .txt excepto README.txt
*.txt
!README.txt
```

### Crear .gitignore para Python

```bash
cat > .gitignore << 'EOF'
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
ENV/
env/
.venv/

# IDEs
.vscode/
.idea/
*.sublime-project
*.sublime-workspace
.spyproject/

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Jupyter Notebook
.ipynb_checkpoints/

# Environment variables
.env
.env.local

# OS
.DS_Store
Thumbs.db
*.swp
*.swo
*~

# Project specific
logs/
temp/
cache/
EOF
```

### Problema Común: Archivo Ya Trackeado

Si un archivo ya está en Git y luego lo añades a `.gitignore`, Git seguirá rastreándolo. Necesitas quitarlo del índice:

```bash
# Quitar del índice pero mantener en disco
git rm --cached archivo.txt

# Quitar directorio del índice
git rm -r --cached directorio/

# Commitear el cambio
git commit -m "chore: dejar de trackear archivo.txt"
```

### .gitignore Global

Para ignorar archivos en TODOS tus proyectos:

```bash
# Crear gitignore global
touch ~/.gitignore_global

# Configurar Git para usarlo
git config --global core.excludesfile ~/.gitignore_global
```

Contenido recomendado para `~/.gitignore_global`:

```bash
# OS files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Editor files
*.swp
*.swo
*~
.vscode/
.idea/

# Python
__pycache__/
*.pyc
.ipynb_checkpoints/
```

### EJERCICIO 9: Configurar .gitignore

**Objetivo:** Crear un .gitignore efectivo y manejar archivos ignorados.

**Pasos:**

1. En tu proyecto calculadora-python, crea el .gitignore:

```bash
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*.so
.Python

# Virtual environments
venv/
env/
.venv/

# IDEs
.vscode/
.idea/

# Testing
.pytest_cache/
.coverage

# Environment
.env

# Logs
*.log

# OS
.DS_Store
Thumbs.db
EOF
```

2. Commitea el .gitignore:

```bash
git add .gitignore
git commit -m "chore: agregar .gitignore para Python"
```

3. Crea algunos archivos que deberían ser ignorados:

```bash
mkdir __pycache__
touch __pycache__/calculadora.pyc
touch debug.log
mkdir .vscode
touch .vscode/settings.json
```

4. Verifica que Git los ignora:

```bash
git status
```

No deberías ver ninguno de esos archivos.

5. Crea un archivo .env con datos sensibles:

```bash
cat > .env << 'EOF'
API_KEY=mi_clave_secreta_12345
DATABASE_URL=postgresql://usuario:password@localhost/db
EOF
```

6. Verifica que está ignorado:

```bash
git status
```

7. Accidentalmente añade el archivo .env:

```bash
git add .env
```

8. Verifica que está staged:

```bash
git status
```

9. Quítalo del staging:

```bash
git restore --staged .env
```

10. Simula que ya habías commiteado el .env antes de tener .gitignore:

```bash
# Temporal: quita .env del .gitignore
sed -i.bak '/^\.env$/d' .gitignore

# Añade y commitea .env
git add .env
git commit -m "error: commitear .env (no hacer esto nunca)"

# Restaura .gitignore
mv .gitignore.bak .gitignore
git add .gitignore
git commit -m "fix: agregar .env a .gitignore"

# Verifica que Git sigue rastreando .env
echo "OTRA_KEY=valor" >> .env
git status
```

Verás que .env sigue siendo rastreado.

11. Quita .env del índice:

```bash
git rm --cached .env
git commit -m "chore: dejar de trackear .env"
```

12. Verifica que ahora está ignorado:

```bash
echo "NUEVA_KEY=test" >> .env
git status
```

No deberías ver .env en el status.

**Resultado esperado:**

Deberías entender:
- Cómo crear un .gitignore efectivo
- La sintaxis de patrones en .gitignore
- Que .gitignore no afecta archivos ya rastreados
- Cómo quitar archivos del tracking con `git rm --cached`
- La diferencia entre .gitignore local y global

***

## 2.7 Ver Contenido de Commits: git show

`git show` muestra información detallada sobre objetos Git (commits, tags, trees, blobs).

### Uso Básico

```bash
# Mostrar el último commit completo
git show

# Mostrar commit específico
git show abc1234

# Mostrar solo el diff sin metadata
git show abc1234 --no-patch

# Mostrar estadísticas en lugar de diff completo
git show abc1234 --stat
```

### Referencias Relativas

```bash
# Commit anterior al HEAD
git show HEAD^
git show HEAD~1

# Dos commits atrás
git show HEAD~2

# Tercer commit en el branch feature
git show feature~3

# Primer padre de un merge commit
git show HEAD^1

# Segundo padre de un merge commit
git show HEAD^2
```

### Ver Archivos Específicos

```bash
# Contenido de un archivo en cierto commit
git show abc1234:calculadora.py

# Contenido de un archivo en HEAD
git show HEAD:README.md

# Contenido de un archivo dos commits atrás
git show HEAD~2:calculadora.py
```

### EJERCICIO 10: Explorar Commits

**Objetivo:** Usar git show para investigar el historial.

**Pasos:**

1. Ve el último commit completo:

```bash
git show
```

2. Ve solo las estadísticas del último commit:

```bash
git show --stat
```

3. Ve el penúltimo commit:

```bash
git show HEAD~1
```

4. Ve los últimos 3 commits en formato compacto:

```bash
git log -3 --oneline
```

Copia el hash del commit más antiguo de esos 3.

5. Muestra ese commit específico:

```bash
git show <hash-copiado>
```

6. Ve el contenido de calculadora.py en ese commit:

```bash
git show <hash-copiado>:calculadora.py
```

7. Compara con el contenido actual:

```bash
cat calculadora.py
```

8. Ve todos los commits que modificaron calculadora.py:

```bash
git log --oneline -- calculadora.py
```

9. Muestra el primer commit que modificó calculadora.py:

```bash
# Toma el hash del último en la lista (el más antiguo)
git show <hash-primer-commit>:calculadora.py
```

**Resultado esperado:**

Deberías poder:
- Ver commits completos con `git show`
- Navegar commits con referencias relativas (HEAD~1, HEAD~2)
- Ver contenido de archivos en commits específicos
- Comparar versiones de archivos entre commits

***

## Checkpoint: Parte 2

Antes de continuar, verifica que puedes:

- Inicializar un repositorio con `git init`
- Añadir archivos al staging con `git add`
- Crear commits con `git commit`
- Escribir mensajes de commit descriptivos usando Conventional Commits
- Ver el historial con `git log` en diferentes formatos
- Ver diferencias con `git diff` y `git diff --staged`
- Descartar cambios en working directory con `git restore`
- Quitar archivos del staging con `git restore --staged`
- Modificar el último commit con `git commit --amend`
- Deshacer commits con `git reset` (soft, mixed, hard)
- Crear y usar archivos .gitignore
- Quitar archivos del tracking con `git rm --cached`
- Explorar commits con `git show`

Si no dominas alguno de estos conceptos, repasa los ejercicios correspondientes.

***

# PARTE 3: BRANCHES Y MERGING

## 3.1 Entendiendo Branches

### Qué es un Branch

Un branch en Git es simplemente un puntero ligero y móvil a un commit. El branch por defecto se llama `main` (anteriormente `master`).

### Cómo Funciona HEAD

`HEAD` es un puntero especial que indica en qué branch estás actualmente.

```
Ejemplo:

main -> C3
         ↑
        HEAD

Esto significa: estás en el branch main, que apunta al commit C3
```

### Visualización de Branches

```
Un repositorio con un solo branch:

C1 <- C2 <- C3 <- C4
                  ↑
                 main
                  ↑
                 HEAD

Repositorio con múltiples branches:

C1 <- C2 <- C3 <- C4
            ↑     ↑
            |    main
            |     ↑
            |    HEAD
            |
            C5 <- C6
                  ↑
                feature
```

### Crear Branches

```bash
# Ver branches actuales
git branch

# Crear nuevo branch (sin cambiar a él)
git branch nombre-branch

# Crear y cambiar al nuevo branch
git checkout -b nombre-branch

# Método nuevo (Git 2.23+)
git switch -c nombre-branch

# Ver todos los branches con último commit
git branch -v
```

### Cambiar de Branch

```bash
# Método tradicional
git checkout nombre-branch

# Método nuevo (Git 2.23+)
git switch nombre-branch

# Cambiar al branch anterior
git switch -
```

### Eliminar Branches

```bash
# Eliminar branch (solo si está merged)
git branch -d nombre-branch

# Forzar eliminación (aunque no esté merged)
git branch -D nombre-branch
```

### EJERCICIO 11: Crear y Navegar Branches

**Objetivo:** Crear múltiples branches y entender cómo funcionan.

**Pasos:**

1. Verifica en qué branch estás:

```bash
git branch
```

Deberías estar en `main`.

2. Crea un branch para agregar tests:

```bash
git branch feature-tests
```

3. Lista los branches:

```bash
git branch
```

Deberías ver:
```
  feature-tests
* main
```

El asterisco indica tu branch actual.

4. Cambia al nuevo branch:

```bash
git switch feature-tests
```

5. Verifica el cambio:

```bash
git branch
```

Ahora el asterisco debería estar en `feature-tests`.

6. Crea un archivo de tests:

```bash
cat > test_calculadora.py << 'EOF'
import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculadora()
    
    def test_suma(self):
        resultado = self.calc.sumar(5, 3)
        self.assertEqual(resultado, 8)
    
    def test_resta(self):
        resultado = self.calc.restar(10, 4)
        self.assertEqual(resultado, 6)
    
    def test_multiplicacion(self):
        resultado = self.calc.multiplicar(3, 4)
        self.assertEqual(resultado, 12)
    
    def test_division(self):
        resultado = self.calc.dividir(10, 2)
        self.assertEqual(resultado, 5.0)
    
    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()
EOF
```

7. Commitea los tests:

```bash
git add test_calculadora.py
git commit -m "test: agregar tests unitarios para calculadora"
```

8. Ve el historial:

```bash
git log --oneline --graph --all
```

Deberías ver algo como:
```
* abc1234 (HEAD -> feature-tests) test: agregar tests unitarios para calculadora
* def5678 (main) chore: dejar de trackear .env
...
```

9. Cambia de vuelta a main:

```bash
git switch main
```

10. Verifica que el archivo de tests no existe en main:

```bash
ls test_calculadora.py
```

Debería dar error: "No such file or directory"

11. Vuelve al branch de tests:

```bash
git switch feature-tests
```

12. Verifica que el archivo vuelve a aparecer:

```bash
ls test_calculadora.py
```

13. Crea otro branch desde main para una nueva feature:

```bash
git switch main
git switch -c feature-potencia
```

14. Implementa la función de potencia:

```bash
cat >> calculadora.py << 'EOF'
    
    def potencia(self, base, exponente):
        """Calcula base elevada a exponente"""
        self.resultado = base ** exponente
        return self.resultado
EOF
```

15. Commitea:

```bash
git add calculadora.py
git commit -m "feat: implementar operación de potencia"
```

16. Ve el historial gráfico:

```bash
git log --oneline --graph --all
```

Deberías ver algo como:
```
* xyz7890 (HEAD -> feature-potencia) feat: implementar operación de potencia
| * abc1234 (feature-tests) test: agregar tests unitarios para calculadora
|/
* def5678 (main) chore: dejar de trackear .env
...
```

17. Lista todos tus branches:

```bash
git branch -v
```

**Resultado esperado:**

Deberías tener tres branches:
- main
- feature-tests (con archivo de tests)
- feature-potencia (con función de potencia)

Y entender que:
- Los branches son punteros a commits
- Cambiar de branch cambia los archivos en tu working directory
- Los commits en un branch no afectan otros branches
- Puedes tener múltiples branches divergiendo desde el mismo punto

***

## 3.2 Merging: Integrar Cambios

Merge es el proceso de integrar cambios de un branch a otro.

### Tipos de Merge

#### Fast-Forward Merge

Ocurre cuando el branch destino no ha avanzado desde que se creó el branch fuente.

```
Antes del merge:

main:    C1 <- C2
                ↑
               main
                
feature: C1 <- C2 <- C3 <- C4
                           ↑
                         feature

Después de git merge feature (desde main):

main:    C1 <- C2 <- C3 <- C4
                           ↑
                          main
                         feature
```

Git simplemente mueve el puntero de `main` hacia adelante.

#### Three-Way Merge

Ocurre cuando ambos branches han avanzado independientemente.

```
Antes del merge:

        C3 <- C4
       /        (feature)
C1 <- C2 <- C5
             ↑
            main

Después de git merge feature (desde main):

        C3 <- C4
       /         \
C1 <- C2 <- C5 <- M
                  ↑
                 main

M es un "merge commit" con dos padres
```

### Comandos de Merge

```bash
# Mergear branch-origen en el branch actual
git merge branch-origen

# Merge forzando creación de merge commit (no fast-forward)
git merge --no-ff branch-origen

# Merge con mensaje personalizado
git merge branch-origen -m "Merge feature X"

# Ver qué branches están merged en el actual
git branch --merged

# Ver qué branches NO están merged
git branch --no-merged
```

### EJERCICIO 12: Fast-Forward Merge

**Objetivo:** Realizar un merge fast-forward.

**Pasos:**

1. Asegúrate de estar en main:

```bash
git switch main
```

2. Verifica el estado antes del merge:

```bash
git log --oneline --graph --all
```

3. Mergea el branch feature-tests:

```bash
git merge feature-tests
```

Deberías ver un mensaje indicando "Fast-forward".

4. Verifica el historial:

```bash
git log --oneline --graph --all
```

Ahora `main` apunta al mismo commit que `feature-tests`.

5. Verifica que el archivo de tests existe en main:

```bash
ls test_calculadora.py
```

6. Opcionalmente, elimina el branch feature-tests (ya no lo necesitas):

```bash
git branch -d feature-tests
```

**Resultado esperado:**

- El branch main ahora incluye el archivo test_calculadora.py
- No se creó un merge commit nuevo (fue fast-forward)
- El historial es lineal

***

### EJERCICIO 13: Three-Way Merge

**Objetivo:** Realizar un merge de tres vías y crear un merge commit.

**Pasos:**

1. Asegúrate de estar en main:

```bash
git switch main
```

2. Crea un cambio en main (simula que el equipo siguió trabajando):

```bash
cat >> README.md << 'EOF'

## Testing

Ejecuta los tests con:

```bash
python -m unittest test_calculadora.py
```
EOF
```

3. Commitea:

```bash
git add README.md
git commit -m "docs: agregar instrucciones para ejecutar tests"
```

4. Ve el historial:

```bash
git log --oneline --graph --all
```

Deberías ver que `main` y `feature-potencia` han divergido.

5. Mergea feature-potencia:

```bash
git merge feature-potencia
```

Git abrirá tu editor para el mensaje del merge commit. Guarda y cierra.

6. Ve el historial:

```bash
git log --oneline --graph --all
```

Deberías ver un merge commit con dos padres.

7. Verifica que tienes ambos cambios:

```bash
# La función potencia de feature-potencia
grep "def potencia" calculadora.py

# Las instrucciones de testing de main
grep "Testing" README.md
```

8. Elimina el branch feature-potencia:

```bash
git branch -d feature-potencia
```

**Resultado esperado:**

- Se creó un merge commit con dos padres
- main ahora contiene tanto la función potencia como las instrucciones de testing
- El historial muestra la divergencia y convergencia de los branches

***

## 3.3 Conflictos de Merge

Un conflicto ocurre cuando Git no puede fusionar automáticamente cambios porque ambos branches modificaron las mismas líneas de un archivo.

### Cómo Se Ve un Conflicto

```python
<<<<<<< HEAD
def sumar(self, a, b):
    """Suma dos números con validación"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser números")
    return a + b
=======
def sumar(self, a, b):
    """Suma dos números"""
    result = a + b
    print(f"Resultado: {result}")
    return result
>>>>>>> feature-branch
```

Secciones:
- `<<<<<<< HEAD`: Inicio del contenido en tu branch actual
- `=======`: Separador
- `>>>>>>> feature-branch`: Fin del contenido del branch que estás mergeando

### Resolver Conflictos

```bash
# 1. Intentar merge
git merge feature-branch

# Git indica conflictos
# CONFLICT (content): Merge conflict in archivo.py

# 2. Ver archivos con conflictos
git status

# 3. Abrir archivo y resolver manualmente

# 4. Marcar como resuelto
git add archivo.py

# 5. Completar el merge
git commit
```

### Abortar un Merge

Si prefieres cancelar el merge:

```bash
git merge --abort
```

Esto regresa tu repositorio al estado antes del merge.

### EJERCICIO 14: Resolver Conflictos

**Objetivo:** Crear y resolver un conflicto de merge intencionalmente.

**Pasos:**

1. Crea un branch para agregar validación:

```bash
git switch -c feature-validacion
```

2. Modifica la función sumar para agregar validación:

```bash
# Edita calculadora.py y reemplaza la función sumar
```

Usa tu editor para cambiar:

```python
def sumar(self, a, b):
    """Suma dos números"""
    self.resultado = a + b
    return self.resultado
```

Por:

```python
def sumar(self, a, b):
    """Suma dos números con validación de tipos"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser números")
    self.resultado = a + b
    return self.resultado
```

3. Commitea:

```bash
git add calculadora.py
git commit -m "feat: agregar validación de tipos en suma"
```

4. Vuelve a main:

```bash
git switch main
```

5. Modifica la misma función pero de forma diferente:

Usa tu editor para cambiar la función sumar por:

```python
def sumar(self, a, b):
    """Suma dos números con logging"""
    self.resultado = a + b
    print(f"Suma: {a} + {b} = {self.resultado}")
    return self.resultado
```

6. Commitea:

```bash
git add calculadora.py
git commit -m "feat: agregar logging en suma"
```

7. Intenta mergear feature-validacion:

```bash
git merge feature-validacion
```

Deberías ver:
```
Auto-merging calculadora.py
CONFLICT (content): Merge conflict in calculadora.py
Automatic merge failed; fix conflicts and then commit the result.
```

8. Ve el estado:

```bash
git status
```

9. Abre calculadora.py y busca la sección con conflicto:

```python
<<<<<<< HEAD
    def sumar(self, a, b):
        """Suma dos números con logging"""
        self.resultado = a + b
        print(f"Suma: {a} + {b} = {self.resultado}")
        return self.resultado
=======
    def sumar(self, a, b):
        """Suma dos números con validación de tipos"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Los argumentos deben ser números")
        self.resultado = a + b
        return self.resultado
>>>>>>> feature-validacion
```

10. Resuelve el conflicto combinando ambos cambios:

Reemplaza todo el bloque del conflicto (desde `<<<<<<<` hasta `>>>>>>>`) por:

```python
    def sumar(self, a, b):
        """Suma dos números con validación y logging"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Los argumentos deben ser números")
        self.resultado = a + b
        print(f"Suma: {a} + {b} = {self.resultado}")
        return self.resultado
```

11. Marca el conflicto como resuelto:

```bash
git add calculadora.py
```

12. Verifica el estado:

```bash
git status
```

Debería decir "All conflicts fixed but you are still merging."

13. Completa el merge:

```bash
git commit
```

Git abrirá el editor con un mensaje de merge. Guarda y cierra.

14. Ve el historial:

```bash
git log --oneline --graph --all -10
```

15. Verifica que la función tiene ambas características:

```bash
grep -A 8 "def sumar" calculadora.py
```

16. Elimina el branch:

```bash
git branch -d feature-validacion
```

**Resultado esperado:**

- Creaste un conflicto intencionalmente
- Resolviste el conflicto manualmente
- Completaste el merge exitosamente
- La función final combina ambos cambios

***
## 3.4 Estrategias de Merge Avanzadas

### Merge con Squash

Combina todos los commits de un branch en un solo commit antes de mergear.

```bash
# Mergear con squash
git merge --squash feature-branch

# Esto NO crea el commit automáticamente
# Debes commitearlo manualmente
git commit -m "feat: agregar feature X completa"
```

**Cuándo usar:**
- Features desarrolladas con muchos commits pequeños
- Quieres mantener el historial de main limpio
- No necesitas preservar el historial detallado del branch

**Visualización:**

```
Antes:
main:    C1 <- C2
feature: C1 <- C2 <- C3 <- C4 <- C5

Después de merge --squash:
main:    C1 <- C2 <- C6
                     (C6 contiene los cambios de C3+C4+C5)
```

### Merge con --no-ff

Siempre crea un merge commit, incluso si es posible fast-forward.

```bash
git merge --no-ff feature-branch
```

**Cuándo usar:**
- Quieres preservar información de que existió un branch
- Políticas de equipo que requieren merge commits
- Facilita revertir una feature completa

**Visualización:**

```
Con fast-forward (default):
C1 <- C2 <- C3 <- C4
                  ↑
                 main

Con --no-ff:
      C3 <- C4
     /         \
C1 <- C2 -------- M
                  ↑
                 main
```

### EJERCICIO 15: Merge con Squash

**Objetivo:** Usar merge con squash para mantener un historial limpio.

**Pasos:**

1. Crea un branch para una feature con múltiples commits pequeños:

```bash
git switch -c feature-raiz-cuadrada
```

2. Implementa la función en varios pasos (simulando desarrollo iterativo):

```bash
# Paso 1: Función básica
cat >> calculadora.py << 'EOF'
    
    def raiz_cuadrada(self, n):
        """Calcula la raíz cuadrada"""
        self.resultado = n ** 0.5
        return self.resultado
EOF

git add calculadora.py
git commit -m "wip: agregar función raiz_cuadrada básica"
```

3. Añade validación:

```bash
# Edita la función para agregar validación
# Reemplaza la función con tu editor por:
cat > temp_raiz.py << 'EOF'
    
    def raiz_cuadrada(self, n):
        """Calcula la raíz cuadrada"""
        if n < 0:
            raise ValueError("No se puede calcular raíz cuadrada de número negativo")
        self.resultado = n ** 0.5
        return self.resultado
EOF

# Usa tu editor para actualizar calculadora.py con el contenido de temp_raiz.py
# Por simplicidad, reemplaza manualmente la función

git add calculadora.py
git commit -m "wip: agregar validación para números negativos"
```

4. Mejora la documentación:

```bash
# Edita con tu editor para mejorar el docstring
# Cambia el docstring a:
# """Calcula la raíz cuadrada de un número no negativo"""

git add calculadora.py
git commit -m "docs: mejorar docstring de raiz_cuadrada"
```

5. Optimiza la implementación:

```bash
# Edita con tu editor para usar import math
# Cambia la implementación para usar math.sqrt

git add calculadora.py
git commit -m "refactor: usar math.sqrt para mejor precisión"
```

6. Ve el historial del branch:

```bash
git log --oneline main..feature-raiz-cuadrada
```

Deberías ver 4 commits pequeños.

7. Vuelve a main:

```bash
git switch main
```

8. Mergea con squash:

```bash
git merge --squash feature-raiz-cuadrada
```

9. Ve el estado:

```bash
git status
```

Los cambios están staged pero no commiteados.

10. Crea un solo commit con todos los cambios:

```bash
git commit -m "feat: implementar cálculo de raíz cuadrada"
```

11. Ve el historial:

```bash
git log --oneline -5
```

Deberías ver un solo commit para la feature completa, no los 4 commits intermedios.

12. Elimina el branch:

```bash
git branch -D feature-raiz-cuadrada
```

Nota: Usamos `-D` (mayúscula) porque Git piensa que el branch no está merged (técnicamente no lo está, se hizo squash).

**Resultado esperado:**

- El historial de main muestra un solo commit limpio
- Los commits intermedios del desarrollo no están en main
- La funcionalidad completa está implementada

***

## 3.5 Recuperación de Emergencia

### Recuperar Branch Eliminado

Si eliminaste un branch accidentalmente:

```bash
# Ver el log de referencia (reflog)
git reflog

# Busca el commit donde estaba el branch
# Ejemplo de salida:
# abc1234 HEAD@{0}: checkout: moving from feature to main
# def5678 HEAD@{1}: commit: último commit del branch

# Recrear el branch
git branch branch-recuperado def5678
```

### Recuperar Commit Perdido

```bash
# Ver todos los commits, incluso los "perdidos"
git reflog

# Recuperar commit específico
git cherry-pick abc1234

# O crear branch desde ese commit
git branch commit-recuperado abc1234
```

### EJERCICIO 16: Recuperación con Reflog

**Objetivo:** Practicar recuperación de commits "perdidos".

**Pasos:**

1. Crea un branch temporal con algunos commits:

```bash
git switch -c experimento-temporal
```

2. Haz algunos cambios:

```bash
echo "# Experimento" >> calculadora.py
git commit -am "experimento 1"

echo "# Más experimento" >> calculadora.py
git commit -am "experimento 2"
```

3. Anota el hash del último commit:

```bash
git log --oneline -1
```

Copia ese hash (ejemplo: abc1234).

4. Vuelve a main:

```bash
git switch main
```

5. Elimina el branch forzosamente:

```bash
git branch -D experimento-temporal
```

6. Intenta acceder al commit (debería fallar):

```bash
git show abc1234
```

En realidad debería funcionar porque Git mantiene los objetos por un tiempo.

7. Ve el reflog:

```bash
git reflog
```

Deberías ver el historial de movimientos de HEAD, incluyendo los commits del branch eliminado.

8. Recupera el branch:

```bash
git branch experimento-recuperado abc1234
```

9. Verifica que se recuperó:

```bash
git switch experimento-recuperado
git log --oneline -3
```

10. Limpia:

```bash
git switch main
git branch -D experimento-recuperado
```

**Resultado esperado:**

- Entiendes que Git raramente pierde datos
- Puedes usar reflog para encontrar commits "perdidos"
- Puedes recuperar branches eliminados accidentalmente

***

## Checkpoint: Parte 3

Antes de continuar, verifica que puedes:

- Crear branches con `git branch` o `git switch -c`
- Cambiar entre branches con `git switch`
- Entender la diferencia entre fast-forward y three-way merge
- Mergear branches con `git merge`
- Identificar y resolver conflictos de merge
- Usar `git merge --squash` para combinar múltiples commits
- Usar `git merge --no-ff` para crear merge commits explícitos
- Recuperar branches eliminados con `git reflog`
- Ver qué branches están merged con `git branch --merged`
- Eliminar branches con `git branch -d`

Si no dominas estos conceptos, repasa los ejercicios correspondientes.

***

# PARTE 4: REBASE Y REESCRIBIR HISTORIAL

## 4.1 Entendiendo Rebase

Rebase es una alternativa al merge para integrar cambios. En lugar de crear un merge commit, rebase reaplica tus commits encima de otro branch.

### Merge vs Rebase

**Con Merge:**

```
      C3 <- C4
     /         \
C1 <- C2 <- C5 <- M
                  ↑
                 main

Historial preserva la divergencia
```

**Con Rebase:**

```
C1 <- C2 <- C5 <- C3' <- C4'
                        ↑
                       main

Historial lineal (C3' y C4' son nuevos commits)
```

### Cuándo Usar Cada Uno

**Usa Merge cuando:**
- Estás integrando cambios de branches públicos
- Quieres preservar el historial exacto
- Trabajas en features compartidas por múltiples personas
- Quieres poder revertir una feature completa fácilmente

**Usa Rebase cuando:**
- Estás actualizando tu branch personal con cambios de main
- Quieres un historial lineal y limpio
- Trabajas solo en el branch
- No has pusheado los commits todavía

### Regla de Oro del Rebase

**NUNCA hagas rebase de commits que ya pusheaste a un repositorio compartido**

Esto reescribe el historial y causará problemas a todos los colaboradores.

### Rebase Básico

```bash
# Desde tu feature branch
git rebase main

# Proceso:
# 1. Git "guarda" tus commits temporalmente
# 2. Mueve tu branch al tip de main
# 3. Reaplica tus commits uno por uno
```

### EJERCICIO 17: Rebase Simple

**Objetivo:** Usar rebase para mantener un historial lineal.

**Pasos:**

1. Crea un branch para nueva feature:

```bash
git switch -c feature-modulo
```

2. Implementa función módulo:

```bash
cat >> calculadora.py << 'EOF'
    
    def modulo(self, a, b):
        """Calcula el módulo (resto) de la división"""
        if b == 0:
            raise ValueError("No se puede calcular módulo con divisor cero")
        self.resultado = a % b
        return self.resultado
EOF

git add calculadora.py
git commit -m "feat: implementar operación módulo"
```

3. Simula que alguien más actualizó main mientras trabajabas:

```bash
git switch main

cat >> README.md << 'EOF'

## Operaciones Disponibles

- Suma
- Resta
- Multiplicación
- División
- Potencia
- Raíz cuadrada
EOF

git add README.md
git commit -m "docs: listar operaciones disponibles"
```

4. Ve el historial gráfico:

```bash
git log --oneline --graph --all -10
```

Deberías ver que main y feature-modulo han divergido.

5. Vuelve a tu feature branch:

```bash
git switch feature-modulo
```

6. Haz rebase sobre main:

```bash
git rebase main
```

Si no hay conflictos, debería completarse automáticamente.

7. Ve el historial ahora:

```bash
git log --oneline --graph --all -10
```

Ahora tu commit está aplicado encima de main, creando un historial lineal.

8. Mergea a main (será fast-forward):

```bash
git switch main
git merge feature-modulo
```

9. Ve el historial final:

```bash
git log --oneline --graph -10
```

Completamente lineal.

10. Limpia:

```bash
git branch -d feature-modulo
```

**Resultado esperado:**

- Entiendes cómo rebase mueve tus commits
- El historial queda lineal sin merge commits
- El merge final fue fast-forward porque rebaseaste primero

***

## 4.2 Resolver Conflictos Durante Rebase

Los conflictos durante rebase se resuelven commit por commit.

### Proceso de Resolución

```bash
# 1. Iniciar rebase
git rebase main

# Si hay conflictos:
# CONFLICT (content): Merge conflict in archivo.py
# error: could not apply abc1234... mensaje del commit

# 2. Ver qué está en conflicto
git status

# 3. Resolver conflictos en el archivo

# 4. Marcar como resuelto
git add archivo.py

# 5. Continuar el rebase
git rebase --continue

# Si quieres abortar:
git rebase --abort

# Si quieres saltear un commit:
git rebase --skip
```

### EJERCICIO 18: Resolver Conflictos en Rebase

**Objetivo:** Practicar resolución de conflictos durante rebase.

**Pasos:**

1. Crea un branch para mejorar validación:

```bash
git switch -c feature-validacion-mejorada
```

2. Modifica la función dividir para mejor manejo de errores:

Edita con tu editor y reemplaza la función `dividir` por:

```python
    def dividir(self, a, b):
        """Divide dos números con validación mejorada"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Los argumentos deben ser números")
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        self.resultado = a / b
        return self.resultado
```

3. Commitea:

```bash
git add calculadora.py
git commit -m "feat: mejorar validación en división"
```

4. Simula cambios en main:

```bash
git switch main
```

Edita la función dividir pero de forma diferente:

```python
    def dividir(self, a, b):
        """Divide dos números con logging"""
        if b == 0:
            raise ValueError("División por cero no permitida")
        self.resultado = a / b
        print(f"División: {a} / {b} = {self.resultado}")
        return self.resultado
```

5. Commitea:

```bash
git add calculadora.py
git commit -m "feat: agregar logging en división"
```

6. Vuelve a tu feature branch:

```bash
git switch feature-validacion-mejorada
```

7. Intenta rebase:

```bash
git rebase main
```

Deberías ver un conflicto.

8. Ve el estado:

```bash
git status
```

9. Abre calculadora.py y resuelve el conflicto combinando ambos cambios:

```python
    def dividir(self, a, b):
        """Divide dos números con validación mejorada y logging"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Los argumentos deben ser números")
        if b == 0:
            raise ValueError("División por cero no permitida")
        self.resultado = a / b
        print(f"División: {a} / {b} = {self.resultado}")
        return self.resultado
```

10. Marca como resuelto:

```bash
git add calculadora.py
```

11. Continúa el rebase:

```bash
git rebase --continue
```

12. Ve el historial:

```bash
git log --oneline --graph --all -10
```

13. Mergea a main:

```bash
git switch main
git merge feature-validacion-mejorada
```

14. Limpia:

```bash
git branch -d feature-validacion-mejorada
```

**Resultado esperado:**

- Resolviste un conflicto durante rebase
- Usaste `git rebase --continue` para continuar
- El historial final es lineal

***

## 4.3 Rebase Interactivo

Rebase interactivo te permite reescribir el historial: reordenar commits, combinarlos, editar mensajes, etc.

### Comandos de Rebase Interactivo

```bash
# Rebase interactivo de los últimos N commits
git rebase -i HEAD~3

# Rebase interactivo desde cierto commit
git rebase -i abc1234
```

### Opciones Disponibles

Cuando ejecutas rebase interactivo, Git abre un editor con algo así:

```
pick abc1234 primer commit
pick def5678 segundo commit
pick ghi9012 tercer commit

# Comandos:
# p, pick = usar commit
# r, reword = usar commit pero editar mensaje
# e, edit = usar commit pero detener para enmendar
# s, squash = usar commit pero combinar con anterior
# f, fixup = como squash pero descartar mensaje
# d, drop = eliminar commit
```

### EJERCICIO 19: Limpiar Historial con Rebase Interactivo

**Objetivo:** Usar rebase interactivo para limpiar commits antes de merge.

**Pasos:**

1. Crea un branch para nueva feature:

```bash
git switch -c feature-valor-absoluto
```

2. Implementa en varios commits pequeños (simulando desarrollo real):

```bash
# Commit 1: Función básica
cat >> calculadora.py << 'EOF'
    
    def valor_absoluto(self, n):
        self.resultado = abs(n)
        return self.resultado
EOF

git add calculadora.py
git commit -m "wip: agregar valor absoluto"
```

3. Segundo commit: Mejorar documentación

```bash
# Edita con tu editor para mejorar el docstring
# Cambia a: """Calcula el valor absoluto de un número"""

git add calculadora.py
git commit -m "fix: mejorar docstring"
```

4. Tercer commit: Typo en comentario

```bash
echo "# Función para calcular valor absoluto" >> calculadora.py

git add calculadora.py
git commit -m "fix typo"
```

5. Cuarto commit: Agregar test

```bash
cat >> test_calculadora.py << 'EOF'
    
    def test_valor_absoluto_positivo(self):
        resultado = self.calc.valor_absoluto(5)
        self.assertEqual(resultado, 5)
    
    def test_valor_absoluto_negativo(self):
        resultado = self.calc.valor_absoluto(-5)
        self.assertEqual(resultado, 5)
EOF

git add test_calculadora.py
git commit -m "test: agregar tests para valor absoluto"
```

6. Ve el historial:

```bash
git log --oneline -5
```

Deberías ver 4 commits algo desordenados.

7. Inicia rebase interactivo para los últimos 4 commits:

```bash
git rebase -i HEAD~4
```

8. Git abrirá tu editor con algo así:

```
pick abc1234 wip: agregar valor absoluto
pick def5678 fix: mejorar docstring
pick ghi9012 fix typo
pick jkl3456 test: agregar tests para valor absoluto
```

9. Combina los tres primeros commits y reordena:

Cambia a:

```
pick abc1234 wip: agregar valor absoluto
fixup def5678 fix: mejorar docstring
fixup ghi9012 fix typo
pick jkl3456 test: agregar tests para valor absoluto
```

O mejor aún, reword el primero:

```
reword abc1234 wip: agregar valor absoluto
fixup def5678 fix: mejorar docstring
fixup ghi9012 fix typo
pick jkl3456 test: agregar tests para valor absoluto
```

10. Guarda y cierra el editor.

11. Git abrirá otro editor para cambiar el mensaje del primer commit. Cámbialo a:

```
feat: implementar cálculo de valor absoluto
```

12. Guarda y cierra.

13. Ve el historial limpio:

```bash
git log --oneline -5
```

Ahora deberías ver solo 2 commits:
- feat: implementar cálculo de valor absoluto
- test: agregar tests para valor absoluto

14. Mergea a main:

```bash
git switch main
git merge feature-valor-absoluto
```

15. Limpia:

```bash
git branch -d feature-valor-absoluto
```

**Resultado esperado:**

- Combinaste múltiples commits en uno
- Mejoraste los mensajes de commit
- El historial está limpio y profesional

***

## 4.4 Reescribir Historial con filter-branch y filter-repo

### Eliminar Archivo del Historial Completo

Si accidentalmente commiteaste información sensible:

```bash
# Método nuevo (recomendado): git-filter-repo
# Primero instala: pip install git-filter-repo

git filter-repo --path archivo-sensible.txt --invert-paths

# Método antiguo (lento):
git filter-branch --tree-filter 'rm -f archivo-sensible.txt' HEAD
```

**Advertencia:** Esto reescribe TODO el historial. Solo úsalo en emergencias.

### Cambiar Autor/Email en Todo el Historial

```bash
git filter-branch --env-filter '
if [ "$GIT_COMMITTER_EMAIL" = "email-viejo@ejemplo.com" ]; then
    export GIT_COMMITTER_NAME="Nombre Nuevo"
    export GIT_COMMITTER_EMAIL="email-nuevo@ejemplo.com"
fi
if [ "$GIT_AUTHOR_EMAIL" = "email-viejo@ejemplo.com" ]; then
    export GIT_AUTHOR_NAME="Nombre Nuevo"
    export GIT_AUTHOR_EMAIL="email-nuevo@ejemplo.com"
fi
' --tag-name-filter cat -- --branches --tags
```

***

## 4.5 Cherry-Pick: Aplicar Commits Específicos

Cherry-pick te permite aplicar commits específicos de un branch a otro.

```bash
# Aplicar un commit específico al branch actual
git cherry-pick abc1234

# Aplicar múltiples commits
git cherry-pick abc1234 def5678 ghi9012

# Aplicar un rango de commits
git cherry-pick abc1234..def5678
```

### EJERCICIO 20: Usar Cherry-Pick

**Objetivo:** Aplicar commits selectivamente entre branches.

**Pasos:**

1. Crea un branch experimental:

```bash
git switch -c experimento-features
```

2. Haz varios commits diferentes:

```bash
# Feature 1: Función útil
cat >> calculadora.py << 'EOF'
    
    def porcentaje(self, valor, porcentaje):
        """Calcula el porcentaje de un valor"""
        self.resultado = (valor * porcentaje) / 100
        return self.resultado
EOF

git add calculadora.py
git commit -m "feat: agregar cálculo de porcentaje"

# Feature 2: Función experimental que no queremos
cat >> calculadora.py << 'EOF'
    
    def experimental(self):
        """Función experimental - no usar"""
        pass
EOF

git add calculadora.py
git commit -m "feat: función experimental"

# Feature 3: Otra función útil
cat >> calculadora.py << 'EOF'
    
    def promedio(self, *numeros):
        """Calcula el promedio de números"""
        if not numeros:
            raise ValueError("Debe proporcionar al menos un número")
        self.resultado = sum(numeros) / len(numeros)
        return self.resultado
EOF

git add calculadora.py
git commit -m "feat: agregar cálculo de promedio"
```

3. Ve el historial y anota los hashes:

```bash
git log --oneline -4
```

Copia los hashes del primer y tercer commit (porcentaje y promedio).

4. Vuelve a main:

```bash
git switch main
```

5. Aplica solo los commits que quieres:

```bash
# Reemplaza con tus hashes reales
git cherry-pick <hash-porcentaje>
git cherry-pick <hash-promedio>
```

6. Verifica que solo esas features están en main:

```bash
grep -n "def porcentaje" calculadora.py
grep -n "def promedio" calculadora.py
grep -n "def experimental" calculadora.py
```

Las dos primeras deberían encontrarse, la última no.

7. Limpia el branch experimental:

```bash
git branch -D experimento-features
```

**Resultado esperado:**

- Aplicaste commits selectivamente a otro branch
- Evitaste incorporar commits no deseados
- Entiendes cuándo cherry-pick es útil

***

## Checkpoint: Parte 4

Antes de continuar, verifica que puedes:

- Explicar la diferencia entre merge y rebase
- Usar `git rebase` para mantener historial lineal
- Resolver conflictos durante rebase con `git rebase --continue`
- Abortar un rebase con `git rebase --abort`
- Usar rebase interactivo con `git rebase -i`
- Combinar commits con `squash` y `fixup`
- Reordenar y editar commits en rebase interactivo
- Aplicar commits específicos con `git cherry-pick`
- Entender cuándo NO usar rebase (commits públicos)

***

# PARTE 5: TRABAJAR CON REPOSITORIOS REMOTOS

## 5.1 Conceptos de Repositorios Remotos

### Qué es un Remoto

Un repositorio remoto es una versión de tu proyecto hospedada en internet o red. Los más comunes:

- GitHub
- GitLab
- Bitbucket
- Servidor propio

### Ver Remotos

```bash
# Listar remotos
git remote

# Listar remotos con URLs
git remote -v

# Ver información detallada de un remoto
git remote show origin
```

### Agregar Remotos

```bash
# Agregar nuevo remoto
git remote add nombre-remoto https://github.com/usuario/repo.git

# El remoto principal se llama convencionalmente "origin"
git remote add origin https://github.com/usuario/mi-proyecto.git
```

### Renombrar y Eliminar Remotos

```bash
# Renombrar remoto
git remote rename viejo-nombre nuevo-nombre

# Eliminar remoto
git remote remove nombre-remoto
```

***

## 5.2 Clonar Repositorios

```bash
# Clonar repositorio
git clone https://github.com/usuario/repo.git

# Clonar a directorio específico
git clone https://github.com/usuario/repo.git mi-directorio

# Clonar solo cierta profundidad (historial limitado)
git clone --depth 1 https://github.com/usuario/repo.git
```

Cuando clonas:
1. Git descarga todo el historial
2. Crea un remoto llamado "origin" automáticamente
3. Crea un branch local "main" que trackea "origin/main"

***

## 5.3 Fetch, Pull y Push

### git fetch

Descarga cambios del remoto pero NO los integra:

```bash
# Fetch de todos los remotos
git fetch --all

# Fetch de un remoto específico
git fetch origin

# Fetch de un branch específico
git fetch origin main
```

Después de fetch, los cambios están en branches remotos (`origin/main`) pero no en tus branches locales.

### git pull

Descarga E integra cambios:

```bash
# Pull del branch actual
git pull

# Pull con rebase en lugar de merge
git pull --rebase

# Pull de branch específico
git pull origin main
```

`git pull` es equivalente a:

```bash
git fetch origin
git merge origin/main
```

### git push

Sube tus commits al remoto:

```bash
# Push del branch actual
git push

# Push y establecer upstream
git push -u origin main

# Push de branch específico
git push origin feature-branch

# Push todos los branches
git push --all

# Push tags
git push --tags

# Forzar push (peligroso)
git push --force
# O más seguro:
git push --force-with-lease
```

***

## 5.4 Branches Remotos y Tracking

### Ver Branches Remotos

```bash
# Ver branches remotos
git branch -r

# Ver todos los branches (locales y remotos)
git branch -a

# Ver branches con tracking info
git branch -vv
```

### Tracking Branches

Un tracking branch es un branch local que tiene relación directa con un branch remoto.

```bash
# Crear branch local que trackea remoto
git checkout -b feature origin/feature

# Método nuevo
git switch -c feature origin/feature

# O automáticamente si el nombre coincide
git switch feature
```

### Establecer Upstream

```bash
# Al pushear por primera vez
git push -u origin feature-branch

# Para branch existente
git branch --set-upstream-to=origin/feature-branch
```

***
## 5.5 Workflows con Remotos

### Workflow Típico de Colaboración

```bash
# 1. Actualizar tu copia local
git pull origin main

# 2. Crear branch para tu feature
git switch -c feature-nueva

# 3. Trabajar y commitear
git add .
git commit -m "feat: implementar nueva funcionalidad"

# 4. Actualizar con cambios recientes de main
git switch main
git pull origin main
git switch feature-nueva
git rebase main

# 5. Pushear tu branch
git push -u origin feature-nueva

# 6. Crear Pull Request en GitHub/GitLab

# 7. Después de merge, actualizar y limpiar
git switch main
git pull origin main
git branch -d feature-nueva
git push origin --delete feature-nueva
```

### EJERCICIO 21: Simular Trabajo con Remoto

**Objetivo:** Practicar el flujo completo de trabajo con repositorio remoto.

Como no podemos crear un repositorio real en GitHub en este ejercicio, simularemos con un repositorio "bare" local que actúa como remoto.

**Pasos:**

**Parte A: Configurar Repositorio "Remoto" Simulado**

1. Crea un directorio para el remoto simulado:

```bash
cd ~
mkdir git-remote-simulado
cd git-remote-simulado
git init --bare calculadora-remote.git
```

El flag `--bare` crea un repositorio sin working directory, similar a GitHub.

2. Ve a tu proyecto calculadora:

```bash
cd ~/calculadora-python
```

3. Agrega el remoto:

```bash
git remote add origin ~/git-remote-simulado/calculadora-remote.git
```

4. Verifica:

```bash
git remote -v
```

5. Pushea tu branch main:

```bash
git push -u origin main
```

**Parte B: Simular Otro Desarrollador**

1. Clona el repositorio en otra ubicación (simula otro desarrollador):

```bash
cd ~
git clone ~/git-remote-simulado/calculadora-remote.git calculadora-colaborador
cd calculadora-colaborador
```

2. Verifica el contenido:

```bash
ls
git log --oneline -5
```

3. Como "colaborador", crea una nueva feature:

```bash
git switch -c feature-factorial
```

4. Implementa factorial:

```bash
cat >> calculadora.py << 'EOF'
    
    def factorial(self, n):
        """Calcula el factorial de un número entero no negativo"""
        if not isinstance(n, int):
            raise TypeError("El factorial solo acepta enteros")
        if n < 0:
            raise ValueError("El factorial no está definido para negativos")
        if n == 0 or n == 1:
            return 1
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        self.resultado = resultado
        return self.resultado
EOF

git add calculadora.py
git commit -m "feat: implementar cálculo de factorial"
```

5. Pushea el branch:

```bash
git push -u origin feature-factorial
```

**Parte C: Volver al Repositorio Original**

1. Regresa a tu repositorio original:

```bash
cd ~/calculadora-python
```

2. Haz fetch para ver los cambios del colaborador:

```bash
git fetch origin
```

3. Ve los branches remotos:

```bash
git branch -r
```

Deberías ver `origin/feature-factorial`.

4. Revisa los cambios del colaborador:

```bash
git log origin/feature-factorial --oneline -3
```

5. Crea un branch local para revisar:

```bash
git switch -c review-factorial origin/feature-factorial
```

6. Revisa el código:

```bash
cat calculadora.py | grep -A 15 "def factorial"
```

7. Si apruebas los cambios, mergea a main:

```bash
git switch main
git merge review-factorial
```

8. Pushea main actualizado:

```bash
git push origin main
```

9. Elimina el branch local y remoto:

```bash
git branch -d review-factorial
git push origin --delete feature-factorial
```

**Parte D: Colaborador Actualiza**

1. Vuelve al directorio del colaborador:

```bash
cd ~/calculadora-colaborador
```

2. Actualiza main:

```bash
git switch main
git pull origin main
```

3. Verifica que tiene los cambios:

```bash
git log --oneline -3
```

4. Limpia su branch local:

```bash
git branch -d feature-factorial
```

**Resultado esperado:**

- Simulaste el flujo completo de colaboración
- Entiendes fetch, pull y push
- Sabes cómo trabajar con branches remotos
- Practicaste el ciclo de feature branch y merge

***

## 5.6 Resolver Conflictos en Pull

### Cuando Pull Causa Conflictos

Si alguien modificó las mismas líneas que tú:

```bash
git pull origin main

# Auto-merging archivo.py
# CONFLICT (content): Merge conflict in archivo.py
# Automatic merge failed; fix conflicts and then commit the result.

# Resolver conflictos
# Editar archivo.py

git add archivo.py
git commit -m "merge: resolver conflictos con origin/main"
```

### Pull con Rebase

Para mantener historial lineal:

```bash
git pull --rebase origin main

# Si hay conflictos:
# 1. Resolver conflicto
# 2. git add archivo.py
# 3. git rebase --continue
```

### EJERCICIO 22: Resolver Conflictos en Pull

**Objetivo:** Practicar resolución de conflictos cuando varios desarrolladores modifican lo mismo.

**Pasos:**

**Parte A: Crear Conflicto**

1. En el repositorio colaborador, modifica README:

```bash
cd ~/calculadora-colaborador
git switch main
```

2. Agrega documentación:

```bash
cat >> README.md << 'EOF'

## Funciones Avanzadas

El módulo incluye funciones matemáticas avanzadas:
- Factorial
- Combinaciones
EOF

git add README.md
git commit -m "docs: agregar sección de funciones avanzadas"
git push origin main
```

**Parte B: Modificar Mismo Archivo en Repo Original**

1. Sin hacer pull, modifica README en tu repo original:

```bash
cd ~/calculadora-python
```

2. Agrega diferente documentación al mismo archivo:

```bash
cat >> README.md << 'EOF'

## Características Especiales

Esta calculadora incluye:
- Validación de tipos
- Manejo de errores robusto
- Logging de operaciones
EOF

git add README.md
git commit -m "docs: agregar características especiales"
```

**Parte C: Intentar Push (Fallará)**

1. Intenta pushear:

```bash
git push origin main
```

Deberías ver:

```
! [rejected]        main -> main (fetch first)
error: failed to push some refs to '~/git-remote-simulado/calculadora-remote.git'
hint: Updates were rejected because the remote contains work that you do not have locally.
```

**Parte D: Pull y Resolver Conflicto**

1. Haz pull:

```bash
git pull origin main
```

Deberías ver conflicto en README.md.

2. Abre README.md y verás:

```markdown
<<<<<<< HEAD
## Características Especiales

Esta calculadora incluye:
- Validación de tipos
- Manejo de errores robusto
- Logging de operaciones
=======
## Funciones Avanzadas

El módulo incluye funciones matemáticas avanzadas:
- Factorial
- Combinaciones
>>>>>>> abc1234
```

3. Resuelve el conflicto combinando ambas secciones:

```markdown
## Características Especiales

Esta calculadora incluye:
- Validación de tipos
- Manejo de errores robusto
- Logging de operaciones

## Funciones Avanzadas

El módulo incluye funciones matemáticas avanzadas:
- Factorial
- Combinaciones
```

4. Marca como resuelto y commitea:

```bash
git add README.md
git commit -m "merge: combinar documentación de características"
```

5. Ahora sí pushea:

```bash
git push origin main
```

6. Verifica en el colaborador:

```bash
cd ~/calculadora-colaborador
git pull origin main
cat README.md
```

**Resultado esperado:**

- Entiendes por qué push puede ser rechazado
- Sabes resolver conflictos durante pull
- Practicaste el flujo de resolver y pushear

***

## 5.7 Trabajar con Pull Requests

### Qué es un Pull Request (PR)

Un Pull Request es una solicitud para integrar tus cambios en otro branch. Es el mecanismo estándar de colaboración en GitHub/GitLab.

### Flujo de Pull Request

1. **Fork** (si no tienes permisos) o **Clone** del repositorio
2. Crear **feature branch**
3. Hacer cambios y **commits**
4. **Push** del branch
5. Crear **Pull Request** en la plataforma
6. **Code review** por el equipo
7. Hacer cambios adicionales si se solicitan
8. **Merge** del PR (por maintainer)

### Comandos Relacionados

```bash
# Crear branch para PR
git switch -c feature-pr

# Hacer cambios
git add .
git commit -m "feat: nueva funcionalidad"

# Pushear branch
git push -u origin feature-pr

# Después de merge del PR en GitHub:
git switch main
git pull origin main
git branch -d feature-pr
git push origin --delete feature-pr
```

### Actualizar PR con Nuevos Cambios

```bash
# Estás en tu feature branch
git add .
git commit -m "fix: atender comentarios del review"
git push origin feature-pr

# Los cambios aparecen automáticamente en el PR
```

### Actualizar PR con Cambios de Main

Si main avanzó mientras trabajabas en tu PR:

```bash
# Opción 1: Merge (crea merge commit en el PR)
git switch feature-pr
git merge main
git push origin feature-pr

# Opción 2: Rebase (historial más limpio)
git switch feature-pr
git rebase main
git push --force-with-lease origin feature-pr
```

***

## 5.8 Git Tags

Los tags marcan puntos específicos en el historial como importantes, típicamente releases.

### Tipos de Tags

**Lightweight tags:** Solo una referencia a un commit

```bash
git tag v1.0.0
```

**Annotated tags:** Objetos completos con metadata (recomendado)

```bash
git tag -a v1.0.0 -m "Release versión 1.0.0"
```

### Listar y Ver Tags

```bash
# Listar tags
git tag

# Listar tags con patrón
git tag -l "v1.*"

# Ver información de un tag
git show v1.0.0
```

### Pushear Tags

```bash
# Pushear tag específico
git push origin v1.0.0

# Pushear todos los tags
git push origin --tags

# Pushear solo annotated tags
git push origin --follow-tags
```

### Eliminar Tags

```bash
# Eliminar tag local
git tag -d v1.0.0

# Eliminar tag remoto
git push origin --delete v1.0.0
```

### Checkout de Tags

```bash
# Ver código en cierto tag
git checkout v1.0.0

# Crear branch desde tag
git switch -c hotfix-v1.0.0 v1.0.0
```

### EJERCICIO 23: Trabajar con Tags

**Objetivo:** Crear y gestionar tags para versiones.

**Pasos:**

1. En tu repositorio principal:

```bash
cd ~/calculadora-python
git switch main
```

2. Verifica que estás en un estado limpio:

```bash
git status
```

3. Crea un tag para la versión 1.0.0:

```bash
git tag -a v1.0.0 -m "Release 1.0.0: Calculadora con operaciones básicas"
```

4. Ve el tag:

```bash
git show v1.0.0
```

5. Lista todos los tags:

```bash
git tag
```

6. Pushea el tag al remoto:

```bash
git push origin v1.0.0
```

7. Verifica en el colaborador:

```bash
cd ~/calculadora-colaborador
git fetch origin --tags
git tag
```

8. Haz algunos cambios adicionales en el original:

```bash
cd ~/calculadora-python

cat >> calculadora.py << 'EOF'
    
    def maximo(self, *numeros):
        """Encuentra el máximo de varios números"""
        if not numeros:
            raise ValueError("Debe proporcionar al menos un número")
        self.resultado = max(numeros)
        return self.resultado
    
    def minimo(self, *numeros):
        """Encuentra el mínimo de varios números"""
        if not numeros:
            raise ValueError("Debe proporcionar al menos un número")
        self.resultado = min(numeros)
        return self.resultado
EOF

git add calculadora.py
git commit -m "feat: agregar funciones máximo y mínimo"
git push origin main
```

9. Crea tag v1.1.0:

```bash
git tag -a v1.1.0 -m "Release 1.1.0: Agregar máximo y mínimo"
git push origin v1.1.0
```

10. Crea tag v1.2.0 para release siguiente:

```bash
cat >> calculadora.py << 'EOF'
    
    def redondear(self, n, decimales=0):
        """Redondea un número a cierto número de decimales"""
        self.resultado = round(n, decimales)
        return self.resultado
EOF

git add calculadora.py
git commit -m "feat: agregar función de redondeo"
git push origin main

git tag -a v1.2.0 -m "Release 1.2.0: Agregar redondeo"
git push origin v1.2.0
```

11. Lista tags con patrón:

```bash
git tag -l "v1.*"
```

12. Compara versiones:

```bash
git diff v1.0.0 v1.2.0
```

13. Simula que necesitas hacer un hotfix en v1.1.0:

```bash
git switch -c hotfix-v1.1.1 v1.1.0
```

14. Haz un pequeño fix:

```bash
# Supón que encontraste un bug en la función máximo
# (esto es solo simulación)
echo "# Hotfix aplicado" >> calculadora.py
git add calculadora.py
git commit -m "fix: corregir edge case en función máximo"
```

15. Crea tag de hotfix:

```bash
git tag -a v1.1.1 -m "Hotfix 1.1.1: Corregir bug en máximo"
```

16. Mergea a main:

```bash
git switch main
git merge hotfix-v1.1.1
git push origin main
git push origin v1.1.1
```

17. Limpia:

```bash
git branch -d hotfix-v1.1.1
```

18. Ve todos los tags ordenados:

```bash
git tag | sort -V
```

**Resultado esperado:**

- Creaste tags annotated para versiones
- Pusheaste tags al remoto
- Comparaste código entre versiones
- Creaste un hotfix desde un tag
- Entiendes el versionado semántico (major.minor.patch)

***

## 5.9 Git Stash: Guardar Trabajo Temporal

Stash te permite guardar cambios temporalmente sin commitear.

### Comandos Básicos

```bash
# Guardar cambios en stash
git stash

# Guardar con mensaje descriptivo
git stash push -m "trabajo en progreso en feature X"

# Listar stashes
git stash list

# Ver contenido de un stash
git stash show stash@{0}
git stash show -p stash@{0}  # con diff completo

# Aplicar último stash (mantiene en stash)
git stash apply

# Aplicar y eliminar último stash
git stash pop

# Aplicar stash específico
git stash apply stash@{1}

# Eliminar stash específico
git stash drop stash@{0}

# Eliminar todos los stashes
git stash clear

# Crear branch desde stash
git stash branch nombre-branch stash@{0}
```

### Stash Selectivo

```bash
# Stash solo archivos staged
git stash --staged

# Stash incluyendo untracked files
git stash -u

# Stash incluyendo untracked e ignored
git stash -a

# Stash interactivo (seleccionar qué cambios)
git stash -p
```

### EJERCICIO 24: Usar Git Stash

**Objetivo:** Practicar guardar y recuperar trabajo temporal.

**Pasos:**

**Parte A: Stash Básico**

1. En tu repositorio, inicia trabajo en nueva feature:

```bash
cd ~/calculadora-python
git switch -c feature-logaritmo
```

2. Empieza a implementar:

```bash
cat >> calculadora.py << 'EOF'
    
    def logaritmo(self, n, base=10):
        """Calcula logaritmo en base especificada"""
        # TODO: implementar validación
        import math
EOF

git add calculadora.py
```

3. Recibes urgencia para fix en main:

```bash
# Guarda tu trabajo sin commitear
git stash push -m "WIP: implementando logaritmo"
```

4. Verifica que working directory está limpio:

```bash
git status
```

5. Cambia a main para el fix urgente:

```bash
git switch main
```

6. Haz el fix urgente:

```bash
cat >> README.md << 'EOF'

## Nota Importante

Esta calculadora está en desarrollo activo.
EOF

git add README.md
git commit -m "docs: agregar nota de desarrollo"
git push origin main
```

7. Vuelve a tu feature:

```bash
git switch feature-logaritmo
```

8. Recupera tu trabajo:

```bash
git stash list
git stash pop
```

9. Continúa trabajando:

```bash
# Completa la implementación
cat >> calculadora.py << 'EOF'
        if n <= 0:
            raise ValueError("Logaritmo solo definido para positivos")
        if base <= 0 or base == 1:
            raise ValueError("Base debe ser positiva y diferente de 1")
        self.resultado = math.log(n, base)
        return self.resultado
EOF

git add calculadora.py
git commit -m "feat: implementar cálculo de logaritmo"
```

**Parte B: Múltiples Stashes**

1. Inicia otro trabajo:

```bash
echo "# Cambio en README" >> README.md
```

2. Stash con mensaje:

```bash
git stash push -m "cambios en README"
```

3. Haz más cambios:

```bash
echo "# Otro cambio" >> calculadora.py
```

4. Stash de nuevo:

```bash
git stash push -m "cambios en calculadora"
```

5. Lista stashes:

```bash
git stash list
```

Deberías ver:
```
stash@{0}: On feature-logaritmo: cambios en calculadora
stash@{1}: On feature-logaritmo: cambios en README
```

6. Ve contenido de un stash específico:

```bash
git stash show -p stash@{1}
```

7. Aplica stash específico:

```bash
git stash apply stash@{1}
```

8. Verifica cambios:

```bash
git diff
```

9. Descarta cambios:

```bash
git restore README.md
```

10. Limpia todos los stashes:

```bash
git stash clear
```

**Parte C: Stash con Untracked Files**

1. Crea archivos nuevos:

```bash
echo "notas temporales" > notas.txt
echo "# experimento" >> calculadora.py
```

2. Stash normal (no guarda untracked):

```bash
git stash
```

3. Verifica que notas.txt sigue ahí:

```bash
ls notas.txt
```

4. Recupera stash:

```bash
git stash pop
```

5. Ahora stash incluyendo untracked:

```bash
git stash -u
```

6. Verifica que notas.txt desapareció:

```bash
ls notas.txt
```

Debería dar error.

7. Recupera:

```bash
git stash pop
```

8. Limpia archivos temporales:

```bash
rm notas.txt
git restore calculadora.py
```

9. Mergea tu feature a main:

```bash
git switch main
git merge feature-logaritmo
git push origin main
git branch -d feature-logaritmo
```

**Resultado esperado:**

- Usaste stash para cambiar de contexto rápidamente
- Manejaste múltiples stashes
- Entiendes la diferencia entre apply y pop
- Sabes cómo stash archivos untracked

***

## Checkpoint: Parte 5

Antes de continuar, verifica que puedes:

- Clonar repositorios con `git clone`
- Agregar remotos con `git remote add`
- Hacer fetch, pull y push
- Crear y trabajar con branches remotos
- Establecer upstream con `git push -u`
- Resolver conflictos durante pull
- Crear y gestionar tags
- Pushear tags con `--tags`
- Usar stash para guardar trabajo temporal
- Aplicar y eliminar stashes

***

# PARTE 6: FLUJOS DE TRABAJO PROFESIONALES

## 6.1 Git Flow

Git Flow es un modelo de branching que define estructura estricta para organizar branches.

### Estructura de Branches

**Branches principales (permanentes):**

- `main` (o `master`): Código en producción
- `develop`: Código en desarrollo, base para features

**Branches de soporte (temporales):**

- `feature/*`: Nuevas funcionalidades (desde develop)
- `release/*`: Preparación de releases (desde develop)
- `hotfix/*`: Fixes urgentes en producción (desde main)

### Visualización

```
main:     v1.0 -------- v1.1 -------- v2.0
           |             |             |
           |             |       hotfix/critical
           |             |      /       |
develop:   |--F1--F2--R1.1--F3--F4--R2.0
              |    |    |    |    |
         feature/ feature/ release/
           f1      f2      1.1
```

### Flujo de Feature

```bash
# Iniciar feature
git switch develop
git switch -c feature/nueva-funcionalidad

# Trabajar
git add .
git commit -m "feat: implementar parte 1"
git commit -m "feat: implementar parte 2"

# Finalizar feature
git switch develop
git merge --no-ff feature/nueva-funcionalidad
git branch -d feature/nueva-funcionalidad
git push origin develop
```

### Flujo de Release

```bash
# Iniciar release
git switch develop
git switch -c release/1.1.0

# Preparación (fix bugs menores, actualizar versión)
git commit -am "chore: actualizar versión a 1.1.0"

# Finalizar release
git switch main
git merge --no-ff release/1.1.0
git tag -a v1.1.0 -m "Release 1.1.0"
git push origin main --tags

git switch develop
git merge --no-ff release/1.1.0
git push origin develop

git branch -d release/1.1.0
```

### Flujo de Hotfix

```bash
# Iniciar hotfix desde main
git switch main
git switch -c hotfix/1.1.1

# Fix urgente
git commit -am "fix: corregir bug crítico"

# Finalizar hotfix
git switch main
git merge --no-ff hotfix/1.1.1
git tag -a v1.1.1 -m "Hotfix 1.1.1"
git push origin main --tags

git switch develop
git merge --no-ff hotfix/1.1.1
git push origin develop

git branch -d hotfix/1.1.1
```

### EJERCICIO 25: Implementar Git Flow

**Objetivo:** Practicar el flujo completo de Git Flow.

**Pasos:**

**Parte A: Configurar Git Flow**

1. En tu repositorio, crea branch develop:

```bash
cd ~/calculadora-python
git switch -c develop
git push -u origin develop
```

2. Actualiza configuración para que develop sea el branch por defecto para desarrollo (esto es conceptual).

**Parte B: Feature Branch**

1. Crea feature para nueva funcionalidad:

```bash
git switch develop
git switch -c feature/trigonometria
```

2. Implementa funciones trigonométricas:

```bash
cat >> calculadora.py << 'EOF'
    
    def seno(self, angulo_grados):
        """Calcula el seno de un ángulo en grados"""
        import math
        angulo_radianes = math.radians(angulo_grados)
        self.resultado = math.sin(angulo_radianes)
        return self.resultado
    
    def coseno(self, angulo_grados):
        """Calcula el coseno de un ángulo en grados"""
        import math
        angulo_radianes = math.radians(angulo_grados)
        self.resultado = math.cos(angulo_radianes)
        return self.resultado
    
    def tangente(self, angulo_grados):
        """Calcula la tangente de un ángulo en grados"""
        import math
        angulo_radianes = math.radians(angulo_grados)
        self.resultado = math.tan(angulo_radianes)
        return self.resultado
EOF

git add calculadora.py
git commit -m "feat: implementar funciones trigonométricas básicas"
```

3. Añade tests:

```bash
cat >> test_calculadora.py << 'EOF'
    
    def test_seno_0(self):
        resultado = self.calc.seno(0)
        self.assertAlmostEqual(resultado, 0, places=10)
    
    def test_seno_90(self):
        resultado = self.calc.seno(90)
        self.assertAlmostEqual(resultado, 1, places=10)
    
    def test_coseno_0(self):
        resultado = self.calc.coseno(0)
        self.assertAlmostEqual(resultado, 1, places=10)
EOF

git add test_calculadora.py
git commit -m "test: agregar tests para trigonometría"
```

4. Finaliza feature mergeando a develop:

```bash
git switch develop
git merge --no-ff feature/trigonometria -m "feat: merge funcionalidad trigonometría"
git branch -d feature/trigonometria
git push origin develop
```

**Parte C: Release Branch**

1. Crea release branch:

```bash
git switch develop
git switch -c release/2.0.0
```

2. Actualiza versión en README:

```bash
cat >> README.md << 'EOF'

## Versión

Versión actual: 2.0.0

### Changelog

#### v2.0.0
- Agregadas funciones trigonométricas (seno, coseno, tangente)
- Agregadas funciones estadísticas (máximo, mínimo, promedio)
- Agregadas funciones matemáticas (logaritmo, factorial, potencia)
EOF

git add README.md
git commit -m "chore: actualizar versión a 2.0.0"
```

3. Fix menor si es necesario:

```bash
# Simula un pequeño fix encontrado durante QA
echo "# Verificado en QA" >> calculadora.py
git add calculadora.py
git commit -m "fix: ajuste menor post-QA"
```

4. Mergea a main:

```bash
git switch main
git merge --no-ff release/2.0.0 -m "release: versión 2.0.0"
git tag -a v2.0.0 -m "Release 2.0.0: Funciones trigonométricas y matemáticas avanzadas"
git push origin main --tags
```

5. Mergea de vuelta a develop:

```bash
git switch develop
git merge --no-ff release/2.0.0 -m "chore: merge release 2.0.0 a develop"
git push origin develop
```

6. Elimina release branch:

```bash
git branch -d release/2.0.0
```

**Parte D: Hotfix Branch**

1. Simula bug crítico descubierto en producción:

```bash
git switch main
git switch -c hotfix/2.0.1
```

2. Fix el bug:

```bash
# Simula fix de un bug en división
# (esto es solo para el ejercicio)
cat >> calculadora.py << 'EOF'

# Hotfix 2.0.1: Validación mejorada
EOF

git add calculadora.py
git commit -m "fix: corregir validación en división por cero"
```

3. Mergea a main:

```bash
git switch main
git merge --no-ff hotfix/2.0.1 -m "hotfix: versión 2.0.1"
git tag -a v2.0.1 -m "Hotfix 2.0.1: Corregir validación"
git push origin main --tags
```

4. Mergea a develop:

```bash
git switch develop
git merge --no-ff hotfix/2.0.1 -m "chore: merge hotfix 2.0.1 a develop"
git push origin develop
```

5. Elimina hotfix branch:

```bash
git branch -d hotfix/2.0.1
```

6. Ve el historial completo:

```bash
git log --oneline --graph --all -20
```

**Resultado esperado:**

- Implementaste el flujo completo de Git Flow
- Tienes branches main y develop separados
- Manejaste features, releases y hotfixes correctamente
- El historial muestra claramente el flujo de trabajo

***

## 6.2 Trunk-Based Development

Alternativa más simple a Git Flow para equipos que hacen deployment continuo.

### Principios

- Un solo branch principal (main/trunk)
- Commits frecuentes y directos a main
- Feature flags para funcionalidad incompleta
- Branches de feature muy cortos (máximo 1-2 días)
- Integración continua obligatoria

### Flujo

```bash
# Crear branch corto
git switch -c short-feature
# ... trabajar pocas horas
git commit -am "feat: cambio pequeño"

# Integrar rápido
git switch main
git pull --rebase origin main
git switch short-feature
git rebase main
git switch main
git merge short-feature
git push origin main
git branch -d short-feature
```

### Cuándo Usar

- **Git Flow:** Releases programados, equipos grandes, múltiples versiones en soporte
- **Trunk-Based:** Deployment continuo, equipos pequeños, una versión en producción

***

Continúa con más flujos profesionales...
## 6.3 GitHub Flow

GitHub Flow es más simple que Git Flow, diseñado para deployment continuo.

### Principios

- `main` siempre está en estado deployable
- Crear branches descriptivos para cualquier cambio
- Hacer commits frecuentes al branch
- Abrir Pull Request temprano para feedback
- Mergear solo después de review y tests pasando
- Deploy inmediatamente después de merge

### Flujo Completo

```bash
# 1. Actualizar main
git switch main
git pull origin main

# 2. Crear branch descriptivo
git switch -c add-user-authentication

# 3. Hacer cambios y commits
git add .
git commit -m "feat: implement JWT authentication"
git commit -m "feat: add login endpoint"
git commit -m "test: add auth tests"

# 4. Pushear branch
git push -u origin add-user-authentication

# 5. Abrir Pull Request en GitHub
# (se hace en la interfaz web)

# 6. Después de review y merge automático en GitHub:
git switch main
git pull origin main
git branch -d add-user-authentication
```

### Ventajas

- Simple de entender y seguir
- Fomenta code review
- Integración continua natural
- Deployment rápido

### Cuándo Usar

- Proyectos web con deployment continuo
- Equipos pequeños a medianos
- Cuando quieres simplicidad sobre estructura rígida

***

## 6.4 Forking Workflow

Usado en proyectos open source donde no todos tienen permisos de escritura.

### Flujo Completo

```bash
# 1. Hacer fork del repositorio en GitHub (web)

# 2. Clonar TU fork
git clone https://github.com/TU-USUARIO/proyecto.git
cd proyecto

# 3. Agregar upstream (repositorio original)
git remote add upstream https://github.com/ORIGINAL/proyecto.git

# 4. Verificar remotos
git remote -v
# origin    https://github.com/TU-USUARIO/proyecto.git (fetch)
# origin    https://github.com/TU-USUARIO/proyecto.git (push)
# upstream  https://github.com/ORIGINAL/proyecto.git (fetch)
# upstream  https://github.com/ORIGINAL/proyecto.git (push)

# 5. Crear branch para tu feature
git switch -c fix-bug-123

# 6. Hacer cambios
git add .
git commit -m "fix: resolver issue #123"

# 7. Pushear a TU fork
git push origin fix-bug-123

# 8. Crear Pull Request desde tu fork al upstream (web)

# 9. Mantener tu fork actualizado
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```

### Sincronizar Fork con Upstream

```bash
# Fetch cambios del upstream
git fetch upstream

# Mergear upstream/main a tu main local
git switch main
git merge upstream/main

# O hacer rebase
git rebase upstream/main

# Pushear a tu fork
git push origin main

# Actualizar tu feature branch
git switch fix-bug-123
git rebase main
git push --force-with-lease origin fix-bug-123
```

***

## 6.5 Estrategias de Commit

### Commits Atómicos

Cada commit debe ser una unidad lógica completa y funcional.

**Bien:**
```bash
git commit -m "feat: agregar validación de email"
git commit -m "feat: agregar validación de contraseña"
git commit -m "test: agregar tests de validación"
```

**Mal:**
```bash
git commit -m "cambios varios"  # Incluye validación + tests + refactor
```

### Commits Semánticos (Conventional Commits)

Formato estándar para mensajes de commit: [gist.github](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13)

```
<tipo>[ámbito opcional]: <descripción>

[cuerpo opcional]

[footer opcional]
```

**Tipos principales:**

- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `docs`: Solo documentación
- `style`: Formato (no afecta código)
- `refactor`: Refactorización (no cambia funcionalidad)
- `perf`: Mejora de rendimiento
- `test`: Agregar o modificar tests
- `build`: Cambios en build system
- `ci`: Cambios en CI/CD
- `chore`: Tareas de mantenimiento

**Ejemplos:**

```bash
git commit -m "feat(auth): implement OAuth2 login"
git commit -m "fix(api): handle null response in getUserData"
git commit -m "docs(readme): add installation instructions"
git commit -m "refactor(utils): simplify date formatting logic"
git commit -m "perf(database): add index on user_id column"
git commit -m "test(calculator): add edge case tests"
```

**Breaking changes:**

```bash
git commit -m "feat(api)!: change response format to JSON API spec

BREAKING CHANGE: API responses now follow JSON API specification.
Old clients need to be updated.
"
```

### EJERCICIO 26: Practicar Commits Semánticos

**Objetivo:** Escribir commits siguiendo Conventional Commits.

**Pasos:**

1. Crea un nuevo branch:

```bash
cd ~/calculadora-python
git switch develop
git switch -c feature/mejoras-calidad
```

2. Agrega documentación (tipo docs):

```bash
cat > CONTRIBUTING.md << 'EOF'
# Guía de Contribución

## Cómo Contribuir

1. Fork el repositorio
2. Crea un branch para tu feature
3. Haz commits con mensajes descriptivos
4. Abre un Pull Request

## Estándares de Código

- Usa PEP 8 para Python
- Escribe docstrings para funciones públicas
- Agrega tests para nueva funcionalidad
EOF

git add CONTRIBUTING.md
git commit -m "docs: agregar guía de contribución"
```

3. Refactoriza código (tipo refactor):

```bash
# Supón que extraes validación a función separada
cat >> calculadora.py << 'EOF'

def _validar_numero(valor, nombre="valor"):
    """Valida que un valor sea numérico"""
    if not isinstance(valor, (int, float)):
        raise TypeError(f"{nombre} debe ser un número")
    return True
EOF

git add calculadora.py
git commit -m "refactor(calculadora): extraer validación a función helper"
```

4. Agrega tests (tipo test):

```bash
cat >> test_calculadora.py << 'EOF'
    
    def test_operaciones_encadenadas(self):
        """Test de múltiples operaciones en secuencia"""
        self.calc.sumar(5, 3)
        resultado1 = self.calc.resultado
        self.calc.multiplicar(resultado1, 2)
        resultado2 = self.calc.resultado
        self.assertEqual(resultado2, 16)
EOF

git add test_calculadora.py
git commit -m "test(calculadora): agregar test de operaciones encadenadas"
```

5. Mejora rendimiento (tipo perf):

```bash
# Simula optimización (ejemplo conceptual)
echo "# Optimización de cálculos" >> calculadora.py

git add calculadora.py
git commit -m "perf(calculadora): optimizar cálculos usando cache"
```

6. Tarea de mantenimiento (tipo chore):

```bash
cat > .editorconfig << 'EOF'
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 4

[*.py]
max_line_length = 88
EOF

git add .editorconfig
git commit -m "chore: agregar configuración de EditorConfig"
```

7. Ve el historial con commits semánticos:

```bash
git log --oneline
```

8. Mergea a develop:

```bash
git switch develop
git merge --no-ff feature/mejoras-calidad -m "chore: merge mejoras de calidad"
git branch -d feature/mejoras-calidad
```

**Resultado esperado:**

- Todos tus commits siguen Conventional Commits
- Los tipos de commit reflejan claramente qué cambió
- El historial es autodocumentado y fácil de entender

***

## 6.6 Code Review Best Practices

### Crear Pull Requests Efectivos

**Buenas prácticas:**

1. **Título descriptivo:**
   ```
   feat(auth): implement two-factor authentication
   ```

2. **Descripción completa:**
   ```markdown
   ## Cambios

   - Implementa 2FA usando TOTP
   - Agrega endpoints para activar/desactivar 2FA
   - Incluye tests unitarios e integración

   ## Por qué

   Los usuarios solicitaron 2FA para mayor seguridad (issue #234)

   ## Cómo probar

   1. Ejecutar tests: `npm test`
   2. Probar manualmente: ver docs/2fa-testing.md

   ## Screenshots

   [incluir si aplica]

   ## Checklist

   - [x] Tests pasando
   - [x] Documentación actualizada
   - [x] Sin conflictos con main
   - [x] Code coverage > 80%
   ```

3. **PRs pequeños:** 
   - Máximo 400 líneas de cambio
   - Una funcionalidad por PR
   - Fácil de revisar en < 30 minutos

4. **Commits limpios:**
   - Usar squash si tienes muchos commits pequeños
   - O rebase interactivo para limpiar historial

### Hacer Code Review

**Como reviewer:**

1. **Revisar rápido:** Máximo 24 horas
2. **Ser constructivo:** Sugerir, no ordenar
3. **Enfocarse en:**
   - Lógica correcta
   - Tests adecuados
   - Seguridad
   - Rendimiento
   - Legibilidad

**Ejemplos de comentarios:**

```
❌ Mal:
"Esto está mal"

✅ Bien:
"Este enfoque podría causar N+1 queries. ¿Qué tal usar prefetch_related?
Ver: [link a documentación]"

❌ Mal:
"No uses esto"

✅ Bien:
"Sugerencia: En lugar de un loop manual, podrías usar list comprehension
para mejor rendimiento y legibilidad:
[código sugerido]"
```

**Como autor del PR:**

1. **Responder a todos los comentarios**
2. **Hacer cambios solicitados en nuevos commits** (facilita ver qué cambió)
3. **Agradecer feedback constructivo**
4. **No tomar críticas personalmente**

***

## 6.7 Gestión de Branches

### Estrategias de Nombrado

**Feature branches:**
```
feature/nombre-descriptivo
feature/user-authentication
feature/JIRA-123-add-payment
```

**Bug fixes:**
```
fix/nombre-bug
fix/login-redirect-issue
fix/ISSUE-456-memory-leak
```

**Hotfixes:**
```
hotfix/version-numero
hotfix/1.2.3-critical-security
```

**Release branches:**
```
release/version
release/2.0.0
```

### Limpieza de Branches

```bash
# Ver branches merged
git branch --merged main

# Eliminar branches locales merged
git branch --merged main | grep -v "main" | xargs git branch -d

# Ver branches remotos obsoletos
git remote prune origin --dry-run

# Eliminar referencias a branches remotos eliminados
git remote prune origin

# Eliminar branch remoto
git push origin --delete nombre-branch
```

### Branches de Larga Duración

**Evitar branches de larga duración:**

- Causan conflictos masivos
- Dificultan integración
- Código desincronizado con main

**Si son inevitables:**

```bash
# Sincronizar frecuentemente (diario)
git switch long-lived-branch
git fetch origin
git rebase origin/main

# O merge si ya es público
git merge origin/main
```

***

## 6.8 Versionado Semántico

### Formato: MAJOR.MINOR.PATCH

**Ejemplo: 2.4.7**

- **MAJOR (2):** Cambios incompatibles en API
- **MINOR (4):** Nueva funcionalidad compatible
- **PATCH (7):** Bug fixes compatibles

### Cuándo Incrementar

**MAJOR:** Breaking changes
```bash
# API cambió de forma incompatible
git tag -a v2.0.0 -m "BREAKING: Cambiar formato de respuestas API"
```

**MINOR:** Nueva funcionalidad
```bash
# Nueva feature pero compatible
git tag -a v1.5.0 -m "Agregar autenticación OAuth"
```

**PATCH:** Bug fixes
```bash
# Corrección de bug
git tag -a v1.4.3 -m "Corregir memory leak en cache"
```

### Versionado con Pre-releases

```
1.0.0-alpha.1    # Alpha release
1.0.0-beta.2     # Beta release
1.0.0-rc.1       # Release candidate
1.0.0            # Versión estable
```

### EJERCICIO 27: Implementar Versionado Semántico

**Objetivo:** Practicar versionado semántico completo.

**Pasos:**

1. Verifica la versión actual:

```bash
cd ~/calculadora-python
git tag | sort -V | tail -1
```

Supongamos que estás en v2.0.1.

2. Crea release candidate para v2.1.0:

```bash
git switch develop
git switch -c release/2.1.0-rc.1
```

3. Actualiza documentación de versión:

```bash
cat >> README.md << 'EOF'

#### v2.1.0-rc.1
- Agregadas funciones trigonométricas avanzadas
- Mejoras en validación de entrada
- Optimizaciones de rendimiento
EOF

git add README.md
git commit -m "chore: preparar release candidate 2.1.0-rc.1"
```

4. Crea tag de release candidate:

```bash
git tag -a v2.1.0-rc.1 -m "Release Candidate 2.1.0-rc.1"
git push origin v2.1.0-rc.1
```

5. Después de testing, si encuentras bug:

```bash
echo "# Fix menor pre-release" >> calculadora.py
git add calculadora.py
git commit -m "fix: corregir validación en seno"
```

6. Crea nuevo RC:

```bash
git tag -a v2.1.0-rc.2 -m "Release Candidate 2.1.0-rc.2"
git push origin v2.1.0-rc.2
```

7. Si RC2 pasa testing, lanza versión estable:

```bash
git switch main
git merge --no-ff release/2.1.0-rc.1 -m "release: versión 2.1.0"
git tag -a v2.1.0 -m "Release 2.1.0

Nuevas funcionalidades:
- Funciones trigonométricas (seno, coseno, tangente)
- Validación mejorada en todas las operaciones

Mejoras:
- Optimizaciones de rendimiento en cálculos

Correcciones:
- Fix en validación de seno
"

git push origin main --tags
```

8. Mergea de vuelta a develop:

```bash
git switch develop
git merge main
git push origin develop
```

9. Limpia:

```bash
git branch -d release/2.1.0-rc.1
```

10. Simula hotfix (PATCH):

```bash
git switch main
git switch -c hotfix/2.1.1

echo "# Hotfix crítico" >> calculadora.py
git add calculadora.py
git commit -m "fix: corregir división por cero en tangente 90°"

git switch main
git merge --no-ff hotfix/2.1.1
git tag -a v2.1.1 -m "Hotfix 2.1.1: Corregir tangente en 90 grados"
git push origin main --tags

git switch develop
git merge main
git push origin develop

git branch -d hotfix/2.1.1
```

11. Ve historial de versiones:

```bash
git tag -l "v2.*" | sort -V
```

**Resultado esperado:**

- Implementaste versionado semántico correctamente
- Usaste release candidates para testing
- Manejaste incrementos MAJOR, MINOR y PATCH apropiadamente
- El historial de tags refleja claramente las versiones

***

## 6.9 Automatización con Git Hooks

Git hooks son scripts que se ejecutan automáticamente en eventos específicos.

### Tipos de Hooks

**Client-side (local):**

- `pre-commit`: Antes de crear commit
- `prepare-commit-msg`: Antes de abrir editor de commit
- `commit-msg`: Validar mensaje de commit
- `post-commit`: Después de crear commit
- `pre-push`: Antes de push
- `post-checkout`: Después de checkout
- `post-merge`: Después de merge

**Server-side (remoto):**

- `pre-receive`: Antes de aceptar push
- `update`: Por cada branch pusheado
- `post-receive`: Después de aceptar push

### Ubicación

Hooks están en `.git/hooks/`. Git incluye ejemplos (`.sample`).

### EJERCICIO 28: Crear Hooks Útiles

**Objetivo:** Implementar hooks para automatizar validaciones.

**Pasos:**

**Parte A: Hook pre-commit para validar código**

1. Crea hook pre-commit:

```bash
cd ~/calculadora-python
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash

echo "Ejecutando validaciones pre-commit..."

# Verificar que archivos Python no tienen print() statements de debug
if git diff --cached --name-only | grep -q '\.py$'; then
    for file in $(git diff --cached --name-only | grep '\.py$'); do
        if grep -n "print(" "$file" | grep -v '"""' | grep -v "if __name__"; then
            echo "❌ Error: Encontrado print() de debug en $file"
            echo "Por favor remueve los print statements antes de commitear"
            exit 1
        fi
    done
fi

# Verificar sintaxis Python
echo "Verificando sintaxis Python..."
for file in $(git diff --cached --name-only | grep '\.py$'); do
    python3 -m py_compile "$file"
    if [ $? -ne 0 ]; then
        echo "❌ Error de sintaxis en $file"
        exit 1
    fi
done

echo "✅ Validaciones pre-commit pasaron"
exit 0
EOF

chmod +x .git/hooks/pre-commit
```

2. Prueba el hook (debería fallar):

```bash
echo 'print("debug info")' >> calculadora.py
git add calculadora.py
git commit -m "test: probar hook"
```

Debería rechazar el commit.

3. Revierte el cambio:

```bash
git restore --staged calculadora.py
git restore calculadora.py
```

4. Prueba commit válido:

```bash
echo "# Comentario válido" >> calculadora.py
git add calculadora.py
git commit -m "docs: agregar comentario"
```

Debería pasar.

**Parte B: Hook commit-msg para validar mensajes**

1. Crea hook commit-msg:

```bash
cat > .git/hooks/commit-msg << 'EOF'
#!/bin/bash

commit_msg=$(cat "$1")

# Verificar que sigue Conventional Commits
if ! echo "$commit_msg" | grep -qE "^(feat|fix|docs|style|refactor|perf|test|build|ci|chore)(\(.+\))?!?: .+"; then
    echo "❌ Mensaje de commit inválido"
    echo ""
    echo "El mensaje debe seguir Conventional Commits:"
    echo "tipo(ámbito opcional): descripción"
    echo ""
    echo "Tipos válidos: feat, fix, docs, style, refactor, perf, test, build, ci, chore"
    echo ""
    echo "Ejemplos:"
    echo "  feat: agregar nueva funcionalidad"
    echo "  fix(auth): corregir validación de token"
    echo "  docs: actualizar README"
    exit 1
fi

# Verificar longitud de primera línea
first_line=$(echo "$commit_msg" | head -n1)
if [ ${#first_line} -gt 72 ]; then
    echo "❌ Primera línea del commit muy larga (máximo 72 caracteres)"
    echo "Actual: ${#first_line} caracteres"
    exit 1
fi

echo "✅ Mensaje de commit válido"
exit 0
EOF

chmod +x .git/hooks/commit-msg
```

2. Prueba con mensaje inválido (debería fallar):

```bash
echo "# Otro comentario" >> README.md
git add README.md
git commit -m "cambios varios"
```

Debería rechazar.

3. Prueba con mensaje válido:

```bash
git commit -m "docs: actualizar README con ejemplos"
```

Debería pasar.

**Parte C: Hook pre-push para ejecutar tests**

1. Crea hook pre-push:

```bash
cat > .git/hooks/pre-push << 'EOF'
#!/bin/bash

echo "Ejecutando tests antes de push..."

# Ejecutar tests unitarios
python3 -m unittest test_calculadora.py 2>&1

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Tests fallaron. Push cancelado."
    echo "Arregla los tests antes de pushear."
    exit 1
fi

echo "✅ Tests pasaron. Procediendo con push."
exit 0
EOF

chmod +x .git/hooks/pre-push
```

2. Prueba el hook:

```bash
# Primero asegúrate de que tests pasan
python3 -m unittest test_calculadora.py
```

3. Intenta push:

```bash
git push origin develop
```

Si los tests pasan, el push procederá.

**Parte D: Compartir Hooks (usando directorio versionado)**

Los hooks en `.git/hooks/` no se versionan. Para compartirlos:

1. Crea directorio para hooks:

```bash
mkdir hooks
```

2. Mueve hooks al directorio versionado:

```bash
cp .git/hooks/pre-commit hooks/
cp .git/hooks/commit-msg hooks/
cp .git/hooks/pre-push hooks/
```

3. Crea script de instalación:

```bash
cat > hooks/install.sh << 'EOF'
#!/bin/bash

echo "Instalando Git hooks..."

HOOKS_DIR="$(git rev-parse --show-toplevel)/.git/hooks"
SCRIPT_DIR="$(git rev-parse --show-toplevel)/hooks"

cp "$SCRIPT_DIR/pre-commit" "$HOOKS_DIR/pre-commit"
cp "$SCRIPT_DIR/commit-msg" "$HOOKS_DIR/commit-msg"
cp "$SCRIPT_DIR/pre-push" "$HOOKS_DIR/pre-push"

chmod +x "$HOOKS_DIR/pre-commit"
chmod +x "$HOOKS_DIR/commit-msg"
chmod +x "$HOOKS_DIR/pre-push"

echo "✅ Hooks instalados correctamente"
EOF

chmod +x hooks/install.sh
```

4. Documenta en README:

```bash
cat >> README.md << 'EOF'

## Setup de Desarrollo

### Instalar Git Hooks

Para instalar los hooks de Git que validan código:

```bash
./hooks/install.sh
```

Esto instalará:
- pre-commit: Valida sintaxis Python
- commit-msg: Valida mensajes de commit (Conventional Commits)
- pre-push: Ejecuta tests antes de push
EOF

git add hooks/ README.md
git commit -m "chore: agregar Git hooks para validación automática"
```

**Resultado esperado:**

- Creaste hooks para validar código antes de commit
- Validaste mensajes de commit automáticamente
- Ejecutaste tests antes de push
- Compartiste hooks con el equipo de forma versionada

***

## Checkpoint: Parte 6

Antes de continuar, verifica que puedes:

- Explicar y usar Git Flow (main, develop, feature, release, hotfix)
- Entender GitHub Flow y cuándo usarlo
- Implementar Forking Workflow para open source
- Escribir commits semánticos (Conventional Commits)
- Crear Pull Requests efectivos
- Hacer code review constructivo
- Aplicar versionado semántico (MAJOR.MINOR.PATCH)
- Usar release candidates y tags de versión
- Crear y usar Git hooks para automatización
- Compartir hooks con el equipo

***

# PARTE 7: TÉCNICAS AVANZADAS Y DEBUGGING

## 7.1 Git Bisect: Encontrar Bugs con Búsqueda Binaria

Git bisect te ayuda a encontrar qué commit introdujo un bug usando búsqueda binaria.

### Cómo Funciona

```
Historial con bug:
C1 (✓) - C2 (✓) - C3 (✓) - C4 (✗) - C5 (✗) - C6 (✗)
                           ↑
                    Primer commit con bug

Git bisect hace búsqueda binaria:
1. Marca C6 como bad
2. Marca C1 como good
3. Prueba C3 (punto medio)
4. Según resultado, continúa en mitad correspondiente
5. Encuentra C4 como primer bad commit
```

### Uso Manual

```bash
# Iniciar bisect
git bisect start

# Marcar commit actual como malo
git bisect bad

# Marcar último commit bueno conocido
git bisect good abc1234

# Git hace checkout a commit intermedio
# Prueba si el bug existe

# Si el bug existe:
git bisect bad

# Si NO existe:
git bisect good

# Repetir hasta encontrar el primer bad commit

# Git dirá: "abc1234 is the first bad commit"

# Terminar bisect
git bisect reset
```

### Uso Automático

```bash
# Con script que retorna 0 si está bien, 1 si está mal
git bisect start
git bisect bad HEAD
git bisect good abc1234

git bisect run python3 test_script.py

# Git automáticamente encuentra el commit
git bisect reset
```

### EJERCICIO 29: Usar Git Bisect

**Objetivo:** Encontrar qué commit introdujo un bug usando bisect.

**Pasos:**

**Parte A: Crear Historial con Bug**

1. Crea serie de commits, uno con bug:

```bash
cd ~/calculadora-python
git switch develop
git switch -c feature-bisect-demo
```

2. Commit 1 (bueno):

```bash
cat >> calculadora.py << 'EOF'

def cuadrado(self, n):
    """Calcula el cuadrado de un número"""
    self.resultado = n * n
    return self.resultado
EOF

git add calculadora.py
git commit -m "feat: agregar función cuadrado"
```

3. Commit 2 (bueno):

```bash
cat >> calculadora.py << 'EOF'

def cubo(self, n):
    """Calcula el cubo de un número"""
    self.resultado = n * n * n
    return self.resultado
EOF

git add calculadora.py
git commit -m "feat: agregar función cubo"
```

4. Commit 3 (introduce bug):

```bash
cat >> calculadora.py << 'EOF'

def raiz_cubica(self, n):
    """Calcula la raíz cúbica - CON BUG"""
    # Bug intencional: debería ser n ** (1/3)
    self.resultado = n ** 3  # ESTO ESTÁ MAL
    return self.resultado
EOF

git add calculadora.py
git commit -m "feat: agregar función raíz cúbica"
```

5. Commit 4 (bueno, pero el bug persiste):

```bash
cat >> calculadora.py << 'EOF'

def potencia_n(self, base, exp):
    """Calcula base elevada a exponente n"""
    self.resultado = base ** exp
    return self.resultado
EOF

git add calculadora.py
git commit -m "feat: agregar potencia genérica"
```

6. Commit 5 (bueno):

```bash
cat >> test_calculadora.py << 'EOF'

    def test_cuadrado(self):
        resultado = self.calc.cuadrado(5)
        self.assertEqual(resultado, 25)
EOF

git add test_calculadora.py
git commit -m "test: agregar test de cuadrado"
```

**Parte B: Usar Bisect para Encontrar el Bug**

1. Crea script de prueba que detecta el bug:

```bash
cat > test_raiz_cubica.py << 'EOF'
#!/usr/bin/env python3
import sys
from calculadora import Calculadora

calc = Calculadora()

# Test: raíz cúbica de 8 debería ser 2
try:
    resultado = calc.raiz_cubica(8)
    if abs(resultado - 2.0) < 0.01:  # Permitir pequeño error de redondeo
        print("✓ Test pasó")
        sys.exit(0)
    else:
        print(f"✗ Test falló: esperado 2.0, obtenido {resultado}")
        sys.exit(1)
except AttributeError:
    # La función no existe en este commit
    print("✓ Función no existe aún (commit antes de introducir función)")
    sys.exit(0)
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)
EOF

chmod +x test_raiz_cubica.py
```

2. Verifica que el bug existe actualmente:

```bash
python3 test_raiz_cubica.py
```

Debería fallar.

3. Anota el hash del primer commit de esta serie:

```bash
git log --oneline | grep "agregar función cuadrado"
```

Copia ese hash (ejemplo: def5678).

4. Inicia bisect:

```bash
git bisect start
```

5. Marca HEAD como malo:

```bash
git bisect bad
```

6. Marca el commit antes de introducir las funciones como bueno:

```bash
git bisect good def5678^  # El ^ significa "commit anterior"
```

7. Git hará checkout a un commit intermedio. Prueba:

```bash
python3 test_raiz_cubica.py
```

8. Según el resultado:

```bash
# Si pasa:
git bisect good

# Si falla:
git bisect bad
```

9. Repite hasta que Git encuentre el commit culpable:

```
abc1234 is the first bad commit
commit abc1234
Author: Tu Nombre
Date: ...

    feat: agregar función raíz cúbica
```

10. Ve el commit problemático:

```bash
git show
```

Deberías ver claramente el bug: `n ** 3` en lugar de `n ** (1/3)`.

11. Termina bisect:

```bash
git bisect reset
```

12. Corrige el bug:

```bash
# Edita calculadora.py y corrige la función raiz_cubica
# Cambia:    self.resultado = n ** 3
# Por:       self.resultado = n ** (1/3)
```

Usa tu editor para hacer el cambio, luego:

```bash
git add calculadora.py
git commit -m "fix: corregir cálculo de raíz cúbica"
```

13. Verifica la corrección:

```bash
python3 test_raiz_cubica.py
```

Debería pasar ahora.

14. Limpia archivos de prueba:

```bash
rm test_raiz_cubica.py
git add -A
git commit -m "chore: limpiar archivos de prueba bisect"
```

**Resultado esperado:**

- Usaste bisect para encontrar el commit exacto que introdujo el bug
- Entiendes cómo bisect hace búsqueda binaria
- Sabes cómo automatizar bisect con scripts de prueba

***

## 7.2 Git Blame: Rastrear Cambios Línea por Línea

Git blame muestra quién modificó cada línea de un archivo y cuándo.

### Uso Básico

```bash
# Ver blame de archivo completo
git blame archivo.py

# Ver blame con formato más legible
git blame -s archivo.py  # Sin autor
git blame -e archivo.py  # Con email

# Ver blame de rango de líneas
git blame -L 10,20 archivo.py

# Ver blame ignorando whitespace
git blame -w archivo.py

# Ver blame desde cierto commit
git blame abc1234 archivo.py
```

### Formato de Salida

```
abc1234 (David García 2026-01-15 10:30:15 +0100  5)     def sumar(self, a, b):
def5678 (María López  2026-01-20 14:22:33 +0100  6)         """Suma dos números"""
def5678 (María López  2026-01-20 14:22:33 +0100  7)         self.resultado = a + b
abc1234 (David García 2026-01-15 10:30:15 +0100  8)         return self.resultado
```

Columnas:
- Hash del commit
- Autor
- Fecha
- Número de línea
- Contenido

### Comandos Relacionados

```bash
# Ver historial de una función específica
git log -L :nombre_funcion:archivo.py

# Ver quién movió/copió líneas
git blame -M archivo.py  # Detecta líneas movidas
git blame -C archivo.py  # Detecta líneas copiadas de otros archivos

# Ignorar commits específicos (ej: reformateo masivo)
git blame --ignore-rev abc1234 archivo.py

# Ignorar múltiples commits
cat > .git-blame-ignore-revs << EOF
# Reformateo con black
abc1234
# Cambio de tabs a espacios
def5678
EOF

git blame --ignore-revs-file .git-blame-ignore-revs archivo.py
```

### EJERCICIO 30: Investigar con Git Blame

**Objetivo:** Usar blame para rastrear el origen de código.

**Pasos:**

1. Ve el blame completo de calculadora.py:

```bash
cd ~/calculadora-python
git blame calculadora.py
```

2. Ve el blame de solo las primeras 20 líneas:

```bash
git blame -L 1,20 calculadora.py
```

3. Encuentra quién escribió la función `sumar`:

```bash
git blame calculadora.py | grep -A 5 "def sumar"
```

4. Ve el commit completo que introdujo esa línea:

```bash
# Copia el hash del commit
git show <hash-del-commit>
```

5. Ve el historial de la función `dividir`:

```bash
git log -L :dividir:calculadora.py
```

Esto muestra todos los cambios que afectaron específicamente esa función.

6. Crea un commit de reformateo (para simular cambio cosmético):

```bash
# Añade espacios en blanco (cambio cosmético)
sed -i 's/def /def  /g' calculadora.py
git add calculadora.py
git commit -m "style: ajustar espaciado en definiciones de funciones"

# Anota el hash de este commit
git log --oneline -1
```

7. Ve blame normal (incluye el reformateo):

```bash
git blame calculadora.py | head -20
```

Verás que muchas líneas ahora se atribuyen al commit de reformateo.

8. Ve blame ignorando ese commit:

```bash
git blame --ignore-rev <hash-reformateo> calculadora.py | head -20
```

Ahora las líneas se atribuyen a quien hizo el cambio real, no el reformateo.

9. Crea archivo para ignorar commits cosméticos permanentemente:

```bash
cat > .git-blame-ignore-revs << EOF
# Reformateo de funciones
<hash-reformateo>
EOF

git add .git-blame-ignore-revs
git commit -m "chore: agregar commits a ignorar en blame"
```

10. Configura Git para usar ese archivo automáticamente:

```bash
git config blame.ignoreRevsFile .git-blame-ignore-revs
```

11. Revierte el cambio cosmético para limpiar:

```bash
git revert HEAD~1 --no-edit
```

**Resultado esperado:**

- Sabes usar blame para encontrar quién cambió qué
- Puedes rastrear el historial de funciones específicas
- Entiendes cómo ignorar commits cosméticos en blame

***

## 7.3 Git Log Avanzado

### Búsquedas Complejas

```bash
# Commits que agregaron o eliminaron cierta palabra
git log -S "palabra_clave"

# Commits que cambiaron cierta expresión regular
git log -G "def.*suma"

# Commits que modificaron cierta función
git log -L :nombre_funcion:archivo.py

# Commits en un rango de fechas
git log --since="2 weeks ago" --until="yesterday"

# Commits de múltiples autores
git log --author="David\|María"

# Commits que NO son merges
git log --no-merges

# Solo merge commits
git log --merges

# Commits que tocaron ciertos archivos
git log -- "*.py" "*.js"
```

### Formatos Personalizados

```bash
# Log con estadísticas
git log --stat

# Log con diff completo
git log -p

# Log en una línea con más info
git log --pretty=format:"%h - %an, %ar : %s"

# Log con gráfico ASCII
git log --graph --oneline --all

# Log con fechas relativas
git log --pretty=format:"%h %ar - %s" --date=relative

# Log agrupado por autor
git shortlog

# Contar commits por autor
git shortlog -sn
```

### Analizar Cambios

```bash
# Ver archivos que cambiaron entre commits
git diff --name-only abc1234 def5678

# Ver estadísticas de cambios
git diff --stat abc1234 def5678

# Ver cambios en un archivo entre commits
git diff abc1234:archivo.py def5678:archivo.py

# Ver commits que afectaron un archivo
git log --follow archivo.py  # Sigue renames

# Ver cambios en directorio
git log -- src/
```

### EJERCICIO 31: Análisis de Repositorio

**Objetivo:** Usar log avanzado para análisis de proyecto.

**Pasos:**

1. Encuentra todos los commits que mencionan "validación":

```bash
git log --grep="validación" --oneline
```

2. Encuentra commits que agregaron la palabra "TypeError":

```bash
git log -S "TypeError" --oneline
```

3. Ve el commit completo:

```bash
git log -S "TypeError" -p
```

4. Encuentra cuántos commits hizo cada autor:

```bash
git shortlog -sn
```

5. Ve los commits de la última semana:

```bash
git log --since="1 week ago" --oneline
```

6. Ve estadísticas de archivos más modificados:

```bash
git log --pretty=format: --name-only | sort | uniq -c | sort -rg | head -10
```

7. Ve el historial completo de calculadora.py siguiendo renames:

```bash
git log --follow --oneline -- calculadora.py
```

8. Analiza actividad por día de la semana:

```bash
git log --pretty=format:"%ad" --date=format:"%A" | sort | uniq -c
```

9. Ve los 5 commits más recientes con diff:

```bash
git log -5 -p
```

10. Crea un reporte de cambios entre dos tags:

```bash
git log v2.0.0..v2.1.0 --pretty=format:"- %s (%an)" --no-merges
```

**Resultado esperado:**

- Puedes buscar commits por contenido, autor, fecha
- Sabes analizar la actividad del repositorio
- Puedes generar reportes de cambios
- Entiendes las opciones avanzadas de log

***

## 7.4 Git Reflog: El Salvavidas

Reflog registra TODOS los movimientos de HEAD, incluso los que no están en el historial normal.

### Cuándo Usar Reflog

- Recuperar commits "perdidos" después de reset
- Recuperar branches eliminados
- Ver dónde estuviste hace N operaciones
- Deshacer operaciones destructivas

### Comandos

```bash
# Ver reflog completo
git reflog

# Ver reflog de branch específico
git reflog show nombre-branch

# Ver reflog con timestamps
git reflog show --date=iso

# Ver últimas N entradas
git reflog -10

# Reflog de todos los branches
git reflog show --all
```

### Notación de Reflog

```bash
HEAD@{0}  # Posición actual
HEAD@{1}  # Una operación atrás
HEAD@{2}  # Dos operaciones atrás
HEAD@{yesterday}  # Ayer
HEAD@{2.hours.ago}  # Hace 2 horas
```

### EJERCICIO 32: Rescate con Reflog

**Objetivo:** Practicar recuperación de desastres con reflog.

**Pasos:**

**Parte A: Recuperar después de reset hard**

1. Crea algunos commits:

```bash
cd ~/calculadora-python
git switch develop

echo "# Cambio 1" >> calculadora.py
git commit -am "cambio 1"

echo "# Cambio 2" >> calculadora.py
git commit -am "cambio 2"

echo "# Cambio 3" >> calculadora.py
git commit -am "cambio 3"
```

2. Anota el hash del último commit:

```bash
git log --oneline -1
```

3. Simula desastre: reset hard 3 commits atrás:

```bash
git reset --hard HEAD~3
```

4. Verifica que los commits "desaparecieron":

```bash
git log --oneline -5
```

5. Usa reflog para encontrar los commits perdidos:

```bash
git reflog
```

Deberías ver algo como:

```
abc1234 HEAD@{0}: reset: moving to HEAD~3
def5678 HEAD@{1}: commit: cambio 3
ghi9012 HEAD@{2}: commit: cambio 2
jkl3456 HEAD@{3}: commit: cambio 1
```

6. Recupera los commits:

```bash
git reset --hard HEAD@{1}
```

7. Verifica que volvieron:

```bash
git log --oneline -3
```

**Parte B: Recuperar branch eliminado**

1. Crea un branch temporal:

```bash
git switch -c temporal-branch
echo "# Trabajo importante" >> importante.txt
git add importante.txt
git commit -m "trabajo importante"
```

2. Anota mentalmente el contenido o el hash:

```bash
git log --oneline -1
```

3. Vuelve a develop y elimina el branch:

```bash
git switch develop
git branch -D temporal-branch
```

4. Intenta acceder al branch (debería fallar):

```bash
git switch temporal-branch
```

5. Busca en reflog:

```bash
git reflog | grep "temporal-branch"
```

6. Recupera el branch:

```bash
# Encuentra el commit del branch en reflog
git branch temporal-recuperado <hash-del-commit>
```

7. Verifica la recuperación:

```bash
git switch temporal-recuperado
cat importante.txt
```

8. Limpia:

```bash
git switch develop
git branch -D temporal-recuperado
rm -f importante.txt
```

**Parte C: Ver historial de movimientos**

1. Ve dónde estabas hace 10 operaciones:

```bash
git reflog -10
```

2. Ve el estado del repositorio de hace 2 horas:

```bash
git reflog show HEAD@{2.hours.ago}
```

3. Ve todos los checkouts que hiciste:

```bash
git reflog | grep "checkout:"
```

**Resultado esperado:**

- Recuperaste commits después de reset hard
- Recuperaste un branch eliminado
- Entiendes que reflog es tu red de seguridad
- Sabes navegar el historial de operaciones

***

## 7.5 Git Cherry-Pick Avanzado

### Opciones Avanzadas

```bash
# Cherry-pick sin commitear automáticamente
git cherry-pick -n abc1234

# Cherry-pick editando el mensaje
git cherry-pick -e abc1234

# Cherry-pick de merge commit (especificar padre)
git cherry-pick -m 1 abc1234

# Cherry-pick de rango
git cherry-pick abc1234..def5678

# Cherry-pick resolviendo conflictos
git cherry-pick abc1234
# Si hay conflicto:
# Resolver conflicto
git add archivo.py
git cherry-pick --continue

# Abortar cherry-pick
git cherry-pick --abort
```

### EJERCICIO 33: Cherry-Pick Selectivo

**Objetivo:** Aplicar commits específicos entre branches.

**Pasos:**

1. Crea branch experimental con varios commits:

```bash
git switch develop
git switch -c experimental

echo "# Feature A" >> features.txt
git add features.txt
git commit -m "feat: implementar feature A"

echo "# Feature B (experimental)" >> features.txt
git commit -am "feat: implementar feature B experimental"

echo "# Feature C" >> features.txt
git commit -am "feat: implementar feature C"

echo "# Feature D (experimental)" >> features.txt
git commit -am "feat: implementar feature D experimental"
```

2. Anota los hashes:

```bash
git log --oneline -4
```

Identifica los hashes de Feature A y Feature C (los no experimentales).

3. Vuelve a develop:

```bash
git switch develop
```

4. Cherry-pick solo features A y C:

```bash
git cherry-pick <hash-feature-A>
git cherry-pick <hash-feature-C>
```

5. Verifica que solo esos commits están en develop:

```bash
git log --oneline -5
cat features.txt
```

Solo deberías ver Feature A y C, no B y D.

6. Limpia:

```bash
git branch -D experimental
rm -f features.txt
git add -A
git commit -m "chore: limpiar archivos experimentales"
```

**Resultado esperado:**

- Aplicaste commits selectivamente entre branches
- Entiendes cuándo cherry-pick es mejor que merge
- Sabes resolver conflictos durante cherry-pick

***

## 7.6 Git Submodules y Subtrees

### Git Submodules

Submodules permiten incluir otros repositorios Git dentro de tu repositorio.

```bash
# Agregar submodule
git submodule add https://github.com/usuario/libreria.git libs/libreria

# Clonar repositorio con submodules
git clone --recurse-submodules https://github.com/usuario/proyecto.git

# Inicializar submodules después de clonar
git submodule init
git submodule update

# Actualizar submodule
cd libs/libreria
git pull origin main
cd ../..
git add libs/libreria
git commit -m "chore: actualizar submodule libreria"

# Actualizar todos los submodules
git submodule update --remote

# Eliminar submodule
git submodule deinit libs/libreria
git rm libs/libreria
rm -rf .git/modules/libs/libreria
```

### Git Subtree

Alternativa a submodules, más simple pero menos flexible.

```bash
# Agregar subtree
git subtree add --prefix=libs/libreria https://github.com/usuario/libreria.git main --squash

# Actualizar subtree
git subtree pull --prefix=libs/libreria https://github.com/usuario/libreria.git main --squash

# Push de cambios al upstream del subtree
git subtree push --prefix=libs/libreria https://github.com/usuario/libreria.git main
```

### Submodules vs Subtrees

**Submodules:**
- Más complejo
- Referencias explícitas a commits
- Mejor para dependencias que rara vez cambias
- Mantiene historiales separados

**Subtrees:**
- Más simple
- Código se integra completamente
- Mejor si modificas la dependencia frecuentemente
- Historial combinado

***

## 7.7 Git Worktrees

Worktrees permiten tener múltiples working directories del mismo repositorio.

### Por Qué Usar Worktrees

- Trabajar en múltiples branches simultáneamente
- Revisar PRs sin perder trabajo actual
- Ejecutar tests en un branch mientras desarrollas en otro

### Comandos

```bash
# Crear worktree
git worktree add ../proyecto-feature feature-branch

# Listar worktrees
git worktree list

# Remover worktree
git worktree remove ../proyecto-feature

# Limpiar worktrees obsoletos
git worktree prune
```

### EJERCICIO 34: Usar Worktrees

**Objetivo:** Trabajar en múltiples branches simultáneamente.

**Pasos:**

1. Crea worktree para revisar código:

```bash
cd ~/calculadora-python
git worktree add ../calculadora-review develop
```

2. Verifica los worktrees:

```bash
git worktree list
```

3. Trabaja en el worktree principal:

```bash
# En ~/calculadora-python
git switch develop
echo "# Trabajo en main worktree" >> main-work.txt
git add main-work.txt
git commit -m "trabajo en main worktree"
```

4. Simultáneamente, revisa código en otro worktree:

```bash
cd ../calculadora-review
ls
# Verás los mismos archivos pero en develop branch
```

5. Haz cambios en el worktree de review:

```bash
echo "# Review notes" >> review-notes.txt
git add review-notes.txt
git commit -m "agregar notas de review"
```

6. Vuelve al worktree principal:

```bash
cd ~/calculadora-python
```

7. Ve los cambios del otro worktree:

```bash
git log --oneline -3
```

8. Limpia el worktree:

```bash
git worktree remove ../calculadora-review
```

9. Limpia archivos de prueba:

```bash
rm -f main-work.txt review-notes.txt
git add -A
git commit -m "chore: limpiar archivos de prueba"
```

**Resultado esperado:**

- Trabajaste en múltiples branches simultáneamente
- No perdiste contexto cambiando de branch
- Entiendes cuándo worktrees son útiles

***

## 7.8 Optimización y Mantenimiento

### Limpiar Repositorio

```bash
# Ver tamaño del repositorio
du -sh .git

# Limpiar objetos innecesarios
git gc

# Limpiar agresivamente
git gc --aggressive --prune=now

# Ver objetos grandes
git rev-list --objects --all \
  | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' \
  | sed -n 's/^blob //p' \
  | sort --numeric-sort --key=2 \
  | tail -10

# Remover archivo del historial completo (DESTRUCTIVO)
git filter-repo --path archivo-grande.bin --invert-paths

# Verificar integridad
git fsck --full
```

### Configuración de Performance

```bash
# Habilitar cache de credenciales
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=3600'

# Habilitar parallel fetch
git config --global fetch.parallel 0

# Habilitar rebase.autostash
git config --global rebase.autostash true

# Habilitar rerere (reuse recorded resolution)
git config --global rerere.enabled true
```

### EJERCICIO 35: Mantenimiento del Repositorio

**Objetivo:** Optimizar y limpiar el repositorio.

**Pasos:**

1. Ve el tamaño actual:

```bash
cd ~/calculadora-python
du -sh .git
```

2. Ejecuta garbage collection:

```bash
git gc
```

3. Ve el nuevo tamaño:

```bash
du -sh .git
```

4. Verifica integridad:

```bash
git fsck --full
```

5. Habilita configuraciones de performance:

```bash
git config rebase.autostash true
git config rerere.enabled true
```

6. Verifica la configuración:

```bash
git config --list | grep -E "(autostash|rerere)"
```

**Resultado esperado:**

- El repositorio está optimizado
- Configuraste opciones de performance
- Entiendes el mantenimiento básico de Git

***

## Checkpoint: Parte 7

Antes de continuar, verifica que puedes:

- Usar `git bisect` para encontrar commits que introducen bugs
- Usar `git blame` para rastrear cambios línea por línea
- Hacer búsquedas avanzadas con `git log`
- Recuperar commits perdidos con `git reflog`
- Aplicar commits selectivamente con `git cherry-pick`
- Entender submodules y subtrees
- Usar worktrees para múltiples branches
- Mantener y optimizar repositorios

***

# PARTE 8: MEJORES PRÁCTICAS Y TIPS PROFESIONALES

## 8.1 Estructura de Mensajes de Commit

### Template de Commit Completo

```
tipo(ámbito): descripción corta (máx 50 caracteres)

Cuerpo detallado explicando QUÉ y POR QUÉ (no cómo).
Envolver en ~72 caracteres.

Puede tener múltiples párrafos.

- Listas con viñetas también funcionan
- Típicamente para enumerar cambios relacionados

Resolves: #123
See also: #456, #789
```

### Configurar Template

```bash
# Crear template
cat > ~/.gitmessage << 'EOF'
# tipo(ámbito): descripción corta

# Cuerpo (opcional)

# Footer (opcional)
# Resolves: #
# See also: #

# Tipos: feat, fix, docs, style, refactor, perf, test, build, ci, chore
# Ámbito: componente afectado (opcional)
EOF

# Configurar Git para usar template
git config --global commit.template ~/.gitmessage
```

### EJERCICIO 36: Commits Profesionales

**Objetivo:** Practicar escritura de commits de calidad profesional.

**Pasos:**

1. Configura el template:

```bash
git config --global commit.template ~/.gitmessage
```

2. Haz un cambio complejo:

```bash
cd ~/calculadora-python
git switch develop

# Implementa feature compleja
cat >> calculadora.py << 'EOF'

def ecuacion_cuadratica(self, a, b, c):
    """
    Resuelve ecuación cuadrática ax² + bx + c = 0
    
    Returns:
        tuple: (x1, x2) las dos soluciones, o (x,) si hay una solución única
    
    Raises:
        ValueError: Si no tiene soluciones reales
    """
    import math
    
    if a == 0:
        raise ValueError("'a' no puede ser cero en ecuación cuadrática")
    
    discriminante = b**2 - 4*a*c
    
    if discriminante < 0:
        raise ValueError("La ecuación no tiene soluciones reales")
    elif discriminante == 0:
        x = -b / (2*a)
        self.resultado = x
        return (x,)
    else:
        sqrt_disc = math.sqrt(discriminante)
        x1 = (-b + sqrt_disc) / (2*a)
        x2 = (-b - sqrt_disc) / (2*a)
        self.resultado = (x1, x2)
        return self.resultado
EOF

git add calculadora.py
```

3. Haz commit usando el template:

```bash
git commit
```

El editor se abrirá con el template. Llénalo:

```
feat(calculadora): implementar resolución de ecuaciones cuadráticas

Agrega método para resolver ecuaciones de la forma ax² + bx + c = 0.
El método calcula las raíces usando la fórmula cuadrática y maneja
apropiadamente los casos de discriminante cero, positivo y negativo.

La implementación incluye:
- Validación de que 'a' no sea cero
- Cálculo del discriminante
- Manejo de casos sin soluciones reales
- Retorno de una o dos soluciones según corresponda

Esta funcionalidad fue solicitada por usuarios para aplicaciones
en física y matemáticas avanzadas.

Resolves: #142
See also: #98
```

4. Agrega tests con commit igualmente detallado:

```bash
cat >> test_calculadora.py << 'EOF'

    def test_ecuacion_cuadratica_dos_soluciones(self):
        """Test con discriminante positivo"""
        x1, x2 = self.calc.ecuacion_cuadratica(1, -5, 6)
        self.assertAlmostEqual(x1, 3.0)
        self.assertAlmostEqual(x2, 2.0)
    
    def test_ecuacion_cuadratica_una_solucion(self):
        """Test con discriminante cero"""
        x, = self.calc.ecuacion_cuadratica(1, -4, 4)
        self.assertAlmostEqual(x, 2.0)
    
    def test_ecuacion_cuadratica_sin_soluciones(self):
        """Test con discriminante negativo"""
        with self.assertRaises(ValueError):
            self.calc.ecuacion_cuadratica(1, 0, 1)
    
    def test_ecuacion_cuadratica_a_cero(self):
        """Test con a=0 (no es cuadrática)"""
        with self.assertRaises(ValueError):
            self.calc.ecuacion_cuadratica(0, 2, 1)
EOF

git add test_calculadora.py
git commit
```

Mensaje:

```
test(calculadora): agregar tests comprehensivos para ecuación cuadrática

Cubre todos los casos edge:
- Discriminante positivo (dos soluciones)
- Discriminante cero (una solución)
- Discriminante negativo (sin soluciones reales)
- Coeficiente 'a' igual a cero (caso inválido)

La cobertura de tests para esta funcionalidad es del 100%.
```

5. Ve el historial con mensajes completos:

```bash
git log -2
```

**Resultado esperado:**

- Tus commits tienen mensajes descriptivos y profesionales
- Explican QUÉ, POR QUÉ y contexto
- Facilitan entender cambios meses después

***

## 8.2 Estrategias de Branching

### Nomenclatura de Branches

**Por tipo:**
```
feature/nombre-descriptivo
bugfix/descripcion-del-bug
hotfix/numero-version-problema
release/numero-version
docs/que-se-documenta
refactor/que-se-refactoriza
test/que-se-testea
```

**Por ticket:**
```
feature/JIRA-123-login-oauth
bugfix/ISSUE-456-memory-leak
```

**Por autor (equipos pequeños):**
```
david/implementar-api
maria/refactor-database
```

### Duración de Branches

**Branches de corta duración (recomendado):**
- Máximo 2-3 días
- Máximo 400 líneas de cambio
- Integrar frecuentemente

**Branches de larga duración (evitar):**
- Solo para releases o features muy grandes
- Sincronizar diariamente con main
- Considerar feature flags en su lugar

***

## 8.3 Code Review Checklist

### Para el Autor del PR

**Antes de crear PR:**

```bash
# Actualizar con main
git fetch origin
git rebase origin/main

# Ejecutar tests
./run-tests.sh

# Verificar que no hay debug code
git diff origin/main | grep -i "console.log\|print(\|debugger"

# Verificar calidad de commits
git log origin/main..HEAD --oneline

# Si commits están sucios, limpiar con rebase interactivo
git rebase -i origin/main
```

**Checklist del PR:**

- [ ] Tests pasan
- [ ] Código linted (sin warnings)
- [ ] Documentación actualizada
- [ ] CHANGELOG actualizado
- [ ] Sin código comentado
- [ ] Sin TODOs sin issue asociado
- [ ] Sin merge conflicts
- [ ] Branch actualizado con main
- [ ] Commits limpios y descriptivos
- [ ] Screenshots si hay cambios UI

### Para el Reviewer

**Checklist de Review:**

- [ ] Código cumple estándares del proyecto
- [ ] Lógica es correcta
- [ ] Tests son suficientes
- [ ] Sin problemas de seguridad evidentes
- [ ] Sin problemas de performance
- [ ] Nombres de variables/funciones claros
- [ ] Complejidad apropiada
- [ ] Documentación adecuada
- [ ] Manejo de errores correcto
- [ ] Sin código duplicado

***

## 8.4 Configuración Avanzada

### Archivo .gitattributes

Controla cómo Git maneja ciertos archivos:

```bash
cat > .gitattributes << 'EOF'
# Auto detect text files and normalize line endings
* text=auto

# Force LF for these
*.sh text eol=lf
*.py text eol=lf

# Force CRLF for these
*.bat text eol=crlf

# Binary files
*.png binary
*.jpg binary
*.pdf binary

# Diff personalizado para archivos específicos
*.json diff=json
*.py diff=python

# No diff para archivos grandes
*.min.js -diff
*.min.css -diff

# Linguist (GitHub) - excluir de estadísticas
vendor/* linguist-vendored
docs/* linguist-documentation
EOF

git add .gitattributes
git commit -m "chore: configurar gitattributes"
```

### Configuración Útil

```bash
# Colorear diff moved code
git config --global diff.colorMoved zebra

# Auto-correct typos
git config --global help.autocorrect 1

# Default branch name
git config --global init.defaultBranch main

# Faster status on large repos
git config --global core.untrackedCache true
git config --global core.fsmonitor true

# Better merge conflict style
git config --global merge.conflictstyle zdiff3

# Prune on fetch
git config --global fetch.prune true

# Rebase por default en pull
git config --global pull.rebase true
```

***

## 8.5 Aliases Poderosos

### Aliases Recomendados

```bash
# Guardar en ~/.gitconfig o configurar con git config

[alias]
    # Status y información
    st = status -sb
    s = status
    
    # Log y historial
    lg = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
    ll = log --oneline --graph --all
    last = log -1 HEAD --stat
    dl = "!git ll -1"
    
    # Diff
    d = diff
    ds = diff --staged
    dc = diff --cached
    
    # Commit
    ci = commit
    ca = commit -am
    amend = commit --amend --no-edit
    
    # Checkout y branch
    co = checkout
    cob = checkout -b
    br = branch
    brd = branch -d
    brD = branch -D
    
    # Pull y push
    pl = pull
    ps = push
    psf = push --force-with-lease
    
    # Rebase
    rb = rebase
    rbi = rebase -i
    rbc = rebase --continue
    rba = rebase --abort
    
    # Stash
    sl = stash list
    sa = stash apply
    ss = stash save
    sp = stash pop
    
    # Reset y revert
    unstage = reset HEAD --
    undo = reset --soft HEAD^
    
    # Utilidades
    aliases = config --get-regexp alias
    contributors = shortlog -sn
    whoami = "!git config user.name && git config user.email"
    
    # Limpieza
    cleanup = "!git branch --merged | grep -v '\\*\\|main\\|develop' | xargs -n 1 git branch -d"
    prune-all = "!git remote | xargs -n 1 git remote prune"
    
    # Búsqueda
    find = "!git ls-files | grep -i"
    grep = grep -Ii
    
    # Tracking
    track = "!f() { git branch --set-upstream-to=origin/$1 $1; }; f"
    
    # Pretty formats
    overview = log --all --oneline --no-merges
    recap = log --all --oneline --no-merges --author=\"$(git config user.email)\"
```

### Instalar Aliases

```bash
# Desde archivo
cat >> ~/.gitconfig << 'EOF'
# Pegar aliases aquí
EOF

# O uno por uno
git config --global alias.st "status -sb"
```

***

## 8.6 Troubleshooting Común

### Problemas y Soluciones

**Problema: Commitear en branch equivocado**

```bash
# Deshacer último commit pero mantener cambios
git reset HEAD~1

# Cambiar al branch correcto
git switch branch-correcto

# Volver a commitear
git add .
git commit -m "mensaje"
```

**Problema: Olvidaste agregar archivo en commit**

```bash
git add archivo-olvidado.txt
git commit --amend --no-edit
```

**Problema: Mensaje de commit con typo**

```bash
git commit --amend -m "mensaje corregido"
```

**Problema: Push rechazado**

```bash
# Si alguien pusheó antes que tú
git pull --rebase
git push

# Si reescribiste historial y estás seguro
git push --force-with-lease
```

**Problema: Merge conflicts complicados**

```bash
# Abortar y empezar de nuevo
git merge --abort

# O usar herramienta visual
git mergetool
```

**Problema: Borrar commits accidentalmente**

```bash
# Encontrar commit en reflog
git reflog

# Recuperar
git reset --hard HEAD@{N}
```

**Problema: Archivo grande commiteado por error**

```bash
# Si no has pusheado
git reset --soft HEAD~1
git restore --staged archivo-grande.bin
rm archivo-grande.bin
echo "archivo-grande.bin" >> .gitignore
git add .gitignore
git commit -m "ignorar archivo grande"

# Si ya pusheaste (requiere reescribir historial)
git filter-repo --path archivo-grande.bin --invert-paths
git push --force
```

***

## 8.7 Recursos y Siguientes Pasos

### Herramientas Recomendadas

**GUI Clients:**
- GitKraken (multiplataforma, visual)
- SourceTree (gratuito, potente)
- GitHub Desktop (simple, ideal para principiantes)
- Git Fork (rápido y elegante)

**Extensiones de Editor:**
- VSCode: GitLens, Git Graph
- JetBrains IDEs: integración nativa excelente
- Vim: vim-fugitive
- Emacs: Magit

**Herramientas CLI:**
- `tig`: Navegador de texto para Git
- `lazygit`: TUI simple para Git
- `diff-so-fancy`: Diffs más legibles
- `git-extras`: Comandos extra útiles

### Práctica Continua

**Proyectos para practicar:**

1. **Contribuir a Open Source:**
   - Busca proyectos con etiqueta "good first issue"
   - Practica fork workflow
   - Aprende de code reviews

2. **Crear tu propio proyecto:**
   - Implementa Git Flow completo
   - Configura CI/CD
   - Practica releases y hotfixes

3. **Laboratorio de desastres:**
   - Crea escenarios de problemas
   - Practica recuperación
   - Domina reflog y reset

### Documentación Oficial

- Git Documentation: https://git-scm.com/doc
- Pro Git Book: https://git-scm.com/book/en/v2
- GitHub Guides: https://guides.github.com
- GitLab Documentation: https://docs.gitlab.com

***

## Resumen Final

Has completado un tutorial comprehensivo de Git que cubre:

**Fundamentos:**
- Instalación y configuración
- Objetos Git internos
- Estados y áreas de trabajo

**Operaciones Básicas:**
- Commits, diff, log
- Deshacer cambios
- .gitignore

**Branches y Merging:**
- Crear y gestionar branches
- Merge y resolución de conflictos
- Fast-forward vs three-way merge

**Rebase y Historial:**
- Rebase simple e interactivo
- Cherry-pick
- Reescritura de historial

**Repositorios Remotos:**
- Clone, fetch, pull, push
- Branches remotos
- Tags y releases
- Stash

**Workflows Profesionales:**
- Git Flow
- GitHub Flow
- Trunk-based development
- Conventional Commits
- Code review

**Técnicas Avanzadas:**
- Bisect y blame
- Reflog y recuperación
- Submodules y worktrees
- Optimización

**Mejores Prácticas:**
- Mensajes de commit profesionales
- Configuración avanzada
- Aliases productivos
- Troubleshooting

***

## Certificación de Conocimientos

Si puedes hacer lo siguiente sin consultar documentación, dominas Git:

- [ ] Explicar cómo Git almacena datos (blobs, trees, commits)
- [ ] Crear repositorio e historial limpio con commits semánticos
- [ ] Trabajar con múltiples branches y mergear sin problemas
- [ ] Resolver conflictos de merge complejos
- [ ] Usar rebase para mantener historial lineal
- [ ] Recuperar trabajo perdido con reflog
- [ ] Implementar Git Flow completo
- [ ] Crear y revisar Pull Requests profesionales
- [ ] Usar bisect para encontrar bugs
- [ ] Configurar hooks para automatización
- [ ] Troubleshoot problemas comunes
