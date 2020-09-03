#module Pepita
class pajaritoClass():
  pio='priiiip priiiip'

  def __init__(self,nombre="Pajarito"):
    self.nombre=nombre
    self._ciudad=None
    self._energia=100 #ej10
    self.ciudades_anteriores=list()


  def __eq__(self,other):
    result = (id(self)==id(other))
    return result

  def cantar(self):
    result = type(self).pio
    return result

  def __repr__(self):
    result=type(self).pio+" soy "+self.nombre
    return result

  @property
  def energia(self):
    return self._energia

  @energia.setter
  def energia(self,ahora_vale):
    self._energia=ahora_vale     #validacion?


  @property
  def ciudad(self):
    return self._ciudad

  @ciudad.setter
  def ciudad(self,ahora_es):
    #ciudad.setter: validacion? TODO: usar volar_hacia() ?
    self._ciudad=ahora_es

  def cantar(self):
    return type(self).pio

  def comer_lombriz(self):
    self.energia += 20 #ej10
    return self.energia

  def comer_alpiste(self,energia_adicional):
    self.energia += energia_adicional * 15 #TODO: validar entrada
    return self.energia

  def volar_en_circulos(self):
    self.energia -= 10 #ej10
    return self.energia

  def volar_hacia(self, ciudad_destino):
    if self.ciudad is None:
      nombre_desde = None
    else:
      nombre_desde = self.ciudad.nombre
    volar_desde=ciudad_anterior(nombre=nombre_desde, energia_partida=self.energia)
    if True:# TODO: validar energia necesaria, energia actual, destino
      self.ciudades_anteriores.append(volar_desde)
      if self.ciudad is not None:
        self.energia -= self.ciudad.distancia_con(ciudad_destino) * 3
      self.ciudad = ciudad_destino
    else:
      pass
    return self.ciudad

Pepita = pajaritoClass(nombre="Pepita")
Pepita.energia = 100
Pepita.ciudad = Oberá
