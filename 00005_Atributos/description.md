Analicemos el código que acabamos de escribir:

```ruby
module Pepita
  @energia = 100
  
  def self.volar_en_circulos!
    @energia = @energia - 10
  end
end
```

Decimos que `Pepita` _conoce_ o _tiene_ un nivel de energía, que es variable, e inicialmente toma el valor `100`. La energía es un **atributo** de nuestro objeto, y la forma de **asignarle** un valor es escribiendo `@energia = 100`.

Por otro lado, cuando `Pepita` recibe el mensaje `volar_en_circulos!`, su energía disminuye: se realiza una nueva **asignación** del atributo y pasa a valer lo que valía antes (o sea, `@energia`), menos `10`.

> Sabiendo esto, implementá la versión correcta del método `comer_lombriz!`, que provoca que `Pepita` gane `20` puntos de energía.

