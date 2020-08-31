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
  def kilometros(self):
    return self._kilometros

  def distancia_con(self, una_ciudad):
    #   def self.distancia(self, una_ciudad):
    #     (self.ciudad.kilometro - una_ciudad.kilometro).abs
    return abs(self.kilometros - una_ciudad.kilometros)

  def __repr__(self):
    return self.nombre

Ushuaia = ciudadClass("Ushuaia",0) # cercana al centro geográfico de Argentina según https://www.ign.gob.ar/gallery-app/mapas-escolares/medium/argentina_bicontinental_fisico.jpg

BuenosAires = ciudadClass("BuenosAires",2360) #CABA está lejos de muuchas ciudades, incluyendo al centro geográfico de Argentina: https://es.wikipedia.org/wiki/Ushuaia
Buenos_Aires = BuenosAires

Iruya=ciudadClass(nombre="Iruya", kilometros=4070) #mantinene distancia con BuenosAires, pero no respeta https://es.wikipedia.org/wiki/Ushuaia

Oberá=ciudadClass(nombre="Oberá", kilometros=3400) #mantinene distancia con BuenosAires según https://es.wikipedia.org/wiki/Ushuaia
Obera=Oberá


class objeto:
  def __init__(self):
    self._attrs = {}

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
    else:
      return self._attrs[name]

  def __repr__(self):
    if '__repr__' in self._attrs:
      return self._attrs['__repr__']()
    else:
      return super().__repr__()

