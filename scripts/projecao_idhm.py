# Projeção do Índice de Desenvolvimento Humano Municipal (IDHM) para 2020

# Este script realiza a projeção dos valores do IDHM (geral, renda e educação) das subprefeituras de São Paulo 
# para o ano de 2020, com base nos dados disponíveis dos anos de 2000 e 2010.

# Duas abordagens são aplicadas:
# - Projeção Linear: estima o crescimento com base na diferença entre 2000 e 2010.
# - Projeção Exponencial: considera o crescimento percentual médio anual e aplica sobre 20 anos.

# Etapas do script:
# - Carrega a base de dados (formato .xlsx ou .csv),
# - Calcula as projeções para 2020,
# - Exporta os resultados para um novo arquivo Excel.

# Desenvolvido em Python 3.13 no IDLE e adaptado para uso em Jupyter Notebook.   

import pandas as pd
import numpy as np

# Definir o arquivo de entrada
arquivo_entrada = "idhm_subpref_anos.xlsx"  # ou "idhm_subpref_anos.xlsx.csv"

# Carregar o arquivo Excel ou CSV
try:
    if arquivo_entrada.endswith(".xlsx"):
        df = pd.read_excel(arquivo_entrada)
    else:
        df = pd.read_csv(arquivo_entrada)
except FileNotFoundError:
    print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado. Verifique o nome e tente novamente.")
    exit()

# Criar previsões para 2020
for indicador in ["IDHM", "IDHM_Renda", "IDHM_Educacao"]:
    df[f"{indicador}_Linear_2020"] = df[f"{indicador}_2010"] + (df[f"{indicador}_2010"] - df[f"{indicador}_2000"])

    # Modelo Exponencial
    df[f"{indicador}_r"] = np.log(df[f"{indicador}_2010"] / df[f"{indicador}_2000"]) / 10
    df[f"{indicador}_Exp_2020"] = df[f"{indicador}_2000"] * np.exp(df[f"{indicador}_r"] * 20)

# Salvar a saída em um novo arquivo
arquivo_saida = "idhm_projecao_2020.xlsx"
df.to_excel(arquivo_saida, index=False)

print(f"Projeção concluída! Arquivo salvo como: {arquivo_saida}")
