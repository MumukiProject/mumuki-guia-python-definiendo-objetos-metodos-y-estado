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
    cartel="el método {nombre}.ciudad_actual() tiene devolver al atributo {nombre}.ciudad".format(nombre="Pepita")
    self.assertEqual(Pepita.ciudad_actual(),Pepita.ciudad,cartel)

  def test_existen_las_ciudades_del_enunciado(self):
    for identificador_esperado in ("BuenosAires","Oberá","Iruya"):
      cartel="tiene que existir el objeto {identificador_esperado}".format(identificador_esperado=identificador_esperado)
      
    BuenosAires.nombre="BuenosAires"
    Iruya.nombre="Iruya"
    Oberá.nombre="Oberá"
  def test_las_ciudades_saben_en_qué_kilómetro_están(self):
    for c, cnombre, km in ((BuenosAires, _BuenosAires.nombre, _BuenosAires.kilometros),
                                 (Oberá,_Oberá.nombre,_Oberá.kilometros), (Iruya,_Iruya.nombre,_Iruya.kilometros)):
      cartel="el mensaje {identificador}.kilómetro() tiene que devolver {km}".format(identificador=cnombre, km=km)
      self.assertEqual(c.kilómetro(), km, cartel)
      pass

  def test_no_pierde_energía_si_está_en_Oberá_y_vuela_a_Oberá(self):
    """
      it 'no pierde energía si está en Oberá y vuela a Oberá':
        Pepita.volar_hacia!(Obera)
        expect(Pepita.energia).to eq 1000
    """
    cartel="el método {nombre}.volar_hacia() tiene mantener la energía sin cambios cuando el argumento de entrada es el mismo que {nombre}.ciudad_actual()".format(nombre="Pepita")
    Pepita.volar_hacia(BuenosAires)
    energia_antes=Pepita.energia_actual()
    Pepita.volar_hacia(BuenosAires)
    self.assertEqual(Pepita.energia_actual(),energia_antes,cartel)


  def test_pierde_520_unidades_de_energía_si_está_en_Buenos_Aires_y_vuela_a_Oberá(self):
    """
    it 'pierde 520 unidades de energía si está en Buenos Aires y vuela a Oberá':
      Pepita.ciudad = BuenosAires
      Pepita.volar_hacia!(Obera)
      expect(Pepita.energia).to eq 480
    """
    Pepita.volar_hacia(BuenosAires)
    Pepita.energia=1000
    Pepita.volar_hacia(Oberá)
    cartel="al recibir el mensaje {nombre}.volar_hacia({destino}), nuestra golondrina partió de {origen} (km {kmOrigen}) con 1000 de energía. Al llegar a {destino} (km {kmDestino}) tendría que haber perdido 0.5*({kmDestino}-{kmOrigen}) de energía".format(nombre="Pepita",kmDestino=_Oberá.kilometros,kmOrigen=_BuenosAires.kilometros,destino=_Oberá.nombre,origen=_BuenosAires.nombre)
    self.assertEqual(Pepita.energia_actual(),480,cartel)

  def test_pierde_520_unidades_de_energía_si_está_en_Oberá_y_vuela_a_Buenos_Aires(self):
    Pepita.volar_hacia(Oberá)
    Pepita.energia=1000
    Pepita.volar_hacia(BuenosAires)
    cartel="al recibir el mensaje {nombre}.volar_hacia({destino}), nuestra golondrina partió de {origen} (km {kmOrigen}) con 1000 de energía. Al llegar a {destino} (km {kmDestino}) tendría que haber perdido 0.5*({kmOrigen}-{kmDestino}) de energía".format(nombre="Pepita",kmOrigen=_Oberá.kilometros,kmDestino=_BuenosAires.kilometros,origen=_Oberá.nombre,destino=_BuenosAires.nombre)
    self.assertEqual(Pepita.energia_actual(),480,cartel)

  def test_cambia_de_ciudad_cuando_vuela(self):
    """
    it 'cambia de ciudad cuando vuela':
      Pepita.volar_hacia!(Iruya)
      expect(Pepita.ciudad).to eq Iruya
    """
    Pepita.volar_hacia(BuenosAires)
    Pepita.volar_hacia(Iruya)
    cartel="al recibir el mensaje {nombre}.volar_hacia({destino}), nuestra golondrina tiene que  llegar a {destino}".format(nombre="Pepita",destino=_Iruya.nombre)
    self.assertEqual(Iruya,Pepita.ciudad_actual(),cartel)

