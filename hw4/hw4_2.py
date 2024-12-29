import numpy as np

# 定義函數
def f(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

def monte_carlo_integration(f, bounds, num_samples):
    dim = len(bounds)
    random_points = [np.random.uniform(low, high, num_samples) for low, high in bounds]
    f_values = f(*random_points)
    volume = np.prod([high - low for low, high in bounds])
    return np.mean(f_values) * volume

# 定義邊界與樣本數
bounds = [(0, 1), (0, 1), (0, 1)]
num_samples = 1000000

# 計算蒙地卡羅積分
result = monte_carlo_integration(f, bounds, num_samples)
print(f"蒙地卡羅法近似積分結果：{result}")