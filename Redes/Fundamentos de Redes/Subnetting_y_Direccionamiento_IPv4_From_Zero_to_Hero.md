# Subnetting y Direccionamiento IPv4 — *From Zero to Hero*

> **Propósito**: Este documento (apuntes para el alumno) te lleva **desde cero** hasta ser capaz de **diseñar y configurar redes IPv4 sencillas**, crear **subredes (subnetting)**, comprender **máscaras/prefijos**, elegir **puertas de enlace**, y **conectar redes con uno o más routers** (incluyendo enlaces punto a punto entre routers).  
> **Qué conseguirás al terminar**: podrás **proponer un plan de direccionamiento**, **calcular redes/broadcast/rangos**, **dividir un bloque en subredes (VLSM)** y **encaminar** entre redes con **rutas estáticas** básicas.

---

## 0) Mapa de ruta (lo que vas a aprender)
1. **Fundamentos de IPv4**: qué es una IP, máscara, prefijo CIDR, red, broadcast, hosts y gateway.
2. **Tipos de direcciones**: públicas, privadas, especiales (loopback, enlace local/APIPA, default).
3. **Subnetting paso a paso**: métodos prácticos de cálculo (incremento de bloque, binario ligero), tabla de referencia.
4. **Ejemplos esenciales**: varios cálculos de redes de distinto tamaño.
5. **VLSM (Subnetting variable)**: diseño realista asignando por necesidades.
6. **Routers y rutas**: cómo une redes un router, enlaces /30 y /31, rutas estáticas y por defecto.
7. **Casos resueltos (complejos)**: tres escenarios completos con diagramas y pasos.
8. **Verificación y troubleshooting**: checklist, comandos típicos, errores frecuentes.
9. **Apéndices**: tablas de prefijos/hosts, binario de referencia, plantillas y diagramas (ASCII + Mermaid).

---

## 1) Fundamentos de IPv4

### 1.1 ¿Qué es una dirección IP?
- Una **IP (IPv4)** identifica de forma única a un **host** en una **red**. Formato habitual: **decimal con puntos**, ej. `192.168.10.25`. Internamente son **32 bits** (4 octetos).
- Una IP se compone de **parte de red** y **parte de host**. La **máscara** indica dónde acaba la red y dónde empieza el host.

### 1.2 Máscara y prefijo CIDR
- **Máscara** en decimal: `255.255.255.0` (ej.).  
- **Prefijo CIDR**: `/24` (equivale a `255.255.255.0`).  
- **Idea**: los bits a `1` (en la máscara) marcan la **red**; los bits a `0`, los **hosts**.
- **Dirección de red**: la **primera** dirección del bloque (todos los bits de host a 0).
- **Broadcast**: la **última** dirección del bloque (todos los bits de host a 1).
- **Rango de hosts**: entre **red+1** y **broadcast−1**.

> **Regla de oro**: En cada subred hay **2 direcciones reservadas**: red y broadcast. Las **útiles** son el resto.

### 1.3 Puerta de enlace (gateway por defecto)
- Es la **IP del router** dentro de tu subred por donde **saldrá el tráfico** hacia otras redes.  
- En una red `192.168.10.0/24`, podrías elegir `192.168.10.1` como **gateway** (no es obligatorio, pero es típico).

---

## 2) Tipos de direcciones IPv4 útiles en la vida real

- **Privadas (RFC1918)**: no ruteables en Internet, para redes internas.
  - `10.0.0.0/8` (10.x.x.x)
  - `172.16.0.0/12` (172.16.0.0–172.31.255.255)
  - `192.168.0.0/16` (192.168.x.x)
- **Públicas**: ruteables en Internet.
- **Loopback**: `127.0.0.0/8` (habitual `127.0.0.1`) — “yo mismo”.
- **Enlace local (APIPA)**: `169.254.0.0/16` — aparece si falla DHCP en redes locales.
- **Default route / dirección comodín**: `0.0.0.0`.
- **Broadcast limitado**: `255.255.255.255` (no se usa en routing normal).

---

## 3) Subnetting (dividir redes) — *paso a paso*

### 3.1 ¿Qué es subnetting?
- Es **dividir** un bloque de direcciones en **subredes más pequeñas**.  
- Sirve para **organizar**, **aislar** y **aprovechar** mejor la IP. Ej.: separar usuarios, servidores, IoT, etc.

### 3.2 Métodos prácticos de cálculo
**A) Método del “incremento de bloque”**
- Encuentra el **octeto relevante** (donde no es 255 ni 0 total) en la máscara.
- **Incremento = 256 − ese octeto**. Ese es el **salto** entre redes.
- Las **redes comienzan** en múltiplos del incremento en ese octeto.
- **Ejemplo**: `/26` → máscara `255.255.255.192` → octeto relevante: `192` → incremento **64**.  
  Redes: `.0, .64, .128, .192`. Cada subred tiene **64** direcciones (62 hosts útiles).

**B) “Powers of two” (potencias de dos)**
- Número de **hosts útiles** ≈ `2^(bits_host) − 2`.  
- **Bits host** = `32 − prefijo`.  
- Útil para elegir el **prefijo mínimo** según necesidades.

**C) “Binario ligero” (cuando el límite cae entre octetos)**
- Si el prefijo corta el tercer o cuarto octeto, **localiza el bit** que define el incremento:
  - Bits de host en el **octavo** (LSB) valen: 128, 64, 32, 16, 8, 4, 2, 1.
  - El **incremento** es el valor del primer bit de host en ese octeto.
  - Ej.: `/23` → máscara `255.255.254.0` → incremento **2** en el **tercer** octeto (…`x.0.0`, `x.2.0`, `x.4.0`…).

### 3.3 Tabla rápida de referencia (más comunes)

| Prefijo | Máscara              | # Dir totales | Hosts útiles | Incremento (octeto relevante) |
|--------:|----------------------|---------------|--------------|-------------------------------|
| /30     | 255.255.255.252      | 4             | 2            | 4 en 4º octeto                |
| /29     | 255.255.255.248      | 8             | 6            | 8 en 4º octeto                |
| /28     | 255.255.255.240      | 16            | 14           | 16 en 4º octeto               |
| /27     | 255.255.255.224      | 32            | 30           | 32 en 4º octeto               |
| /26     | 255.255.255.192      | 64            | 62           | 64 en 4º octeto               |
| /25     | 255.255.255.128      | 128           | 126          | 128 en 4º octeto              |
| /24     | 255.255.255.0        | 256           | 254          | 1 en 3º octeto (siguiente)    |
| /23     | 255.255.254.0        | 512           | 510          | 2 en 3º octeto                |
| /22     | 255.255.252.0        | 1024          | 1022         | 4 en 3º octeto                |
| /21     | 255.255.248.0        | 2048          | 2046         | 8 en 3º octeto                |

> **Tip**: Para enlaces router–router usa **/30** (2 hosts) o **/31** (RFC 3021, 2 hosts sin red/broadcast tradicional).

---

## 4) Ejemplos esenciales (cálculo de red/broadcast/hosts)

> Siempre: **1)** Identifica máscara/prefijo. **2)** Calcula **incremento** y **red** más cercana. **3)** Obtén **broadcast** (red + tamaño − 1). **4)** Rango de **hosts** = (red+1) … (broadcast−1).

### Ejemplo 1 — `192.168.10.130/26`
- `/26` → máscara `255.255.255.192` → **incremento 64** (en 4º octeto).  
- Redes: `.0, .64, .128, .192`.  
- `130` cae en **.128** a **.191**.  
- **Red**: `192.168.10.128`  
- **Broadcast**: `192.168.10.191`  
- **Hosts**: `192.168.10.129–192.168.10.190` (62 hosts).

### Ejemplo 2 — `172.16.5.200/23`
- `/23` → máscara `255.255.254.0` → incremento **2** en **3er octeto**.  
- Bloques en 3er octeto: `…4.0`–`…5.255` (porque 4 es par, 6 sería el siguiente bloque).  
- **Red**: `172.16.4.0`  
- **Broadcast**: `172.16.5.255`  
- **Hosts**: `172.16.4.1–172.16.5.254` (510 hosts).

### Ejemplo 3 — `10.12.200.77/28`
- `/28` → máscara `255.255.255.240` → incremento **16** en 4º octeto.  
- Redes: `.0, .16, .32, …, .240`. `77` cae en **.64–.79**.  
- **Red**: `10.12.200.64`  
- **Broadcast**: `10.12.200.79`  
- **Hosts**: `10.12.200.65–10.12.200.78` (14 hosts).

### Ejemplo 4 — `192.168.100.9/30` (enlace p2p router–router)
- `/30` → máscara `255.255.255.252` → incremento **4**.  
- Rango: `.8–.11`.  
- **Red**: `192.168.100.8`  
- **Broadcast**: `192.168.100.11`  
- **IPs válidas**: `192.168.100.9` y `192.168.100.10` (2 hosts).

### Ejemplo 5 — **/31** para enlaces (avanzado)
- `/31` (máscara `255.255.255.254`) **ahorra IPs** en enlaces punto a punto.  
- No hay red/broadcast “clásicos”; las **2 direcciones** son **válidas** para los extremos.  
- Ej.: `10.0.0.0/31` → hosts: `10.0.0.0` y `10.0.0.1` (solo para **p2p**).

---

## 5) VLSM: Subnetting por necesidades reales

**VLSM (Variable Length Subnet Mask)** = usar **máscaras de distintos tamaños** dentro de un bloque, **ajustando** a cada necesidad para **no desperdiciar** IPs.

**Proceso recomendado:**
1. **Lista de subredes** necesarias con **hosts requeridos** (incluye crecimiento futuro si quieres margen).
2. **Ordena** de mayor a menor **tamaño** (la más grande primero).
3. **Asigna** bloques contiguos **sin solaparse**, respetando tamaños (potencias de 2).
4. Documenta **red, broadcast, hosts, gateway** de cada subred.
5. Reserva bloques pequeños **/30 o /31** para **enlaces entre routers**.

**Mini–tabla de tamaño mínimo (hosts → prefijo mínimo):**
- 2 hosts → `/30` (o `/31` p2p)
- 6 hosts → `/29`
- 14 hosts → `/28`
- 30 hosts → `/27`
- 62 hosts → `/26`
- 126 hosts → `/25`
- 254 hosts → `/24`
- etc.

---

## 6) Routers y rutas: uniendo subredes

### 6.1 ¿Qué hace un router?
- **Conecta redes distintas**. Un host en `192.168.10.0/24` no “ve” directamente a `192.168.20.0/24` sin un router que **reenvíe** el tráfico.
- Cada interfaz del router está en **una subred** distinta y tiene **su IP** dentro de esa subred (actúa como **gateway** para esa red).

### 6.2 Dos subredes con **un solo router**
```
LAN A (192.168.10.0/24)        Router R1         LAN B (192.168.20.0/24)
PCs → 192.168.10.100           [Gi0/0=192.168.10.1]    PCs → 192.168.20.50
GW  → 192.168.10.1     <---->  [Gi0/1=192.168.20.1]    GW  → 192.168.20.1
```
- **Puertas de enlace** de cada LAN apuntan a la **IP del router** en su subred.
- El router **conoce** ambas rutas por estar **conectadas directamente**.

### 6.3 **Dos routers** conectados por un enlace p2p
```
LAN A (192.168.10.0/24)          R1                R2          LAN B (192.168.20.0/24)
GW A: 192.168.10.1           [S0/0=10.0.0.1/30]--[S0/0=10.0.0.2/30]           GW B: 192.168.20.1
                              (enlace /30: 10.0.0.0/30)
```
- **R1** conoce 192.168.10.0/24 (directa) y 10.0.0.0/30 (directa), pero **no** 192.168.20.0/24.
- **R2** conoce 192.168.20.0/24 y 10.0.0.0/30, pero **no** 192.168.10.0/24.
- Solución: **rutas estáticas** cruzadas.
  - En **R1**: ruta a `192.168.20.0/24` **vía 10.0.0.2**.
  - En **R2**: ruta a `192.168.10.0/24` **vía 10.0.0.1**.

> **Ruta por defecto (default route)**: si una red no está en la tabla, envíala a un **gateway de última salida** (0.0.0.0/0 → siguiente salto). Muy útil para “salir a Internet” por un router borde.

### 6.4 Enlaces /31 (ahorro de IPs)
- En p2p puedes usar `/31`. Ej.: `10.0.0.4/31` (hosts: `.4` y `.5`).  
- Requiere que el equipo soporte RFC 3021. En muchos routers modernos es estándar.

---

## 7) **Casos resueltos (complejos)**

### Caso 1 — **Pyme con /24 y 3 LAN + 1 enlace WAN**
**Requisitos** (hosts útiles mínimos):
- Admin: **60** → `/26` (62 hosts)
- Ventas: **30** → `/27` (30 hosts exacto, pero recuerda 30 útiles; ok)
- IoT: **12** → `/28` (14 hosts)
- Enlace R1–R2: **p2p** → `/30`

**Bloque asignado**: `192.168.50.0/24`

**Ordenamos por tamaño** y **asignamos** dentro del /24:
1) **/26** (incremento 64): redes posibles `…0, …64, …128, …192`
   - **Admin** → `192.168.50.0/26`  
     - Red: `192.168.50.0` | Broadcast: `192.168.50.63` | Hosts: `.1–.62` | **GW**: `.1`
2) **/27** (incremento 32): siguientes libres dentro del /24 tras usar `.0–.63` → `…64, …96, …128, …160, …192, …224`
   - **Ventas** → `192.168.50.64/27`  
     - Red: `192.168.50.64` | Bc: `192.168.50.95` | Hosts: `.65–.94` | **GW**: `.65`
3) **/28** (incremento 16): libres tras `…64/27` → `…96, …112, …128, …144, …160, …176, …192, …208, …224, …240`
   - **IoT** → `192.168.50.96/28`  
     - Red: `192.168.50.96` | Bc: `192.168.50.111` | Hosts: `.97–.110` | **GW**: `.97`
4) **/30** (incremento 4): reservar por fuera (otro bloque privado) o **dentro** del mismo /24 si cabe. Entra sin problema.
   - **R1–R2 p2p** → `192.168.50.112/30`  
     - Red: `192.168.50.112` | Bc: `192.168.50.115` | Hosts: `.113` y `.114`  
     - **R1 S0/0 = .113** | **R2 S0/0 = .114**

> **Resumen de asignación** (lo restante del /24 queda libre para futuro):
- Admin `192.168.50.0/26` (GW .1)  
- Ventas `192.168.50.64/27` (GW .65)  
- IoT `192.168.50.96/28` (GW .97)  
- Enlace R1–R2 `192.168.50.112/30` (R1 .113, R2 .114)

**Diagrama (ASCII)**:
```
LAN Admin (50.0/26) --GW .1--+
                             | Gi0/0 R1
LAN Ventas (50.64/27) --GW .65--+        R1 S0/0 50.113  ── p2p ── 50.114 S0/0 R2
                                \__________________________/
LAN IoT (50.96/28) --GW .97--+
```

**Rutas estáticas** (conceptuales):
- **R1** debe llegar a las LAN “del otro lado” si existen; en este caso, si **R2** tiene otra LAN (añade más abajo), desde R1: `ip route RED_R2 MASK via 192.168.50.114`.
- **R2** debe llegar a las LAN de R1:  
  - a `192.168.50.0/26` vía `192.168.50.113`  
  - a `192.168.50.64/27` vía `192.168.50.113`  
  - a `192.168.50.96/28` vía `192.168.50.113`  
  (O una **ruta resumida** si encaja; aquí no todas son contiguas en el mismo prefijo.)

> **Variación**: si quieres que todo lo que **no sea local** en R2 vaya hacia R1 (salida a Internet simulada), pon en **R2** una **ruta por defecto** `0.0.0.0/0 via 192.168.50.113`.

---

### Caso 2 — **Campus con /22, 5 subredes dispares y 2 enlaces entre 3 routers**

**Bloque asignado**: `10.20.0.0/22` (1024 direcciones, 1022 hosts útiles; abarca `10.20.0.0–10.20.3.255`).

**Necesidades** (hosts útiles):
- Aulas: **200** → `/24` (254)
- Laboratorios: **120** → `/25` (126)
- Administración: **60** → `/26` (62)
- IoT: **25** → `/27` (30)
- Invitados: **10** → `/28` (14)
- Enlaces: **2 p2p** → `/30` y `/30` (o `/31` y `/31`)

**Orden y asignación** (de mayor a menor, sin solaparse):
1) **Aulas /24** → `10.20.0.0/24`  
   - Red: `10.20.0.0` | Bc: `10.20.0.255` | Hosts: `.1–.254` | **GW**: `.1`
2) **Laboratorios /25** → siguiente bloque libre grande dentro del /22: `10.20.1.0/25`  
   - Red: `10.20.1.0` | Bc: `10.20.1.127` | Hosts: `.1–.126` | **GW**: `.1`
3) **Administración /26** → `10.20.1.128/26`  
   - Red: `10.20.1.128` | Bc: `10.20.1.191` | Hosts: `.129–.190` | **GW**: `.129`
4) **IoT /27** → `10.20.1.192/27`  
   - Red: `10.20.1.192` | Bc: `10.20.1.223` | Hosts: `.193–.222` | **GW**: `.193`
5) **Invitados /28** → `10.20.1.224/28`  
   - Red: `10.20.1.224` | Bc: `10.20.1.239` | Hosts: `.225–.238` | **GW**: `.225`
6) **Enlace R1–R2 /30** → `10.20.1.240/30` (hosts `.241` y `.242`)  
7) **Enlace R2–R3 /30** → `10.20.1.244/30` (hosts `.245` y `.246`)

> **Libre para futuro**: `10.20.2.0/23` entero (mucho margen).

**Topología (ASCII)**:
```
   Aulas (10.20.0.0/24)        R1                R2              R3
        GW .1              .241/30   .242    .245/30   .246
                            |   p2p R1-R2     |   p2p R2-R3
                            |                 |
                    Admin (10.20.1.128/26)    IoT (10.20.1.192/27)
                    GW .129                   GW .193
                    Labs (10.20.1.0/25)      Invitados (10.20.1.224/28)
                    GW .1                     GW .225
```

**Rutas (conceptuales)**:
- Cada router conoce sus **directamente conectadas**. Para el resto:
  - En **R1**: rutas hacia subredes de R2/R3 vía `10.20.1.242`.
  - En **R2**: rutas hacia subredes de R1 vía `10.20.1.241`, y hacia subredes de R3 vía `10.20.1.246`.
  - En **R3**: rutas hacia subredes de R1/R2 vía `10.20.1.245`.
- **Opción resumen** (si fueran contiguas): agrupar bloques para reducir entradas de ruta.

---

### Caso 3 — **Triángulo de routers con enlaces /31 y 2 LAN** (ahorro máximo)

**Objetivo**: unir **R1–R2–R3** en triángulo usando **/31** (2 direcciones por enlace), y agregar dos LAN en R1 y R3.

**Bloque p2p**: `172.16.100.0/30` (para ejemplo, pero usaremos /31 dentro)
- **R1–R2**: `172.16.100.0/31` → hosts: `.0` y `.1`
- **R2–R3**: `172.16.100.2/31` → hosts: `.2` y `.3`
- **R3–R1**: `172.16.100.4/31` → hosts: `.4` y `.5`

**LANs**:
- LAN R1: `192.168.10.0/24` (GW `192.168.10.1`)
- LAN R3: `192.168.30.0/24` (GW `192.168.30.1`)

**Topología (ASCII)**:
```
      172.16.100.0/31                 172.16.100.2/31
R1 .0 ---------------- R2 .1      R2 .2 --------------- R3 .3
  \                                          /
   \___________ 172.16.100.4/31 ____________/ 
            R1 .4                      R3 .5

LAN R1: 192.168.10.0/24 (GW 192.168.10.1)      LAN R3: 192.168.30.0/24 (GW 192.168.30.1)
```

**Rutas**:
- En **R1**: para llegar a `192.168.30.0/24`, next-hop cualquiera de los dos vecinos (e.g. `172.16.100.1` **o** `172.16.100.5`). En equipos avanzados podrías añadir dos rutas (redundancia).
- En **R2**: rutas hacia LAN R1 (`via 172.16.100.0`) y LAN R3 (`via 172.16.100.3`).
- En **R3**: ruta hacia LAN R1 (`via 172.16.100.4`).

> **Notas /31**: solo para **punto a punto**. Ahorra 50% de IPs frente a /30. Requiere soporte RFC 3021 (común en routers modernos).

---

## 8) Verificación y troubleshooting

**Checklist rápido**:
1. **IP del host** pertenece al **rango** de la subred correcta.
2. **Máscara** del host coincide con la de la subred.
3. **Gateway** del host = IP del **router en esa subred**.
4. El **router** tiene **ruta** hacia la red de destino (directa, estática o por defecto).
5. **Solapamientos**: no hay dos subredes que se pisen.
6. **Enlaces p2p**: prefijos correctos (/30 o /31) en **ambos extremos**.
7. **Pruebas**:
   - `ping` a **tu gateway** (debe responder).
   - `ping` a un **host remoto** en otra subred.
   - `traceroute` para ver por dónde pasa y dónde se corta.
8. Si falla: revisa **tabla de rutas**, **máscaras** y **IPs** (el 90% de errores está ahí).

**Comandos típicos (orientativos)**:
- Ver IP en host: `ipconfig` (Windows), `ip a` / `ifconfig` (Linux).
- Añadir ruta estática en router (concepto): `ip route <red> <máscara> <next-hop>`
- Mostrar tabla de rutas: `show ip route` (routers), `route print`/`ip route` (SO).

**Errores comunes**:
- Elegir **gateway** de otra subred (no funciona).
- **Máscara** incorrecta (host queda fuera de su red real).
- Enlazar routers con **/24** desperdiciando direcciones (mejor /30 o /31).
- **Rutas** ausentes o mal orientadas (next-hop mal).
- **Solapamiento** de subredes en VLSM.

---

## 9) Apéndices

### 9.1 Tabla ampliada de prefijos
| / | Máscara             | # dirs | Hosts | Incremento | Uso típico                         |
|--:|---------------------|--------|-------|------------|------------------------------------|
| /32 | 255.255.255.255   | 1      | 1     | N/A        | Host individual (loopback, rutas)  |
| /31 | 255.255.255.254   | 2      | 2(*)  | 2          | Enlaces p2p (RFC 3021)             |
| /30 | 255.255.255.252   | 4      | 2     | 4          | Enlace p2p clásico                  |
| /29 | 255.255.255.248   | 8      | 6     | 8          | Equipos muy pocos                   |
| /28 | 255.255.255.240   | 16     | 14    | 16         | Pequeñas LAN/IoT                    |
| /27 | 255.255.255.224   | 32     | 30    | 32         | LAN pequeña                         |
| /26 | 255.255.255.192   | 64     | 62    | 64         | LAN media                           |
| /25 | 255.255.255.128   | 128    | 126   | 128        | LAN grande                          |
| /24 | 255.255.255.0     | 256    | 254   | 1 3er oct. | Segmento típico de campus           |
| /23 | 255.255.254.0     | 512    | 510   | 2 3er oct. | Dos /24 unidos                      |
| /22 | 255.255.252.0     | 1024   | 1022  | 4 3er oct. | Cuatro /24                          |

(*) En /31 “válidos” ambos extremos, sin red/bc clásicos.

### 9.2 Binario de referencia (1 octeto)
- Bits: **128 64 32 16 8 4 2 1**  
- Ej.: `11100000` = 224; `11000000` = 192; `11110000` = 240 → así nacen los saltos **32, 64, 16**…

### 9.3 Plantilla de plan de direccionamiento
```
Bloque base: ____________________
┌───────────────────────────────────────────────────────────────┐
│ Subred      | Prefijo | Red           | Broadcast      | GW  │
├─────────────┼─────────┼───────────────┼────────────────┼─────┤
│             | /__     | __.__.__.__   | __.__.__.__    |     │
│             | /__     | __.__.__.__   | __.__.__.__    |     │
│             | /__     | __.__.__.__   | __.__.__.__    |     │
└───────────────────────────────────────────────────────────────┘
Enlaces p2p:
- R?–R?: ________/30  (IPs: __.__.__.__ y __.__.__.__)
- R?–R?: ________/31  (IPs: __.__.__.__ y __.__.__.__)
```

### 9.4 Diagrama Mermaid (opcional si tu visor lo soporta)
```mermaid
flowchart LR
  subgraph LAN_A["LAN A 192.168.10.0/24"]
    A1[PC A1]\nGW=192.168.10.1
    A2[PC A2]
  end
  subgraph R1["R1"]
    R1GI0[Gi0/0=192.168.10.1]
    R1S0[S0/0=10.0.0.1/30]
  end
  subgraph R2["R2"]
    R2S0[S0/0=10.0.0.2/30]
    R2GI0[Gi0/0=192.168.20.1]
  end
  subgraph LAN_B["LAN B 192.168.20.0/24"]
    B1[PC B1]\nGW=192.168.20.1
    B2[PC B2]
  end
  LAN_A --- R1
  R1S0 --- R2S0
  R2 --- LAN_B
```

---

## 10) Ejercicios propuestos (con solución al final)

> **Recomendación**: Intenta resolverlos antes de mirar la solución. No uses calculadora de subredes al principio; ejercita cabeza y método.

**E1.** Para `192.168.1.100/27`: red, broadcast, rango de hosts.  
**E2.** Divide `10.0.0.0/24` en subredes para **50**, **25**, **10** y **5** hosts. Asigna gateways.  
**E3.** Dado `172.16.8.0/23`, ¿cuál es la 3ª subred /27 dentro de ese rango? (red, bc, hosts).  
**E4.** Diseña un enlace **R1–R2** con **/31** y dos LAN (`192.168.10.0/24` y `192.168.20.0/24`). Indica IPs de interfaces y rutas estáticas.  
**E5.** En `192.168.100.0/22`, asigna VLSM para: 180, 60, 20, 12 hosts y 2 enlaces p2p. Dibuja diagrama y tabla final.

---

## 11) Soluciones (paso a paso)

**E1.** `/27` → máscara `255.255.255.224` → incremento 32. Redes: `.0, .32, .64, .96, .128, .160, .192, .224`. `100` ∈ `.96–.127`.  
- Red: `192.168.1.96` | Bc: `192.168.1.127` | Hosts: `.97–.126`

**E2.** Orden: 50→`/26`, 25→`/27`, 10→`/28`, 5→`/29`.  
- `/26`: `10.0.0.0/26` → red `10.0.0.0` | bc `10.0.0.63` | hosts `.1–.62` | **GW .1**
- `/27`: `10.0.0.64/27` → red `10.0.0.64` | bc `10.0.0.95` | hosts `.65–.94` | **GW .65**
- `/28`: `10.0.0.96/28` → red `10.0.0.96` | bc `10.0.0.111` | hosts `.97–.110` | **GW .97`
- `/29`: `10.0.0.112/29` → red `10.0.0.112` | bc `10.0.0.119` | hosts `.113–.118` | **GW .113`

**E3.** `172.16.8.0/23` abarca `172.16.8.0–172.16.9.255`. Dentro, subredes `/27` (incremento 32 en 4º octeto).  
- Listado `8.0/27`: `.0–.31`, `.32–.63`, `.64–.95`, `.96–.127`, …  
- **3ª** es `.64–.95`: Red `172.16.8.64`, Bc `172.16.8.95`, Hosts `.65–.94`.

**E4.** /31 en p2p, ejemplo `10.10.10.0/31`: R1=`.0`, R2=`.1`.  
- LANs: R1 Gi0/0=`192.168.10.1/24`; R2 Gi0/0=`192.168.20.1/24`.  
- Rutas:  
  - En R1: `ip route 192.168.20.0 255.255.255.0 10.10.10.1`  
  - En R2: `ip route 192.168.10.0 255.255.255.0 10.10.10.0`  
- Gateways de hosts: `192.168.10.1` y `192.168.20.1`.

**E5.** `192.168.100.0/22` (1022 hosts útiles). Necesidades: 180→`/24`, 60→`/26`, 20→`/27`, 12→`/28`, 2 p2p→`/30` y `/30`.  
- `180` → `192.168.100.0/24` (GW `.1`)  
- `60`  → `192.168.101.0/26` (GW `.1`)  
- `20`  → `192.168.101.64/27` (GW `.65`)  
- `12`  → `192.168.101.96/28` (GW `.97`)  
- p2p1 → `192.168.101.112/30` (IPs `.113` y `.114`)  
- p2p2 → `192.168.101.116/30` (IPs `.117` y `.118`)  
- Libre: `192.168.102.0/23` para futuro.

---

## 12) Cierre
Con este documento ya puedes **diseñar redes IPv4** razonables, con **subredes adaptadas**, **routers y rutas** para conectarlas y **verificación** básica. El secreto es **método y orden**: define necesidades → elige prefijos mínimos → asigna sin solape → documenta → prueba.

> **Mantra del subnetting**: **“Incremento, red, broadcast, hosts, gateway.”** Repite y fluye 🚀
