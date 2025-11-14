# 50 preguntas explicadas sobre subnetting y redes

## 1. ¿Cuál es la dirección de red de 192.168.1.130 con máscara 255.255.255.0?

Primero, convierte ambos a binario:
- 192.168.1.130 → 11000000.10101000.00000001.10000010
- 255.255.255.0 → 11111111.11111111.11111111.00000000

Haz un AND bit a bit por octetos:
- El último octeto (130 AND 0) = 0
Así, la dirección de red es **192.168.1.0**.## 2. Una IP es 172.16.50.5 y la máscara 255.255.0.0. ¿Qué dirección de red le corresponde?

La máscara tiene dos primeros octetos a 255 (covering 16 bits), así que la dirección de red es **172.16.0.0** (todo lo relativo al host se pone a 0).## 3. Si tienes la IP 192.168.1.75 y la máscara /26, ¿qué red y rango de hosts tiene?

Máscara /26 = 255.255.255.192, bloque de 64. 

Divide el último octeto entre 64: 75 // 64 = 1, entonces la red es 64.
- Red: 192.168.1.64/26
- Rango de hosts: 65-126
- Broadcast: 127## 4. ¿Cuántas subredes genera la máscara 255.255.255.224 en una red clase C?

Esta máscara equivale a /27, por lo que se "piden prestados" 3 bits para subredes. Se obtienen **8 subredes** (2^3).## 5. En la IP 10.0.0.5 con máscara 255.0.0.0, ¿a qué clase pertenece y cuál es la red?

Es una IP de clase A (primer octeto entre 1-126). La red es **10.0.0.0**.## 6. Quiero dividir 192.168.1.0/24 en 4 subredes. ¿Qué máscara uso y qué rangos salen?

Necesitas 2 bits para subredes (2^2=4). Cambias la máscara de /24 a /26, que es 255.255.255.192. Cada subred tiene 64 direcciones:
- Subred 1: .0 - .63
- Subred 2: .64 - .127
- Subred 3: .128 - .191
- Subred 4: .192 - .255## 7. ¿Cómo determinas si dos IPs están en la misma subred con máscara /27?

Divide el último octeto de cada IP entre 32 (bloque de /27). Si caen en el mismo bloque, están en la misma subred. Ejemplo:
- 50 => 50/32=1 (rango 32–63)
- 90 => 90/32=2 (rango 64–95)
No están en la misma subred.## 8. ¿Cuál es el rango de hosts de la red 172.16.8.0/22?

/22 en clase B tiene bloque de 4 en el tercer octeto. 8.0 es la red, el último host es 11.254, broadcast es 11.255. Rango: 8.1–11.254## 9. ¿Cuántas IPs útiles tiene una subred /28?

Con /28 hay 16 direcciones, pero se descuentan la red y el broadcast, entonces quedan **14 hosts válidos**.## 10. Si una IP es 192.168.10.62 con /26, ¿es válido como host?

/26 tiene bloques de 64. .62 cae en el rango 0–63, y el broadcast es .63, por tanto .62 es un host válido.## 11. ¿Por qué se usa /30 en enlaces punto a punto (P2P)?

Porque sólo necesitas dos hosts, y /30 proporciona 4 direcciones: 1 de red, 2 hosts, 1 broadcast. Así se optimizan IPs.## 12. ¿Qué ventaja tiene usar /31 en vez de /30 para P2P (según RFC 3021)?

/31 da sólo 2 direcciones, ambas usables en extremos. Es más eficiente, pero requiere equipos que soporten RFC 3021.## 13. ¿Cómo calcularías la red de 172.16.37.99 con máscara /27?

Bloque de /27 es 32, 99/32=3, 3×32=96. Red: 172.16.37.96. Los hosts válidos van desde 97 hasta 126.## 14. Si tienes 192.168.1.100 con máscara 255.255.255.0, ¿cómo calculas la dirección de red y broadcast?

Red: el último octeto se pone a 0 → 192.168.1.0
Broadcast: el último octeto se pone a 255 → 192.168.1.255## 15. Si divides la red 192.168.10.0/24 en 8 subredes, ¿qué máscara resulta y cuánto dura cada bloque?

8 subredes → 2^3 = 8 → b=3 → /27 (255.255.255.224), cada bloque son 32 IPs.## 16. ¿Cómo averiguas el "bloque" cuando te dan una máscara en decimal?

Bloque = 256 – valor del octeto interesante.
Ejemplo: máscara 255.255.255.192 (192 en el cuarto octeto), bloque = 256−192 = 64.## 17. Para la IP 10.0.4.255 con máscara /20, ¿sería un host válido o broadcast?

/20 implica bloques de 16 en el segundo octeto. Mirando el rango, .4 no es broadcast; sería 10.0.15.255. Por tanto, 10.0.4.255 es válido.## 18. ¿Cómo defines la dirección de broadcast de una subred?

Es la última dirección del rango de la subred, donde todos los bits de host se ponen a 1. Ejemplo: en /26 (bloque 64), si la red es 192, broadcast es 255.## 19. ¿Para qué sirve la operación AND binaria entre IP y máscara?

Sirve para calcular la dirección de red: cada bit de la IP se combina con el bit correspondiente de la máscara (si ambos son 1, resulta 1; si alguno es 0, resulta 0).## 20. ¿Qué IP sería el primer host en la subred 192.168.1.0/29?

/29: bloque de 8 direcciones. Primer host es .1, la red es .0 y el broadcast es .7. Primer host: 192.168.1.1## 21. Si tienes una red 172.16.0.0/16 y quieres al menos 200 subredes, ¿qué prefijo resulta?

200 subredes → b=8 (porque 2^8=256 > 200), el prefijo final es /24. Se crean subredes variando el tercer octeto.## 22. ¿Por qué en cada subred los extremos del rango no pueden usarse como hosts?

Porque son reservados: la primera dirección es la red, la última es broadcast. Los hosts válidos van entre ambas.## 23. En una red /23, ¿son hosts válidos 10.10.10.255 y 10.10.11.1?

El rango va de .0 a .255, pero el broadcast es .255. Así, 10.10.10.255 no es válido (broadcast), pero 10.10.11.1 sí.## 24. ¿Qué implica "octeto interesante" en cálculos de subredes?

El octeto interesante es aquel cuyo valor en la máscara no es 255 ni 0. Es donde varía la numeración de redes y determina el cálculo del bloque.## 25. ¿Cuántos hosts válidos tiene una subred /29?

Un /29 tiene 8 direcciones, menos 2 reservadas (red y broadcast), quedan **6 hosts válidos**.## 26. ¿Cuál sería el broadcast de 172.16.24.0/22?

/22: bloque de 4. La red es .24.0, el broadcast es .27.255.## 27. Si tienes que asegurar una red con exactamente 6 hosts por subred en clase C, ¿qué máscara empleas?

Para 6 hosts, necesitas h=3 (2^3-2=6), así que el prefijo es /29.## 28. ¿Cómo enumero los rangos de subredes en 192.168.100.0/26?

/26 = bloque 64, redes: .0/26, .64/26, .128/26, .192/26.## 29. En el escenario 10.1.0.0/20, ¿cuál es la dirección de la red número 7?

Bloque = 16; 7×16=112. Por tanto, la red es 10.1.112.0/20.## 30. Al diseñar subredes, ¿cómo calculas cuántos bits adicionales necesitas según los hosts requeridos?

Busca h tal que 2^h - 2 ≥ número de hosts requeridos; la máscara final es el prefijo base + (bits de red + bits de subred necesarios para cubrir los hosts).## 31. Si la IP 10.100.0.0 necesita al menos 20,000 hosts por subred, ¿qué máscara le pones?

h tal que 2^h - 2 ≥ 20,000. 2^15 = 32,768 - 2 = 32,766. Así, necesitas /17 como máscara (255.255.128.0).## 32. En la subred /23 de 172.16.200.0, ¿cuáles son las redes que puedes crear?

/23 tiene bloque 2 en el tercer octeto: redes serían .200.0 y .202.0, etc.## 33. Para una IP 192.168.55.73 con máscara /27, ¿cómo determinas a qué subred pertenece?

Divides 73 entre 32: 73/32=2, 2×32=64. Por tanto, la red es 192.168.55.64/27.## 34. Si una IP termina en .255 y la máscara es /24, ¿es host válido?

No, .255 en /24 es la dirección de broadcast, por tanto no es válida como host.## 35. Cuando te piden 50 subredes con al menos 400 hosts por subred en una red clase A, ¿cómo decides el prefijo?

400 hosts → h=9 (510-2=508 hosts en /23). Para subredes, con /23 tienes b=15, es decir, 32,768 subredes, suficiente.## 36. ¿Cómo identificas si dos IPs están en la misma subred con máscara /20?

Miras el 'octeto interesante' según el bloque (16 en el tercer octeto en /20): ambos deben tener el tercer octeto en el mismo rango.## 37. ¿Por qué el subnetting clásico descuenta siempre 2 direcciones por subred?

Porque una es la red (todos los bits de host en 0) y otra el broadcast (todos en 1), por lo que no pueden usarse como host.## 38. ¿Qué resulta del subnetting de 10.0.0.0/14?

Bloque de 4 en el segundo octeto; subredes desde 0 hasta 252 por saltos de 4.## 39. En la subred 192.168.44.192/26, ¿cuál es su dirección de broadcast?

Bloque de 64. Broadcast: última dirección, .255 en este caso.## 40. ¿Qué implica dividir una red en subredes al nivel de la máscara binaria?

Por cada bit que añades al prefijo, duplicas el número de subredes y divides por la mitad los hosts por subred. El cálculo se basa en manipular los bits de la máscara.## 41. ¿Cómo determinarías si una dirección de host propuesta es la red o broadcast?

Calcula el bloque y el rango; si el host es la primera del rango (red) o la última (broadcast), no es válida.## 42. ¿Qué máscara es idónea para una red de 100 hosts por subred en clase C?

100 hosts → h=7, así /25 (mask 255.255.255.128) es suficiente.## 43. Si te piden 16 subredes a partir de 192.168.1.0/24, ¿qué máscara utilizas?

16 subredes → 4 bits extra → /28 (mask 255.255.255.240), bloques de 16 en el último octeto.## 44. ¿En qué consiste el 'punto a punto' y por qué es típico el uso de /30 o /31?

Son enlaces entre dos routers; /30 da 2 hosts válidos, /31 desde RFC 3021 permite usar las 2 direcciones como hosts (más eficiente).## 45. ¿Cómo listarías rápidamente las subredes posibles en 10.0.0.0/18?

El bloque es 64 en el tercer octeto; redes serían 0, 64, 128, 192 (10.0.0.0/18, 10.0.64.0/18, etc.)## 46. ¿Por qué se utiliza el término 'subred padre' en subnetting jerárquico?

Cuando subdivides una red, cada grupo hijo tiene una máscara más larga que el padre; el padre agrupa todas las subredes hijas. Cada subred hija tiene un rango propio, pero deben pasar por routers para llegar al resto.## 47. ¿Cómo saber si una IP pertenece a la subred de 192.168.1.0/28?

Bloque de 16: la IP debe estar en el rango .0 a .15. Ejemplo: 192.168.1.10 sí pertenece.## 48. ¿Cuál es la diferencia práctica entre tener una red /24 y dividirla en dos /25?

En /24 caben 254 hosts, al dividir en /25 tienes 2 subredes de 126 hosts cada una. Se consigue más control y partición del tráfico y de acceso.## 49. Si necesitas 3000 subredes y cada una debe tener 400 hosts, ¿cómo decides la máscara?

3000 subredes requieren b=12 (/20 si parte de /8); 400 hosts → h=9 (/23). Hay que verificar cuál es el prefijo original y balancear los bits según la clase.## 50. ¿Por qué en redes modernas la planificación de subnetting es esencial para escalabilidad y seguridad?

El subnetting bien planificado permite asignar rangos y máscaras de forma eficiente, facilitando la gestión de tráfico, la expansión futura y una segmentación que mejora la seguridad y la administración de accesos.
