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
    self.energia -= 0.5 * (
                max(self.ciudad.kilómetro(), destino.kilómetro()) - min(self.ciudad.kilómetro(), destino.kilómetro()))


Pepita.gastar_energia = gastar_energia


def volar_hacia(self, destino):
    self.gastar_energia(destino)
    self.ciudad = destino


Pepita.volar_hacia = volar_hacia


def distancia_a(self, destino):
    #...completar con tu algoritmo...
    return #...completar con tu algoritmo...