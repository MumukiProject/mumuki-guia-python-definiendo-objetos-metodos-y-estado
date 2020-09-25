Hay un pequeño problema conceptual con la solución anterior: ¿por qué `Pepita`, una golondrina, es responsable de calcular la distancia entre dos ciudades?

Dicho de otra manera, ¿es _necesario_ contar con una golondrina para poder calcular la distancia entre dos lugares? ¿Cual es el objeto más pequeño que podría saber hacer esto? 

¿Lo pensaste? La respuesta es simple: ¡la misma ciudad! :sunglasses: Por ejemplo, `BuenosAires` podría entender un mensaje `distancia_a(destino)`, que tome otra ciudad y devuelva la distancia entre `destino` y sí misma.  

> Modificá la solución del ejercicio anterior para que sean las ciudades las que calculan las distancias. Pensá que no solo `Oberá` debe tener este método, sino también `BuenosAires`, `Iruya`, `Ushuaia` y `Marambio` para cuando tenga que volver.