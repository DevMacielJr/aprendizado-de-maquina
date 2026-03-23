# 🌳 Árvore de Decisão - Classificação Iris

Este projeto implementa um modelo de **Árvore de Decisão** para classificação das espécies de flores do conjunto de dados Iris, aplicando conceitos de **Aprendizado de Máquina supervisionado** vistos em aula.

---

## 📌 Objetivo

Construir um modelo capaz de classificar automaticamente a espécie de uma flor Iris com base em suas características físicas.

---

## 📊 Base de Dados

* Dataset: Iris Dataset

* Fonte: UCI / disponibilizado via repositório acadêmico

* Atributos utilizados:

  * SepalLengthCm (Comprimento da sépala)
  * SepalWidthCm (Largura da sépala)
  * PetalLengthCm (Comprimento da pétala)
  * PetalWidthCm (Largura da pétala)

* Classes:

  * Setosa
  * Versicolor
  * Virginica

---

## 🤖 Modelo Utilizado

* 🌳 Árvore de Decisão (`DecisionTreeClassifier`)
* Critério: Entropia
* Controle de complexidade: Profundidade máxima (`max_depth`)

---

## ⚙️ Etapas do Projeto

1. Carregamento dos dados
2. Análise exploratória
3. Separação entre treino e teste
4. Treinamento do modelo
5. Avaliação de desempenho
6. Visualização da árvore
7. Teste com novas amostras

---

## 📈 Avaliação

O modelo foi avaliado utilizando:

* ✅ Acurácia
* ✅ Matriz de Confusão
* ✅ Precision, Recall e F1-score

---

## 📊 Visualizações

O projeto inclui diversas visualizações para análise do modelo:

* 🌿 Estrutura da árvore de decisão
* 📉 Matriz de confusão (heatmap)
* 📊 Importância das variáveis
* 📈 Acurácia vs profundidade

---

## 🚀 Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/DevMacielJr/aprendizado-de-maquina.git
```

2. Acesse a pasta do projeto:

```bash
cd aprendizado-de-maquina/arvore-decisao
```

3. Abra o notebook no Google Colab ou Jupyter Notebook.

---

## 🎯 Resultados

* O modelo apresentou alta acurácia na classificação das espécies
* A árvore de decisão mostrou-se interpretável e eficiente
* A análise de profundidade evidenciou o impacto do overfitting

---

## 🧠 Aprendizados

Este projeto permitiu compreender:

* Funcionamento de algoritmos de classificação
* Importância do pré-processamento de dados
* Avaliação de modelos com múltiplas métricas
* Interpretação de modelos baseados em árvore

---

## 👨‍💻 Autor

**Edson Maciel de Barros Junior**
Estudante de Ciência e Tecnologia - UFRN

---

## ⭐ Considerações Finais

A Árvore de Decisão é um modelo simples e interpretável, sendo uma excelente introdução a algoritmos de classificação em Machine Learning. Este projeto demonstra sua aplicação prática em um problema clássico da área.
