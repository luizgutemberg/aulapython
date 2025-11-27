'''Crie uma função que receba o lado de uma quadrado e retorne o valor da sua área ($A = lado^2$)'''

def quadrado (lado):
    return lado ** 2

medida_lado = float(input("Digite a medida do lado do quadrado: "))

area = quadrado (medida_lado)
print (f"A área do quadrado é: {area}")

