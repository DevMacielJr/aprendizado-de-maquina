# -*- coding: utf-8 -*-
"""Análise de Sentimentos com Google Translate + VADER"""

# ==========================================
# 📦 INSTALAÇÃO DAS BIBLIOTECAS
# ==========================================

!pip install googletrans==4.0.0-rc1

# ==========================================
# 📚 IMPORTAÇÃO DAS BIBLIOTECAS
# ==========================================

import pandas as pd
import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator

# Download do léxico do VADER
nltk.download('vader_lexicon')

# ==========================================
# 📊 CARREGAMENTO DO DATASET
# ==========================================

dataset = pd.read_csv(
    'https://raw.githubusercontent.com/ect-info/ml/master/dados/Restaurant_Reviews.tsv',
    delimiter='\t',
    quoting=3
)

print(dataset.head())

# ==========================================
# 🌐 INICIALIZAÇÃO DO TRADUTOR
# ==========================================

translator = Translator()

# ==========================================
# 😀 INICIALIZAÇÃO DO ANALISADOR VADER
# ==========================================

sid = SentimentIntensityAnalyzer()

# ==========================================
# 📝 EXEMPLO 1
# ==========================================

texto1 = 'Não é um bom aplicativo'

# Tradução PT → EN
texto1_traduzido = translator.translate(
    texto1,
    src='pt',
    dest='en'
).text

print('Texto original:', texto1)
print('Texto traduzido:', texto1_traduzido)

# Análise de sentimento
sentimento1 = sid.polarity_scores(texto1_traduzido)

print('Sentimento:', sentimento1)

# ==========================================
# 📝 EXEMPLO 2
# ==========================================

texto2 = 'Eu gostei do aplicativo'

texto2_traduzido = translator.translate(
    texto2,
    src='pt',
    dest='en'
).text

print('\nTexto original:', texto2)
print('Texto traduzido:', texto2_traduzido)

sentimento2 = sid.polarity_scores(texto2_traduzido)

print('Sentimento:', sentimento2)

# ==========================================
# 🍔 ANÁLISE DE UMA REVIEW DO DATASET
# ==========================================

review = dataset['Review'][2]

print('\nReview original:', review)

# A review já está em inglês
review_traduzida = translator.translate(
    review,
    src='en',
    dest='en'
).text

sentimento_review = sid.polarity_scores(review_traduzida)

print('Sentimento da review:', sentimento_review)