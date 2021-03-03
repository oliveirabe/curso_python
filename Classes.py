class Celular:
    def __init__(self, marca, modelo, ano, dono):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.dono = dono
        self.estaLigado = False

    def caracteristicas(self):
        return self.marca, self.modelo, self.ano, self.dono

    def ligar(self):
        self.estaLigado = True

        return 'Ligando...'

    def mensagem(self):
        if self.estaLigado == True:
            return 'Saudaçao'
        else:
            return 'Precisa ligar antes...'

    def desligar(self):
        self.estaLigado = False

        return 'Desligando...'


meuCelular = Celular('Samsung', 'A30', '2020', 'Beatriz')

print(meuCelular.caracteristicas())
print(meuCelular.ligar())
print(meuCelular.mensagem())
print(meuCelular.desligar())
print(meuCelular.mensagem())

print ('----------------------------------------------------')

class Carro:
    def __init__(self, nome, marca, ano, portas, dono, estilos):
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.portas = portas
        self.dono = dono
        self.estilos = estilos
        self.radioLigado = False

    def caracteristicas (self):
        return self.nome, self.marca, self.ano, self.portas, self.dono

    def abrir (self):
        self.abrir = True

        return 'Abrindo o carro'

    def ligarSom (self):
        self.radioLigado = True

        return 'Ligando o som'

    def escolherRadio (self):
        if self.radioLigado == True:
            if self.estilos == 'Rock':
                return 'Aumentando o som'
            else:
                return 'Abaixando o som'
        else:
            self.pergunta = input('Quer ligar?')

            if self.pergunta == 'Sim':
                return self.ligarSom()
            else:
                return 'O som precisa ser ligado'    


meuCarro = Carro('Polo', 'Volkswagen', 2020, '4 portas', 'Beatriz', 'Rock')

print(meuCarro.caracteristicas())
print(meuCarro.abrir())
print(meuCarro.ligarSom())
print(meuCarro.escolherRadio())

print ('----------------------------------------------------')
