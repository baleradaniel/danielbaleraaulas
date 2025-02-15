nome_clientes = ['daniel', 'caio', 'eberth', 'kaio', 'matheus']
telefone_clientes = [11996791720, 47985730214, 47182930485, 47839210475, 47182391320]
bairro_clientes = ['itinga', 'panagua', 'jarivatuba','comazza', 'bowherwald']

nome = input('Insira o nome do cliente: '.casefold())

if nome in nome_clientes:
    i = nome_clientes.index(nome)
    telefone = telefone_clientes[i]
    bairro = bairro_clientes[i]
    print('Cliente {}: \n Telefone: {} \n Bairro: {}'.format(nome, telefone, bairro).title())
else:
    print('Cliente {} não encontrado! Tente novamente.'.format(nome).title())