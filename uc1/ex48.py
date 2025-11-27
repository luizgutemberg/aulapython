def ler_inteiro ():
    
    try:
        numero = int(input("Digite um número inteiro:"))    
    except ValueError:
        print ("Erro:  você deve digitar apenas números inteiros!")
    else:
        print (f"Número digitado com sucesso {numero}")   
    finally:
        print ("Fim do progrma de conversão")
        
ler_inteiro ()