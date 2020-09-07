# module Pepita
#   def self.energi(self):
#     self.energia
#
#
#   def self.ciuda(self):
#     self.ciudad
sombra_de_Pepita=pajaritoClass()
sombra_de_Pepita.energia = 100
Pepita_energia_original = Pepita.energia

# describe '':
#   it 'Iruya existe':
#     expect(Iruya).to be
# no hace falta

# it 'Obera existe':
#   expect(Obera).to be
# no hace falta

# context 'Pepita':
#   it 'empieza con 100 de energía':
#     expect(Pepita.energia).to eq 100


class Test(unittest.TestCase):
  # it 'empieza en Iruya':
  #     expect(Pepita.ciudad).to eq Iruya
  def Pepita_tiene_comenzar_con_100_de_energia(self):


    it 'entiende el mensaje volar_hacia!':
      expect(Pepita).to respond_to :volar_hacia!


    it 'pierde 100 unidades de energía cuando vuela':
      Pepita.volar_hacia!(Obera)
      expect(Pepita.energia).to eq 0


    it 'cambia de ciudad cuando vuela':
      Pepita.volar_hacia!(Obera)
      expect(Pepita.ciudad).to eq Obera


