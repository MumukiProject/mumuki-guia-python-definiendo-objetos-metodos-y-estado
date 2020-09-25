sombra_de_Pepita=pajaritoClass()
sombra_de_Pepita.energia = 100
sombra_de_Pepita.ciudad = _Oberá
Pepita_energia_original = Pepita.energia

#pruebas
Pepita=pajaritoClass()
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
  def test_Pepita_tiene_comenzar_en_Iruya_con_100_de_energia(self):
    self.assertEqual(sombra_de_Pepita.energia,Pepita.energia,"Pepita.energia vale {} pero debe comenzar con {}".format(Pepita.energia,sombra_de_Pepita.energia))
    args=dict()
    args["espero"] = sombra_de_Pepita.ciudad.nombre
    args["obtengo"] = Pepita.ciudad
    args["mensaje"] = "Pepita.energia vale {} pero debe comenzar con {}".format(args["obtengo"],args["espero"])
    self.assertEqual(args["espero"],args["obtengo"],args["mensaje"])

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
    ciudades = [_Oberá.nombre, _Iruya.nombre]
    for miCiudad in ciudades:
      args=dict()
      args["member"] = miCiudad
      args["container"] = dir() #__dict__ customizado
      args["mensaje"] = "tienen que existir las {} ciudades {}".format(len(ciudades), ciudades)
      self.assertIn(args["member"],args["container"],args["mensaje"])

    Pepita.volar_hacia(_Oberá.nombre)
    sombra_de_Pepita.volar_hacia(ciudad_destino=_Oberá,energia_fija=100) #cambia el comportamiento
    args=dict()
    args["espero"] = sombra_de_Pepita.ciudad.nombre
    args["obtengo"] = Pepita.ciudad
    args["mensaje"] = "Pepita.energia vale {} pero debe comenzar con {}".format(args["obtengo"],args["espero"])
    self.assertEqual(args["espero"],args["obtengo"],args["mensaje"])


  def test_Pepita_cambia_de_ciudad_cuando_vuela(self):
    # it 'cambia de ciudad cuando vuela':
    #   Pepita.volar_hacia!(Obera)
    #   expect(Pepita.ciudad).to eq Obera
    ciudades = [_Oberá, _Iruya]
    for miCiudad in ciudades:
      sombra_de_Pepita.volar_hacia(miCiudad)
      Pepita.volar_hacia(miCiudad)
      args=dict()
      args["espero"] = sombra_de_Pepita.ciudad.nombre
      args["obtengo"] = Pepita.ciudad
      args["mensaje"] = "Pepita.ciudad vale '{obtengo}' pero debe valer '{espero}' luego del mensaje Pepita.volar_hacia({espero})".format(obtengo=args["obtengo"],espero=args["espero"])
      self.assertEqual(args["espero"],args["obtengo"],args["mensaje"])


