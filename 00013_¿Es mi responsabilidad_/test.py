class Test(unittest.TestCase):

  def test_Oberá_puede_calcular_la_distancia_hasta_Iruya(self):
    """
    # describe 'Obera':
    #   it 'entiende distancia_a':
    #     expect(Obera).to respond_to :distancia_a
    #   it 'puede calcular la distancia hasta Iruya':
    #     expect(Obera.distancia_a(Iruya)).to eq 670
    """
    cartel="La distancia entre Iruya y Oberá es de 670 Km. Tanto de ida, como de vuelta ;)"
    self.assertEqual(Oberá.distancia_a(Iruya),670,cartel)
    self.assertEqual(Iruya.distancia_a(Oberá),670,cartel)

  def test_Marambio_puede_calcular_la_distancia_hasta_Iruya(self):
    cartel="La distancia entre Iruya y Marambio es de 5270 Km. Tanto de ida, como de vuelta ;)"
    self.assertEqual(Marambio.distancia_a(Iruya),5270,cartel)
    self.assertEqual(Iruya.distancia_a(Marambio),5270,cartel)

  def test_BuenosAires_puede_calcular_la_distancia_hasta_Ushuaia(self):
    cartel="La distancia entre Ushuaia y BuenosAires es de 2360 Km. Tanto de ida, como de vuelta ;)"
    self.assertEqual(BuenosAires.distancia_a(Ushuaia),2360,cartel)
    self.assertEqual(Ushuaia.distancia_a(BuenosAires),2360,cartel)





  def test_Pepita_ahora_NO_entiende_el_mensaje_distancia_a(self):
    """
    #   it 'no entiende distancia_a':
    #     expect(Pepita).not_to respond_to :distancia_a
    """
    espero="distancia_a()"
    self.assertFalse(espero in dir(Pepita),
                         "método '{metodo}' tiene no tiene que ser parte de la interfaz de {nombre}".format(metodo=espero,nombre="Pepita"))

  def test_Pepita_no_pierde_energía_si_está_en_Oberá_y_vuela_a_Oberá(self):
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


  def test_Pepita_pierde_520_unidades_de_energía_si_está_en_Buenos_Aires_y_vuela_a_Oberá(self):
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

  def test_Pepita_pierde_520_unidades_de_energía_si_está_en_Oberá_y_vuela_a_Buenos_Aires(self):
    Pepita.volar_hacia(Oberá)
    Pepita.energia=1000
    Pepita.volar_hacia(BuenosAires)
    cartel="al recibir el mensaje {nombre}.volar_hacia({destino}), nuestra golondrina partió de {origen} (km {kmOrigen}) con 1000 de energía. Al llegar a {destino} (km {kmDestino}) tendría que haber perdido 0.5*({kmOrigen}-{kmDestino}) de energía".format(nombre="Pepita",kmOrigen=_Oberá.kilometros,kmDestino=_BuenosAires.kilometros,origen=_Oberá.nombre,destino=_BuenosAires.nombre)
    self.assertEqual(Pepita.energia_actual(),480,cartel)

  def test_Pepita_cambia_de_ciudad_cuando_vuela(self):
    """
    it 'cambia de ciudad cuando vuela':
      Pepita.volar_hacia!(Iruya)
      expect(Pepita.ciudad).to eq Iruya
    """
    Pepita.volar_hacia(BuenosAires)
    Pepita.volar_hacia(Iruya)
    cartel="al recibir el mensaje {nombre}.volar_hacia({destino}), nuestra golondrina tiene que  llegar a {destino}".format(nombre="Pepita",destino=_Iruya.nombre)
    self.assertEqual(Iruya,Pepita.ciudad_actual(),cartel)
