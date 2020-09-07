Pepita = objeto()
  
Pepita.energia = 100   

def volar_en_circulos(self):   
  self.energia = self.energia - 10
  #pass no tiene efecto, marca para bloques vacios
  pass #ultima línea del procedimiento 

# (fin del procedimiento por la indentación)
# Seguí por acá...

Pepita.volar_en_circulos = volar_en_circulos
# y por acá ....

