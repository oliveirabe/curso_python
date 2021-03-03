
class Violao: 
    def __init__(self, marca, modelo, tipoCorda, dono):
        self.marca = marca
        self.modelo = modelo
        self.tipoCorda = tipoCorda
        self.dono = dono
        self.temCorda = True
        self.afinado = True

    def caracteristicas(self):
        return self.marca, self.modelo, self.tipoCorda, self.dono

    def tocar(self):
        if self.temCorda == True:
            return 'Começar a tocar'
        else:
            return 'Precisa colocar cordas'

    def continuar(self):
        if self.afinado == True:
            return 'Continue tocando'
        else:
            return 'Precisa afinar'

meuViolao = Violao('Tagima', 'Walnut Five', 'Aço', 'João')

print(meuViolao.caracteristicas())
print(meuViolao.tocar())
print(meuViolao.continuar())

print ('----------------------------------------------------')

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.temEmprego = True
        self.temDinheiro = True
        self.lojaAberta = True
        
    def caracteristicas(self):
        return self.nome, self.sobrenome, self.idade

    def emprego(self):
        if self.temEmprego == True:
            return 'Guarde dinheiro'
        else:
            return 'Precisa de um emprego'

    def comprarCarro(self):
        if self.temDinheiro == True:
            return 'Vá até a concessionaria'
        else: 
            return 'Precisava ter guardado dinheiro'

    def concessionaria(self):
        if self.lojaAberta == True:
            return 'Procure um vendedor'
        else:
            return 'Volte outro dia'
    
alguem = Pessoa('Maria', 'Santos', 52)

print(alguem.caracteristicas())
print(alguem.emprego())
print(alguem.comprarCarro())
print(alguem.concessionaria())

print ('----------------------------------------------------')

class Notebook:
    def __init__(self, marca, cor, modelo, memoria, processador, dono):
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
        self.memoria = memoria
        self.processador = processador
        self.dono = dono 
        self.bateria = True
        self.ligado = True
        self.navegadorAberto = True
        self.sitePesquisa = True
        self.busca = True

    def caracteristicas(self):
        return self.marca, self.cor, self.modelo, self.memoria, self.processador, self.dono


    def ligar(self):
        if self.bateria == True:
            return 'Pode ligar'
        else:
            return 'Notebook s/ bateria.'

    def abrirNavegador(self):
        if self.ligado == True:
            return 'Abrindo navegador'
        else:
            return 'O notebook não está ligado'
    
    def fazerPesquisa(self):
        if self.navegadorAberto == True:
            return 'Abrindo site de pesquisa'
        else:
            return 'Precisa abrir o navegador'

    def assuntoPesquisa(self):
        if self.sitePesquisa == True:
            return 'Faça sua pesquisa'
        else:
            return 'Vá para o site de pesquisa'

    def pesqisaEncontrada(self):
        if self.busca == True:
            return 'Assunto encontrado'
        else: 
            return 'Nenhum resultado pra sua busca'



meuNote = Notebook('Dell', 'Preto', 'Latitude 5480', '1TB', 'Intel Core i5', 'Giovanni' )

print(meuNote.caracteristicas())
print(meuNote.ligar())
print(meuNote.abrirNavegador())
print(meuNote.fazerPesquisa())
print(meuNote.assuntoPesquisa())
print(meuNote.pesqisaEncontrada())

print ('----------------------------------------------------')

