'''Peça dois números em uma operação. Use try-execpt-else-finally para tratar erros como divisão por zero e valores inválidos.
utilize a estrutura match case para decidir com os caracteres abaixo suas respectivvas operações
+ para adição
- para subtração
* para multiplicação
/ para divisão

def dividir (a, b):
    try:
        n1 = float(input("Digite a primeira nota: "))
        n2 = float(input("Digite a segunda nota: "))
        resultado = a / b
    
    except ZeroDivisionError:
        print ("Erro: divisão por zero não é permitida")
    except ValueError:
        print ("Erro: valor inválido informado")        
    else:
        print (f"Resultdo da divisão: {resultado}")
    finally:
        print ("Operação finaliada (com ou sem erro).")'''
        
def calculadora ():
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segudo número: "))
        op = input("Digie a operação (+, -, *, /): ")
    
        match op:
            case '+':
                resultado = a + b    
            case '-':
                resultado = a - b
            case '*':
                resultado = a * b
            case '/':
                resultado = a / b
            case _:
                raise ValueError("Operação inválida")
        
    except ZeroDivisionError:
        print ("Erro: Divisão por zero!")
    except ValueError as e:
        print (f"Erro: {e}")
    else:
        print (f"Resultado: {resultado}")
    finally:
        print ("Calculo encerrado")
        
calculadora ()