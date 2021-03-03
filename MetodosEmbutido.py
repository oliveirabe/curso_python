nome = 'Claudia'
frase = 'Meu nome é Ana'
idade = 42.2
frase2 = 'HELLO WORLD'
frase3 = 'olá mundo'
lista = [1, 2, 3, 4, 5, 1, 1]


# len => Mostra o tamanho de um dado (quantidade)
# in => verifica se existe um daddo dentro de outro
# lower => transforma uma string em letra minuscula
# upper => transforma uma string em letra maiuscula 

print(nome.count('z'))
print(nome.find('ud')) 
print(len(nome))


print(lista.count(1))
print(lista.index(4))

lista.extend([12, 22, 31])
print(lista)
