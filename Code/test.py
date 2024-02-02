import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 模型参数
a = 0.1  # 兔子的自然增长率
b = 0.02 # 狼捕食兔子的率
c = 0.3  # 狼的自然死亡率
d = 0.01 # 狼因捕食兔子而增长的率

# 洛特卡-沃尔泰拉方程
def lotka_volterra(y, t, a, b, c, d):
    rabbit, wolf = y
    dydt = [a * rabbit - b * rabbit * wolf, d * rabbit * wolf - c * wolf]
    return dydt

# 初始条件y

rabbit0 = 40
wolf0 = 9
y0 = [rabbit0, wolf0]

# 时间点
t = np.linspace(0, 200, 500)

# 求解ODE
solution = odeint(lotka_volterra, y0, t, args=(a, b, c, d))

# 绘图
plt.figure(figsize=(8, 4))
plt.plot(t, solution[:, 0], label='兔子')
plt.plot(t, solution[:, 1], label='狼')
plt.xlabel('时间')
plt.ylabel('种群数量')
plt.title('洛特卡-沃尔泰拉模型')
plt.legend()
plt.show()
