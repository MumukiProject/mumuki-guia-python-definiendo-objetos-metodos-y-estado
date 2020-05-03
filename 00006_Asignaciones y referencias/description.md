Miremos este método con más detenimiento: 

```ruby
def volar_en_circulos!
   @energia = @energia - 10
end
```

Lo que estamos haciendo es cambiar la energía de `Pepita`: pasa de su valor actual, `@energia`, a ese valor menos `10`. Por ejemplo, pasa de `100` a `90`. ¿Significa esto que el `100` _se transforma_ en un `90` ? :frowning: :thought_balloon:

No, en absoluto. En objetos trabajamos con **referencias**: `energia` (un atributo) es una referencia a un objeto, que inicialmente _apunta_  al objeto `100`. Si pensamos a los objetos como círculos y las referencias como flechas, podemos graficarlo de la siguiente manera:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-ruby-definiendo-objetos-metodos-y-estado/master/assets/pepita-energia-100.png" width="300" />

Luego, la operación de asignación cambia ese apuntador, que pasa a referenciar al `90`:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-ruby-definiendo-objetos-metodos-y-estado/master/assets/pepita-energia-90.png" width="300" />

En este caso se da una particularidad: el objeto asignado a la referencia es el resultado de **enviar el mensaje** `-` al objeto apuntado originalmente por la referencia: `@energia = @energia - 10`. Y como esta operación es tan común, se puede escribir de una forma más corta: `@energia -= 10`.

> Reescribí los métodos que hiciste en el ejercicio anterior para que usen cuando puedan el `-=`, y su contrapartida, el `+=`.
