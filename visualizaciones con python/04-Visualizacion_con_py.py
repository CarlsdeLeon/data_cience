import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#Datos para el grafico de ejemplo
edades = [20, 25, 30, 25, 40]

plt.plot(edades)
plt.title("Mi primer grafico en py")
plt.show()

print(sns.get_dataset_names())
titanic = sns.load_dataset('titanic')
print(titanic.head())

plt.scatter(titanic['age'], titanic['fare'])
plt.xlabel('Edad')
plt.ylabel('Tarifa')
plt.title("Relacion entre Edad y tarifa")

plt.show()


### Seaborn

sns.boxplot(x='survived', y='age', data=titanic, palette='Set2')
plt.title('Distribucion de edad por supervivencia')

plt.show()

sns.barplot(x='pclass', y='survived', data=titanic, errorbar=None, hue='sex', ci=None, palette='muted', legend=True)
plt.title('Tasa de supervivencia por clase ')
plt.show()


fig = px.scatter(titanic, x='age', y='fare', color='survived', title='Relacion edad-tarifa por supervivencia', labels={'survived': 'sobrevivio'})
fig.show()

fig1 = px.scatter_3d(titanic, x='age', y='fare', z='pclass', color='survived', symbol="sex", title="Analisis 3D - Titanic", labels={'survived':'Supervivencia'})
fig1.show()
