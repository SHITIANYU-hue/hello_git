import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)  # 创建在一定范围内间隔均匀数字列表
plt.plot(x, np.sin(x))       # 绘制每个x点的正弦值
plt.show()                   # 显示列表