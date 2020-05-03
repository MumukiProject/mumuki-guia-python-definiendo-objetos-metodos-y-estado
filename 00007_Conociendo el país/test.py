module Pepita
  def self.energi(self):
    self.energia


  def self.ciuda(self):
    self.ciudad



describe '':
  it 'Iruya existe':
    expect(Iruya).to be


  it 'Obera existe':
    expect(Obera).to be


  context 'Pepita':
    it 'empieza con 100 de energía':
      expect(Pepita.energia).to eq 100


    it 'empieza en Iruya':
      expect(Pepita.ciudad).to eq Iruya


    it 'entiende el mensaje volar_hacia!':
      expect(Pepita).to respond_to :volar_hacia!


    it 'pierde 100 unidades de energía cuando vuela':
      Pepita.volar_hacia!(Obera)
      expect(Pepita.energia).to eq 0


    it 'cambia de ciudad cuando vuela':
      Pepita.volar_hacia!(Obera)
      expect(Pepita.ciudad).to eq Obera


