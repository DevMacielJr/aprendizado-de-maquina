import pandas as pd
import numpy as np

from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
    GridSearchCV,
    cross_val_score
)
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)

# ====================================
# 1) Carregar base
# ====================================
df = pd.read_csv("heart_disease_uci.csv")

# ====================================
# 2) Criar alvo binário
# ====================================
df["target"] = (df["num"] > 0).astype(int)

# ====================================
# 3) Selecionar atributos
# ====================================
X = df.drop(columns=["id", "dataset", "num", "target"])
y = df["target"]

# ====================================
# 4) Separar tipos
# ====================================
num_cols = X.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X.select_dtypes(include=["object", "bool"]).columns

# ====================================
# 5) Pré-processamento
# ====================================
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

# ====================================
# 6) Divisão treino/teste
# ====================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# ====================================
# 7) Pipeline base
# ====================================
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", MLPClassifier(
        activation="relu",
        solver="adam",
        early_stopping=True,
        validation_fraction=0.1,
        n_iter_no_change=20,
        max_iter=2000,
        random_state=42
    ))
])

# ====================================
# 8) Grid Search
# ====================================
param_grid = {
    "classifier__hidden_layer_sizes": [
        (8,),
        (16,),
        (16, 8),
        (32, 16)
    ],
    "classifier__alpha": [0.0001, 0.001, 0.01],
    "classifier__learning_rate_init": [0.001, 0.01]
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

grid = GridSearchCV(
    pipeline,
    param_grid,
    cv=cv,
    scoring="f1",
    n_jobs=-1
)

# ====================================
# 9) Treinamento
# ====================================
grid.fit(X_train, y_train)

best_model = grid.best_estimator_

print("Melhores parâmetros:")
print(grid.best_params_)

# ====================================
# 10) Predição
# ====================================
y_pred = best_model.predict(X_test)
y_proba = best_model.predict_proba(X_test)[:, 1]

# ====================================
# 11) Avaliação
# ====================================
print("\nAcurácia:", accuracy_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_proba))

print("\nRelatório:")
print(classification_report(y_test, y_pred))

print("\nMatriz de confusão:")
print(confusion_matrix(y_test, y_pred))

# ====================================
# 12) Cross-validation final
# ====================================
scores = cross_val_score(
    best_model,
    X,
    y,
    cv=cv,
    scoring="f1"
)

print("\nF1 médio na validação cruzada:", scores.mean())