module Pepita
  def self.ciudad=(self, una_ciudad):
    self.ciudad = una_ciudad


  def self.reiniciar!
    self.ciudad = Obera
    self.energia = 1000



describe 'Buenos Aires':
  it 'entiende distancia_a':
    expect(BuenosAires).to respond_to :distancia_a



describe 'Obera':
  it 'entiende distancia_a':
    expect(Obera).to respond_to :distancia_a


  it 'puede calcular la distancia hasta Iruya':
    expect(Obera.distancia_a(Iruya)).to eq 670



describe 'Iruya':
  it 'entiende distancia_a':
    expect(Iruya).to respond_to :distancia_a



describe 'Pepita':
  before(:each):
    Pepita.reiniciar!


  it 'no entiende distancia_a':
    expect(Pepita).not_to respond_to :distancia_a


  it 'no pierde energía si está en Oberá y vuela a Oberá':
    Pepita.volar_hacia!(Obera)
    expect(Pepita.energia).to eq 1000


  it 'pierde 520 unidades de energía si está en Buenos Aires y vuela a Oberá':
    Pepita.ciudad = BuenosAires
    Pepita.volar_hacia!(Obera)
    expect(Pepita.energia).to eq 480


  it 'pierde 520 unidades de energía si está en Oberá y vuela a Buenos Aires':
    Pepita.volar_hacia!(BuenosAires)
    expect(Pepita.energia).to eq 480


  it 'pierde 335 unidades de energía si está en Iruya y vuela a Oberá':
    Pepita.ciudad = Iruya
    Pepita.volar_hacia!(Obera)
    expect(Pepita.energia).to eq 665


  it 'cambia de ciudad cuando vuela':
    Pepita.volar_hacia!(Iruya)
    expect(Pepita.ciudad).to eq Iruya

