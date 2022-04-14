import pandas as pd
import numpy as np
import seaborn as sns
import csv
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, export_graphviz  # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn import metrics
from six import StringIO
import IPython.display
import pydotplus

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)

# making data frame from  data file
df = pd.read_csv(r'abc.csv')
print(df)

feature_cols = ['Gender', 'Age(yrs)', 'Income(thousand)', 'Education level', 'Professional Employment']
X = df[feature_cols]  # Features
y = df.SubscriptionStatus  # Target variable

a = X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier(criterion='entropy')

clf = clf.fit(X_train, y_train)
clf = clf.fit(X, y)

y_pred = clf.predict(X_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data, filled=True, rounded=True, special_characters=True, feature_names=feature_cols, class_names=['0', '1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('diabetes.png')
IPython.display.Image(graph.create_png())
