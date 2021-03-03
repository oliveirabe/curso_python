# Compreensão de lista

lista = [x for x in range (0,10)]

print(lista)

lista2 = [x for x in range (0, 101, 10)]
print(lista2)



# Exercicios
'''
1. numerosPares = [x for x in range(0, 11, 2)]
2. numerosImpares = [y for y in range(0, 11, 3)]
3. listaNumeros = [z for z in range(1, 11) if z != 5 and z != 7]
4. 
'''

numerosPares = []

for x in range(0,11,2):
    numerosPares.append(x)

print(numerosPares)

numerosImpares = []

for y in range(0, 11, 3):
    numerosImpares.append(y)
    
print(numerosImpares)

listaNumeros = []

for z in range (1, 11):    
    if z != 5 and z != 7:
        listaNumeros.append(z)

print(listaNumeros)

listaIdade = []

for x in range (0, 51, 5):
    listaIdade.append(x)

print(listaIdade)
        
listaIdade2 = [x for x in range (0,51, 5)]

print(listaIdade2)

listaFruta = ['pitaya', 'maracujá', 'siriguela', 'pitomba', 'morango']

for x in listaFruta:
    print(x)

fruta =  ['banana', 'maca', 'pera']

listaFruta2 = [x for x in fruta]
print(listaFruta2)
