v1 = int(input("Digite o primeiro valor"))
v2 = int(input("Digite o segundo valor"))
v3 = int(input("Digite o terceiro valor"))

if ( v1 > v2 and v1 > v3):
    print (f"{v1} é maior")
elif ( v2 > v3 and v2 > v1 ):
    print (f"{v2} é maior")
else:
    print (f"{v3} é maior")