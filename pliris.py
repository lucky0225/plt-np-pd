import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

#Dataset
iris = load_iris()
#Spaltennamen
iris.feature_names

#Dataset mit Spaltennamen
Data_iris=iris.data
Data_iris = pd.DataFrame(Data_iris, columns = iris.feature_names)

#Spalte "label" hinzufügen -> "label" = iris.target
Data_iris["label"] = iris.target

#Scatterplot "Data_iris"
#alle rows, 2col
#alle rows, 3col
#c -> farbig
plt.scatter(Data_iris.iloc[:,2], Data_iris.iloc[:, 3], c = iris.target)
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.show()

#alle rows, erste 4 col
x = Data_iris.iloc[:,0:4]
y = Data_iris.iloc[:,4]

from sklearn.neighbors import KNeighborsClassifier

kNN = KNeighborsClassifier(n_neighbors=6, metric="minkowski", p=1)
print(kNN)

kNN.fit(x, y)

x_N = np.array([[5.6,3.4,1.4,0.1]])
kNN.predict(x_N)

x_N2 = np.array([[7.5, 4, 4.5, 2]])
kNN.predict(x_N2)