'''Lezione di base con scykit.learn'''

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
#load the iris dataset 

#iris è un dataset molto utilizzato, è preinstallato in molti framework
iris = sns.load_dataset('iris')

#la funzione head() restituisce le prime 5 righe del dataset.
#print(iris.head())

#ogni riga della tabella rappresenta un fiore, sulle colonne sono riportate le caratteristiche di quello specifico fiore.


'''
Le seguenti linee di codice servono a visualizzare la distribuzione di alcuni dati
    sns.pairplot(iris, hue = 'species', height=2)
    plt.show()
'''

#Bisogna preparare i dati in modo da avere una lista di samples e di label

X_iris = iris.drop('species',axis=1) #escludiamo l'ultima colonna (che rappresenta i label)

#ora vogliamo prendere i label prendendo solo l'ultima colonna 

y_iris = iris['species']

#create training and test data set
X_train,X_test,y_train,y_test = train_test_split(X_iris,y_iris,train_size=0.8)

#crea un istanza del modello 
model = GaussianNB()

#train the model 
model.fit(X_train,y_train)

y_prediction = model.predict(X_test)

#controllo dell'accuratezza del modello
accuracy = accuracy_score(y_prediction,y_test)

print(accuracy)

