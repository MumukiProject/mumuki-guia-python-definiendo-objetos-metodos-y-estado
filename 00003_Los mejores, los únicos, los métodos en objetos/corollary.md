Perfecto, ahora `Pepita` entiende casi todos los mismos mensajes que en la lección anterior. Pero, ¿hacen lo mismo?

Antes de seguir, enviá algunos de los mensajes en la **Consola** y fijate qué *efecto* producen sobre nuestra golondrina.

Notaste la sutileza de que *primero* definimos un procedimiento *suelto*:   

```python   
ム #definimos un procedimiento:   
ム def procedimiento(self):   
```

 y *luego* le "enseñamos" a Pepita ese procedimiento:   

```python  
ム Pepita.cantar = procedimiento  
ム Pepita.cantar()   
"priiiip priiiip soy Pepita"  
ム 
```

Esa secuencia,  aunque se usa a veces,  **no es** normal en Python (para la alternativa, tendrás que completar ésta guía y pasar a la siguiente) :stuck_out_tongue: :satisfied: