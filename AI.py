import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, Matern

# data(can be SQL)
X = np.array([[0], [25], [50], [75], [100]])  # A  (%)
y = np.array([1.5, 0.8, 0.5, 0.9, 1.2])      # IC50


kernel_rbf = 1.0 * RBF(length_scale=10.0)
kernel_matern = 1.0 * Matern(length_scale=10.0, nu=1.5)

model_rbf = GaussianProcessRegressor(kernel=kernel_rbf, alpha=1e-6)
model_matern = GaussianProcessRegressor(kernel=kernel_matern, alpha=1e-6)

# --- 3. 訓練---
model_rbf.fit(X, y)
model_matern.fit(X, y)

# --- 4. 預測---
X_pred = np.linspace(0, 100, 200).reshape(-1, 1)
y_rbf, std_rbf = model_rbf.predict(X_pred, return_std=True)
y_matern, std_matern = model_matern.predict(X_pred, return_std=True)

# --- 5. 畫---
plt.figure(figsize=(10, 5))
plt.scatter(X, y, c='red', label='文獻數據點')
plt.plot(X_pred, y_rbf, '--', label='RBF (平滑)')
plt.plot(X_pred, y_matern, '-', label='Matern (可折角)')
plt.fill_between(X_pred.ravel(), y_rbf - std_rbf, y_rbf + std_rbf, alpha=0.2)
plt.fill_between(X_pred.ravel(), y_matern - std_matern, y_matern + std_matern, alpha=0.2)
plt.xlabel('A 比例 (%)')
plt.ylabel('IC50')
plt.legend()
plt.show()