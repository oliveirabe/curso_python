nome = 'Giovanni'
print (nome)

print('====================================================')
listaNomes = ['Giovanni', 'Beatriz']
print(listaNomes)

print('====================================================')

meuDicionario = {
    "nome": "Strutz",
    "idade": "23"
}

print(meuDicionario['idade'])

print('====================================================')

listaNumeros = [10, 20, 30]

for numero in listaNumeros:
    print(numero)

print('====================================================')


print('Meu nome é ' + nome)

listaNomes.append('Nathan')
print(listaNomes)

print('====================================================')

def media(nota1, nota2):
    return (nota1 + nota2) / 2


def media2(nota1, nota2):
    calc = (nota1 + nota2) / 2

    return calc


print(media2(20, 30))
