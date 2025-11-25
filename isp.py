import pandas as pd

df = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep=';', encoding= 'latin1')



'''print (df.head(5))'''
'''print (df.describe())'''
'''print (df.tail(5))'''

df_roubo_celular_dp = df.groupby ('cisp') ['roubo_celular'].sum().reset_index()
df_roubo_celular_dp = df_roubo_celular_dp.sort_values (by = 'roubo_celular', ascending = False).head (20)


print (df_roubo_celular_dp)