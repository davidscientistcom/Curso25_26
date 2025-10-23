Positional Encoding (codificación posicional):
Como el Transformer no tiene una estructura recurrente, no “sabe” la posición de cada token por sí solo. Se añade a los embeddings una señal que indica la posición (una codificación posicional, por ejemplo senos/cosenos, o aprendida) para dotar de información de orden.


Que diferencia hay en cada una.
Query (Q), Key (K), Value (V).


Porque?
Se calcula una puntuación (score) entre la query de un elemento y todas las claves K de la secuencia, para determinar cuánto debería “prestar atención” ese elemento a los demás.


Esto no queda bien explicado, no se que es multihead? para frases largas?
En Multi-Head Attention, haces esto en múltiples cabezas con distintas proyecciones lineales de Q, K, V, para que se capture información desde diferentes subespacios.

Que es feed forward
l feed-forward) s