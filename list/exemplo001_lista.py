Lista1 = [1,2,3,4,5]
Lista2 = [6,7,8,9,10]
Lista3 = [11,12,13,14,15]
todas_listas = [Lista1,Lista2,Lista3]
print(todas_listas)

produtos = ['tv','celular','mouse','teclado','tablet']
print(produtos[1])

vendas = [1000, 1500, 350, 270, 900]
print('as vendas de {} foram de {}'.format(produtos[1],vendas[1]))

i = produtos.index('mouse')
print('o valor de i é '+ str(i))
print('o produto da posição i é '+ str(produtos[i]))

produtos = ['tv','celular','tablet','mouse','teclado','geladeira','forno']
estoque = [100,150,100,120,70,180,80]

produto = input('Insira o nome do produto em letra minuscula ')
if produto in produtos:
    i = produtos.index(produto)
    qtde_estoque = estoque[i]
    print('Temos {} unidades de {} no estoque'.format(qtde_estoque,produto))
else:
    print('{} não existe no estoque'.format(produto))
