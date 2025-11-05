ano_nasc_cand = (int (input ("Digite o ano de nasciento")))
genero = input ("Digite o sexo M ou F").upper ()


idade=2025 - ano_nasc_cand

if (idade >= 18 and genero == "M"):
    print ("Apto")

    
else:
    print("Não apto")