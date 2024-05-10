import numpy as np, pandas as pd
from IPython.display import display

n = 10_000
X = np.random.randn(n, 10)
valuable_features = [0, 1, 4, 5, 8]

# y = sign(f0 + f1 + f4 + f5 + f8)
noise = np.random.randn(n) / 5
y = ((X[:, valuable_features].sum(axis=1) + noise) > 0).astype(np.uint8)

display(pd.Series(y).value_counts())

from sklearn.model_selection import train_test_split

X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.3, stratify=y, shuffle=True, random_state=911)