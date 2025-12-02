import pandas as pd


dados = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', encoding='ISO-8859-1', sep=';')

# 2. Filtrar só os dados da capital (município 'Rio de Janeiro')
dados_capital = dados[dados['municipio'] == 'Rio de Janeiro']

# 3. Criar uma coluna com a SOMA total de furto e roubo de veículos por mês
dados_capital['total_crimes'] = dados_capital['roubo_de_veiculo'] + dados_capital['furto_de_veiculo']

# 4. Somar TUDO por delegacia (CISP)
# Agrupamos pelo código da delegacia ('cisp') e somamos a coluna 'total_crimes'
resumo_por_delegacia = dados_capital.groupby('cisp')['total_crimes'].sum().reset_index()

# 5. Encontrar a delegacia com o MAIOR número de crimes
# Ordenamos os resultados do maior para o menor e pegamos a primeira linha (iloc[0])
delegacia_outlier = resumo_por_delegacia.sort_values(by='total_crimes', ascending=False).iloc[0]

# 6. Mostrar o resultado
print("--- Delegacia que mais destoa (Outlier) na Capital ---")
print(f"CISP (Código da Delegacia): {delegacia_outlier['cisp']}")
print(f"Total Histórico de Ocorrências: {delegacia_outlier['total_crimes']:,.0f}")
print("-----------------------------------------------------")