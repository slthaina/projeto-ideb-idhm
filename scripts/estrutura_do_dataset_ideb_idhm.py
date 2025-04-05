# Análise Estrutural dos Dados de IDEB e IDHM

# Este script realiza uma inspeção inicial das principais bases de dados utilizadas no projeto: 
# - IDEB dos anos iniciais,
# - IDEB dos anos finais,
# - IDHM por subprefeitura da cidade de São Paulo.

# As análises iniciais incluem:
# - Dimensão das bases (linhas e colunas),
# - Tipagem das variáveis,
# - Contagem de valores ausentes e registros duplicados.

# Essas verificações são fundamentais para garantir a integridade dos dados antes das etapas posteriores de análise estatística, # # visualização e modelagem.

# Desenvolvido em Python 3.13 e compatível com execução em Jupyter Notebook.

import pandas as pd

# Caminhos dos arquivos
caminho_ideb_iniciais = "ideb_anos_iniciais.xlsx"
caminho_ideb_finais = "ideb_anos_finais.xlsx"
caminho_idhm = "idhm_subpref_anos.xlsx"

# Leitura dos datasets
ideb_iniciais = pd.read_excel(caminho_ideb_iniciais)
ideb_finais = pd.read_excel(caminho_ideb_finais)
idhm = pd.read_excel(caminho_idhm)

# Função de análise básica
def analisar_dataset(nome, df):
    print(f"\nAnálise do dataset: {nome}")
    print(f"- Total de linhas: {df.shape[0]}")
    print(f"- Total de colunas: {df.shape[1]}")
    print(f"- Tipos de dados:\n{df.dtypes}")
    print(f"- Valores ausentes: {df.isnull().sum().sum()}")
    print(f"- Registros duplicados: {df.duplicated().sum()}")

# Executar análise para cada dataset
analisar_dataset("IDEB - Anos Iniciais", ideb_iniciais)
analisar_dataset("IDEB - Anos Finais", ideb_finais)
analisar_dataset("IDHM", idhm)
