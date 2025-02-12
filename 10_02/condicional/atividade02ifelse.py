# Faça um programa que receba uma nota do aluno e se for superior ou igual a 7 apareça mensafem que ele esta aprovado,
#  se for inferior a 5 ele esta "não aprovado/reprovado direto" e se estiver entre 5 e 7 apareça a mensagem "não aprovado/recuperação".

nota = float(input('Insira uma nota: '))

if nota >= 7:
  print('Aprovado')
else:
    if nota >= 5 :
        print('Não aprovado/Recuperação')
    else:
       print('Não aprovado/reprovado direto')