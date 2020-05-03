describe 'Pepita entiende el mensaje: ' do
  it 'cantar!' do
    expect(Pepita).to respond_to :cantar!
  end
  
  it 'volar_en_circulos!' do
    expect(Pepita).to respond_to :volar_en_circulos!
  end
  
  it 'comer_lombriz!' do
    expect(Pepita).to respond_to :comer_lombriz!
  end
end