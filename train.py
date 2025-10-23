# train.py
# Foi trocado para uma Arvore de classificação
# A base de dados foi colocada como a iris

!pip install ucimlrepo
from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier


# 1. Leitura dos dados
df = fetch_ucirepo(id=53)

X = df.data.features
y = df.data.targets

# 2. Divisão dos dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Treinamento do modelo
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 4. Avaliação
y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred)

# 5. Salvamento do relatório
with open("report.txt", "w") as f:
    f.write(report)
