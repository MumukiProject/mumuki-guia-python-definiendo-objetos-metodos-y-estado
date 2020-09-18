mayusminus = "para Python, 'A' no es el mismo que 'a'."
interfaz_ejemplo = "['atributo1','atributo_dos']"


class Test(unittest.TestCase):

    def test_estado_Norita_con_palabras_en_minusculas(self):
        interfaz_entregada = estado_norita
        todos_minusculas = all([str(x).islower() for x in interfaz_entregada])
        self.assertTrue(todos_minusculas,
                        mayusminus + " el estado de {nombre} tiene todas palabras en minúsculas (que pueden estar unidas por espacios subrayados), es algo como {iface}".format(
                            nombre="Norita", iface=interfaz_ejemplo))

    def test_estado_Norita_tiene_todos_los_atributos(self):
        """  it 'Pepita':
            expect(estado_pepita).to match_array ['energia', 'ciudad']
        """
        interfaz_esperada = ["energia","ciudad"]
        interfaz_entregada = estado_norita

        self.assertEqual(set(interfaz_esperada), set(interfaz_entregada),
                         "el estado de {nombre} es algo como {iface}".format(nombre="Norita", iface=interfaz_ejemplo))



    def test_estado_Kiano1100_tiene_la_cantidad_de_miembros_correcta(self):
      """
        it 'Kiano1100':
        expect(estado_kiano1100).to eq []
      """
      interfaz_ejemplo = []
      interfaz_entregada = estado_kiano1100
      self.assertEqual(len(interfaz_ejemplo),len(interfaz_entregada),
                mayusminus + " el estado de {nombre} tiene mas (o menos) miembros de lo esperado. La lista es algo como {iface}".format(
                  nombre="Kiano1100", iface=interfaz_ejemplo))

    def test_estado_Kiano1100_tiene_la_cantidad_de_miembros_correcta(self):
      """
        it 'Kiano1100':
        expect(estado_kiano1100).to eq []
      """
      interfaz_ejemplo = []
      interfaz_entregada = estado_kiano1100
      self.assertEqual(len(interfaz_ejemplo),len(interfaz_entregada),
                " el estado de {nombre} tiene {cantidad} miembros, no es la cantidad esperada. La lista es algo como {iface}".format(
                  cantidad=len(interfaz_entregada), nombre="Kiano1100", iface=interfaz_ejemplo))

    def test_estado_RolamotoC115_tiene_la_cantidad_de_miembros_correcta(self):
      """
        it 'RolamotoC115':
        expect(estado_RolamotoC115).to eq []
      """
      interfaz_ejemplo = []
      interfaz_entregada = estado_rolamotoC115
      self.assertEqual(len(interfaz_ejemplo),len(interfaz_entregada),
                " el estado de {nombre} tiene {cantidad} miembros, no es la cantidad esperada. La lista es algo como {iface}".format(
                  cantidad=len(interfaz_entregada), nombre="RolamotoC115", iface=interfaz_ejemplo))


    def test_estado_Enrique_con_palabras_en_minusculas(self):
        interfaz_entregada = estado_Enrique
        todos_minusculas = all([str(x).islower() for x in interfaz_entregada])
        self.assertTrue(todos_minusculas,
                        mayusminus + " el estado de {nombre} tiene todas palabras en minúsculas (que pueden estar unidas por espacios subrayados), es algo como {iface}".format(
                            nombre="Enrique", iface=interfaz_ejemplo))

    def test_estado_Enrique_tiene_todos_los_atributos(self):
        """   it 'Enrique':
            expect(estado_enrique).to match_array ['celular', 'dinero_en_billetera', 'frase_favorita']
        """
        interfaz_esperada = ['celular', 'dinero_en_billetera', 'frase_favorita']
        interfaz_entregada = estado_Enrique
        self.assertEqual(set(interfaz_esperada), set(interfaz_entregada),
                         "el estado de {nombre} es algo como {iface}".format(nombre="Enrique", iface=interfaz_ejemplo))

