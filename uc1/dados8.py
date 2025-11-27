import pandas as pd

df = pd.read_csv ('ClassicDisco.csv')

# Detalhes das colunas
for coluna in df.columns:
    print ("Coluna: ", coluna)