animal = 'macaco'

if animal == 'cobra':
    print('Não encontrado!')
else:
    print('Você acertou')

nota = 7

if nota >= 7:
    print ('Aprovado')
elif nota >= 5:
    print ('Recuperação')
else:
    print ('Reprovado!')


idades = [12, 15, 22, 18, 13, 7, 50]

for idade in idades:
    if idade >= 18:
        print (str(idade) + ' - Maior de Idade')
    else:
        print(str(idade) + ' - Menor de Idade') 

#str é um função que transforma qualquer tipo de dado p/ string

valores = [41, 20, 53, 30, 15, 13, 37]

for valor in valores:
    if valor % 2 == 0:
        print (str(valor) + ' - Número Par')
    else:
        print(str(valor) + ' - Número ímpar')

pessoas = ['Antônio', 'João', 'Maria', 'José', 'Glória']

for pessoa in pessoas:
    if pessoa == 'Antônio' or pessoa == 'José':
        print('Está na lista!')
    else:
        print('Não encotrado')