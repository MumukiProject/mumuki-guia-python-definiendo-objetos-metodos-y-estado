class Test(unittest.TestCase):
  # it 'empieza en Iruya':
  #     expect(Pepita.ciudad).to eq Iruya
  def test_Pepita_tiene_comenzar_en_Iruya_con_100_de_energia(self):
    self.assertEqual(100,Pepita.energia,"Pepita.energia vale {} pero debe valer {}".format(Pepita.energia,100))
    self.assertEqual(Iruya,Pepita.ciudad,"Pepita.ciudad vale {} pero debe valer {}".format(Pepita.ciudad,Iruya))

  def test_Pepita_entiende_el_mensaje_volar_hacia(self):
    # it 'entiende el mensaje volar_hacia!':
    #   expect(Pepita).to respond_to :volar_hacia!
    args=dict()
    args["member"] = "volar_hacia()"
    args["container"] = dir(Pepita) #__dict__ customizado
    args["mensaje"] = "Pepita tiene que entender el mensaje {}, por ahora entiende {}".format(args["member"],args["container"])
    self.assertIn(args["member"],args["container"],args["mensaje"])

  def test_Pepita_pierde_100_unidades_de_energía_cuando_vuela(self):
    # it 'pierde 100 unidades de energía cuando vuela':
    #   Pepita.volar_hacia!(Obera)
    #   expect(Pepita.energia).to eq 0
    Pepita.energia = 200
    Pepita.volar_hacia(Oberá)
    energía_antes=Pepita.energia
    Pepita.volar_hacia(Iruya)
    self.assertEqual(Pepita.energia,energía_antes-100,"al volar de Oberá a Iruya, Pepita.energía, debió perder 100, por ejemplo: pasar de {} a {}".format(Pepita.energia,energía_antes-100) )
    energía_antes=Pepita.energia
    Pepita.volar_hacia(Oberá)
    self.assertEqual(Pepita.energia,energía_antes-100,"al volar de Iruya a Oberá, Pepita.energía, debió perder 100, por ejemplo: pasar de {} a {}".format(Pepita.energia,energía_antes-100) )


  def test_Pepita_cambia_de_ciudad_cuando_vuela(self):
    """
    it 'cambia de ciudad cuando vuela':
      Pepita.volar_hacia!(Iruya)
      expect(Pepita.ciudad).to eq Iruya
    """
    Pepita.volar_hacia(Oberá)
    Pepita.volar_hacia(Iruya)
    cartel="al recibir el mensaje {nombre}.volar_hacia({destino}), nuestra golondrina tiene que  llegar a {destino}".format(nombre="Pepita",destino=_Iruya.nombre)
    self.assertEqual(Iruya,Pepita.ciudad,cartel)
