import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers


df = pd.read_csv('data.csv', index_col=0)
print(df.describe())

features = df[['x', 'y']]
target = pd.get_dummies(df['target'])

X_train, X_test, y_train, y_test = train_test_split(
    features, target,
    test_size=0.3,
    random_state=0,
    shuffle=True,
)

model = keras.Sequential([
    layers.Input(shape=features.shape[1]),
    layers.Dense(20, activation='relu'),
    layers.Dense(20, activation='relu'),
    layers.Dense(target.shape[1], activation='softmax'),
])
model.summary()

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-3),
    loss=keras.losses.CategoricalCrossentropy(),
    metrics=['accuracy'],
)
history = model.fit(X_train, y_train, epochs=100)

fig, ax = plt.subplots()
ax.set(title='Training loss during fitting', xlabel='Epoch', ylabel='Loss')
ax = sns.lineplot(x=history.epoch, y=history.history['loss'], ax=ax)

fig, ax = plt.subplots()
ax.set(title='Accuracy during fitting', xlabel='Epoch', ylabel='Accuracy')
ax = sns.lineplot(x=history.epoch, y=history.history['accuracy'], ax=ax)

y_test_hat = model.predict(X_test)
labels_predicted = y_test_hat.argmax(axis=1)
labels_reference = y_test.idxmax(axis=1)  # this is a pd.DataFrame --> using idxmax instead of argmax

cm = confusion_matrix(labels_reference, labels_predicted)
print('Confusion matrix:', cm, sep='\n', end='\n\n')
print(f'Accuracy on test set: {np.diag(cm).sum() / cm.sum():.3f}')

plt.show()
