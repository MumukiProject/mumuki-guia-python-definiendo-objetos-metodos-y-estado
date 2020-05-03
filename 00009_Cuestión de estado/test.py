describe 'Estado de' do
  it 'Pepita' do
    expect(estado_pepita).to match_array ['energia', 'ciudad']
  end

  it 'Kiano1100' do
    expect(estado_kiano1100).to eq []
  end

  it 'RolamotoC115' do
    expect(estado_rolamotoC115).to eq []
  end  
  
  it 'Enrique' do
    expect(estado_enrique).to match_array ['celular', 'dinero_en_billetera', 'frase_favorita']
  end
end