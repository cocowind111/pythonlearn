import numpy as np
import matplotlib.pyplot as plt

# 参数设置
nx = 100  # 网格数量
L = 10.0  # 水槽长度
dx = L / nx  # 网格间距
dt = 0.01  # 时间步长
g = 9.81  # 重力加速度
Tmax = 2.0  # 模拟时间
x = np.linspace(0, L, nx)  # 空间网格

# 初始化水深和速度
h = np.ones(nx)  # 水深初始值
u = np.zeros(nx)  # 速度初始值

# 初始条件：在中心加一个小波动
h[int(nx/2)-5:int(nx/2)+5] = 2.0
u[int(nx/2)-5:int(nx/2)+5] = 1.0

# 更新函数：Lax-Friedrichs 方法
def update(h, u, dx, dt, g):
    h_new = h.copy()
    u_new = u.copy()

    # 计算新的水深和速度
    for i in range(1, nx-1):
        # 质量守恒方程
        h_new[i] = h[i] - dt/dx * (h[i] * u[i] - h[i-1] * u[i-1])

        # 动量方程
        u_new[i] = u[i] - dt/dx * (u[i]**2 + 0.5*g*h[i]**2 - u[i-1]**2 - 0.5*g*h[i-1]**2)

    # 边界条件：简单的反射边界条件
    h_new[0] = h_new[1]
    h_new[-1] = h_new[-2]
    u_new[0] = -u_new[1]
    u_new[-1] = -u_new[-2]

    return h_new, u_new

# 时间步进
t = 0.0
fig, ax = plt.subplots()

while t < Tmax:
    h, u = update(h, u, dx, dt, g)
    t += dt
    
    # 可视化当前状态
    if int(t*10) % 1 == 0:
        ax.clear()
        ax.plot(x, h, label="Water Depth")
        ax.set_title(f"Time: {t:.2f} seconds")
        ax.set_xlabel("x (m)")
        ax.set_ylabel("Water Depth (m)")
        ax.legend()
        plt.pause(0.1)

plt.show()