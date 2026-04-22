# 📊 K-Means Clustering - Customer Segmentation

Projeto de **Aprendizado de Máquina (Machine Learning)** utilizando o algoritmo **K-Means** para segmentação de clientes com base em características demográficas e comportamentais.

---

## 🚀 Objetivo

Aplicar técnicas de **aprendizado não supervisionado** para identificar grupos de clientes com perfis semelhantes, permitindo análises estratégicas e tomada de decisão baseada em dados.

---

## 📂 Dataset

* Base: *Customer Segmentation Dataset*
* Fonte: Kaggle
* Atributos incluem dados como:

  * Idade
  * Renda
  * Score de gasto
  * Outros dados demográficos

---

## ⚙️ Tecnologias Utilizadas

* Python 🐍
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🧠 Etapas do Projeto

### 1. Análise Exploratória

* Visualização dos dados
* Estatísticas descritivas

### 2. Pré-processamento

* Seleção de atributos numéricos
* Tratamento de dados

### 3. Normalização

* Uso do `StandardScaler`
* Essencial para algoritmos baseados em distância

### 4. Clusterização (K-Means)

* Definição do número de clusters (método do cotovelo)
* Treinamento do modelo

### 5. Análise dos Centróides

* Interpretação dos perfis médios de cada grupo
* Comparação entre clusters

---

## 📊 Visualizações

### 📌 Método do Cotovelo

Identificação do número ideal de clusters.

### 📌 Gráfico de Barras dos Centróides

Comparação dos atributos médios por cluster.

### 📌 Heatmap

Visualização intuitiva das diferenças entre grupos.

### 📌 Visualização 2D (Clusters)

Representação gráfica dos agrupamentos.

---

## 📈 Resultados

O modelo K-Means conseguiu separar os clientes em grupos distintos, revelando padrões como:

* Clientes de alto consumo
* Clientes econômicos
* Perfis intermediários

Os centróides permitiram entender o comportamento médio de cada grupo.

---

## 🧪 Teste com Novo Cliente

O modelo permite classificar novos clientes em um dos clusters, facilitando aplicações práticas como:

* Marketing direcionado
* Personalização de serviços

---

## 📌 Estrutura do Projeto

```
k-means/
│
├── k-means.py
├── segmentation data.csv
├── segmentation data legend.xlsx
└── README.md
```

---

## 💡 Melhorias Futuras

* Aplicação de PCA para visualização 2D mais robusta
* Uso de Silhouette Score para avaliação
* Dashboard interativo com Streamlit
* Deploy do modelo

---

## 👨‍💻 Autor

**Edson Maciel e Barros Junior**
Curso de Ciências e Tecnologia

---

## 📚 Conclusão

Este projeto demonstrou a aplicação prática do algoritmo K-Means em um problema real de segmentação de clientes.

A análise dos centróides e das visualizações permitiu extrair insights relevantes, reforçando conceitos de aprendizado não supervisionado.

---
