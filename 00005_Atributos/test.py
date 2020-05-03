module Pepita
  def self.energia
    @energia
  end
  
  def self.reiniciar!
    @energia = 100
  end
end

describe 'Pepita' do
  it 'tiene inicialmente 100 unidades de energía' do
    expect(Pepita.energia).to eq 100
  end
  
  it 'pierde 10 unidades de energía cuando vuela en círculos' do
    Pepita.reiniciar!
    Pepita.volar_en_circulos!
    expect(Pepita.energia).to eq 90
  end

  it 'gana 20 unidades de energía cuando come una lombriz' do
    Pepita.reiniciar!
    Pepita.comer_lombriz!
    expect(Pepita.energia).to eq 120
  end
end