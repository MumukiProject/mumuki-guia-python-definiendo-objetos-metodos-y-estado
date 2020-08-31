class Test(unittest.TestCase):
    def test_00001_Pepita_existe(self):
        nuevo_identificador = "Pepita"
        self.assertIn(nuevo_identificador, dir(),"{} tiene que existir (con ese 'identificador', mayúsculas/minúsculas, etc)".format(nuevo_identificador))


    def test_00002_Pepita_es_un_objeto(self):
        nuevo_identificador = "Pepita"
        self.assertIsInstance(Pepita, objeto, "'{}' tiene que ser del tipo 'objeto'".format(nuevo_identificador))
