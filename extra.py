# traer de la Biblioteca: ciudades: ['BuenosAires', '_Buenos_Aires', '_Iruya', '_Obera', '_Oberá', '_Ushuaia']
#<elipsis-for-student@
import types,collections

ciudad_anterior = collections.namedtuple("ciudad_anterior", "nombre energia_partida")

class ciudadClass:
  def __init__(self,nombre="Estación Espacial Internacional",kilometros=36000):
    self._nombre=nombre
    self._kilometros=kilometros

  @property
  def nombre(self):
    return self._nombre

  @nombre.setter
  def nombre(self,ahora_vale):
    raise ValueError("'nombre' vale '{}', se fijó durante su  creación y no se puede cambiar".format(self.nombre))
    return None

  @property
  def kilometros(self): #compatibilidad para atras?
    return self._kilometros

  def distancia_con(self, una_ciudad): #compatibilidad para atras?
    #   def self.distancia(self, una_ciudad):
    #     (self.ciudad.kilometro - una_ciudad.kilometro).abs
    return abs(self.kilometros - una_ciudad.kilometros)


  def distancia_a(self, una_ciudad):
    """
    usamos en l2/ej11/extra.py

    :param una_ciudad:
    :return:
    """
    #   def self.distancia(self, una_ciudad):
    #     (self.ciudad.kilometro - una_ciudad.kilometro).abs
    numeroMayor = max(self.kilómetro(), una_ciudad.kilómetro())
    numeroMenor = min(self.kilómetro(), una_ciudad.kilómetro())
    return numeroMayor - numeroMenor

  def kilómetro(self):
    """
    usamos en l2/ej11/extra.py

    :param una_ciudad:
    :return:
    """
    return self._kilometros

  def __repr__(self):
    return self.nombre

class pajaritoClass():
  pio='priiiip priiiip'

  def __init__(self,nombre="Pajarito"):
    self.nombre=nombre
    self._ciudad=None
    self._energia=100 #ej10
    self.ciudades_anteriores=list()


  def __eq__(self,other):
    # necesario para 00003_El derecho a la Identidad
    # TODO: obj1==obj2 no funciona en el runner
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
    #energia.setter
    #
    #   def self.energia=(self, una_energia):
    #     self.energia = una_energia
    #   def self.energi(self):
    #     self.energia
    self._energia=ahora_vale     #validacion?


  @property
  def ciudad(self):
    return self._ciudad

  @ciudad.setter
  def ciudad(self,ahora_es):
    #ciudad.setter: validacion? TODO: usar volar_hacia() ?
    self._ciudad=ahora_es

  def cantar(self):
    #   def self.cantar!
    #     'pri pri pri'
    return type(self).pio

  def comer_lombriz(self):
    #   def self.comer_lombriz!
    #     self.energia += 20
    #     return
    self.energia += 20 #ej10
    return self.energia

  def comer_alpiste(self,energia_adicional):
    #   def self.comer_alpiste!(self, una_energia):
    #     self.energia += una_energia * 15
    #     return
    self.energia += energia_adicional * 15 #TODO: validar entrada
    # no seria mejor asi:
    #def comer_alpiste(self, gramos):
    # energia_adicional = gramos * 15
    # self.energia += energia_adicional
    return self.energia

  def volar_en_circulos(self):
    #   def self.volar_en_circulos!
    #     self.energia -= 10
    #     return
    self.energia -= 10 #ej10
    return self.energia

  def volar_hacia(self, ciudad_destino,energia_fija=0):
    #   def self.volar_hacia!(self, una_ciudad):
    #     self.energia -= self.distancia(una_ciudad) * 3
    #     self.ciudad = una_ciudad
    #     return

    if self.ciudad is None:
      nombre_desde = None
    else:
      nombre_desde = self.ciudad.nombre
    volar_desde=ciudad_anterior(nombre=nombre_desde, energia_partida=self.energia)
    if True:# TODO: validar energia necesaria, energia actual, destino
      if energia_fija > 0:
        self.energia -= energia_fija
      else:
        self.ciudades_anteriores.append(volar_desde)
        if self.ciudad is not None:
          self.energia -= self.ciudad.distancia_con(ciudad_destino) * 3
      self.ciudad = ciudad_destino
    else:
      pass
    return self.ciudad

_Marambio = ciudadClass("Marambio",-1200) #https://es.wikipedia.org/wiki/Base_Marambio

_Ushuaia = ciudadClass("Ushuaia",0) # cercana al centro geográfico de Argentina según https://www.ign.gob.ar/gallery-app/mapas-escolares/medium/argentina_bicontinental_fisico.jpg

_BuenosAires = ciudadClass("BuenosAires",2360) #CABA está lejos de muuchas ciudades, incluyendo al centro geográfico de Argentina: https://es.wikipedia.org/wiki/Ushuaia
_Buenos_Aires = _BuenosAires

_Iruya=ciudadClass(nombre="Iruya", kilometros=4070) #mantinene distancia con BuenosAires, pero no respeta https://es.wikipedia.org/wiki/Ushuaia

_Oberá=ciudadClass(nombre="Oberá", kilometros=3400) #mantinene distancia con BuenosAires según https://es.wikipedia.org/wiki/Ushuaia
_Obera=_Oberá
#@elipsis-for-student>

# traer de la Biblioteca: clases: ['objeto']
#<elipsis-for-student@
class objeto:
  def __init__(self,nombre="Sin Nombre"):
    self._attrs = dict()
    self._attrs["nombre"]=nombre

  def __setattr__(self, name, value):
    if name == '_attrs':
      super().__setattr__(name, value)
    elif isinstance(value, types.FunctionType):
      self._attrs[name] = value.__get__(self, objeto)
    else:
      self._attrs[name] = value

  def __getattr__(self, name):
    if name == '_attrs':
      return super().__getattr__(name)
    elif name in self._attrs.keys():
      return self._attrs[name]
    else: #AttributeError: 'object' object has no attribute 'dasd'
      raise  AttributeError("object has no attribute '{name}' (atributo '{name}' no encontrado )".format(name=name))

  def __dir__(self):
    result = [ attr for attr in self._attrs.keys() if not attr.startswith("_") ]
    for idx,mensaje in enumerate(result):
      if isinstance(self._attrs[mensaje], types.MethodType):
        result[idx]=result[idx]+"()"
    return result
#@elipsis-for-student>

# traer de la Biblioteca: objeto: ['Pepita']
#<elipsis-for-student@
Pepita=objeto(nombre="Sin Nombre")

def __repr__(self):
  pio = "priiiip priiiip"
  result = pio + " soy " + self.nombre
  return result

Pepita.__repr__=__repr__
Pepita.energia=100
#@elipsis-for-student>
