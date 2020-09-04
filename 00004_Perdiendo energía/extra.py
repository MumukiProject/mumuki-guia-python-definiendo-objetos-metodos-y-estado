def volar_en_circulos(self):
    self.energia = self.energia - 5
    self.energia -= 5  #linea equivalente a la anterior... x - 10 == x - 5 - 5
    return self.energia

Pepita.volar_en_circulos = volar_en_circulos