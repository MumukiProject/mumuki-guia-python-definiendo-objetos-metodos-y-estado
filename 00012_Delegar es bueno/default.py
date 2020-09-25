
Pepita = objeto()

Pepita.energia = 1000

Pepita.ciudad = Oberá


def energia_actual(self):
    return self.energia


Pepita.energia_actual = energia_actual


def ciudad_actual(self):
    return self.ciudad


Pepita.ciudad_actual = ciudad_actual


def gastar_energia(self, destino):
    distancia = self.ciudad.distancia_a(destino) #delegamos a  self.ciudad el cálculo de la distancia
    self.energia -= 0.5 * distancia  #usamos lo que nos diga self.ciudad, ojo con el '-='


Pepita.gastar_energia = gastar_energia


def volar_hacia(self, destino):
    self.gastar_energia(destino)
    self.ciudad = destino


Pepita.volar_hacia = volar_hacia


def distancia_a(self, destino):
    # ... completá con tu algoritmo ...
    # ... recordá que tenés una "ayuda" en el enunciado ...
    return #... qué devolvemos? ...
