import pandas as pd

df = pd.read_csv ('ClassicDisco.csv')

#Exibindo as colunas numeradas
for i, coluna in enumerate(df.columns, start=1):
    print (f"{i}ª coluna: {coluna}")