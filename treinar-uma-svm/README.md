# 🚢 Titanic Survival Prediction - SVM

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Sobre o Projeto

Este projeto utiliza **Machine Learning (SVM - Support Vector Machine)** para prever a sobrevivência de passageiros do Titanic.

A solução foi desenvolvida como atividade prática de **aprendizado supervisionado**, com foco em classificação binária.

---

## 🧠 Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 📊 Dataset

Base de dados disponível no Kaggle:

🔗 https://www.kaggle.com/competitions/titanic/data

---

## 🎯 Objetivo

Prever a variável:

* `Survived`

  * 0 → Não sobreviveu
  * 1 → Sobreviveu

---

## 📌 Variáveis Utilizadas

| Variável | Descrição       |
| -------- | --------------- |
| Pclass   | Classe social   |
| Sex      | Sexo            |
| Age      | Idade           |
| SibSp    | Irmãos/Cônjuges |
| Parch    | Pais/Filhos     |
| Fare     | Tarifa          |

---

## ⚙️ Pipeline do Projeto

1. 📥 Carregamento dos dados
2. 🧹 Pré-processamento
3. 🔄 Normalização (StandardScaler)
4. ✂️ Divisão treino/teste
5. 🤖 Treinamento (SVM - RBF)
6. 📈 Avaliação do modelo

---

## 📈 Resultados

* ✅ Acurácia média: **~80%**
* ✅ Modelo robusto para classificação binária

---

## 🖼️ Preview

### 📊 Matriz de Confusão

![Confusion Matrix](https://via.placeholder.com/600x300.png?text=Matriz+de+Confus%C3%A3o)

### 📈 Comparação de Kernels

![Kernel Comparison](https://via.placeholder.com/600x300.png?text=Compara%C3%A7%C3%A3o+de+Kernels)

---

## 🚀 Como Executar

```bash
git clone https://github.com/DevMacielJr/aprendizado-de-maquina.git
cd aprendizado-de-maquina
pip install -r requirements.txt
python treinar_uma_svm.py
```

---

## 📌 Estrutura do Projeto

```
aprendizado-de-maquina/
│
├── treinar-uma-svm/
│   └── treinar_uma_svm.py
│
├── README.md
└── requirements.txt
```

---

## 💡 Melhorias Futuras

* 🔥 GridSearchCV para otimização
* 📊 Dashboard interativo (Streamlit)
* 🤖 Comparação com outros modelos (Random Forest, KNN)

---

## 👨‍💻 Autor

**Edson Maciel e Barros Junior**
📚 Ciência e Tecnologia

---

## ⭐ Contribuição

Se gostou do projeto, deixe uma ⭐ no repositório!
