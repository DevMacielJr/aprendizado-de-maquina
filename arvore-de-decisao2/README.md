# 🧠 Árvore de Decisão - Classificação de Parkinson

Este projeto aplica técnicas de **Aprendizado de Máquina** para classificar a gravidade da doença de Parkinson com base em características vocais dos pacientes.

---

## 📌 Objetivo

Transformar um problema de regressão em um problema de **classificação supervisionada**, utilizando uma Árvore de Decisão para identificar se um paciente apresenta um nível **leve** ou **grave** da doença.

---

## 📊 Base de Dados

* Dataset: Parkinsons Telemonitoring
* Fonte: Kaggle / UCI Machine Learning Repository
* Registros: ~5.800 amostras
* Atributos: Características biomédicas e vocais

### 🔎 Principais variáveis:

* `age` → idade do paciente
* `sex` → sexo
* `jitter`, `shimmer` → variações na frequência vocal
* `hnr`, `nhr` → relação harmônica do som
* `rpde`, `dfa`, `ppe` → parâmetros avançados de voz

---

## 🎯 Variável Alvo

A variável `total_updrs` foi transformada em uma classificação binária:

* **Leve** → valores ≤ 20
* **Grave** → valores > 20

Após a transformação, a variável original foi removida para evitar redundância.

---

## 🤖 Modelo Utilizado

* 🌳 Árvore de Decisão (`DecisionTreeClassifier`)
* Critério: Entropia
* Controle de complexidade: Profundidade máxima (`max_depth`)

---

## ⚙️ Etapas do Projeto

1. Carregamento dos dados
2. Análise exploratória
3. Tratamento e limpeza dos dados
4. Transformação do problema (regressão → classificação)
5. Divisão treino/teste
6. Treinamento do modelo
7. Avaliação de desempenho
8. Análise de variáveis importantes

---

## 📈 Avaliação

O modelo foi avaliado utilizando:

* ✅ Acurácia
* ✅ Matriz de Confusão
* ✅ Precision, Recall e F1-score

---

## 📊 Visualizações

O projeto inclui diversas análises gráficas:

* 📉 Matriz de correlação
* 📊 Distribuição das classes
* 📦 Boxplots das variáveis
* 🌳 Estrutura da árvore de decisão
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
cd aprendizado-de-maquina/arvore-de-decisao
```

3. Execute o notebook no Google Colab ou Jupyter Notebook.

---

## 🎯 Resultados

* O modelo apresentou bom desempenho na classificação da gravidade da doença
* Variáveis relacionadas à frequência vocal mostraram alta relevância
* O controle da profundidade da árvore impactou diretamente o desempenho

---

## 🧠 Aprendizados

Este projeto permitiu desenvolver:

* Transformação de problemas de regressão em classificação
* Aplicação prática de Árvores de Decisão
* Interpretação de modelos baseados em árvore
* Análise exploratória de dados reais

---

## 👨‍💻 Autor

**Edson Maciel de Barros Junior**
Estudante de Ciência e Tecnologia - UFRN

---

## ⭐ Considerações Finais

A Árvore de Decisão demonstrou ser uma abordagem eficiente e interpretável para classificação de dados biomédicos, sendo uma ferramenta importante no apoio à análise de doenças como o Parkinson.
