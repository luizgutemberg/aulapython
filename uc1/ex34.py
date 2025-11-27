'''Desenvolva um código python usando apenas while que digite um nome e imprima, o programa so vai parar quando for digitado "sair" em maiusculo'''

nome = ""

while nome != "SAIR":
    nome = input("Digite um nome (ou SAIR para encerrar): ") .upper ()
    if nome != "SAIR":
        print(f"Nome digitado: {nome}")

