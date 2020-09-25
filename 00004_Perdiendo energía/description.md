Acabamos de aprender una de las reglas fundamentales del envío de mensajes: si a un objeto no le decímos **cómo** reaccionar ante un mensaje, y se lo envíamos, no lo entenderá y nuestro programa se romperá. Y la forma de hacer esto es **declarando un método**.

Ahora bien, los métodos que definiste recién no eran muy interesantes: se trataba de _métodos vacíos_ que evitaban que el programa se rompiera, pero no hacían nada. En realidad, `Pepita` tiene energía y los diferentes mensajes que entiende deberían modificarla.

¿Cómo podríamos decir que cuando `Pepita` vuela een círculos, pierde `10` unidades de energía? ¿Y que inicialmente esta energía es `100`? Así:

```python
ム Pepita = objeto()
ム    
ム Pepita.energia = 100   
ム   
ム def volar_en_circulos(self):   
ム     self.energia = self.energia - 10
ム 
ム Pepita.volar_en_circulos = volar_en_circulos
```

> Una vez más, ya definimos a `Pepita` por vos. Probá, en orden, las siguientes consultas:
>
> ```python
> ム Pepita.volar_en_circulos()
> ム Pepita.volar_en_circulos()
> ム Pepita.energia
> ```
> Puede que los resultados te sorprendan, en breve hablaremos de esto.
