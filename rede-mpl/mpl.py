import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# =========================
# 1) Carregar base
# =========================
df = pd.read_csv("heart_disease_uci.csv")

# =========================
# 2) Criar alvo binário
# =========================
df["target"] = (df["num"] > 0).astype(int)

# =========================
# 3) Selecionar atributos
# =========================
X = df.drop(columns=["id", "dataset", "num", "target"])
y = df["target"]

# =========================
# 4) Separar numéricos e categóricos
# =========================
num_cols = X.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X.select_dtypes(include=["object", "bool"]).columns

# =========================
# 5) Pipeline de pré-processamento
# =========================
numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_transformer, num_cols),
    ("cat", categorical_transformer, cat_cols)
])

# =========================
# 6) Divisão treino/teste
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# 7) Modelo MLP
# =========================
mlp = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

# Pipeline final
model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", mlp)
])

# =========================
# 8) Treinamento
# =========================
model.fit(X_train, y_train)

# =========================
# 9) Predição
# =========================
y_pred = model.predict(X_test)

# =========================
# 10) Avaliação
# =========================
print("Acurácia:", accuracy_score(y_test, y_pred))
print("\nRelatório:")
print(classification_report(y_test, y_pred))
print("\nMatriz de confusão:")
print(confusion_matrix(y_test, y_pred))