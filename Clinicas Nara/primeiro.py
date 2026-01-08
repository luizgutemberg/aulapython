# Passo 7: Média e mediana por especialidade
print("\n=== MÉDIA E MEDIANA POR ESPECIALIDADE ===")
por_especialidade = consultas_realizadas.groupby('especialidade')['tempo_espera_minutos'].agg(['mean', 'median'])
por_especialidade = por_especialidade.round(1)  # arredonda para ficar mais bonito
print(por_especialidade)

# Passo 8: Média e mediana por médico (só os 10 primeiros para não encher a tela)
print("\n=== MÉDIA E MEDIANA POR MÉDICO (primeiros 10) ===")
por_medico = consultas_realizadas.groupby('id_medico')['tempo_espera_minutos'].agg(['mean', 'median'])
por_medico = por_medico.round(1)
print(por_medico.head(10))

# Passo 9: Média e mediana por clínica (só os 10 primeiros)
print("\n=== MÉDIA E MEDIANA POR CLÍNICA (primeiros 10) ===")
por_clinica = consultas_realizadas.groupby('id_clinica')['tempo_espera_minutos'].agg(['mean', 'median'])
por_clinica = por_clinica.round(1)
print(por_clinica.head(10))

# Passo 10: Ver a relação entre tempo de espera e nota de satisfação
print("\n=== CORRELAÇÃO COM A NOTA DOS PACIENTES ===")
# Junta as duas tabelas usando o id_consulta
dados_juntos = pd.merge(consultas_realizadas, avaliacoes, on='id_consulta', how='inner')

if len(dados_juntos) > 0:
    correlacao = dados_juntos['tempo_espera_minutos'].corr(dados_juntos['nota_satisfacao'])
    print(f"Correlação: {correlacao:.3f}")
    print(" (Se for perto de 0 = pouca relação, perto de 1 = espera maior = nota maior, perto de -1 = espera maior = nota menor)")
else:
    print("Não tem avaliações para comparar.")

print("\nPronto! Tudo concluído. 😊")