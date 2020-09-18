Pepita = objeto()

Pepita.energia = 100

def energia_subir(self, porcentaje):
  self.energia = self.energia * (1 + porcentaje / 100)  # para subir 25%, multiplicamos por 1.25
  return self.energia

