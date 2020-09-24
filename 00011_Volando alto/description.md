Volar de ciudad en ciudad no es tarea tán fácil: en realidad, `Pepita` pierde tanta energía como la mitad de kilómetros que tenga que recorrer.

Si por ejemplo la distancia hasta la próxima ciudad fuese de 1200 kilómetros, `Pepita` necesitaría 600 unidades de energía cambiar de ciudad.

Aunque en el mapa real no sea así, imaginaremos que las ciudades están ubicadas en línea recta, para facilitar los cálculos:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python-definiendo-objetos-metodos-y-estado/master/assets/ciudades.png" width="500" />

Entonces, para ir de Ushuaia a BuenosAires, `Pepita` necesitaría 1190 unidades de energía, calculadas como 0.5*(2390-0) 

Otro ejemplo: para ir de Oberá a Marambio , `Pepita` necesitaría 2300 unidades de energía, calculadas como 0.5*(3400-(-1200)) 

Es decir, siempre se resta el número mas positivo al numero menos positivo.

> Sabiendo esto:
>
> * Creá el objeto que representa a `BuenosAires`.
> * Agregá a `Oberá`, `Iruya` y `BuenosAires` un mensaje `kilómetro()` que devuelva la altura a la que se encuentran, según el esquema. ¡Ojo! No tenés que guardar el valor en un atributo `self.kilometro` sino simplemente devolver el número que corresponde.
> * Modificá el método `volar_hacia()` de `Pepita` la lógica necesaria para hacer el cálculo y alterar la energía. Para acceder al kilometro inicial de `Pepita` tenes que hacer `self.ciudad.kilometro()`

Para que el ejemplo tenga sentido, vamos a hacer que `Pepita` arranque con la energía en 1000.
