En el ejercicio anterior vimos que un objeto (en ese caso, `Pepita`) le puede enviar mensajes a otros objetos que conozca (para `Pepita` son  ciudades como `Oberá` o `BuenosAires`):

```python
Pepita = objeto()
def volar_hacia(self, destino):
    numeroMayor = max(self.ciudad.kilómetro(), destino.kilómetro())  #acá Pepita envía dos mensajes... los ves?
    numeroMenor = min(self.ciudad.kilómetro(), destino.kilómetro())  #envía OTROS dos mensajes... 
    self.energia -= 0.5 * ( numeroMayor - numeroMenor ) #por fin... calculamos! OJO con el '-='
    self.ciudad = destino
Pepita.volar_hacia = volar_hacia
```

Esto se conoce como _delegar una responsabilidad_, o simplemente, **delegar**: la responsabilidad de saber en qué kilómetro se encuentra una ciudad de ese _objeto ciudad_, y no de `Pepita`.

A veces nos va a pasar que un objeto tiene un método muy complejo, y nos gustaría subdividirlo en problemas más chicos que **el mismo objeto** puede resolver. Pero, ¿cómo se envía un objeto mensajes a sí mismo?

Un objeto puede enviarse un mensaje a sí mismo fácilmente usando `self` como receptor del mensaje.

```python
Pepita = objeto()

def gastar_energia(self, destino): #¡Ojo! No hicimos Pepita.gastar_energia!(destino)
    numeroMayor = max(self.ciudad.kilómetro(), destino.kilómetro())  #acá Pepita envía dos mensajes... los ves?
    numeroMenor = min(self.ciudad.kilómetro(), destino.kilómetro())  #envía OTROS dos mensajes... 
    self.energia -= 0.5 * ( numeroMayor - numeroMenor ) #por fin... calculamos! OJO con el '-='


def volar_hacia(self, destino):
    self.gastar_energia(destino)
    self.ciudad = destino

Pepita.gastar_energia = gastar_energia
Pepita.volar_hacia = volar_hacia

```

> Pero esto se puede mejorar un poco más. Delegá el cálculo de la distancia a los objetos que sean ciudades. El nuevo  método de Pepita, llamado `distancia_a`, toma un destino y devuelve la distancia desde la ciudad `self.ciudad` hasta el destino.
> Por ejemplo:   


```Python
ム Pepita.volar_hacia(Ushuaia)
ム Pepita.distancia_a(Marambio)
=> 1200
```