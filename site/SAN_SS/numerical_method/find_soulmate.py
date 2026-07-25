import numpy as np
import matplotlib.pyplot as plt

# 设置参数
N = 100
simulations = 10000
success_rates = []

# 蒙特卡洛模拟核心逻辑
for k in range(1, N + 1):
    success = 0
    for _ in range(simulations):
        # 1-N的随机排列，数值越大越适合，N为最优
        candidates = np.random.permutation(N) + 1
        best_in_sample = max(candidates[:k-1], default=0)
        
        # 开发期：遇到更好的就直接选定
        for i in range(k-1, N):
            if candidates[i] > best_in_sample:
                if candidates[i] == N:  # 命中全局最优
                    success += 1
                break
    success_rates.append(success / simulations)

# 生成拟合曲线与图表
x_ratio = np.arange(1, N + 1) / N
plt.figure(figsize=(9, 6))

# 绘制离散的模拟数据点
plt.plot(x_ratio, success_rates, marker='o', markersize=4, linestyle='-', alpha=0.7, label='Simulated Probability')

# 绘制理论方程对应的平滑曲线： y = -x*ln(x)
x_theory = np.linspace(0.01, 0.99, 100)
y_theory = -x_theory * np.log(x_theory)
plt.plot(x_theory, y_theory, 'r-', linewidth=2.5, label='Theoretical Curve: $y = -x \ln(x)$')

# 标示最优截止点
plt.axvline(x=1/np.e, color='green', linestyle='--', label='Optimal Rule (1/e $\\approx$ 36.8%)')

plt.title("Optimization of Stopping Strategy in Candidate Selection")
plt.xlabel("Observation Fraction (k/N)")
plt.ylabel("Probability of Selecting the Absolute Best")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()