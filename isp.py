import pandas as pd

df = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep=';', encoding= 'latin1')



'''print (df.head(5))'''
'''print (df.describe())'''
'''print (df.tail(5))'''

df_roubo_celular_dp = df.groupby ('cisp') ['roubo_celular'].sum().reset_index()
df_roubo_celular_dp = df_roubo_celular_dp.sort_values (by = 'roubo_celular', ascending = False).head (10)


print (df_roubo_celular_dp)




# --- 1. CARREGAR OS DADOS ---
print("1. Carregando os dados da internet...")
# Carrega o arquivo CSV diretamente da URL
# 'sep=;': O separador do arquivo é ponto e vírgula
# 'encoding=latin1': Usamos essa codificação para ler caracteres especiais do português
df = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep=';', encoding='latin1')

# Vemos as primeiras linhas do que carregamos
# print(df.head())


# --- 2. AGRUPAR E SOMAR OS FURTOS DE CELULAR POR DELEGACIA (CISP) ---

# Vamos criar uma nova tabela (DataFrame) que agrupa os dados pela coluna 'cisp'
# e depois SOMA o total da coluna 'furto_celular' para cada delegacia.
df_furto_cisp = df.groupby('cisp')['furto_celular'].sum().reset_index()

# Renomeia a coluna para ficar mais claro o que ela representa
df_furto_cisp.columns = ['cisp', 'total_furto_celular']

# Ordenamos a tabela da delegacia com MAIS furtos para a com MENOS
df_furto_cisp = df_furto_cisp.sort_values(by='total_furto_celular', ascending=False)

print("\n2. Total de Furtos de Celular por Delegacia (as 10 maiores):")
print(df_furto_cisp.head(10))


# --- 3. ANÁLISE ESTATÍSTICA DESCRITIVA (MÉDIA, MEDIANA E QUARTIS) ---

# Primeiro, transformamos a coluna de totais de furto em um 'array' do numpy
# para facilitar o cálculo das estatísticas.
array_furto_celular = np.array(df_furto_cisp['total_furto_celular'])

# A. Calcular Média e Mediana
media = np.mean(array_furto_celular)
mediana = np.median(array_furto_celular) # A mediana é igual ao Q2

# B. Calcular os Quartis
q1 = np.quantile(array_furto_celular, 0.25) # 25% (Primeiro Quartil)
q3 = np.quantile(array_furto_celular, 0.75) # 75% (Terceiro Quartil)

print("\n3. Resultados da Análise Estatística (baseada no total de furtos por delegacia):")
print(f'A média de furtos de celular por delegacia é: {media:.2f}')
print(f'A mediana (Q2) de furtos de celular por delegacia é: {mediana:.2f}')
print(f'O Primeiro Quartil (Q1) - 25% dos menores - é: {q1:.2f}')
print(f'O Terceiro Quartil (Q3) - 25% dos maiores - é: {q3:.2f}')


# --- 4. IDENTIFICAR DELEGACIAS POR QUARTIL ---

# A. Delegacias com o menor número de furtos (Abaixo de Q1)
# O Q1 (25%) representa o valor que separa as 25% delegacias com menos furtos.
# Queremos as delegacias que estão ABAIXO desse valor.
delegacias_menor_furto = df_furto_cisp.loc[df_furto_cisp['total_furto_celular'] <= q1]

print("\n4A. Delegacias que representam os 25% com MENOR número de furtos (total <= Q1):")
print(delegacias_menor_furto)
print(f"Total de delegacias nesta faixa: {len(delegacias_menor_furto)}")

# B. Delegacias com o maior número de furtos (Acima de Q3)
# O Q3 (75%) representa o valor que separa as 25% delegacias com mais furtos.
# Queremos as delegacias que estão ACIMA desse valor.
delegacias_maior_furto = df_furto_cisp.loc[df_furto_cisp['total_furto_celular'] >= q3]

print("\n4B. Delegacias que representam os 25% com MAIOR número de furtos (total >= Q3):")
print(delegacias_maior_furto)
print(f"Total de delegacias nesta faixa: {len(delegacias_maior_furto)}")