from re import T
from smtplib import quotedata
from tkinter.tix import Tree


class Carro():
    def __init__(self, cor, qtd_portas, tipo_combustivel, potencia, qtd_combustivel, is_ligado, velociade ):
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = qtd_combustivel
        self.is_ligado = is_ligado
        self.velociade = velociade
        
    def abastecer(self, qtd_combustivel):
        self.qtd_combustivel += qtd_combustivel
        
    def ligar(self):
        if self.is_ligado:
            print("O carro já está ligado")
        else:
            self.is_ligado = True
            print("O carro foi ligado")
            
    def desligar(self):
        if self.is_ligado == False:
            print("O carro já está desligado")
        else:
            self.is_ligado = False
        
        
    
        
        