# Análise de Correlação entre o IDEB e o IDHM nas Subprefeituras de São Paulo

# Este script tem como objetivo principal investigar a relação entre o Índice de Desenvolvimento da Educação Básica (IDEB) 
# e o Índice de Desenvolvimento Humano Municipal (IDHM) nas subprefeituras da cidade de São Paulo, utilizando dados dos 
# anos de 2000, 2010 e projeções para 2020.

# A partir de dados públicos, o código:
# - Agrupa o IDEB por subprefeitura e período;
# - Integra com os dados do IDHM (renda e educação);
# - Gera estatísticas descritivas;
# - Calcula correlações e produz mapas de calor;
# - Cria gráficos de dispersão e histogramas;
# - Exporta planilhas com os resultados.

# Este projeto foi originalmente desenvolvido em Python 3.13 no IDLE e adaptado para execução em Jupyter Notebook 
# para fins de reprodutibilidade e compartilhamento no GitHub.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Criar pasta de saída para resultados
output_dir = "resultados_analise"
os.makedirs(output_dir, exist_ok=True)

# Carregar os arquivos
file_idhm = "idhm_subpref_anos.xlsx"
file_ideb_finais = "ideb_anos_finais.xlsx"
file_ideb_iniciais = "ideb_anos_iniciais.xlsx"

idhm_df = pd.read_excel(file_idhm, sheet_name="subprefeitura")
ideb_finais_df = pd.read_excel(file_ideb_finais, sheet_name="Sheet1")
ideb_iniciais_df = pd.read_excel(file_ideb_iniciais, sheet_name="Sheet1")

# Converter para numérico e tratar valores ausentes
ideb_cols_finais_2000 = ["IDEB_2005_finais", "IDEB_2009_finais"]
ideb_cols_finais_2010 = ["IDEB_2011_finais", "IDEB_2013_finais", "IDEB_2015_finais", "IDEB_2017_finais", "IDEB_2019_finais"]
ideb_cols_finais_2020 = ["IDEB_2021_finais", "IDEB_2023_finais"]

ideb_cols_iniciais_2000 = ["IDEB_2005_iniciais", "IDEB_2009_iniciais"]
ideb_cols_iniciais_2010 = ["IDEB_2011_iniciais", "IDEB_2013_iniciais", "IDEB_2015_iniciais", "IDEB_2017_iniciais", "IDEB_2019_iniciais"]
ideb_cols_iniciais_2020 = ["IDEB_2021_iniciais", "IDEB_2023_iniciais"]

for col in ideb_cols_finais_2000 + ideb_cols_finais_2010 + ideb_cols_finais_2020:
    if col in ideb_finais_df.columns:
        ideb_finais_df[col] = pd.to_numeric(ideb_finais_df[col], errors='coerce')
for col in ideb_cols_iniciais_2000 + ideb_cols_iniciais_2010 + ideb_cols_iniciais_2020:
    if col in ideb_iniciais_df.columns:
        ideb_iniciais_df[col] = pd.to_numeric(ideb_iniciais_df[col], errors='coerce')

# Calcular a média do IDEB por Prefeitura Regional
ideb_finais_media_2000 = ideb_finais_df.groupby("Prefeitura Regional")[ideb_cols_finais_2000].mean().reset_index()
ideb_finais_media_2010 = ideb_finais_df.groupby("Prefeitura Regional")[ideb_cols_finais_2010].mean().reset_index()
ideb_finais_media_2020 = ideb_finais_df.groupby("Prefeitura Regional")[ideb_cols_finais_2020].mean().reset_index()

ideb_iniciais_media_2000 = ideb_iniciais_df.groupby("Prefeitura Regional")[ideb_cols_iniciais_2000].mean().reset_index()
ideb_iniciais_media_2010 = ideb_iniciais_df.groupby("Prefeitura Regional")[ideb_cols_iniciais_2010].mean().reset_index()
ideb_iniciais_media_2020 = ideb_iniciais_df.groupby("Prefeitura Regional")[ideb_cols_iniciais_2020].mean().reset_index()

# Unir com os dados do IDHM
idhm_2000 = idhm_df[["Prefeitura Regional", "IDHM_2000", "IDHM_Renda_2000", "IDHM_Educacao_2000"]]
idhm_2010 = idhm_df[["Prefeitura Regional", "IDHM_2010", "IDHM_Renda_2010", "IDHM_Educacao_2010"]]
idhm_2020 = idhm_df[["Prefeitura Regional", "IDHM_2020", "IDHM_Renda_2020", "IDHM_Educacao_2020"]]

def merge_and_analyze(ideb_df, idhm_df, title):
    df = pd.merge(ideb_df, idhm_df, on="Prefeitura Regional", how="inner")
    print(f"\nEstatísticas descritivas - {title}")
    print(df.describe())

    # Salvar planilha com dados combinados
    df.to_excel(os.path.join(output_dir, f"dados_{title.replace(' ', '_')}.xlsx"), index=False)

    # Correlação
    df_corr = df.select_dtypes(include=['number'])
    plt.figure(figsize=(12, 5))
    sns.heatmap(df_corr.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(f"Correlação {title}")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"heatmap_correlacao_{title.replace(' ', '_')}.png"))
    plt.close()

    # Dispersão IDEB vs IDHM
    for ideb_col in [col for col in df.columns if "IDEB" in col]:
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=df[ideb_col], y=df["IDHM_" + title[-4:]], alpha=0.7)
        plt.title(f"{ideb_col} vs IDHM {title[-4:]}")
        plt.xlabel(ideb_col)
        plt.ylabel(f"IDHM {title[-4:]}")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f"scatter_{ideb_col}_vs_IDHM_{title[-4:]}.png"))
        plt.close()

    # Outras medidas de dispersão
    amplitude = df.max(numeric_only=True) - df.min(numeric_only=True)
    coef_var = (df.std(numeric_only=True) / df.mean(numeric_only=True)) * 100
    amplitude.to_excel(os.path.join(output_dir, f"amplitude_{title.replace(' ', '_')}.xlsx"))
    coef_var.to_excel(os.path.join(output_dir, f"coef_variacao_{title.replace(' ', '_')}.xlsx"))

    # Histogramas
    df.select_dtypes(include='number').hist(figsize=(15, 10), bins=10, edgecolor='black')
    plt.suptitle(f"Histogramas - {title}")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(os.path.join(output_dir, f"histogramas_{title.replace(' ', '_')}.png"))
    plt.close()

    # Tabela de frequência (Prefeitura Regional)
    freq = df["Prefeitura Regional"].value_counts()
    freq.to_excel(os.path.join(output_dir, f"frequencia_prefeitura_{title.replace(' ', '_')}.xlsx"))

# Análises para cada período
merge_and_analyze(ideb_finais_media_2000, idhm_2000, "IDEB (Anos Finais) e IDHM 2000")
merge_and_analyze(ideb_iniciais_media_2000, idhm_2000, "IDEB (Anos Iniciais) e IDHM 2000")
merge_and_analyze(ideb_finais_media_2010, idhm_2010, "IDEB (Anos Finais) e IDHM 2010")
merge_and_analyze(ideb_iniciais_media_2010, idhm_2010, "IDEB (Anos Iniciais) e IDHM 2010")
merge_and_analyze(ideb_finais_media_2020, idhm_2020, "IDEB (Anos Finais) e IDHM 2020")
merge_and_analyze(ideb_iniciais_media_2020, idhm_2020, "IDEB (Anos Iniciais) e IDHM 2020")

