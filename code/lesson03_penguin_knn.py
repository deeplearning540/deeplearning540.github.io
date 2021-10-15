#!/usr/bin/env python3

"""
KNN classification using the penguin dataset.

Use all possible combinations of 2, 3 or all 4 features. Also vary n_neighbors
and show that none of them helps to build a classifier that provides a fully
diagonal confusion matrix (= perfect classification), however some are close,
e.g.

n_neighbors=6, features=('bill_length_mm', 'bill_depth_mm')
[[29  1  0]
 [ 1 13  0]
 [ 0  0 25]]

n_neighbors=5, features=('bill_length_mm', 'bill_depth_mm')
[[29  1  0]
 [ 0 14  0]
 [ 0  0 25]]
"""

import itertools

import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier


##df = pd.read_csv("https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv")
# seaborn will create cache ~/seaborn-data by default, so should be faster than
# pd.read_csv() polling github in each run
df = sns.load_dataset("penguins").drop(columns=["island", "sex"]).dropna()
df["species"] = df["species"].astype("category")
df_features = df.drop(columns=["species"])
sr_target = df["species"]
y = sr_target.cat.codes.to_numpy()

# df_features.columns = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
feature_combos = list(
    itertools.chain(
        *(itertools.combinations(df_features.columns, n) for n in [2, 3, 4])
    )
)
for n_neighbors in [4, 5, 6]:
    for cols in feature_combos:
        X = df_features[list(cols)].values
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=0,
            shuffle=True,
            stratify=y,
        )

        model = KNeighborsClassifier(n_neighbors).fit(X_train, y_train)
        print("")
        print(f"{n_neighbors=}, features={cols}")
        print(confusion_matrix(y_test, model.predict(X_test)))
