import numpy as np

def f(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

n = 100 
x_vals = np.linspace(0, 1, n)
y_vals = np.linspace(0, 1, n)
z_vals = np.linspace(0, 1, n)

# 創建三維網格
X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals, indexing='ij')

# 計算函數值
F = f(X, Y, Z)

dx = dy = dz = 1 / (n - 1)

# 使用 NumPy 求和
riemann_sum = np.sum(F) * dx * dy * dz

print(f"黎曼和法近似結果：{riemann_sum}")