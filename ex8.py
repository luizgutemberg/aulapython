# código pythom que verifica se o nome é correto

nome = input ("Qua seu nome")
sobrenome = input ("Digite seu Sobrenome")

nome = nome.upper()
sobrenome = sobrenome.upper()

if (nome == "SENAC" and sobrenome == "SANTA LUZIA"):
    print (f"Seja bem vindo ao {nome} {sobrenome}")
else:
    print ("não é Senac")