
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

## 📌 Metodologia

1. **Coleta**: Dados extraídos de plataformas públicas da Prefeitura de São Paulo, INEP e IBGE.
2. **Tratamento**: Limpeza de dados, remoção de duplicatas, análise de tipos e valores nulos.
3. **Exploração**: Visualizações com histogramas, boxplots, tabelas de frequência e mapas de calor.
4. **Correlação**: Análise entre IDEB e componentes do IDHM (renda e educação).
5. **Projeções**: Estimativas do IDHM para 2020 com modelos linear e exponencial.
6. **Modelagem** *(em desenvolvimento)*: Regressão, ANOVA e predição de desempenho educacional.

---

## 🔧 Ambiente de Desenvolvimento

Projeto desenvolvido em **Jupyter Notebook**, utilizando a linguagem **Python 3.10**.

**Bibliotecas principais:**

- `pandas`, `numpy` – Manipulação de dados  
- `matplotlib`, `seaborn` – Visualização gráfica  
- `scikit-learn` – Análise estatística e modelagem  
- `geopandas` – Análise espacial  

---

## 🧠 Conclusão Esperada

Espera-se que distritos com menor desenvolvimento humano apresentem, em média, IDEBs mais baixos — reforçando a necessidade de políticas públicas que integrem aspectos educacionais e sociais.
