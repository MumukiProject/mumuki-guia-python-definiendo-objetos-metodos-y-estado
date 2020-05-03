module Pepita
  def self.ciudad=(una_ciudad)
    @ciudad = una_ciudad
  end
  
  def self.reiniciar!
    @ciudad = Obera
    @energia = 1000
  end
end

describe 'BuenosAires' do
  it 'existe' do 
    expect(BuenosAires).to be
  end
  
  it 'sabe en qué kilómetro está' do
    expect(BuenosAires.kilometro).to eq 0
  end
end

describe 'Obera' do
  it 'sabe en qué kilómetro está' do
    expect(Obera.kilometro).to eq 1040
  end
end

describe 'Iruya' do
  it 'sabe en qué kilómetro está' do
    expect(Iruya.kilometro).to eq 1710
  end
end

describe 'Pepita' do
  before(:each) do
    Pepita.reiniciar!
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