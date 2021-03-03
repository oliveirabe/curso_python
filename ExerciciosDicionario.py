dicionarioFamilia = {
    'mãe':'Maria',
    'pai':'José',
    'irmão':'João'
}

print(dicionarioFamilia)
print(dicionarioFamilia['pai'])

dicionarioComida = {
    'frutas': ['Banana', 'Maçã', 'Pêra'],
    'verduras': ['Repolho', 'Agrião', 'Couve'],
    'doces': ['Chocolate', 'Surpiro', 'Pirulito']
}

print(dicionarioComida)
print(dicionarioComida['verduras'])

dicionarioRestaurante = {
    'hamburguer': ['Madero', 'Burger King', 'Jeronimo',],
    'frango': ['Popyes', 'KFC'],
    'churrasco': ['Mania de Churrasco', 'Tendal'],
    'bolo': 'sodiê'    
}

print(dicionarioRestaurante)
print(dicionarioRestaurante['bolo'])

dicionarioBebidas = {
    'suco': ['Laranja', 'Acerola', 'Maracujá'],
    'chá': ['Camomila','Verde','Capim Santo'],
    'refrigetante': ['Coca-Cola', 'Jesus', 'Guaraná'],
    'água':['Tônica', 'C/ Gás']
}

dicionarioBebidas['suco'].append('Uva')
print(dicionarioBebidas)

dicionarioCores = {
    'comA': ['azul','amarelo'],
    'comR': ['rosa', 'roxo'],
    'comV': ['verde', 'vermelho'],
    'comL': ['Laranja','lilás']
}

print(dicionarioCores['comL'])

dicionarioEsporte = {
    'individual':['Atletismo', 'Tênis'],
    'coletivo': ['Futebol', 'Vôlei']
}

dicionarioEsporte['individual'].append('Cliclismo')
print(dicionarioEsporte)

dicionarioCarro = { 
    'modelo': 'Fusca',
    'ano': 1997,
    'portas': 2,
    'cor': 'azul',
    'dono' : {
        'nome': 'José',
        'cpf': '041XXX065-16',
        'endereço': 'R. dos Bobos, nº 0' 
}
}

print(dicionarioCarro)
print(dicionarioCarro['dono'])