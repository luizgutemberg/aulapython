cargo = input ("Digite o seu cargo")

#caixa = 1500 vendedor = 2400 gerente = 4000


if (cargo == "caixa"):
    salario = 1500
elif (cargo == "vendedor"):
    salario = 2400
elif (cargo == "gerente"):
    salario = 4000
else:
    print ("Cargo inválido")

inss = salario * 0.12

if (salario > 2000):
    irrf = salario * 0.14
else:
    irrf = salario *0.08

sn = salario - irrf - inss

print (f"seu salario é {salario}")
print (f"INSS {inss}")
print (f"IRRF {irrf}")
print (f"seu salario final é {sn}")