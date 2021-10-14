import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def plot_prediction(X, y, y_pred, *, title=''):
    if isinstance(X, pd.DataFrame):
        X = X.to_numpy()
    fig, (left, right) = plt.subplots(ncols=2, figsize=(14, 6))
    fig.suptitle(title)
    left.set(title='Ground truth labels')
    left.scatter(*X.transpose(), c=y)
    right.set(title='Predicted labels')
    right.scatter(*X.transpose(), c=y_pred)


df = pd.read_csv('data.csv', index_col=0)

features = df[['x', 'y']]
target = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    features, target,
    test_size=0.3,
    random_state=0,
    shuffle=True,
)

model = RidgeClassifier()
model.fit(X_train, y_train)

cm_train = confusion_matrix(y_train, model.predict(X_train))
print(
    'Confusion matrix for training data:', cm_train,
    f'Accuracy: {np.diag(cm_train).sum() / cm_train.sum()}',
    sep='\n',
)
cm_test = confusion_matrix(y_test, model.predict(X_test))
print(
    'Confusion matrix for test data:', cm_test,
    f'Accuracy: {np.diag(cm_test).sum() / cm_test.sum()}',
    sep='\n',
)

plot_prediction(X_train, y_train, model.predict(X_train), title='Training data')
plot_prediction(X_test, y_test, model.predict(X_test), title='Test data')
plt.show()
