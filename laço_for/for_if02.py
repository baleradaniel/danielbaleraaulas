vendas = [100,20,110,231,30,21,90,75,45,82,200,123,156,122]
meta = 100
qtde_bateu_meta = 0
for venda in vendas:
    if venda >= meta:
        qtde_bateu_meta += 1
qtde_funcionarios = len(vendas)
print('O percentual de pessoas que bateram a meta foi de {:.1%}'.format(qtde_bateu_meta/qtde_funcionarios))