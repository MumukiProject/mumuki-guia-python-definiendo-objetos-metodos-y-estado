describe 'Pepita' do
  it 'entiende el mensaje ciudad' do
    expect(Pepita).to respond_to :ciudad
  end
  
  it 'comienza en Oberá' do
    expect(Pepita.ciudad).to eq Obera
  end
end