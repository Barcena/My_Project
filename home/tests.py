from django.test import TestCase

#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Credit Scoring

@author: 0jmbea0

Logistic Regression
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" The first 20,046 rows are the important ones (aprox 200,000 rows)"""
dataset = pd.read_csv('./../../../../../Documents/dataset/loan.csv')

""" values are amount ($) & duration (month) """
X = dataset.iloc[:20046, [1,6]].values
""" value is paidOnTime (1 or 0) """
y = dataset.iloc[:20046, 4].values

""" 
    Split dataset with train & test to evaluate performance 
"""
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

""" 
    Scaling
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

"""
    Train the classifier with train set
"""
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

"""
    Predicting the Test set results
"""
y_pred = classifier.predict(X_test)

"""
    Confusion Matrix to eval if the model makes good decisions
"""
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

classifier.score(X = X_test, y = y_test)

from matplotlib.colors import ListedColormap
"""
    Visualising the training set
"""
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:,0].min() - 1, stop = X_set[:,0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:,0].min() - 1, stop = X_set[:,0].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
plt.show()