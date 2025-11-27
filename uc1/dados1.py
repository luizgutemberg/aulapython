import pandas as pd

dados = {
    'Cargos' : ["Assistente", "Analista", "Gerente", "Diretor"],
    'Salarios' : [1000, 2000, 3000, 4000]
}

dados_bi = pd.DataFrame(dados)
print (dados_bi)