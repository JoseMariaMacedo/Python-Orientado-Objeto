import carro

uno_vermelho = carro.Carro("vermelhor", 4,"Flex", 1.0, 0, False)
uno_vermelho.ligar()
uno_vermelho.abastecer()
uno_vermelho.abastecer()
print(f"A quantidade de combustivel do carro e: {uno_vermelho.qtd_combustivel} litros")