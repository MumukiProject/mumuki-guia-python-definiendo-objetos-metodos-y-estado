describe 'Estado de':
  it 'Pepita':
    expect(estado_pepita).to match_array ['energia', 'ciudad']


  it 'Kiano1100':
    expect(estado_kiano1100).to eq []


  it 'RolamotoC115':
    expect(estado_rolamotoC115).to eq []


  it 'Enrique':
    expect(estado_enrique).to match_array ['celular', 'dinero_en_billetera', 'frase_favorita']

