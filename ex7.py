n1 = float (input ("Digite a nota de Matemátca "))
n2 = float (input ("Digite a nota de Portugues "))
n3 = float (input ("Digite a nota de Fisica "))
n4 = float (input ("Digite a nota de Quimica "))

media = (n1 + n2 + n3 + n4) / 4

print (f"A media das notas é {media}")


if ( media >= 6):
    print (f"Você está aprovado com a nota total {media}")

else: 
    print (f"Você não está aprovado, sua média foi {media}")