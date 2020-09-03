En el ejercicio anterior vimos que un objeto (en ese caso, `Pepita`) le puede enviar mensajes a otro que conozca (en ese caso, ciudades como `Obera` o `BuenosAires`):

```python
module Pepita
  # ...etc...

  def self.volar_hacia(self, destino):
    self.energia -= (self.ciudad.kilometro - destino.kilometro).abs / 2
    self.ciudad = destino


```

Esto se conoce como _delegar una responsabilidad_, o simplemente, **delegar**: la responsabilidad de saber en qué kilómetro se encuentra es de la ciudad, y no de `Pepita`.

A veces nos va a pasar que un objeto tiene un método muy complejo, y nos gustaría subdividirlo en problemas más chicos que **el mismo objeto** puede resolver. Pero, ¿cómo se envía un objeto mensajes a sí mismo?

Un objeto puede enviarse un mensaje a sí mismo fácilmente usando `self` como receptor del mensaje.

```python
module Pepita
  # ...etc...

  def self.volar_hacia(self, destino):
    self.gastar_energia!(destino) #¡Ojo! No hicimos Pepita.gastar_energia!(destino)
    self.ciudad = destino


  def self.gastar_energia!(self, destino):
    self.energia -= (self.ciudad.kilometro - destino.kilometro).abs / 2


```

> Pero esto se puede mejorar un poco más. Delegá el cálculo de la distancia en un método `distancia_a`, que tome un destino y devuelva la distancia desde la ciudad actual hasta el destino.
