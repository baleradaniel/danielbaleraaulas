pessoas_presente = ['daniel', 'matheus', 'eberth', 'caio', 'kaio']
chamada = 'daniel'
for pessoa in pessoas_presente:
    if pessoa == chamada:
        print('{} está presente.'.format(chamada))
        break
    else:
        print('Só um print para mostrar que o for passou pela pessoa:'+str(pessoa))

pessoas_presente = ['daniel', 'matheus', 'eberth', 'caio', 'kaio']
chamada = 'daniel'
for pessoa in pessoas_presente:
    if pessoa == chamada:
        print('{} está presente.'.format(chamada))
        break
    else:
        print('Só um print para mostrar que o for passou pela pessoa:'+str(pessoa))
        continue
        print('só para mostrar que ')