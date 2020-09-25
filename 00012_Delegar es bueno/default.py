Pepita = objeto()

Pepita.energia = 1000

Pepita.ciudad = Oberá

def ciudad_actual(self):
    return self.ciudad

Pepita.ciudad_actual = ciudad_actual

def gastar_energia(self, destino):
    numeroMayor = max(self.kilómetro(), destino.kilómetro())  # acá Pepita envía dos mensajes... los ves?
    numeroMenor = min(self.kilómetro(), destino.kilómetro())  # envía OTROS dos mensajes...
    self.energia -= 0.5 * ( numeroMayor - numeroMenor )
  
Pepita.gastar_energia = gastar_energia

def volar_hacia(self, destino):
  self.gastar_energia(destino)
  self.ciudad = destino

Pepita.volar_hacia = volar_hacia

