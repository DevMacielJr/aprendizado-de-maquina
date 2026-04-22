# 🧠 MLP - Classificação de Câncer de Mama

Este projeto aplica uma **Rede Neural Artificial (MLP - Multi-Layer Perceptron)** para classificar tumores como **malignos ou benignos** com base em características celulares.

---

## 📌 Objetivo

Construir e avaliar um modelo de **aprendizado supervisionado** capaz de realizar **classificação binária** em dados médicos.

---

## 📊 Dataset

O projeto utiliza o dataset **Breast Cancer Wisconsin**, disponível na biblioteca `scikit-learn`.

### 🔍 Características:

* 569 amostras
* 30 atributos numéricos
* Classes:

  * **Maligno**
  * **Benigno**

---

## 🧠 Modelo Utilizado

Foi utilizada uma **Rede Neural MLP** com a seguinte arquitetura:

* Camada de entrada: 30 variáveis
* Camada oculta 1: 16 neurônios
* Camada oculta 2: 8 neurônios
* Função de ativação: ReLU
* Otimizador: Adam

---

## ⚙️ Tecnologias Utilizadas

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🚀 Etapas do Projeto

1. Carregamento dos dados
2. Análise exploratória
3. Tratamento de dados (remoção de NaN)
4. Normalização (StandardScaler)
5. Divisão treino/teste
6. Treinamento da MLP
7. Avaliação do modelo
8. Visualizações gráficas

---

## 📈 Resultados

O modelo apresentou alta performance:

* ✅ Acurácia: ~95% a 98%
* 🔍 Boa separação entre classes
* 📊 Matriz de confusão consistente

---

## 📊 Visualizações

O projeto inclui:

* Matriz de confusão
* Curva de perda (loss)
* Distribuição das classes
* Correlação entre variáveis
* Boxplot de atributos

---

## 🔬 Testes Realizados

* Comparação entre diferentes arquiteturas de rede
* Variação da taxa de aprendizado
* Comparação com Random Forest

---

## ⚠️ Observações Importantes

* A normalização dos dados é essencial para o desempenho da MLP
* O tratamento de valores ausentes (NaN) é obrigatório
* A escolha da arquitetura impacta diretamente os resultados

---

## 📂 Estrutura do Projeto

```
📁 projeto-mlp-cancer
│
├── 📄 mlp_cancer.ipynb
├── 📄 README.md
└── 📄 requirements.txt
```

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o notebook:

```bash
jupyter notebook
```

---

## 📦 Dependências

```txt
numpy
pandas
matplotlib
seaborn
scikit-learn
```

---

## 👨‍💻 Autor

**Edson Macield e Barros Junior**
🎓 Ciências e Tecnologia

---

## 📌 Conclusão

A Rede Neural MLP demonstrou excelente desempenho na classificação de tumores, sendo uma alternativa eficiente para problemas de classificação em dados médicos.

O projeto reforça a importância do pré-processamento e da escolha adequada de hiperparâmetros para alcançar bons resultados em aprendizado de máquina.
