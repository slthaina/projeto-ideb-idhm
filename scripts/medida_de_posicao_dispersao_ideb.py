# Este script realiza o cálculo de estatísticas descritivas (medidas de posição e dispersão) 
# e gera visualizações da evolução do IDEB (Índice de Desenvolvimento da Educação Básica) ao 
# longo do tempo, segmentadas por subprefeitura da cidade de São Paulo. São analisados dados 
# dos anos iniciais e finais do ensino fundamental, permitindo uma visão comparativa do desempenho 
# educacional em diferentes regiões da cidade.

# Objetivo:
# Explorar tendências regionais de desempenho educacional e identificar variações temporais e 
# espaciais no IDEB, contribuindo para uma análise das desigualdades educacionais no município.

# Principais funcionalidades:
# - Cálculo de média, mediana, moda, quartis e outros percentis por subprefeitura;
# - Geração de gráficos de linha que mostram a evolução do IDEB entre 2005 e 2023;
# - Exportação dos resultados em arquivos .csv e .png.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

try:
    # Criar diretório para salvar os gráficos
    os.makedirs("analises/graficos_plots", exist_ok=True)

    # Carregar os dados do IDEB para anos iniciais e finais
    df_ideb_iniciais = pd.read_excel("ideb_anos_iniciais.xlsx")
    df_ideb_finais = pd.read_excel("ideb_anos_finais.xlsx")

    # Definir colunas para os dois níveis de ensino
    colunas_ideb_iniciais = [
        'IDEB_2005_iniciais', 'IDEB_2009_iniciais', 'IDEB_2011_iniciais', 'IDEB_2013_iniciais', 
        'IDEB_2015_iniciais', 'IDEB_2017_iniciais', 'IDEB_2019_iniciais', 'IDEB_2021_iniciais', 'IDEB_2023_iniciais'
    ]
    
    colunas_ideb_finais = [
        'IDEB_2005_finais', 'IDEB_2009_finais', 'IDEB_2011_finais', 'IDEB_2013_finais', 
        'IDEB_2015_finais', 'IDEB_2017_finais', 'IDEB_2019_finais', 'IDEB_2021_finais', 'IDEB_2023_finais'
    ]

    # Converter colunas para numéricas
    df_ideb_iniciais[colunas_ideb_iniciais] = df_ideb_iniciais[colunas_ideb_iniciais].apply(pd.to_numeric, errors='coerce')
    df_ideb_finais[colunas_ideb_finais] = df_ideb_finais[colunas_ideb_finais].apply(pd.to_numeric, errors='coerce')

    # Função para calcular estatísticas descritivas por Prefeitura Regional
    def calcular_estatisticas(df, colunas):
        estatisticas = df.groupby("Prefeitura Regional")[colunas].agg([
            "mean", "median", lambda x: x.mode().iloc[0] if not x.mode().empty else None,
            lambda x: x.quantile(0.25), lambda x: x.quantile(0.75),
            lambda x: x.quantile(0.1), lambda x: x.quantile(0.9)
        ])
        estatisticas.columns = ['_'.join(col).strip() for col in estatisticas.columns.values]
        return estatisticas

    # Paleta de cores para gráficos
    cores = sns.color_palette("tab20", n_colors=31) + sns.color_palette("Set1", n_colors=11)

    # Função para gerar gráficos
    def gerar_graficos(df, colunas, nome_periodo):
        nome_periodo_formatado = nome_periodo.lower().replace(' ', '_').strip()
        anos = [col.split('_')[1] for col in colunas]

        estatisticas = calcular_estatisticas(df, colunas)
        estatisticas.to_csv(f"analises/graficos_plots/estatisticas_{nome_periodo_formatado}.csv")

        # Gráfico de linha (Evolução do IDEB)
        plt.figure(figsize=(14, 8))
        for i, subpref in enumerate(df["Prefeitura Regional"].unique()):
            sub_df = df[df["Prefeitura Regional"] == subpref]
            valores = sub_df[colunas].mean()
            plt.plot(anos, valores, marker='o', label=subpref, color=cores[i % len(cores)])
        
        plt.xticks(rotation=45)
        plt.title(f"Evolução do IDEB ({nome_periodo}) por Subprefeitura")
        plt.ylabel("IDEB")
        plt.xlabel("Ano")
        plt.grid()
        plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small', ncol=2)
        plt.tight_layout()
        plt.savefig(f"analises/graficos_plots/evolucao_ideb_{nome_periodo_formatado}.png", bbox_inches="tight", dpi=300)
        plt.close()

    # Gerar gráficos e estatísticas para anos iniciais e finais
    gerar_graficos(df_ideb_iniciais, colunas_ideb_iniciais, "Anos Iniciais")
    gerar_graficos(df_ideb_finais, colunas_ideb_finais, "Anos Finais")

except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome do arquivo e o caminho.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

