import pandas as pd

#Criar lista de dados
dados = [ 10, 20, 30, 40]

#Criar série
serie = pd.Series (dados, index = ['A', 'B', 'C', 'D' ])

print (serie)