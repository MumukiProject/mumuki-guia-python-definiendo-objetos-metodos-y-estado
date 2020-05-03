module Pepita
  def self.energi(self):
    self.energia


  def self.reiniciar!
    self.energia = 100



describe 'Pepita':
  it 'tiene inicialmente 100 unidades de energía':
    expect(Pepita.energia).to eq 100


  it 'pierde 10 unidades de energía cuando vuela en círculos':
    Pepita.reiniciar!
    Pepita.volar_en_circulos!
    expect(Pepita.energia).to eq 90


  it 'gana 20 unidades de energía cuando come una lombriz':
    Pepita.reiniciar!
    Pepita.comer_lombriz!
    expect(Pepita.energia).to eq 120

