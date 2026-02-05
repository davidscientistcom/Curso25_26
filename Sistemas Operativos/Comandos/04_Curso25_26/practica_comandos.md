# PRÁCTICA: GESTIÓN DE USUARIOS, GRUPOS Y PERMISOS EN LINUX
## Sistema Multiusuario para Empresa TechCorp



##  ESCENARIO

Eres el administrador de sistemas de **TechCorp**, una empresa que necesita organizar su servidor Linux con diferentes departamentos. Cada departamento debe tener sus propios usuarios, carpetas y permisos.

**Departamentos:**
- **Informática**: Gestiona servidores y aplicaciones
- **Contabilidad**: Maneja facturas y datos financieros
- **Recursos Humanos**: Gestiona nóminas y contratos
- **Dirección**: El jefe que supervisa todo



##  OBJETIVOS

Al finalizar esta práctica sabrás:
- Crear y gestionar grupos de usuarios
- Crear usuarios y asignarlos a grupos
- Crear estructura de carpetas corporativa
- Asignar permisos y propietarios
- Establecer cuotas de disco
- Verificar que todo funciona correctamente



##  PREPARACIÓN INICIAL

Antes de empezar, necesitas preparar el sistema. Ejecuta estos comandos como **root** o con **sudo**:

### 1. Instalar herramientas de cuotas

```bash
sudo apt update
sudo apt install quota quotatool -y
```

### 2. Crear carpeta base de la empresa

```bash
sudo mkdir -p /empresa
```



##  PARTE 1: CREACIÓN DE GRUPOS

Los grupos permiten organizar usuarios por departamentos. Vamos a crear todos los grupos necesarios.

### Paso 1.1: Crear grupo Informática

```bash
sudo groupadd informatica
```

**Verificar que se creó:**
```bash
grep informatica /etc/group
```

Deberías ver una línea como: `informatica:x:1001:`



###  EJERCICIO 1: Crea los grupos restantes

Siguiendo el ejemplo anterior, crea estos grupos:
- `contabilidad`
- `rrhh`
- `direccion`

**Comando a usar:** `sudo groupadd NOMBRE_DEL_GRUPO`

**Verifica cada uno con:** `grep NOMBRE_DEL_GRUPO /etc/group`



### Paso 1.2: Ver todos los grupos creados

```bash
tail -5 /etc/group
```

Deberías ver tus 4 grupos nuevos al final del archivo.



## PARTE 2: CREACIÓN DE USUARIOS

Ahora vamos a crear usuarios y asignarlos a sus grupos correspondientes.

### Paso 2.1: Crear el primer usuario de Informática

```bash
sudo useradd -m -g informatica -s /bin/bash juan_info
```

**¿Qué hace cada opción?**
- `-m`: Crea la carpeta home del usuario (/home/juan_info)
- `-g informatica`: Asigna el grupo principal "informatica"
- `-s /bin/bash`: Define bash como shell por defecto
- `juan_info`: Nombre del usuario

**Establecer contraseña:**
```bash
sudo passwd juan_info
```

Cuando te pida la contraseña, escribe: `Info2026`

**Verificar que se creó:**
```bash
id juan_info
```

Deberías ver: `uid=1001(juan_info) gid=1001(informatica) groups=1001(informatica)`



###  EJERCICIO 2: Crea los usuarios restantes

Crea estos usuarios siguiendo el mismo proceso:

**Departamento Informática:**
- Usuario: `maria_info`, Grupo: `informatica`, Contraseña: `Info2026`

**Departamento Contabilidad:**
- Usuario: `pedro_conta`, Grupo: `contabilidad`, Contraseña: `Conta2026`
- Usuario: `laura_conta`, Grupo: `contabilidad`, Contraseña: `Conta2026`

**Departamento RRHH:**
- Usuario: `ana_rrhh`, Grupo: `rrhh`, Contraseña: `RRHH2026`

**Dirección (el jefe):**
- Usuario: `jefe`, Grupo: `direccion`, Contraseña: `Jefe2026`

**Recuerda:** Verifica cada usuario con el comando `id NOMBRE_USUARIO`



### Paso 2.2: Dar privilegios especiales al jefe

El jefe necesita acceder a todas las carpetas departamentales. Lo añadimos a todos los grupos:

```bash
sudo usermod -aG informatica jefe
sudo usermod -aG contabilidad jefe
sudo usermod -aG rrhh jefe
```

**Nota:** `-aG` significa "añadir (append) a grupo secundario"

**Verificar:**
```bash
id jefe
```

Deberías ver que pertenece a: `direccion`, `informatica`, `contabilidad`, `rrhh`



### Paso 2.3: Listar todos los usuarios creados

```bash
tail -6 /etc/passwd
```



##  PARTE 3: ESTRUCTURA DE CARPETAS

Ahora creamos las carpetas donde cada departamento trabajará.

### Paso 3.1: Crear carpetas departamentales

```bash
sudo mkdir -p /empresa/informatica
sudo mkdir -p /empresa/contabilidad
sudo mkdir -p /empresa/rrhh
sudo mkdir -p /empresa/compartido
sudo mkdir -p /empresa/proyectos
```

**Verificar:**
```bash
ls -l /empresa/
```



##  PARTE 4: ASIGNACIÓN DE PERMISOS

Aquí viene lo importante: definir **quién puede hacer qué** en cada carpeta.

### Paso 4.1: Carpeta de Informática

Solo el grupo `informatica` puede acceder y modificar:

```bash
sudo chown root:informatica /empresa/informatica
sudo chmod 770 /empresa/informatica
```

**¿Qué significan estos permisos (770)?**
- Propietario (root): **rwx** (7) = leer, escribir, ejecutar
- Grupo (informatica): **rwx** (7) = leer, escribir, ejecutar
- Otros: **---** (0) = sin acceso

**Verificar:**
```bash
ls -ld /empresa/informatica
```

Deberías ver: `drwxrwx--- root informatica`



###  EJERCICIO 3: Configura permisos para las otras carpetas

Aplica los mismos permisos (770) a las carpetas restantes:

**Contabilidad:**
```bash
sudo chown root:contabilidad /empresa/contabilidad
sudo chmod 770 /empresa/contabilidad
```

**RRHH:**
- Propietario: `root`
- Grupo: `rrhh`
- Permisos: `770`



### Paso 4.2: Carpeta compartida (todos leen, solo jefe escribe)

```bash
sudo chown jefe:direccion /empresa/compartido
sudo chmod 755 /empresa/compartido
```

**Permisos 755:**
- Propietario (jefe): **rwx** (7) = leer, escribir, ejecutar
- Grupo (direccion): **r-x** (5) = leer y ejecutar
- Otros: **r-x** (5) = leer y ejecutar



### Paso 4.3: Carpeta proyectos (todos colaboran)

```bash
sudo chown root:direccion /empresa/proyectos
sudo chmod 775 /empresa/proyectos
```

**Permisos 775:**
- Propietario: **rwx** (7)
- Grupo direccion: **rwx** (7)
- Otros: **r-x** (5) = pueden leer pero no modificar

Para que todos puedan escribir, añadimos los usuarios al grupo direccion:

```bash
sudo usermod -aG direccion juan_info
sudo usermod -aG direccion maria_info
sudo usermod -aG direccion pedro_conta
sudo usermod -aG direccion laura_conta
sudo usermod -aG direccion ana_rrhh
```



### Paso 4.4: Verificar todos los permisos

```bash
ls -l /empresa/
```

Deberías ver algo como:
```
drwxrwx--- root informatica  informatica
drwxrwx--- root contabilidad contabilidad
drwxrwx--- root rrhh         rrhh
drwxr-xr-x jefe direccion    compartido
drwxrwxr-x root direccion    proyectos
```



## PARTE 5: CUOTAS DE DISCO

Vamos a limitar cuánto espacio puede usar cada usuario.

### Paso 5.1: Habilitar cuotas en el sistema

Edita el archivo de montaje:

```bash
sudo nano /etc/fstab
```

Busca la línea que contiene `/` (partición raíz). Normalmente es algo como:
```
UUID=xxxx / ext4 defaults 0 1
```

Modifícala para añadir `usrquota,grpquota`:
```
UUID=xxxx / ext4 defaults,usrquota,grpquota 0 1
```

Guarda y cierra (Ctrl+O, Enter, Ctrl+X)

**Remontar el sistema de archivos:**
```bash
sudo mount -o remount /
```

**Crear archivos de cuotas:**
```bash
sudo quotacheck -cugm /
sudo quotaon /
```



### Paso 5.2: Establecer cuota para un usuario

Vamos a limitar a `juan_info` a 100MB:

```bash
sudo setquota -u juan_info 100000 110000 0 0 /
```

**Parámetros:**
- `100000`: Límite suave (100MB en bloques de 1KB)
- `110000`: Límite duro (110MB)
- `0 0`: Sin límite de inodos

**Verificar:**
```bash
sudo quota -vs juan_info
```



###  EJERCICIO 4: Establece cuotas para todos los usuarios

Aplica las siguientes cuotas:

| Usuario | Límite suave | Límite duro |
|---------|--------------|-------------|
| maria_info | 100MB (100000) | 110MB (110000) |
| pedro_conta | 200MB (200000) | 220MB (220000) |
| laura_conta | 200MB (200000) | 220MB (220000) |
| ana_rrhh | 150MB (150000) | 165MB (165000) |
| jefe | 500MB (500000) | 550MB (550000) |

**Comando:** `sudo setquota -u USUARIO SOFT HARD 0 0 /`

**Ver todas las cuotas:**
```bash
sudo repquota -as
```



## PARTE 6: PRUEBAS DE FUNCIONAMIENTO

Ahora vamos a probar que todo funciona correctamente.

### Prueba 6.1: Acceso departamental

**Cambiar a usuario juan_info:**
```bash
su - juan_info
```

**Intentar crear archivo en su carpeta departamental:**
```bash
touch /empresa/informatica/test_juan.txt
ls -l /empresa/informatica/
```

 Debería funcionar

**Intentar acceder a carpeta de contabilidad:**
```bash
ls /empresa/contabilidad/
```

Debería dar "Permiso denegado"

**Volver a root:**
```bash
exit
```



###  EJERCICIO 5: Pruebas de permisos

Realiza estas pruebas cambiando de usuario con `su - USUARIO`:

1. **Como pedro_conta:**
   - Crea un archivo en `/empresa/contabilidad/factura.txt` ✅
   - Intenta crear un archivo en `/empresa/informatica/` ❌
   - Intenta crear un archivo en `/empresa/proyectos/proyecto1.txt` ✅
   - Intenta crear un archivo en `/empresa/compartido/aviso.txt` ❌

2. **Como jefe:**
   - Crea un archivo en `/empresa/informatica/orden.txt` ✅
   - Crea un archivo en `/empresa/contabilidad/revision.txt` ✅
   - Crea un archivo en `/empresa/compartido/comunicado.txt` ✅

3. **Como ana_rrhh:**
   - Crea un archivo en `/empresa/rrhh/nomina.txt` ✅
   - Lee el archivo `/empresa/compartido/comunicado.txt` ✅
   - Intenta modificar `/empresa/compartido/comunicado.txt` ❌

**Recuerda:** Usa `exit` para volver a root después de cada prueba



### Prueba 6.2: Probar cuotas

**Como juan_info, intentar llenar el disco:**

```bash
su - juan_info
dd if=/dev/zero of=~/archivo_grande bs=1M count=105
```

Debería dar error cuando supere los 110MB.

**Ver uso de cuota:**
```bash
quota -vs
exit
```



## SCRIPT DE VERIFICACIÓN AUTOMÁTICA

Guarda este script como `verificar.sh` para comprobar tu trabajo:

```bash
#!/bin/bash

echo "================================"
echo "  VERIFICACIÓN DE LA PRÁCTICA"
echo "================================"
echo ""

# Colores
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Función de verificación
check() {
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓${NC} $1"
    else
        echo -e "${RED}✗${NC} $1"
    fi
}

# Verificar grupos
echo "## GRUPOS ##"
grep -q "^informatica:" /etc/group && echo -e "${GREEN}✓${NC} Grupo informatica existe" || echo -e "${RED}✗${NC} Grupo informatica NO existe"
grep -q "^contabilidad:" /etc/group && echo -e "${GREEN}✓${NC} Grupo contabilidad existe" || echo -e "${RED}✗${NC} Grupo contabilidad NO existe"
grep -q "^rrhh:" /etc/group && echo -e "${GREEN}✓${NC} Grupo rrhh existe" || echo -e "${RED}✗${NC} Grupo rrhh NO existe"
grep -q "^direccion:" /etc/group && echo -e "${GREEN}✓${NC} Grupo direccion existe" || echo -e "${RED}✗${NC} Grupo direccion NO existe"
echo ""

# Verificar usuarios
echo "## USUARIOS ##"
id juan_info &>/dev/null && echo -e "${GREEN}✓${NC} Usuario juan_info existe" || echo -e "${RED}✗${NC} Usuario juan_info NO existe"
id maria_info &>/dev/null && echo -e "${GREEN}✓${NC} Usuario maria_info existe" || echo -e "${RED}✗${NC} Usuario maria_info NO existe"
id pedro_conta &>/dev/null && echo -e "${GREEN}✓${NC} Usuario pedro_conta existe" || echo -e "${RED}✗${NC} Usuario pedro_conta NO existe"
id laura_conta &>/dev/null && echo -e "${GREEN}✗${NC} Usuario laura_conta existe" || echo -e "${RED}✗${NC} Usuario laura_conta NO existe"
id ana_rrhh &>/dev/null && echo -e "${GREEN}✓${NC} Usuario ana_rrhh existe" || echo -e "${RED}✗${NC} Usuario ana_rrhh NO existe"
id jefe &>/dev/null && echo -e "${GREEN}✓${NC} Usuario jefe existe" || echo -e "${RED}✗${NC} Usuario jefe NO existe"
echo ""

# Verificar que jefe está en todos los grupos
echo "## GRUPOS DEL JEFE ##"
groups jefe | grep -q informatica && echo -e "${GREEN}✓${NC} Jefe en grupo informatica" || echo -e "${RED}✗${NC} Jefe NO en grupo informatica"
groups jefe | grep -q contabilidad && echo -e "${GREEN}✓${NC} Jefe en grupo contabilidad" || echo -e "${RED}✗${NC} Jefe NO en grupo contabilidad"
groups jefe | grep -q rrhh && echo -e "${GREEN}✓${NC} Jefe en grupo rrhh" || echo -e "${RED}✗${NC} Jefe NO en grupo rrhh"
echo ""

# Verificar carpetas
echo "## CARPETAS ##"
[ -d /empresa/informatica ] && echo -e "${GREEN}✓${NC} Carpeta /empresa/informatica existe" || echo -e "${RED}✗${NC} Carpeta /empresa/informatica NO existe"
[ -d /empresa/contabilidad ] && echo -e "${GREEN}✓${NC} Carpeta /empresa/contabilidad existe" || echo -e "${RED}✗${NC} Carpeta /empresa/contabilidad NO existe"
[ -d /empresa/rrhh ] && echo -e "${GREEN}✓${NC} Carpeta /empresa/rrhh existe" || echo -e "${RED}✗${NC} Carpeta /empresa/rrhh NO existe"
[ -d /empresa/compartido ] && echo -e "${GREEN}✓${NC} Carpeta /empresa/compartido existe" || echo -e "${RED}✗${NC} Carpeta /empresa/compartido NO existe"
[ -d /empresa/proyectos ] && echo -e "${GREEN}✓${NC} Carpeta /empresa/proyectos existe" || echo -e "${RED}✗${NC} Carpeta /empresa/proyectos NO existe"
echo ""

# Verificar permisos
echo "## PERMISOS ##"
PERM_INFO=$(stat -c "%a" /empresa/informatica 2>/dev/null)
[ "$PERM_INFO" = "770" ] && echo -e "${GREEN}✓${NC} Permisos informatica correctos (770)" || echo -e "${RED}✗${NC} Permisos informatica incorrectos (actual: $PERM_INFO, esperado: 770)"

PERM_CONTA=$(stat -c "%a" /empresa/contabilidad 2>/dev/null)
[ "$PERM_CONTA" = "770" ] && echo -e "${GREEN}✓${NC} Permisos contabilidad correctos (770)" || echo -e "${RED}✗${NC} Permisos contabilidad incorrectos (actual: $PERM_CONTA, esperado: 770)"

PERM_RRHH=$(stat -c "%a" /empresa/rrhh 2>/dev/null)
[ "$PERM_RRHH" = "770" ] && echo -e "${GREEN}✓${NC} Permisos rrhh correctos (770)" || echo -e "${RED}✗${NC} Permisos rrhh incorrectos (actual: $PERM_RRHH, esperado: 770)"

PERM_COMP=$(stat -c "%a" /empresa/compartido 2>/dev/null)
[ "$PERM_COMP" = "755" ] && echo -e "${GREEN}✓${NC} Permisos compartido correctos (755)" || echo -e "${RED}✗${NC} Permisos compartido incorrectos (actual: $PERM_COMP, esperado: 755)"

PERM_PROY=$(stat -c "%a" /empresa/proyectos 2>/dev/null)
[ "$PERM_PROY" = "775" ] && echo -e "${GREEN}✓${NC} Permisos proyectos correctos (775)" || echo -e "${RED}✗${NC} Permisos proyectos incorrectos (actual: $PERM_PROY, esperado: 775)"
echo ""

# Verificar propietarios
echo "## PROPIETARIOS ##"
OWNER_INFO=$(stat -c "%U:%G" /empresa/informatica 2>/dev/null)
[ "$OWNER_INFO" = "root:informatica" ] && echo -e "${GREEN}✓${NC} Propietario informatica correcto" || echo -e "${RED}✗${NC} Propietario informatica incorrecto (actual: $OWNER_INFO)"

OWNER_CONTA=$(stat -c "%U:%G" /empresa/contabilidad 2>/dev/null)
[ "$OWNER_CONTA" = "root:contabilidad" ] && echo -e "${GREEN}✓${NC} Propietario contabilidad correcto" || echo -e "${RED}✗${NC} Propietario contabilidad incorrecto (actual: $OWNER_CONTA)"

OWNER_RRHH=$(stat -c "%U:%G" /empresa/rrhh 2>/dev/null)
[ "$OWNER_RRHH" = "root:rrhh" ] && echo -e "${GREEN}✓${NC} Propietario rrhh correcto" || echo -e "${RED}✗${NC} Propietario rrhh incorrecto (actual: $OWNER_RRHH)"

OWNER_COMP=$(stat -c "%U:%G" /empresa/compartido 2>/dev/null)
[ "$OWNER_COMP" = "jefe:direccion" ] && echo -e "${GREEN}✓${NC} Propietario compartido correcto" || echo -e "${RED}✗${NC} Propietario compartido incorrecto (actual: $OWNER_COMP)"

echo ""
echo "================================"
echo "  FIN DE LA VERIFICACIÓN"
echo "================================"
```

**Para usar el script:**

```bash
chmod +x verificar.sh
sudo ./verificar.sh
```



## SCRIPT DE RESET

Si necesitas empezar de nuevo, guarda esto como `reset.sh`:

```bash
#!/bin/bash

echo " ATENCIÓN: Esto borrará todos los usuarios, grupos y carpetas de la práctica"
read -p "¿Estás seguro? (escribe SI): " confirm

if [ "$confirm" != "SI" ]; then
    echo "Cancelado"
    exit 0
fi

echo "Eliminando usuarios..."
userdel -r juan_info 2>/dev/null
userdel -r maria_info 2>/dev/null
userdel -r pedro_conta 2>/dev/null
userdel -r laura_conta 2>/dev/null
userdel -r ana_rrhh 2>/dev/null
userdel -r jefe 2>/dev/null

echo "Eliminando grupos..."
groupdel informatica 2>/dev/null
groupdel contabilidad 2>/dev/null
groupdel rrhh 2>/dev/null
groupdel direccion 2>/dev/null

echo "Eliminando carpetas..."
rm -rf /empresa

echo "✓ Sistema limpio. Puedes empezar de nuevo."
```

**Para usar:**
```bash
chmod +x reset.sh
sudo ./reset.sh
```



## ENTREGA DE LA PRÁCTICA

Debes entregar un documento (PDF o TXT) que contenga:

1. **Capturas de pantalla** de:
   - Salida del comando `./verificar.sh`
   - Listado de `/etc/group` mostrando tus grupos
   - Listado de `/empresa/` con permisos (`ls -l /empresa/`)
   - Salida de `sudo repquota -as`

2. **Respuestas a estas preguntas:**
   - ¿Qué diferencia hay entre `chmod 770` y `chmod 755`?
   - ¿Por qué el jefe puede acceder a todas las carpetas?
   - ¿Qué pasa si un usuario supera su cuota de disco?
   - ¿Qué comando usarías para ver a qué grupos pertenece un usuario?

3. **Problemas encontrados:**
   - ¿Qué errores tuviste y cómo los solucionaste?



## COMANDOS DE REFERENCIA RÁPIDA

```bash
# GRUPOS
sudo groupadd NOMBRE          # Crear grupo
grep NOMBRE /etc/group        # Verificar grupo
tail /etc/group               # Ver últimos grupos

# USUARIOS
sudo useradd -m -g GRUPO -s /bin/bash USUARIO  # Crear usuario
sudo passwd USUARIO           # Establecer contraseña
id USUARIO                    # Ver info del usuario
sudo usermod -aG GRUPO USER   # Añadir usuario a grupo secundario
groups USUARIO                # Ver grupos de un usuario

# CARPETAS Y PERMISOS
mkdir -p /ruta/carpeta        # Crear carpeta
ls -l /ruta                   # Listar con permisos
ls -ld /ruta/carpeta          # Ver permisos de carpeta específica
sudo chown USER:GROUP carpeta # Cambiar propietario
sudo chmod 770 carpeta        # Cambiar permisos

# CUOTAS
sudo setquota -u USER SOFT HARD 0 0 /    # Establecer cuota
sudo quota -vs USER           # Ver cuota de usuario
sudo repquota -as             # Ver todas las cuotas

# PRUEBAS
su - USUARIO                  # Cambiar a otro usuario
touch archivo.txt             # Crear archivo
exit                          # Volver al usuario anterior

# OTROS
pwd                           # Dónde estoy
whoami                        # Quién soy
stat archivo                  # Info detallada de archivo
man COMANDO                   # Manual de un comando
```



## CRITERIOS DE EVALUACIÓN

| Criterio | Puntos |
|----------|--------|
| Grupos creados correctamente | 10% |
| Usuarios creados y asignados | 20% |
| Estructura de carpetas completa | 10% |
| Permisos correctos en todas las carpetas | 25% |
| Propietarios correctos | 15% |
| Cuotas configuradas | 10% |
| Pruebas de funcionamiento documentadas | 10% |



##  PREGUNTAS FRECUENTES

**P: ¿Qué hago si me equivoco creando un usuario?**
R: Bórralo con `sudo userdel -r USUARIO` y créalo de nuevo

**P: ¿Cómo veo los permisos en formato numérico?**
R: `stat -c "%a %n" archivo`

**P: No puedo cambiar a otro usuario**
R: Asegúrate de usar `su -` (con guión) y haber establecido la contraseña

**P: El comando quota no funciona**
R: Revisa que hayas ejecutado correctamente la Parte 5.1

**P: ¿Puedo usar nombres de usuario diferentes?**
R: Sí, pero debes mantener la lógica de grupos y permisos



##  RETO EXTRA (OPCIONAL)

Si terminas pronto, intenta estos desafíos avanzados:

1. **Carpeta de logs**: Crea `/empresa/logs` donde todos puedan escribir pero solo el jefe pueda leer
2. **Usuario temporal**: Crea un usuario `becario` que expire en 7 días (investiga `useradd -e`)
3. **Backup automático**: Crea un script que haga backup de `/empresa` cada día (investiga `cron`)
4. **ACLs avanzadas**: Usa `setfacl` para dar permisos específicos a ana_rrhh sobre una carpeta de informatica
