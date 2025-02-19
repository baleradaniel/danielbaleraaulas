venda = input('Registre um produto. ')
vendas = []

while venda != '':
    vendas.append(venda)
    venda = input('Registre um produto. ')
print('Registro Finalizado. As vendas cadastradas foram: {}'.format(vendas))