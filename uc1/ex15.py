genero = input("Digite seu genero (M ou F)").upper()
data = int(input("Digite o ano de nascimento"))
idade = 2025 - data
if ( genero == "M" and idade >= 18):
    print ("está apto")
else:
    print ("não está apto")