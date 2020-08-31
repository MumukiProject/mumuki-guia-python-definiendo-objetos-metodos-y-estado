#...content...#

class Test(unittest.TestCase):
  def test_Pepita_es_un_objeto(self):
      nuevo_identificador = "Pepita"
      self.assertIsInstance(Pepita, objeto, "'{}' tiene que ser del tipo 'objeto'".format(nuevo_identificador))
