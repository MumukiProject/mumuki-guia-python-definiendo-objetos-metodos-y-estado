# module Pepita
#   def self.energi(self):
#     self.energia
#
#
#   def self.reiniciar!
#     self.energia = 100

#describe 'Pepita entiende el mensaje: ':
#  it 'cantar!':
#    expect(Pepita).to respond_to :cantar!


#  it 'volar_en_circulos!':
#    expect(Pepita).to respond_to :volar_en_circulos!


#  it 'comer_lombriz!':
#    expect(Pepita).to respond_to :comer_lombriz!

mayusminus = "para Python, 'A' no es el mismo que 'a'."
interfaz_ejemplo = "['mensaje1','mensaje2()']"

class Test(unittest.TestCase):

  def test_comer_lombriz_incrementa_en_20_la_energia(self):
      Pepita_energia_original = 100
      Pepita.energia = Pepita_energia_original
      Pepita_energia_esperado = Pepita.energia + 20
      Pepita.comer_lombriz()
      self.assertEqual(Pepita_energia_esperado, Pepita.energia,
                       "Pepita.energia valía originalmente {original}, luego del mensaje comer_lombriz() debió quedar con {esperado}".format(original=Pepita_energia_original, esperado=Pepita_energia_esperado))

  def test_volar_en_circulos_decrementa_en_10_la_energia(self):
    Pepita_energia_original = 100
    Pepita.energia = Pepita_energia_original
    Pepita_energia_esperado = Pepita.energia - 10
    Pepita.volar_en_circulos()
    self.assertEqual(Pepita_energia_esperado, Pepita.energia,
                     "Pepita.energia valía originalmente {original}, luego del mensaje volar_en_circulos() debió quedar con {esperado}".format(
                       original=Pepita_energia_original, esperado=Pepita_energia_esperado))

  def test_tus_procedimientos_usan_la_nueva_sintaxis(self):
    import inspect
    pass


#
#
# describe 'Pepita':
#   it 'tiene inicialmente 100 unidades de energía':
#     expect(Pepita.energia).to eq 100
#
#
#   it 'pierde 10 unidades de energía cuando vuela en círculos':
#     Pepita.reiniciar!
#     Pepita.volar_en_circulos!
#     expect(Pepita.energia).to eq 90
#
#
#   it 'gana 20 unidades de energía cuando come una lombriz':
#     Pepita.reiniciar!
#     Pepita.comer_lombriz!
#     expect(Pepita.energia).to eq 120

