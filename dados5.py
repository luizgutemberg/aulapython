import pandas as pd

df = pd.read_csv ('ClassicDisco.csv')

# Exibe o número de linhas e colunas
print(df.shape)

# Exibe o nome das colunas
print(df.columns)