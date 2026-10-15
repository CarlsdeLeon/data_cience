import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize

# 1. Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
n_classes = len(class_names)

# 2. Binarizar las etiquetas para el enfoque One-vs-Rest (Transforma 0, 1, 2 en arreglos one hot)
y_bin = label_binarize(y, classes=[0, 1, 2])
print(y_bin)

# 3. Dividir en entrenamiento y prueba

X_train, X_test, y_train, y_test = train_test_split(X, y_bin, test_size=0.3, random_state=42)

# 4. entrenar el modelo con una estrategia One-vsRest (OvR)
clasificador = OneVsRestClassifier(RandomForestClassifier(n_estimators=100, random_state=42))

y_score = clasificador.fit(X_train, y_train).predict_proba(X_test)

# 5. Valcular ROC y AUC para cada clase

fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:,i], y_score[:,i])
    roc_auc[i] = auc(fpr[i],tpr[i])

# 6. Calcular ROC y aUC 'micro-avarage' (Global)

fpr['micro'], tpr['micro'], _ = roc_curve(y_test.ravel(), y_score.ravel())

roc_auc['micro'] = auc(fpr['micro'], tpr['micro'])

# 7. Graficar las curvas ROc
plt.figure(figsize=(9, 7))

# Curva Micro-promedia
plt.plot(fpr['micro'], tpr['micro'], label=f'Micro-promedio ROC (AUC = {roc_auc['micro']:.2f})', color='deeppink', linestyle=':', linewidth=3)

# Curvas por cada clase
colors = ['darkorange', 'cornflowerblue', 'green']

for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=2, label=f'Curva ROc para {class_names[i]} (AUC = {roc_auc[i]:.2f})')

# Linea de referencia aleatoria
plt.plot([0,1], [0,1], 'k--', lw=1.5, label = 'Clasificador aleatorio (AUC)')

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Tasa de Falsos Positivos (FPR)')
plt.ylabel('Tasa de Verdaderos Positivos (TPR)')
plt.title('Curvas ROC para Clasificación Multiclase (Iris Dataset)')
plt.legend(loc='lower right')
plt.grid(alpha = 0.3)
plt.show()