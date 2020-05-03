_¿Otra vez `undefined method`? ¿Y ahora qué falta?_ :rage:

Para que un objeto entienda un mensaje debemos "enseñarle" cómo hacerlo, y para ello es necesario declarar un **método** dentro de ese objeto:

```ruby
module Pepita
   def self.cantar!
   end
end
```

Un método es, entonces, la descripción de **qué hacer cuando se recibe un mensaje del mismo nombre**. 

> Agregale a la definición de `Pepita` los métodos necesarios para que pueda responder a los mensajes `cantar!`, `comer_lombriz!` y `volar_en_circulos!`.