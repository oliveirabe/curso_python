import math

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        return self.num1 + self.num2

    def subtracao(self):
        if self.num2 >= self.num1:
            return self.num2 - self.num1
        else:
            return self.num1 - self.num2

    def divisao(self):
        if self.num2 >= self.num1:
            return self.num2 / self.num1
        else:
            return self.num1 / self.num2

    def multiplicacao(self):
        return self.num1 * self.num2

    def quadrado(self):
        quadrado1 = pow(self.num1, 2)
        quadrado2 = pow(self.num2, 2)
        
        return quadrado1, quadrado2

    def raizQuadrada(self):
        raiz1 = math.sqrt(self.num1)
        raiz2 = math.sqrt(self.num2)

        return raiz1, raiz2


          
minhaCalculadora = Calculadora(81, 144)

print(minhaCalculadora.soma())
print(minhaCalculadora.subtracao())
print(minhaCalculadora.quadrado())
print(minhaCalculadora.divisao())
print(minhaCalculadora.multiplicacao())
print(minhaCalculadora.raizQuadrada())

