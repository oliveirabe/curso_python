listaCor = ['azul', 'preto', 'vermelho']
listaAnimal = ['onça', 'jacare', 'leão']
listaIdade = [5, 7, 8,]

print(listaCor, listaAnimal, listaIdade)

listaCor.append('Roxo')
listaAnimal.append('elefante')
listaIdade.append('12')
# # .append => acrescenta ítem à lista

print(listaCor, listaAnimal, listaIdade)

listaCidade = ['Cuiabá', 'Maceió', 'Belo Horizonte']
listaEstado = ['Ceará', 'Amazonas', 'Piauí']
listaPais = ['Brasil', 'Argentina', 'Bolívia']

listaCidade.pop()
listaEstado.pop()
listaPais.pop()

# .pop => remove o útimo ítem da lista 

print(listaCidade, listaEstado, listaPais)

listaSamsung = ['A10', 'A20', 'A30']
listaXaiomi = ['Redmi Note 9', 'Redmi Note 9s', 'Redmi Note 11']
listaApple = ['Iphone 7', 'Iphone X', 'Iphone 12']

print(listaSamsung, listaXaiomi, listaApple)

listaSamsung.remove('A10')
listaXaiomi.remove('Redmi Note 9')
listaApple.remove('Iphone X')

# .remove(ítem) => remove um ítem específico da lista 

print(listaSamsung, listaXaiomi, listaApple)

