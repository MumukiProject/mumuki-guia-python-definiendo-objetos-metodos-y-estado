### primero declaramos las ciudades
Marambio = objeto()

def kilométro(self):
    return -1200

Marambio.kilométro = kilométro


Oberá = objeto()

def kilométro(self):
    #return  ... completar acá...

Oberá.kilométro = kilométro

Iruya = objeto()

def kilométro(self):
    # completar acá...

Iruya.kilométro = kilométro

### ahora declaramos a Pepita
Pepita = objeto()

Pepita.energia = 1000

Pepita.ciudad = Obera

def energia_actual(self):
    """
    primer método de acceso a atributos (o "accessor")

    :param self:  es necesario para que una funcion pueda ser miembro de un objeto
    :return: devuelve el valor del atributo self.energia
    """
    return self.energia

Pepita.energia_actual = energia_actual

def ciudad_actual(self):
    return  self.ciudad

Pepita.ciudad_actual = ciudad_actual


def volar_hacia(self, destino):
    self.energia = 0# completar acá...
    self.ciudad = destino
    return self.ciudad


# agregar a volar_ciudad como miembro de Pepita