# #Tupla
# # Diferente de listas convencionais, 
# # a Tupla é uma lista que restringe a adição,
# #  alteração, remoção e o ordenamento do elementos.
    
# # Em uma lista as informações geralmente são 
# # de um mesmo tipo.
# # Enquanto que numa tupla, os elementos são 
# # de tipos distintos, por exemplo, 
# # uma Tupla que contém o dia, o dia da semana, 
# # o mês e o ano.


diaSemana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta')
print (diaSemana)
print (diaSemana[3]) # Isto é uma tupla

cor = ['azul', 'verde', 'amarelo', 'preto', 'lilas']
print (cor[2]) # Isto é uma lista

meses = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun')
print (meses[5])

vogais = ('a', 'e', 'i', 'o', 'u')
print(vogais)

tupla1 = ('amor', 28, 'Casamento')
print (tupla1)

for x in tupla1:
    if x == 28 or 'amor' or 'Casamento':
        print ('Encontrado')
    else:
        print ('Não encontrado')

print(type(tupla1))


tupla2 = (21, 22, 23, 'banana')

for x in tupla2:
    print(tupla2[2])

tupla3 = ('Arroz', 'Feijão', 'Salada', 36, 41, 10)

for x in tupla3:
    print(x)
else:
    print('Dados listados com sucesso')
