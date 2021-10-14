import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


N = 1000
RADIUS = 1

rng = np.random.default_rng(seed=0)

r = rng.uniform(0, RADIUS**2, size=N) ** 0.5
phi = rng.uniform(0, 2*np.pi, size=N)

x = r * np.cos(phi)
y = r * np.sin(phi)

labels = r < (RADIUS/np.sqrt(2))

df = pd.DataFrame(
    data=np.stack([x, y, labels], axis=1),
    columns=['x', 'y', 'target'],
)
df.to_csv('data.csv')

fig, ax = plt.subplots(figsize=(6, 6))
ax.set(xlabel='x', ylabel='y')
ax.scatter(x, y, s=5, c=labels)

plt.show()
