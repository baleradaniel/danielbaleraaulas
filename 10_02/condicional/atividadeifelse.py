# Faça um programa que o usuario digite um numero e diga se o numero é superior a 20, inferior a 10 ou se está entre 10 e 20.

numero = int(input('Digite um numero: '))

if numero > 20:
    print('Numero maior que 20')
elif numero < 10:
    print('Numero menor que 10')
else:
    print('Numero entre 10 e 20')