**Suposiciones**

* Permitimos *subnet zero* (todas las subredes son válidas).
* Fórmulas:

  * Si pides **S subredes** ⇒ toma b bits tal que $2^b \ge S$.
  * Si pides **H hosts/subred** ⇒ toma h bits tal que $2^h - 2 \ge H$.
  * Prefijo nuevo = prefijo por defecto de la clase + b.
  * Hosts por subred = $2^h - 2$.
  * Subredes = $2^b$.
* “Octeto interesante” = el primero cuyo valor en la máscara no es 255 ni 0.
* **Tamaño de bloque** = $256 -$ (valor del octeto interesante en la máscara).
* Para hallar la red: en el octeto interesante, $ \text{red} = \left\lfloor \dfrac{\text{octeto}}{\text{bloque}} \right\rfloor \times \text{bloque}$.
* Broadcast = (misma red, pero octeto interesante + (bloque−1) y los siguientes octetos a 255).
* Rango de hosts = (red+1) … (broadcast−1).



# Clase C (14 ejercicios)

### 1) 192.168.10.0 (Clase C). Quiero **2 subredes**.

**Paso a paso**

1. Clase C ⇒ por defecto /24 (255.255.255.0).
2. 2 subredes ⇒ $2^1=2$ ⇒ b=1 ⇒ nuevo prefijo **/25** (255.255.255.128).
3. Bloque = 256−128 = **128** en el 4º octeto.
4. Subredes: 0 y 128.
   **Resultado**

* Subred 1: **192.168.10.0/25** → red 192.168.10.0, broadcast 192.168.10.127, hosts 192.168.10.1–126 (126 hosts).
* Subred 2: **192.168.10.128/25** → red 192.168.10.128, broadcast 192.168.10.255, hosts 129–254 (126 hosts).



### 2) 192.168.10.0. Quiero **4 subredes**.

**Pasos**: /24 base. $2^2=4$ ⇒ b=2 ⇒ **/26** (255.255.255.192). Bloque = 64.
**Resultado**

* 0: **192.168.10.0/26** → Bcast 63, hosts 1–62.
* 64: **192.168.10.64/26** → Bcast 127, hosts 65–126.
* 128: **192.168.10.128/26** → Bcast 191, hosts 129–190.
* 192: **192.168.10.192/26** → Bcast 255, hosts 193–254. (4 subredes × 62 hosts)



### 3) 192.168.10.0. Quiero **8 subredes**.

**Pasos**: /24. $2^3=8$ ⇒ **/27** (255.255.255.224). Bloque = 32.
**Resultado** (resumo):

* Redes: 0,32,64,96,128,160,192,224.
* p.ej. **192.168.10.96/27** → bcast .127, hosts .97–.126 (30 hosts/subred).



### 4) 192.168.10.0. Quiero **5 subredes** (redondea).

**Pasos**: $2^2=4<5$, $2^3=8$ ⇒ **/27**. Bloque 32.
**Resultado**: usa las **primeras 5**: 0/27, 32/27, 64/27, 96/27, 128/27.



### 5) 192.168.20.0. Quiero **≥20 hosts/subred**.

**Pasos**: busca h tal que $2^h-2\ge 20$ ⇒ h=5 (30).

* /24 base ⇒ host bits por defecto=8 ⇒ b = 8−h = 3 ⇒ **/27**. Bloque 32.
  **Resultado**: cada subred /27 tiene 30 hosts. (redes 0,32,64,96,128,160,192,224).



### 6) Dada **IP 192.168.5.130** con **255.255.255.192 (/26)**.

**Pasos**: Bloque 64 en 4º octeto. 130 // 64 = 2 ⇒ 2×64=**128** (red).
**Resultado**:

* Red: **192.168.5.128**
* Broadcast: **192.168.5.191**
* Hosts: **.129–.190** (62 hosts)



### 7) 192.168.1.0 con **/28**. ¿Cuántas subredes/hosts? Dame la **subred #3**.

**Pasos**: /28 (255.255.255.240). Bloque 16.

* Desde /24 ⇒ b=4 ⇒ **16 subredes**.
* h=4 ⇒ **14 hosts**/subred.
* Subred #3 (empezando en 0): 3×16=**48**.
  **Resultado**: **192.168.1.48/28**, bcast .63, hosts .49–.62.



### 8) ¿Están en la misma subred con /27? **192.168.1.50** y **192.168.1.90**.

**Pasos**: /27 ⇒ bloque 32.

* 50 ∈ 32–63; 90 ∈ 64–95 ⇒ **No**.



### 9) 192.168.100.200 con **/29 (255.255.255.248)**.

**Pasos**: Bloque 8. 200 // 8 = 25 ⇒ 25×8=**200** (red).
**Resultado**: red **192.168.100.200**, bcast **192.168.100.207**, hosts **.201–.206** (6 hosts).



### 10) 192.168.3.0. Quiero subredes de **6 hosts**.

**Pasos**: $2^h-2\ge6 \Rightarrow h=3$ (6). /24 ⇒ b=5 ⇒ **/29**. Bloque 8.
**Primeras 3 subredes**:

* 0/29 → bcast 7, hosts 1–6.
* 8/29 → bcast 15, hosts 9–14.
* 16/29 → bcast 23, hosts 17–22.



### 11) 192.168.7.0 con **/30** (enlaces p2p).

**Pasos**: /30 ⇒ bloque 4 ⇒ 2 hosts/subred.
**Primeras 4 subredes**:

* 0/30 → hosts 1–2, bcast 3.
* 4/30 → hosts 5–6, bcast 7.
* 8/30 → hosts 9–10, bcast 11.
* 12/30 → hosts 13–14, bcast 15.



### 12) 192.168.44.0 **/26**. ¿Subredes/hosts? ¿Bcast de la última?

**Pasos**: desde /24 ⇒ b=2^? /26 → b=2 ⇒ **4 subredes**. h=6 ⇒ **62 hosts**. Bloque 64.
**Última subred**: 192, bcast **192.168.44.255**.



### 13) 192.168.55.73 con **/27 (224)**.

**Pasos**: bloque 32; 73//32=2 ⇒ 2×32=64 ⇒ red **.64**.
**Resultado**: red **192.168.55.64**, bcast **.95**, hosts **.65–.94** (30 hosts).



### 14) ¿Misma subred y válidos? /26 con **192.168.10.62** y **192.168.10.63**.

**Pasos**: /26 ⇒ bloque 64 ⇒ subred 0–63. Ambos caen en **la misma subred**;
pero **.63 es broadcast** ⇒ **no es host válido**.



# Clase B (14 ejercicios)

### 15) 172.16.0.0. Quiero **200 subredes**.

**Pasos**: Clase B ⇒ /16. $2^7=128<200$, $2^8=256$ ⇒ b=8 ⇒ **/24**.

* Subredes: 256. Hosts/subred: $2^{8}-2=254$.
* Bloque en 3er octeto = 256 (porque máscara 255 allí) y “octeto interesante” es el **3º = 255**? Ojo: /24 ⇒ 255.255.255.0 ⇒ interesante es **4º** (0). Para enumerar subredes, aumenta el **3er octeto** de 0→255.
  **Resultado**: p.ej. **172.16.5.0/24** → bcast .5.255, hosts .5.1–.5.254.



### 16) 172.16.0.0. Quiero **≥1000 hosts/subred**.

**Pasos**: $2^{10}-2=1022$ ⇒ h=10 ⇒ prefijo **/22** (255.255.252.0).

* b = /22 − /16 = 6 ⇒ **64 subredes**.
* Bloque en 3er octeto = 4.
  **Resultado (ejemplo)**: **172.16.8.0/22**, bcast **172.16.11.255**, hosts **.8.1–.11.254**.



### 17) IP **172.16.37.99** con **/27 (255.255.255.224)**.

**Pasos**: Bloque 32 en 4º octeto; 99//32=3 ⇒ 3×32=96.
**Resultado**: red **172.16.37.96**, bcast **172.16.37.127**, hosts **.97–.126**.



### 18) ¿Misma subred con **/20**? **172.16.128.10** y **172.16.143.200**.

**Pasos**: /20 ⇒ 255.255.240.0 ⇒ bloque 16 en 3er octeto.

* 128–143 es el mismo bloque ⇒ **Sí**.
* Red **172.16.128.0**, bcast **172.16.143.255**.



### 19) 172.16.0.0 con **/21 (255.255.248.0)**. ¿Subred #10?

**Pasos**: b=/21−/16=5 ⇒ **32 subredes**; h=11 ⇒ **2046 hosts**.

* Bloque en 3er octeto = 8. Subred #10 ⇒ 10×8=**80**.
  **Resultado**: **172.16.80.0/21**, bcast **172.16.87.255**, hosts **.80.1–.87.254**.



### 20) 172.16.5.200 con **/23 (255.255.254.0)**.

**Pasos**: /23 ⇒ bloque 2 en 3er octeto. 5//2=2 ⇒ red 4.
**Resultado**: red **172.16.4.0**, bcast **172.16.5.255**, hosts **.4.1–.5.254**.



### 21) 172.16.0.0. Quiero **30 hosts/subred**.

**Pasos**: $2^5-2=30$ ⇒ h=5 ⇒ **/27**.

* b = 11 ⇒ **2048 subredes**. Bloque 32 en 4º octeto.
  **Primeras 3 subredes**: 172.16.0.0/27, 172.16.0.32/27, 172.16.0.64/27.



### 22) 172.16.0.0 con **/19 (255.255.224.0)**.

**Pasos**: b=3 ⇒ **8 subredes**; h=13 ⇒ **8190 hosts**. Bloque 32 en 3er octeto.
**Última subred**: 224 ⇒ **172.16.224.0/19**, bcast **172.16.255.255**.



### 23) /23: **172.16.200.1** y **172.16.201.255** ¿misma subred? ¿válidos?

**Pasos**: /23 ⇒ pares (200–201). **Sí**, misma subred; pero **.201.255 es broadcast** ⇒ no usable.



### 24) 172.16.0.1 con **/17 (255.255.128.0)**.

**Resultado directo**: red **172.16.0.0**, bcast **172.16.127.255**, hosts **.0.1–.127.254**.



### 25) Desde **172.16.160.0/20**, lista **las 3 siguientes redes /20**.

**Pasos**: /20 ⇒ bloque 16 en 3er octeto.

* Redes: 160.0, **176.0**, **192.0**, **208.0** (/20 cada una).



### 26) 172.16.90.77 con **/30 (255.255.255.252)**.

**Pasos**: bloque 4 en 4º octeto. 77//4=19 ⇒ red 76.
**Resultado**: red **172.16.90.76**, bcast **172.16.90.79**, hosts **.77–.78**.



### 27) 172.16.0.0. Quiero **≥4000 hosts/subred**.

**Pasos**: $2^{12}-2=4094$ ⇒ h=12 ⇒ **/20** (255.255.240.0).

* b = 4 ⇒ **16 subredes**; bloque 16 en 3er octeto.



### 28) 172.16.0.0. **“Tomo 9 bits prestados”**. ¿Subredes/hosts?

**Pasos**: b=9 ⇒ prefijo **/25** (255.255.255.128).

* Subredes $2^9=512$. Hosts $2^7-2=126$. Bloque 128 en 4º octeto.



# Clase A (12 ejercicios)

### 29) 10.0.0.0. Quiero **1000 subredes**.

**Pasos**: $2^{10}=1024$ ⇒ b=10 ⇒ **/18** (255.255.192.0).

* Hosts/subred: $2^{14}-2=16382$.
* Octeto interesante: 3º (192) ⇒ bloque **64** (en 3er octeto).
  **Ejemplo (10.0.x.y)**: para 2º octeto fijo (p.ej. 0), subredes en 3er octeto: 0,64,128,192.



### 30) 10.0.0.0. Quiero **≥500 hosts/subred**.

**Pasos**: $2^9-2=510$ ⇒ h=9 ⇒ prefijo **/23** (255.255.254.0).

* b = 15 ⇒ muchas subredes; bloque 2 en 3er octeto.



### 31) 10.12.5.200 con **/20 (255.255.240.0)**.

**Pasos**: bloque 16 en 3er octeto; 5∈0–15 ⇒ red 10.12.0.0.
**Resultado**: red **10.12.0.0**, bcast **10.12.15.255**, hosts **10.12.0.1–10.12.15.254**.



### 32) ¿Misma subred con **/19**? **10.44.12.10** y **10.44.31.250**.

**Pasos**: /19 ⇒ 255.255.224.0 ⇒ bloque 32 en 3er octeto.

* 12 y 31 están en 0–31 ⇒ **Sí**. Red **10.44.0.0**, bcast **10.44.31.255**.



### 33) 10.0.0.0 con **/14 (255.252.0.0)**. ¿Subredes/hosts?

**Pasos**: b=/14−/8=6 ⇒ **64 subredes**.

* h=32−14=18 ⇒ **262,142 hosts**/subred.
* Bloque en 2º octeto = **4**.



### 34) 10.200.100.77 con **/25 (255.255.255.128)**.

**Pasos**: bloque 128 en 4º octeto; 77<128 ⇒ red **10.200.100.0**.
**Resultado**: bcast **10.200.100.127**, hosts **.1–.126**.



### 35) 10.0.0.0. Quiero **3000 subredes**.

**Pasos**: $2^{11}=2048<3000$, $2^{12}=4096$ ⇒ b=12 ⇒ **/20** (255.255.240.0).

* Hosts/subred: $2^{12}-2=4094$.
* Bloque 16 en 3er octeto.



### 36) ¿Misma subred con **/30**? **10.10.10.10** y **10.10.10.9**.

**Pasos**: /30 ⇒ bloque 4 en 4º octeto.

* 8–11 es el bloque ⇒ **Sí**, misma subred. Ambos **hosts válidos** (no .8 ni .11).



### 37) 10.100.0.0. Quiero **≥20 000 hosts/subred**.

**Pasos**: $2^{15}-2=32766$ ⇒ h=15 ⇒ **/17** (255.255.128.0).

* b = 9 ⇒ **512 subredes**. Bloque 128 en 2º octeto.



### 38) 10.0.0.0 con **/22 (255.255.252.0)**. ¿Subredes/hosts?

**Pasos**: b=/22−/8=14 ⇒ **16384 subredes**.

* h=10 ⇒ **1022 hosts**/subred. Bloque 4 en 3er octeto.



### 39) 10.1.130.1 con **/18 (255.255.192.0)**.

**Pasos**: bloque 64 en 3er octeto; 130 ∈ 128–191 ⇒ red **10.1.128.0**.
**Resultado**: bcast **10.1.191.255**, hosts **10.1.128.1–10.1.191.254**.



### 40) ¿Es **10.2.3.255** broadcast con **/24**?

**Pasos**: /24 ⇒ bcast acaba en **.255**. Red 10.2.3.0, bcast **10.2.3.255**.
**Resultado**: **Sí, es broadcast** ⇒ no es host válido.

¡Vamos allá, Deivit! Te dejo **otro pack potente**: 30 ejercicios resueltos (enfoque “al revés”, validaciones rápidas, binario, casos límite, /30 vs /31, etc.) + **hoja de trucos imprimible** al final. Todo sin VLSM, subnetting clásico.



# Pack 2 — Ejercicios de Subnetting Clásico (30 problemas resueltos)

## A) Problemas “al revés” (te doy máscara / requisito y tú deduces lo demás)

### 1) Clase C, máscara 255.255.255.224. ¿Subredes/hosts? Da las 3 primeras redes.

**Pasos**

* En C: /24 base. 255.255.255.224 ⇒ **/27** ⇒ b=3, h=5.
* Subredes: $2^3=8$. Hosts/subred: $2^5-2=30$. Bloque: 256−224=**32**.
  **Resultado**
* Redes: .0, .32, .64, .96, .128, .160, .192, .224
* 3 primeras: **.0/27** (bcast .31), **.32/27** (bcast .63), **.64/27** (bcast .95).



### 2) Clase C, máscara 255.255.255.192. ¿Cuántas subredes necesito mínimo para 5 departamentos?

**Pasos**

* 255.255.255.192 ⇒ /26 ⇒ **4 subredes**.
* Para 5 dptos no alcanza; necesitarías /27 (8 subredes).
  **Resultado**: Con /26 ⇒ **4**; para 5 ⇒ **subir a /27**.



### 3) Clase B 172.16.0.0 con 255.255.252.0. ¿Subredes/hosts? ¿Red #6?

**Pasos**

* /16 base; 255.255.252.0 ⇒ **/22** ⇒ b=6, h=10.
* Subredes: $2^6=64$. Hosts: $2^{10}-2=1022$. Bloque 3er octeto = **4**.
* Red #6 ⇒ 6×4=**24**.
  **Resultado**: **172.16.24.0/22**, bcast **172.16.27.255**.



### 4) Clase B 172.16.0.0 con 255.255.224.0. ¿Bloque y últimas 2 subredes?

**Pasos**

* /19 ⇒ bloque en 3er octeto = **32**. Subredes: $2^{3}=8$.
* Últimas dos redes: **172.16.192.0/19** (bcast .223.255) y **172.16.224.0/19** (bcast .255.255).
  **Resultado**: Bloque **32**; últimas dos: **192.0/19** y **224.0/19**.



### 5) Clase A 10.0.0.0 con 255.255.240.0. ¿Subredes/hosts?

**Pasos**

* /20 ⇒ b=12, h=12. Subredes: $2^{12}=4096$. Hosts: $2^{12}-2=4094$.
* Bloque 3er octeto = **16**.
  **Resultado**: 4096 subredes, 4094 hosts/subred.



### 6) 192.168.1.0 con 255.255.255.248. Lista 4 redes y su primer/último host.

**Pasos**

* /29 ⇒ bloque **8**.
  **Resultado**
* .0/29 → hosts .1–.6 (bcast .7)
* .8/29 → hosts .9–.14 (bcast .15)
* .16/29 → hosts .17–.22 (bcast .23)
* .24/29 → hosts .25–.30 (bcast .31)



### 7) 10.2.0.0 con 255.255.254.0. ¿Qué 3er octetos entran en una misma /23?

**Pasos**

* /23 ⇒ bloque **2** en 3er octeto.
  **Resultado**: grupos (0–1), (2–3), (4–5), … (254–255).



### 8) 172.16.100.0 con 255.255.255.0. ¿Cuántos hosts y broadcast?

**Pasos**

* /24 ⇒ 254 hosts; broadcast **172.16.100.255**.
  **Resultado**: 254 hosts; bcast **.255**.



### 9) 192.168.50.0 con 255.255.255.128. Dame subred #1 y #2 (empezando en 0).

**Pasos**

* /25 ⇒ bloque **128**.
  **Resultado**
* \#1: **.128/25** (bcast .255, hosts .129–.254)
* \#0 sería .0/25; #2 no existe (solo hay 2 subredes: 0 y 128).



### 10) 10.3.0.0 con 255.255.255.192. ¿Hosts/subred? ¿Cuántas subredes si fijo 2º y 3er octeto?

**Pasos**

* /26 ⇒ 62 hosts.
* Si fijas 10.3.X.Y, el 3er octeto está fijo ⇒ subredes salen del 4º octeto: bloque 64 ⇒ **4 subredes** (.0, .64, .128, .192).
  **Resultado**: 62 hosts/subred; **4 subredes** por 3er octeto fijo.



## B) Pertenencia y validez (¿misma subred? ¿host, red o broadcast?)

### 11) /27: 192.168.2.33 y 192.168.2.62. ¿Misma subred? ¿Válidos?

**Pasos**

* /27 ⇒ bloque 32. 33∈32–63; 62∈32–63 ⇒ **sí** misma subred.
* .62 no es broadcast (sería .63), ambos **válidos**.
  **Resultado**: Sí, y ambos válidos.



### 12) /26: 192.168.10.64 y 192.168.10.127.

**Pasos**

* Bloque 64 ⇒ subred 64–127.
* .64 = **dirección de red**, .127 = **broadcast** ⇒ no hosts válidos.
  **Resultado**: Misma subred, ninguno usable.



### 13) /23: 172.16.9.0 y 172.16.10.255.

**Pasos**

* /23 agrupa pares: 8–9, 10–11 …
* 9 está con 8–9, 10.255 con 10–11 ⇒ **no** misma subred.
  **Resultado**: No.



### 14) /30: 10.1.1.8, 10.1.1.10.

**Pasos**

* /30 ⇒ bloques de 4: 8–11.
* .8 red, .11 bcast, .9 y .10 hosts. .8 y .10 no “ambos válidos” (uno es red).
  **Resultado**: Misma subred; **.10 válido, .8 no**.



### 15) /28: 192.168.0.31. ¿Qué es?

**Pasos**

* /28 bloque 16: 16–31 ⇒ .31 = **broadcast**.
  **Resultado**: Broadcast.



## C) Cálculo binario rápido (practicar el AND y el bloque)

> Tip: Convierte **solo el octeto interesante** a binario si te agobias.

### 16) 192.168.14.203 con /27. Halla red por AND binario (4º octeto).

**Pasos**

* /27 ⇒ máscara 224 ⇒ binario 11100000.
* 203 bin → 11001011. AND ⇒ 11000000 (192 en decimal).
  **Resultado**: Red **192.168.14.192/27**, bcast **.223**.



### 17) 172.16.130.77 con /20 (3er octeto interesante).

**Pasos**

* /20 ⇒ 255.255.240.0 ⇒ 3er octeto máscara 240 (11110000).
* 130 bin 10000010 AND 11110000 = 10000000 (128).
  **Resultado**: Red **172.16.128.0/20**, bcast **172.16.143.255**.



### 18) 10.5.63.19 con /18 (3er octeto).

**Pasos**

* /18 ⇒ 255.255.192.0 ⇒ máscara 192 (11000000).
* 63 bin 00111111 AND 11000000 = 00000000 (0).
  **Resultado**: Red **10.5.0.0/18**, bcast **10.5.63.255**.



## D) Diseño con requisitos (subredes o hosts mínimos)

### 19) Clase C 192.168.7.0 para **5 subredes**, ¿prefijo? Enumera redes.

**Pasos**

* $2^2=4<5$, $2^3=8$ ⇒ **/27**. Bloque 32.
  **Resultado**: .0, .32, .64, .96, .128, .160, .192, .224 (elige 5 primeras).



### 20) Clase C 192.168.60.0 para **≥100 hosts/subred**.

**Pasos**

* $2^7-2=126$ ⇒ h=7 ⇒ **/25**. Bloque 128.
  **Resultado**: .0/25 y .128/25 (2 subredes, 126 hosts cada una).



### 21) Clase B 172.16.0.0 para **≥3000 hosts/subred**.

**Pasos**

* $2^{12}-2=4094$ ⇒ h=12 ⇒ **/20**. Bloque 16 en 3er octeto.
  **Resultado**: /20; 16 subredes si fijas 2º octeto.



### 22) Clase A 10.0.0.0 para **≥50 subredes** y **≥400 hosts/subred**.

**Pasos**

* Hosts ⇒ $2^9-2=510$ ⇒ h=9 ⇒ /23.
* Subredes ⇒ con /23 en clase A: b = /23−/8 = 15 ⇒ $2^{15}=32768$ subredes (de sobra).
  **Resultado**: **/23**.



### 23) 10.10.0.0 para **≥8000 hosts/subred**, ¿prefijo y bloque?

**Pasos**

* $2^{14}-2=16382$ ⇒ h=14 ⇒ **/18**.
* Bloque 3er octeto **64**.
  **Resultado**: /18; bloque 64 en 3er octeto.



## E) Listados y numeración de subredes (práctica de bloques)

### 24) 192.168.100.0/26. Enumera **todas** las subredes.

**Pasos/Resultado**

* Bloque 64 ⇒ **.0/26, .64/26, .128/26, .192/26**.



### 25) 172.16.0.0/22. Da las **primeras 5 redes /22** (variando 3er octeto).

**Resultado**

* **172.16.0.0/22**, **4.0/22**, **8.0/22**, **12.0/22**, **16.0/22** (bcasts .3.255, .7.255, …).



### 26) 10.1.0.0/20. Dame las redes #0, #1, #7, #8 (3er octeto).

**Pasos/Resultado**

* Bloque 16 ⇒ #n = n×16.
* \#0=0, #1=16, #7=112, #8=128 ⇒
  **10.1.0.0/20, 10.1.16.0/20, 10.1.112.0/20, 10.1.128.0/20**.


### 27) 192.168.1.0/31. ¿Cuántos hosts? ¿Para qué sirve?

**Pasos**

* /31 ⇒ 2 direcciones, **sin restar 2** (RFC 3021) para **enlaces punto a punto**.
* En subnetting clásico tradicional se evitaba; hoy es común en P2P.
  **Resultado**: **2 hosts usables** (ambos extremos).



### 28) 192.168.1.0/30. Compáralo con /31 para P2P.

**Resultado**

* /30 ⇒ 4 direcciones: 2 hosts + red + bcast.
* /31 ⇒ 2 direcciones: 2 hosts (más eficiente en P2P).
* En ejercicios “clásicos” se suele usar **/30** para P2P.



### 29) ¿Es válido 172.16.32.0 como host en /19?

**Pasos**

* /19 ⇒ bloque 32 ⇒ 32 es **dirección de red**.
  **Resultado**: **No**, es red.



### 30) ¿Es 10.0.4.255 un broadcast en /20?

**Pasos**

* /20 ⇒ bloque 16 en 3er octeto. El rango 0–15, 16–31, …
* 4.255 pertenece a 0–15 ⇒ bcast de 10.0.15.255; **4.255 es host válido** (bcast es .15.255).
  **Resultado**: **No** es broadcast; es un host de la /20 (ojo a la trampa).


# Mini-checks súper rápidos (para que tus alumnos cojan ritmo)

1. /26 ⇒ bloque 64. ¿Red de 192.168.9.130? → **.128/26**.
2. /23 ⇒ pares. ¿Bcast de 172.16.21.0/23? → **172.16.22.255** (porque red es 20–21).
3. /27 ⇒ bloque 32. ¿Rango hosts en 10.0.0.96/27? → **.97–.126**.
4. /25 ⇒ dos subredes. ¿Broadcast de 192.168.77.128/25? → **192.168.77.255**.
5. /22 ⇒ bloque 4. ¿Red #3 de 172.16.0.0/22? → **172.16.12.0/22**.



# Hoja de trucos (A4, para imprimir y pegar)

**CHULETA SUBNETTING CLÁSICO (sin VLSM)**

* **Prefijos por defecto**:

  * Clase A: /8 (10.0.0.0–10.255.255.255)
  * Clase B: /16 (172.16.0.0–172.31.255.255)
  * Clase C: /24 (192.168.x.0–192.168.x.255)

* **Fórmulas clave**

  * Pidiendo **S subredes** ⇒ coge **b bits** s.t. $2^b \ge S$.
  * Pidiendo **H hosts/subred** ⇒ coge **h bits** s.t. $2^h - 2 \ge H$.
  * **Nuevo prefijo** = prefijo por defecto + b (si diseñas por subredes).
  * **Hosts/subred** = $2^h - 2$ (excepto /31 en P2P).
  * **#Subredes** = $2^b$.
  * **Octeto interesante**: primer octeto ≠ 255 ni 0 en la máscara.
  * **Bloque** = 256 − (valor del octeto interesante).

* **Cálculo rápido de red/broadcast**

  1. Identifica el **bloque**.
  2. Red = $\left\lfloor \dfrac{\text{octeto}}{\text{bloque}} \right\rfloor \times \text{bloque}$.
  3. Broadcast = (red + bloque − 1) en ese octeto; todo lo posterior a **255**.
  4. Rango host = red+1 … broadcast−1.

* **Bloques frecuentes**

  * /25 → 128  | /26 → 64  | /27 → 32  | /28 → 16
  * /29 → 8    | /30 → 4   | /23 → 2   | /22 → 4
  * /21 → 8    | /20 → 16  | /19 → 32  | /18 → 64

* **P2P**

  * **/30** clásico: 2 hosts, 1 red, 1 bcast.
  * **/31** (RFC 3021): 2 direcciones → **2 hosts** (sin red/bcast) para P2P.
