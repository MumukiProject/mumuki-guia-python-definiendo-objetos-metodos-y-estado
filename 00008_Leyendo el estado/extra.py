# module Obera
#
#
# module Iruya
#
#
# module Pepita
#   self.energia = 100
#   self.ciudad = Obera
#
#   def self.energi(self):
#     self.energia
#
#
#   def self.cantar!
#     'pri pri pri'
#
#
#   def self.comer_lombriz!
#     self.energia += 20
#     return
#
#
#   def self.volar_en_circulos!
#     self.energia -= 10
#     return
#
#
#   def self.volar_hacia!(self, destino):
#     self.energia -= 100
#     self.ciudad = destino
#     return
Pepita = objeto()
Pepita.energia = 100

def energia_subir(self, porcentaje):
  # si el argumento en porcentaje es 25, para subir 25%, hay que multiplicar por 1.25
  self.energia = self.energia * (1 + porcentaje / 100)
  return self.energia

Pepita.energia_subir = energia_subir