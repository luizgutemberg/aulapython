produto = input ("Digite o nome do produto")
if (produto == "mouse"):
    preço = 10
elif (produto == "teclado"):
    preço = 20
elif (produto == "memoria"):
    preço = 100
else:
    print ("Produto não existe")

quantidade = (int (input ("Digite quantidade vendida")))
total = preço * quantidade

if quantidade > 10:
    imposto = total * 0.05
else: 
    imposto = total * 0.1

##imposto = quantidade > 10 == 0.05 * total or quantidade < 10 == 0.10 * total

valorfinal = total + imposto


print (f"O preço do {produto} é {preço}")
print (f"A quantidade vendida foi {quantidade}")
print (f"O total é {total}")
print (f"O imposto total é {imposto}")
print (f"O Valor final é {valorfinal}")