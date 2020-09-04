_¿Otra vez `AttributeError: object has no attribute...`? ¿Y ahora qué falta?_ :rage:

Para que un objeto entienda un mensaje debemos "enseñarle" cómo hacerlo, y para ello es necesario declarar un **método** dentro de ese objeto:

```python
ム #definimos un procedimiento:
ム def cantar(self):
ム   #línea1 del procedimiento
ム   #línea2 del procedimiento
ム   #línea3 del procedimiento
ム
ム Pepita.cantar = cantar
```

y luego podrás _invocar_ tu método así:

```python
ム Pepita.cantar()
"priiiip priiiip soy Pepita"
```



Un método es, entonces, la descripción de **qué hacer** cuando se recibe un mensaje del mismo nombre.

> Agregale a la definición de `Pepita` los métodos necesarios para que pueda responder a los mensajes `cantar()`, `comer_lombriz()` y `volar_en_circulos()`.   
>**No** es necesario que hagan nada en particular.
