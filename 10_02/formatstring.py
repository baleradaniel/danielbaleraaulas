faturamento = 2000
custo = 500
lucro = faturamento - custo
print('O faturamento da loja foi de : {}'.format(faturamento))

faturamento = 2000
custo = 500
lucro = faturamento - custo
print('O faturamento da loja foi de : {} O custo foi de: {} O lucro foi de: {}'.format(faturamento, custo, lucro))

faturamento = 2000
custo = 500
lucro = faturamento - custo
print('O faturamento da loja foi de : {0} O custo foi de: {1} O lucro foi de: {2}'.format(faturamento, custo, lucro))

# Uso do %s e %d

faturamento = 2000
custo = 500
lucro = faturamento - custo
print('O faturamento da loja foi de : %s' % faturamento)

faturamento = 2000
custo = 500
lucro = faturamento - custo
print('O faturamento da loja foi de : %d' % faturamento)

# Uso do in

email = 'danielbalera@gmail.com'
print('@' in 'balera@')