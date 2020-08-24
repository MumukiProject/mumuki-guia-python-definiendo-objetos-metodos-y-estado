Antes te mostramos que si enviamos el mensaje `energia`, fallará:

```python
ム  Pepita.energia
undefined method `energia' for Pepita:Module (NoMethodError)
```

El motivo es simple: **los atributos NO son mensajes**.

Entonces, ¿cómo podríamos consultar la energía de `Pepita`? Declarando un método, ¡por supuesto!

```python
module Pepita
   #...atributos y métodos anteriores...

   def energi(self):
      self.energia


```

> Ya agregamos el método `energia` por vos. Probá en la consola ahora las siguientes consultas:
>
> ```python
> ム Pepita.energia
> ム Pepita.energia = 120
> ム energia
```
>
> ¿Todas las consultas funcionan? ¿Por qué?