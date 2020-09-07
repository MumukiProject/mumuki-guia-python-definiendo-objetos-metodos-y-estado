Pepita = objeto()
  
Pepita.energia = 100   

def volar_en_circulos(self):   
  self.energia = self.energia - 10
  pass #ultima línea del procedimiento (pass no tiene efecto, lo usamos principalmente para bloques vacios)

# (fin del proceidmiento por la indentación)
# Seguí por acá...

Pepita.volar_en_circulos = volar_en_circulos
# y por acá ....

