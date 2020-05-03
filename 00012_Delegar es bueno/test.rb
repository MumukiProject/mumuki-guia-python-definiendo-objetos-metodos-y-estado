module Pepita
  def self.ciudad=(una_ciudad)
    @ciudad = una_ciudad
  end
  
  def self.reiniciar!
    @ciudad = Obera
    @energia = 1000
  end
end

describe 'Pepita' do
  before(:each) do
    Pepita.reiniciar!
  end

  it 'entiende gastar_energia!' do
    expect(Pepita).to respond_to :gastar_energia!
  end
  
  it 'entiende distancia_a' do
    expect(Pepita).to respond_to :distancia_a
  end
  
  it 'puede calcular la distancia hasta Iruya, estando en Oberá' do
    expect(Pepita.distancia_a(Iruya)).to eq 670
  end
  
  it 'no pierde energía si está en Oberá y vuela a Oberá' do
    Pepita.volar_hacia!(Obera)
    expect(Pepita.energia).to eq 1000
  end
  
  it 'pierde 520 unidades de energía si está en Buenos Aires y vuela a Oberá' do
    Pepita.ciudad = BuenosAires
    Pepita.volar_hacia!(Obera)
    expect(Pepita.energia).to eq 480
  end
  
  it 'pierde 520 unidades de energía si está en Oberá y vuela a Buenos Aires' do
    Pepita.volar_hacia!(BuenosAires)
    expect(Pepita.energia).to eq 480
  end
  
  it 'pierde 335 unidades de energía si está en Iruya y vuela a Oberá' do
    Pepita.ciudad = Iruya
    Pepita.volar_hacia!(Obera)
    expect(Pepita.energia).to eq 665
  end  
  
  it 'cambia de ciudad cuando vuela' do
    Pepita.volar_hacia!(Iruya)
    expect(Pepita.ciudad).to eq Iruya
  end  
end