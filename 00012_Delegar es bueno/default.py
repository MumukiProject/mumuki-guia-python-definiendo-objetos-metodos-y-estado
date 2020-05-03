module Pepita
  self.energia = 1000
  self.ciudad = Obera

  def self.energi(self):
    self.energia


  def self.ciuda(self):
    self.ciudad


  def self.cantar!
    'pri pri pri'


  def self.comer_lombriz!
    self.energia += 20


  def self.volar_en_circulos!
    self.energia -= 10


  def self.volar_hacia!(self, destino):
    self.gastar_energia!(destino)
    self.ciudad = destino


  def self.gastar_energia!(self, destino):
    self.energia -= (self.ciudad.kilometro - destino.kilometro).abs / 2

