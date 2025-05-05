# FACULDADE DE COMPUTAÇÃO E INFORMÁTICA (FCI)

## 👩‍💻 Autoras

- **Karla Maria Ramos da Silva** – RA: 10441405  
- **Thainá Silva Leite** – RA: 10730503  

---

# PROJETO APLICADO I:  
## Análise do IDEB e das Desigualdades Educacionais no Ensino Público do Município de São Paulo

---

## 🎯 Objetivo

Investigar como o Índice de Desenvolvimento da Educação Básica (IDEB) varia entre os diferentes distritos da cidade de São Paulo, analisando sua evolução ao longo do tempo e identificando **fatores socioeconômicos correlacionados**, especialmente aqueles representados pelo Índice de Desenvolvimento Humano Municipal (IDHM).

> **Hipótese:** Existe uma correlação significativa entre o IDEB e os indicadores socioeconômicos dos distritos de São Paulo, especialmente os componentes de **renda** e **educação** do IDHM.

---

## 📊 Dados Utilizados

- **IDEB** (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira - INEP)
- **IDHM** (Programa das Nações Unidas para o Desenvolvimento - PNUD)

**Metadados principais:**

- Ano de referência (IDEB)
- Código e nome da escola
- Prefeitura Regional (distrito)
- Nota IDEB
- IDHM Geral, Renda e Educação

---

## 📁 Estrutura do Repositório

A estrutura do repositório é organizada da seguinte forma:

```
.
├── dados/            # Conjunto de dados brutos e tratados
├── notebooks/        # Análises em Jupyter Notebook
├── scripts/          # Scripts auxiliares (se houver)
├── requirements.txt  # Bibliotecas necessárias
└── README.md         # Documentação do projeto
```

---

## 📌 Metodologia

1. **Coleta**: Dados extraídos de plataformas públicas da Prefeitura de São Paulo, INEP e IBGE.
2. **Tratamento**: Limpeza de dados, remoção de duplicatas, análise de tipos e valores nulos.
3. **Exploração**: Visualizações com histogramas, boxplots, tabelas de frequência e mapas de calor.
4. **Correlação**: Análise entre IDEB e componentes do IDHM (renda e educação).
5. **Projeções**: Estimativas do IDHM para 2020 com modelos linear e exponencial.
6. **Modelagem** *(em desenvolvimento)*: Regressão, ANOVA e predição de desempenho educacional.

---

## 🔧 Ambiente de Desenvolvimento

Projeto desenvolvido em **Jupyter Notebook**, utilizando a linguagem **Python 3.13**.

**Bibliotecas principais:**

- `pandas`, `numpy` – Manipulação de dados  
- `matplotlib`, `seaborn` – Visualização gráfica  
- `scikit-learn` – Análise estatística e modelagem  
- `geopandas` – Análise espacial  

---

## ⚙️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/slthaina/projeto-ideb-idhm.git
cd projeto-ideb-idhm
```

2. (Opcional) Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts ctivate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute os notebooks:
```bash
jupyter notebook
```
Acesse a pasta `notebooks/` e abra os arquivos `.ipynb`.

---

## 📚 Bibliotecas

As bibliotecas necessárias para rodar o projeto são:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- geopandas

---

## 🧠 Conclusão Esperada

Espera-se que distritos com menor desenvolvimento humano apresentem, em média, IDEBs mais baixos — reforçando a necessidade de políticas públicas que integrem aspectos educacionais e sociais.

