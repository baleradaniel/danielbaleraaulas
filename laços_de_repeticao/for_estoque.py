estoque = [120,130,111,23,456,234,623,12,24,79,31,70,21]
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del vale', 'red bull', 'dolly', 'itubaina', 'java', 'python', 'sql']
nivel_minimo = 50
for i,qtde in enumerate(estoque):
    if qtde < nivel_minimo:
        print(produtos[i], qtde)
