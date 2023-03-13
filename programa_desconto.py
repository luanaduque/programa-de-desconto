valor = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))

resultado = valor*quantidade

if resultado >= 100:
    print('Voce comprou', resultado,'reais.')
    print('Voce tem', resultado*0.1, 'reais de desconto')
    print('Voce pagará', resultado-resultado*0.1, 'reais')
else:
    print('Infelizmente, voce nao tera desconto, pois nao comprou mais de 100 reais, sua compra ficou: ',resultado)
    
