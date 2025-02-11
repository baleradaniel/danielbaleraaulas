#Transforma apenas a primeira letra de uma string em maiuscula
nome = 'daniel'
print(nome.capitalize(),'\n')

#Transforma todas as letras em minusculas
nome = 'DANIEL'
print(nome.casefold(),'\n')

#Conta o numero de vezes que um caractere especifico aparece na string.
nome = 'danielbalera@gmail.com'
print(nome.count('d'),'\n')

#Retorna true ou false para um teste se a string termina com uma string especifica.
nome = 'danielbalera@gmail.com'
print(nome.endswith('gmail.com'),'\n')

#Encontra a posição do termo procurado. Lembre-se, começa do zero
nome = 'danielbalera@gmail.com'
print(nome.find('@'),'\n')

#Verifica se o texto é todo feito com letras.
nome = 'Daniel'
print(nome.isalpha(),'\n')

#Verifica se o texto é feito com numeros.
nome = '123'
print(nome.isnumeric(),'\n')

#Substitui um caractere escolhido por outro.
nome = 'Daniel'
print(nome.replace('l','r'),'\n')

#Spara um texto string baseado em algum caractere indicado.
nome = 'Daniel @ Nier'
print(nome.split('@'),'\n')

#coloca todas as letras iniciais em maiuscula.
nome = 'daniel magalhães cabral balera'
print(nome.title(),'\n')

#retira os caracteres indesejados, como por exemplo espaços que nao agregam valor.
nome = '    daniel magalhães cabral balera  '
print(nome.strip(),'\n')

#retorna true ou false para um teste de uma string se inicia com um texto especifco.
nome = 'daniel 2008'
print(nome.startswith('dan'),'\n')
print(nome.startswith('Dan'),'\n')