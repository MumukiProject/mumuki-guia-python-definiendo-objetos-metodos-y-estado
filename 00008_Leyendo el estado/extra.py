Pepita = objeto()

Pepita.energia = 100

def energia_subir(self, porcentaje):
  factor = (1 + porcentaje / 100)  # para subir 25%, multiplicamos por 1.25
  self.energia *= factor # o sea, self.energia = self.energia * factor
  self.energia = int(self.energia)
  return self.energia

Pepita.energia_subir = energia_subir

del(energia_subir)