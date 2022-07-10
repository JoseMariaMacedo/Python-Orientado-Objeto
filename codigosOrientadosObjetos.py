import carro

uno_vermelho = carro.Carro("vermelhor", 4,"Flex", 1.0, 0, False, 0)
uno_vermelho.ligar()
uno_vermelho.abastecer(21)
uno_vermelho.abastecer(10)
print(f"A quantidade de combustivel do carro e: {uno_vermelho.qtd_combustivel} litros")

ford_preto = carro.Carro("preto", 4,"Flex", 1.5, 0, False, 0)
ford_preto.ligar()
ford_preto.acelerar(35)
print(f"A velocidade do carro e: {ford_preto.velocidade} Km/h")
