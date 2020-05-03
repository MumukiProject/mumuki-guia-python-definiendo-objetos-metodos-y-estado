describe 'Pepita':
  it 'entiende el mensaje ciudad':
    expect(Pepita).to respond_to :ciudad


  it 'comienza en Oberá':
    expect(Pepita.ciudad).to eq Obera

