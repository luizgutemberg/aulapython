'''Leia duas notas, calculle a média e trate erros de entrada (valor inválido ou dinvisão incorreta)

def div (a, b):
    try:
        return (a + b) / 2
    except ZeroDivisionError:
        print ("Erro: cálculo não permitido")
    except ValueError:
        print ("Erro: valor invalido informado")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

print ("A médias das notas é " ,div (n1, n2))'''

def calcular_media ():
    try:
        n1 = float(input("Digite a primeira nota: "))
        n2 = float(input("Digite a segunda nota: "))
        media = (n1 + n2) / 2
    except ValueError:
        print ("Erro: Digite apenas números válidos") 
    else:
        print (f"Média calculada: {media:.2f}")   
    finally:
        print ("Fim do calculo de média")
calcular_media ()