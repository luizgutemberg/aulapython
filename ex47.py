def dividir (a, b):
    try:
        resultado = a / b
    
    except ZeroDivisionError:
        print ("Erro: divisão por zero não é permitida")
    except ValueError:
        print ("Erro: valor inválido informado")        
    else:
        print (f"Resultdo da divisão: {resultado}")
    finally:
        print ("Operação finaliada (com ou sem erro).")
        
try:
    num1 = float (input("Digite o numerador"))
    num2 = float (input("Digite o denominador"))
    dividir (num1, num2)
    
except ValueError:
    print ("Você deve digitar apenas números!")