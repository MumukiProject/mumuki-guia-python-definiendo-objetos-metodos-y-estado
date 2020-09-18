
class Test(unittest.TestCase):

  def test_Pepita_entiende_el_mensaje_ciudad__actual(self):
    """
    it 'entiende el mensaje ciudad':
      expect(Pepita).to respond_to :ciudad
    """
    espero="ciudad_actual()"
    self.assertTrue(espero in dir(Pepita),
                         "método '{metodo}' tiene qe ser parte de la interfaz de {nombre}".format(metodo=espero,nombre="Pepita"))

  def test_el_mensaje_ciudad__actual_devuelve_el_atributo_ciudad(self):
    """
      it 'comienza en Oberá':
        expect(Pepita.ciudad).to eq Obera
    """
    cartel="método {nombre}.ciudad_actual() tiene devolver al atributo {nombre}.ciudad".format(nombre="Pepita")
    self.assertEqual(Pepita.ciudad_actual(),Pepita.ciudad,cartel)



