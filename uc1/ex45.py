'''Crie uma função que receba dois números e retorne o maior deles'''
def maior (a, b):
    if a > b:
        return a
    else:
        return b

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

maior_numero = maior(n1,n2)
print (f"O maior número entre {n1} e {n2} é {maior_numero}")