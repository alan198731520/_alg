import math

# 定義函數 f(x, y)
def f(x, y):
    return math.sin(x * y) + math.exp(x)

# 測試函數
x = 2
y = 3
result = f(x, y)
print(f"f({x}, {y}) = {result}")