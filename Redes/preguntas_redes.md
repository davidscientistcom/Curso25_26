# 50 preguntas fundamentales de redes (con razonamiento)

1. **¿Por qué las redes permiten ahorrar costes en una empresa?**

   Si varios usuarios pueden compartir una impresora o almacenamiento gracias a la red, se evita comprar un aparato por cada persona. Así, los recursos se aprovechan mejor y se reducen los gastos en hardware.

2. **Define brevemente qué es una red de comunicaciones.**

   Es un conjunto de dispositivos (nodos) interconectados (por cable o inalámbricos) que comparten recursos e información.

3. **¿Por qué es importante que los dispositivos de red usen estándares abiertos en sus protocolos?**

   Los estándares abiertos permiten que equipos de distintos fabricantes sean compatibles y la red funcione aunque se mezclen marcas y modelos.

4. **¿Qué ventajas ofrece la segmentación de tráfico por departamentos usando VLANs en una empresa con una sola red física? Razona la respuesta.**

   Una sola red física puede estar virtualmente separada en varias "subredes lógicas" mediante VLANs, de modo que el tráfico de Administración no se mezcle con el de Ventas. Así se mejora la seguridad (menos exposición), la organización (fácil administración) y el rendimiento (menos tráfico inútil).

5. **Pon un ejemplo de situación en la que sería imprescindible acceder a la red local de la empresa desde fuera. ¿Qué protocolo usarías?**

   Si el responsable de sistemas necesita hacer mantenimiento fuera de la oficina, accedería por SSH, que cifra la conexión y permite un canal seguro desde cualquier punto de Internet.## Modelos, capas y razonamiento (OSI/TCP-IP)

6. **Explica por qué el modelo OSI puede ayudar a diagnosticar problemas de red incluso si no se implementa literalmente en las redes modernas.**

   El modelo OSI divide la red en "capas" con funciones concretas. Si hay un fallo, permite aislarlo: si el hardware funciona pero fallan los nombres de dominio, probablemente el error está en la capa de Aplicación o Presentación. Eso ahorra tiempo al técnico.

7. **¿En qué se diferencian los modelos OSI y TCP/IP y por qué TCP/IP es el usado realmente en Internet?**

   OSI tiene 7 capas y es teórico; TCP/IP usa 4 capas agrupando funciones para simplificar la implementación. TCP/IP fue adoptado por el DoD y después por Internet, por su robustez y flexibilidad.

8. **¿Por qué separar en capas el funcionamiento de una red ayuda a los fabricantes, programadores y técnicos?**

   Cada capa tiene estándares y protocolos propios, así los fabricantes pueden crear componentes independientes que funcionen juntos, mientras los técnicos pueden solucionar fallos sin conocer a fondo todo el sistema.

9. **¿Qué función cumple la encapsulación de datos y por qué es esencial para la comunicación entre dispositivos de diferentes redes?**

   Cada capa añade su "cabecera" con información propia, permitiendo a cada extremo leer lo que necesita y dejando que el resto pase sin cambios. Esto posibilita la interoperabilidad entre sistemas distintos.

10. **Explica cómo interactúan direcciones IP y MAC en el envío de un paquete fuera de la red local.**

    La dirección IP identifica el destino final entre redes, pero la red local solo entiende MAC. El gateway traduce la IP de salida a su propia MAC (usando ARP), permitiendo que el paquete salga por la interfaz física adecuada.## Subredes, direccionamiento y planificación

11. **Razona el objetivo de dividir una red grande en subredes más pequeñas (subnetting).**

    Permite aislar el tráfico localmente, reducir el dominio de broadcast, aumentar la seguridad y optimizar el uso de direcciones IP. Así, el fallo en una subred no afecta a todas.

12. **En una empresa con cuatro departamentos, ¿por qué no basta usar solo una LAN y se recomienda subredes o VLANs?**

    Cuando todos están en la misma red, todo el tráfico circula por igual y hay más posibilidades de congestión y riesgos de acceso indebido. Dividir en subredes o VLANs aísla usuarios y facilita la gestión de permisos y acceso.

13. **¿Cómo repartirías la red 192.168.1.0/24 para 5 departamentos de hasta 30 usuarios cada uno, utilizando subredes? Explica el razonamiento.**

    Cada subred necesita al menos 32 direcciones (para 30 hosts útiles, 1 network, 1 broadcast). /27 da 32 direcciones. 192.168.1.0/27 (0-31), 192.168.1.32/27 (32-63), etc. Así, puedes dividirla en 8 subredes de 32 direcciones, suficiente para los 5 departamentos.

14. **¿Para qué sirve el comando `ipconfig` (o `ifconfig` en Linux) y cómo ayuda en el diagnóstico de red?**

    Muestra información de las interfaces de red: IP asignada, máscara, puerta de enlace. Permite verificar si el PC está correctamente configurado y conectado.

15. **Si tienes una red local con DHCP, ¿qué problema puedes tener si asignas manualmente la misma IP a dos dispositivos distintos?**

    Provoca un conflicto de IP: ambos piensan que tienen derecho a esa IP y los paquetes pueden llegar al dispositivo "equivocado" o ser descartados, generando cortes de red.## Equipamiento y tecnologías

16. **¿En qué se parecen y en qué se diferencian un switch y un router?**

    Ambos interconectan dispositivos, pero el switch opera en la capa 2 (Enlace de Datos), dirige el tráfico dentro de una LAN según la MAC. El router opera en capa 3 (Red), conecta redes diferentes (LAN, WAN) encaminando por IP.

17. **¿Qué característica convierte al switch en "inteligente" frente a un hub?**

    El switch sólo reenvía tramas al puerto concreto donde está el destino, minimizando colisiones, mientras que el hub reenvía a todos los puertos indiscriminadamente.

18. **Explica para qué situación práctica podría usarse un router con NAT dinámico y por qué es preferible usar PAT (NAT con sobrecarga) en una red doméstica.**

    NAT dinámico asigna una IP pública de un pool a cada dispositivo; es útil solo cuando tienes varias IPs públicas. En entornos domésticos, donde hay una sola IP pública, se usa PAT que asigna puertos distintos para cada dispositivo, permitiendo compartir la IP pública.

19. **¿Qué ventaja tiene un punto de acceso (AP) respecto a compartir la WiFi desde el propio portátil?**

    El AP da estabilidad, cobertura profesional, control de usuarios y seguridad ampliada. Compartir WiFi desde un portátil es poco robusto, con opciones limitadas y corta distancia.

20. **¿Por qué la dirección MAC no puede usarse para enrutar paquetes fuera de la red local?**

    Porque solo es válida en el alcance del segmento LAN (capa 2); los routers ignoran la MAC y solo se basan en la dirección IP (capa 3) para enviar el paquete fuera.## Ejercicios prácticos y de razonamiento

21. **Tienes que montar una empresa virtual de cuatro departamentos usando VLANs. Explica cómo configuras el switch y qué problemas resuelves al hacerlo.**

    Configuras una VLAN distinta por departamento, asignas cada puerto del switch a una VLAN (por ejemplo, puertos 1-5 a VLAN 10, 6-10 a VLAN 20, etc). Así, los usuarios de una VLAN no pueden ver el tráfico de las otras, lo que mejora seguridad y control. Ninguna configuración física rompe la conectividad; solo alterarías la configuración.

22. **Razona por qué, al conectar dos switches para compartir VLANs, no basta un cable "normal" y necesitas configurar un enlace troncal (trunk).**

    El trunk permite que el tráfico de todas las VLANs viaje etiquetado entre los switches; si solo usas un cable normal configurado como acceso, solo una VLAN circula y pierdes la segmentación entre switches. El trunk etiqueta los paquetes (802.1Q), manteniendo la separación lógica.

23. **Explica la secuencia del proceso DHCP cuando un PC nuevo se conecta a la red de la empresa.**

    Envía un broadcast DHCP Discover para buscar servidores. El servidor responde con una oferta; el PC acepta con un DHCP Request, y recibe una confirmación (ACK) con su nueva IP, máscara, puerta de enlace y DNS. Es un proceso de 4 pasos y se repite cada vez que cambia de red o expira el 'lease'.

24. **¿Por qué es mejor tener un servidor FTP en la subred de servidores y no en una de usuarios (por ejemplo, Matemáticas) para compartir modelos con Informática?**

    Centralizas la administración, reduces problemas de permisos, evitas que un fallo de usuario afecte al servicio y puedes controlar mejor la seguridad y los accesos desde otros departamentos.

25. **En una oficina se cae toda la red al desconectar un cable principal. ¿Cuál es la topología y qué harías diferente para evitar ese problema?**

    Es una topología en Bus: todos los equipos dependen de un único cable de backbone y si se rompe, todos pierden conexión. Para evitarlo se recomienda topología en Estrella, con cada nodo conectado al switch central; si un cable falla, solo afecta a ese nodo.## Avanzadas y razonamiento aplicado

26. **En una empresa grande ¿por qué usarías subredes y VLANs aun teniendo direcciones IP libres para todos?**

    Porque mucha gente en una sola red aumenta el dominio de broadcast y el tráfico inútil; segmentar minimiza colisiones y facilita políticas de seguridad adaptadas a cada área, como recursos solo accesibles para Finanzas, etc.

27. **¿Qué ventajas aporta la gestión centralizada de switches y APs mediante software (rede definida por software o SDN) frente a la configuración manual?**

    La gestión centralizada te permite hacer cambios rápidos para toda la red (crear VLAN, cambiar reglas de acceso) sin ir físicamente a cada dispositivo, reduce errores humanos y escalas la red con facilidad.

28. **Si un cliente remoto no puede conectarse por SSH a un servidor, ¿qué pasos de diagnóstico seguirías usando el modelo de capas?**

    Compruebo primero si tiene red local (física y enlace), después si la IP y gateway están bien (red), si responde al ping (ICMP, red), si hay cortafuegos que permitan el puerto (transporte), y por último los logs de SSH en aplicación.

29. **Explica cómo NAT ayuda a proteger la red interna de accesos no autorizados.**

    Los dispositivos internos sólo son accesibles desde fuera mediante reglas específicas; NAT oculta las IPs privadas. Cualquier intento de acceder sin una redirección configurada es bloqueado por el router.

30. **En una empresa con muchos empleados móviles conectados por WiFi, ¿por qué segregar la WiFi de invitados en una VLAN separada de la WiFi del personal?**

    Así se impide que los dispositivos de invitados accedan a recursos internos (archivos, impresoras empresariales), se gestiona fácilmente el ancho de banda para los visitantes y se mejora la seguridad al aislar el tráfico personal del corporativo.## Profundización y aplicaciones reales

31. **¿Por qué es importante que los dispositivos de red soporten el estándar 802.1Q cuando usas VLANs en varios switches?**

    802.1Q define cómo se etiquetan los paquetes de VLAN; sin esa compatibilidad, los switches no podrían intercambiar tráfico segmentado entre sí, y la red virtual quedaría rota.

32. **¿Qué significa que un switch actúe en la capa 2 del modelo OSI y un router en capa 3? Razona la consecuencia práctica.**

    El switch solo se fija en las MACs y es ideal para conectar equipos en la misma red física. El router mira IPs y permite conectar diferentes redes (por ejemplo, la LAN interna y la WAN/Internet); por eso para salir a Internet siempre necesitas un router al final.

33. **Explica con razonamiento cómo un paquete enviado por HTTP pasa desde la aplicación hasta Internet y luego regresa al usuario.**

    El navegador construye una petición (Aplicación), la codifica (Presentación), abre una sesión (Sesión), se encapsula y se ordena TCP (Transporte), se le añade IP (Red), la MAC para el envío local (Enlace), y se transmite (Física). Por cada salto, los routers quitan y ponen la cabecera de IP según destino. Al llegar, el proceso se invierte.

34. **¿Por qué se recomienda limitar la difusión de broadcast en una red grande? ¿Cómo afecta a la eficiencia?**

    El tráfico broadcast interrumpe a todos los dispositivos en la red, incluso cuando no es relevante para ellos. Si la red es muy grande, esto puede saturarla; segmentar en VLANs o subredes lo reduce, mejorando el rendimiento general.

35. **¿Para qué sirve la dirección de broadcast de una subred y cómo se calcula en 192.168.10.0/28? Razona y explica el procedimiento.**

    Sirve para que los nodos envíen mensajes a todos los hosts de la subred. En /28, tienes bloques de 16 direcciones (2^4). Para 192.168.10.0/28, el broadcast es la última dirección del bloque: 192.168.10.15.## Casos prácticos y comandos

36. **En una red bien configurada ¿por qué un servidor puede tener IP fija y los clientes IP dinámica asignada por DHCP?**

    Un servidor debe ser siempre localizable; si su IP cambia, los servicios fallarían. Los clientes usan IP dinámica porque así se aprovechan automáticamente las IPs libres y se evita configuración manual.

37. **Explica la diferencia lógica entre una máscara de subred 255.255.255.0 y 255.255.255.192, e indica cuántos hosts útiles permite cada una.**

    255.255.255.0 equivale a /24, permite 254 hosts útiles (2^8-2). 255.255.255.192 es /26, permite 62 hosts útiles (2^6-2).

38. **¿Cómo afecta el TTL en los paquetes IP y por qué bajarlo puede ayudar en ciertos escenarios?**

    El TTL limita la vida total de un paquete. Si es bajo, el paquete se descarta rápido (evita bucles). Bajarlo es útil en entornos controlados o pruebas para que los paquetes no circulen infinitamente si hay un fallo de enrutamiento.

39. **¿Por qué es relevante conocer el puerto de destino en protocolos de capa 4, como HTTP (80/tcp) o SSH (22/tcp)?**

    Porque el puerto indica qué servicio debe atender la petición; si se bloquea un puerto por firewall, no podrás conectar ni aunque la IP sea correcta.

40. **Si 'ping' a una dirección funciona pero no 'ssh', ¿en qué capa está el problema y cómo razonas para localizarlo?**

    'Ping' usa ICMP (red), así que la conectividad física y la IP funcionan. Si 'ssh' no va, probablemente el fallo está en capa Aplicación (el servicio SSH no corre) o en capa Transporte (el puerto 22 está bloqueado o filtrado).## Pensamiento crítico y problemas reales

41. **Explica por qué el diseño de subredes afecta a la facilidad de escalabilidad y gestión futura de una red.**

    Si planeo subredes justas, cualquier crecimiento obliga a modificar toda la estructura. Si diseño con margen, es más fácil añadir departamentos o dispositivos sin rehacer toda la topología.

42. **¿Qué ventajas prácticas tiene configurar reservas DHCP en una oficina para impresoras o dispositivos específicos?**

    Asegura que siempre reciben la misma IP sin configurarlas a mano, facilitando el acceso (todo el mundo sabe dónde están) y evitando conflictos de IP en el futuro.

43. **Razona por qué, en una red con switches y routers de diferentes fabricantes, sería prioritario elegir estándares comunes en protocolos y configuración.**

    Distintos fabricantes pueden implementar funciones propietarias incompatibles. Usar estándares comunes garantiza que los dispositivos funcionarán juntos y será más fácil actualizar o reemplazar equipos sin depender de un solo proveedor.

44. **Explica por qué usar un servidor DNS propio en una empresa puede mejorar la disponibilidad y el control, comparado con usar DNS del proveedor de Internet.**

    El DNS propio puede configurarse para resolver nombres internos o caché localmente, acelerando la respuesta y dando resiliencia ante caídas externas. Además, da control sobre qué dominios pueden o no resolverse desde dentro.

45. **¿Por qué la longitud del cable Ethernet (CAT5/6) suele limitarse a 100 metros? ¿Qué ocurre si sobrepasas esa distancia y cómo lo razonamos?**

    A más longitud, mayor atenuación y posibilidades de interferencia y pérdida de señal. Si superas 100m, puedes sufrir errores, lentitud o pérdida total de la conexión; la red solo está garantizada y probada para funcionar dentro de ese rango.## Seguridad y eficiencia

46. **Si tienes dos dispositivos en distintas subredes, ¿por qué no pueden comunicarse directamente aunque estén en la misma red física y qué solución aplicarías?**

    Porque cada subred es un dominio lógico; sin un router entre ambas, los paquetes no pueden moverse de una red a otra aunque estén en la misma máquina física. Solución: configurar un router o una interfaz con varias subredes (multi-homed).

47. **¿Cómo ayuda la autenticación SSH basada en claves a la seguridad de la red frente a las contraseñas estándar?**

    Las claves públicas son virtualmente imposibles de adivinar, mientras que una contraseña puede ser forzada por ataques de diccionario. Usar claves de 2048 bits añade un nivel de seguridad mucho mayor que una contraseña típica.

48. **Razona por qué una red WiFi empresarial debería usar WPA2-Enterprise en vez de WPA2-Personal.**

    WPA2-Personal usa una sola contraseña para todos; si alguien sale de la empresa, debe cambiarse en todos los dispositivos. WPA2-Enterprise gestiona credenciales individuales mediante un servidor (RADIUS), facilitando el control de acceso.

49. **¿Por qué un ataque de suplantación IP (spoofing) amenaza la integridad de la red? ¿Cómo lo mitigarías?**

    Alguien que suplanta una IP válida puede interceptar o lanzar ataques dentro de la red; mitigas el riesgo filtrando ARP, usando switches administrables, y activando medidas como listados de control de acceso (ACLs) y detección de intrusos.

50. **Cuando creas una VLAN de invitados con acceso solo a Internet (no a la red interna), ¿qué mejoras consigues a nivel de seguridad y administración? Razona cómo se implementa esta separación.**

    El tráfico de la VLAN de invitados no puede alcanzar recursos corporativos, minimizando vectores de ataque. Se logra configurando reglas en el router o switch de capa 3, permitiendo únicamente tráfico hacia el gateway de Internet y bloqueando el acceso a subredes corporativas.