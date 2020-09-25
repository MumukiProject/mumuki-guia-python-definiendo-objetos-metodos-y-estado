Analicemos el código que acabamos de escribir:

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

Decimos que `Pepita` _conoce_ o _tiene_ un nivel de energía, que es variable, y le _asignamos_ inicialmente un valor `100`. La energía es un **atributo** de nuestro objeto, y hay dos formas de **asignarle** un valor:
 
 1. en un método del mismo objeto:  `self.atributo = 100`.
 1. por un mensaje al objeto:  `objeto.atributo = 100`.

`self` viene del Inglés, significa _propio_ (en este caso "propio" al objeto en cuestión), y el uso es bastante intuitivo, comparemos como sería Castellano y en Python:

Castellano | Python
---|---
**José** es **cabezón** | josé.cabeza = "grande"
**José** lavó **su auto** | josé.auto = "lavado" 
me duele **la cabeza** | self.cabeza = "dolorida"
lavé **el auto** | self.auto = "lavado"

Entonces, cuando `Pepita` recibe el mensaje `volar_en_circulos()`, su energía disminuye: se realiza una nueva **asignación** del atributo y pasa a valer lo que valía antes (o sea, `self.energia`), menos `10`.
Notá que acá usamos `self.energia` y no `Pepita.energia` porque `volar_en_circulos()` es un método de Pepita

> Sabiendo esto, implementá la versión correcta del método `comer_lombriz()`, que provoca que `Pepita` gane `20` puntos de energía.

