Los objetos pueden tener múltiples atributos y al conjunto de estos atributos se lo denomina **estado**.
Por ejemplo, démosle un estado a `Pepita`:

```python
ム Oberá = objeto()
ム Pepita = objeto()
ム #...atributos y métodos anteriores...
ム Pepita.energia = 100
ム Pepita.ciudad = Oberá
ム #...etc...
```

Lo que podemos observar es que su estado está conformado por `ciudad` y `energia`, dado que son sus atributos. 

Ahora démosle su  estado a `Norita`:

```python
ム Norita.energia = 50 # parte del estado de Norita
ム Norita.ciudad = None  # parte del estado de Norita
```

Es de notar que el *estado* es siempre parte del **espacio de nombres** de un objeto, es decir, una variable "vive" en ese *espacio de nombres* independientemente de los otros espacios de nombres.  

Lo que explica las diferencias entre las salidas a las  siguientes sentencias:

```python
ム energia
ム ciudad
ム Pepita.energia
ム Pepita.ciudad
ム Norita.energia
ム Norita.ciudad
```

Veamos si se entiende... hacé lo siguiente: 

> 1) solapa `>_Consola`: probá las sentencias anteriores   
> 2) solapa `</>Biblioteca`: recorré los objetos declarados   
> 3) solapa `✐ Solución`: listá todos los estado de los objetos anteriores   

