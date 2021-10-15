#!/usr/bin/env python3

"""
Code snippets from [1].

Changes:

* use consistent variable names
* use epochs=500 to converge
* plot train loss and confusion matrix in one figure
* explicitly set learning_rate and batch_size, but use default values

[1] https://carpentries-incubator.github.io/deep-learning-intro/02-keras/index.html
"""

import seaborn as sns

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

import tensorflow
from tensorflow import keras

import matplotlib.pyplot as plt


tensorflow.random.set_seed(2)

df = sns.load_dataset("penguins").drop(columns=["island", "sex"]).dropna()
df["species"] = df["species"].astype("category")
df_features = df.drop(columns=["species"])
df_target = pd.get_dummies(df["species"])

X_train, X_test, y_train, y_test = train_test_split(
    df_features,
    df_target,
    test_size=0.2,
    random_state=0,
    shuffle=True,
    stratify=df_target,
)

inputs = keras.Input(shape=X_train.shape[1])
hidden_layer = keras.layers.Dense(10, activation="relu")(inputs)
output_layer = keras.layers.Dense(3, activation="softmax")(hidden_layer)

model = keras.Model(inputs=inputs, outputs=output_layer)
model.summary()
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss=keras.losses.CategoricalCrossentropy(),
)
history = model.fit(
    X_train,
    y_train,
    epochs=500,
    ##batch_size=X_train.shape[0],
    batch_size=32,
    verbose=0,
    shuffle=True,
)

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))
axs[0].semilogy(history.epoch, history.history["loss"], label="train loss")
axs[0].set_xlabel("epoch")
axs[0].set_ylabel("loss")
axs[0].legend()

y_pred = model.predict(X_test)
df_y_pred = pd.DataFrame(y_pred, columns=df_target.columns)
sr_y_pred_species = df_y_pred.idxmax(axis="columns")
sr_y_true_species = y_test.idxmax(axis="columns")
cm = confusion_matrix(sr_y_true_species, sr_y_pred_species)
print(cm)
df_cm = pd.DataFrame(
    cm, index=y_test.columns.values, columns=y_test.columns.values
)
df_cm.index.name = "true label"
df_cm.columns.name = "predicted label"

axs[1].set_aspect(adjustable="box", aspect=1)
sns.heatmap(df_cm, annot=True, ax=axs[1])

fig.tight_layout()
plt.show()
