# 🧠 CNN para Classificação de Imagens - Fashion MNIST

Este projeto implementa uma **Rede Neural Convolucional (CNN)** para classificação de imagens da base **Fashion MNIST**, utilizando Python e TensorFlow/Keras.

---

## 📌 Sobre o Projeto

O objetivo é treinar um modelo capaz de reconhecer automaticamente tipos de roupas a partir de imagens em escala de cinza (28x28 pixels).

A base Fashion MNIST é composta por **70.000 imagens**, divididas em:

* 60.000 para treino
* 10.000 para teste

---

## 👕 Classes do Dataset

| Classe | Descrição   |
| ------ | ----------- |
| 0      | T-shirt/top |
| 1      | Trouser     |
| 2      | Pullover    |
| 3      | Dress       |
| 4      | Coat        |
| 5      | Sandal      |
| 6      | Shirt       |
| 7      | Sneaker     |
| 8      | Bag         |
| 9      | Ankle boot  |

---

## 🧠 Arquitetura da CNN

A rede utilizada possui:

* 2 camadas convolucionais (Conv2D)
* 2 camadas de pooling (MaxPooling)
* 1 camada Flatten
* 1 camada densa (Dense)
* Dropout para evitar overfitting
* Camada de saída com Softmax

---

## ⚙️ Tecnologias Utilizadas

* Python
* TensorFlow / Keras
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/DevMacielJr/aprendizado-de-maquina.git
```

2. Acesse a pasta:

```bash
cd aprendizado-de-maquina/rede-CNN
```

3. Execute o script:

```bash
python rede_convolucional_fashion_mnist.py
```

---

## 📊 Resultados

O modelo apresentou:

* Alta acurácia no conjunto de teste (~90%+)
* Boa generalização
* Dificuldade em classes visualmente semelhantes (ex: Shirt vs T-shirt)

---

## 📈 Visualizações

O projeto inclui:

* Gráfico de acurácia
* Gráfico de loss
* Matriz de confusão
* Teste com imagens reais

---

## 📚 Aprendizados

* Aplicação prática de CNN
* Pré-processamento de imagens
* Avaliação de modelos de classificação
* Interpretação de métricas

---

## 👨‍💻 Autor

**Edson Maciel e Barros Junior**
Curso de Ciências e Tecnologia

---

## 📌 Conclusão

A utilização de Redes Convolucionais mostrou-se altamente eficaz para tarefas de visão computacional, sendo capaz de extrair automaticamente características relevantes das imagens e realizar classificações com alta precisão.

---
