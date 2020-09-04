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

    def test_interfaz_de_Pepita_tiene_todos_los_mensajes_que_entiende(self):
        interfaz_esperada = ["cantar()", "comer_lombriz()", "volar_en_circulos()"]
        interfaz_entregada = interfaz_Pepita

        self.assertEqual(set(interfaz_esperada), set(interfaz_entregada),
                         "la interfaz de {nombre} es algo como {iface}".format(nombre="Pepita", iface=interfaz_ejemplo))

    def test_interfaz_de_Pepita_con_palabras_en_minusculas(self):
        interfaz_esperada = ["cantar()", "comer_lombriz()", "volar_en_circulos()"]
        interfaz_entregada = interfaz_Pepita
        todos_minusculas = all([str(x).islower() for x in interfaz_entregada])
        self.assertTrue(todos_minusculas,
                        mayusminus + " La interfaz de {nombre} tiene todas palabras en minúsculas (que pueden estar unidas por espacios subrayados), es algo como {iface}".format(
                            nombre="Pepita", iface=interfaz_ejemplo))