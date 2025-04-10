'''Lezione di base con scykit.learn'''

import seaborn as sns
import matplotlib.pyplot as plt

#load the iris dataset 

#iris è un dataset molto utilizzato, è preinstallato in molti framework
iris = sns.load_dataset('iris')

#la funzione head() restituisce le prime 5 righe del dataset.
print(iris.head())

#ogni riga della tabella rappresenta un fiore, sulle colonne sono riportate le caratteristiche di quello specifico fiore.



sns.pairplot(iris, hue = 'species', height=2)
plt.show()