Antes te mostramos que podemos *declarar* nuevos atributos de un objeto:

```python
ム  Pepita=objeto()
ム  Pepita.energia=100
```

Veamos que pasa si enviamos el mensaje `energia()` al objeto `Pepita`:

```python
ム  Pepita.energia("subir 20%")
TypeError: 'int' object is not callable
```
Por qué fallará? :confused:

El motivo es simple: **los atributos NO son mensajes**.

Entonces, ¿cómo podríamos incrementar la energía de `Pepita`? Declarando un *método*, ¡por supuesto!

```python
Pepita=objeto()
#...atributos y métodos anteriores...
Pepita.energia=100

def energia_subir(self,porcentaje):
    self.energia = self.energia * (1 + porcentaje / 100) # para subir 25%, multiplicamos por 1.25
    return self.energia 
    
```

> Ya agregamos el método `energia_subir` por vos. Probá en la consola ahora las siguientes consultas:
>
> ```python
> ム Pepita.energia
> ム Pepita.energia = 10
> ム Pepita.energia  #comentario: si, de nuevo... devuelve 10?
> ム Pepita.energia_subir(50)  #tiene que devolver 15, porque sube 50% 
> ム Pepita.energia_subir(100) #tiene que devolver 30
> ム Pepita.energia_subir      #solo por curiosidad, no es mensaje porque le falta el ()
> ム energia_subir()   # este tiene que fallar
```
>
> ¿Todas las consultas funcionan? ¿Por qué?
