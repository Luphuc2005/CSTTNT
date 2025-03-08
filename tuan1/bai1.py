import matplotlib.pyplot as plt
import numpy as np
data = np.array([[147, 49], [150, 50], [153, 51], [155, 52], [158, 54],
                [160, 56], [163, 58], [165, 59], [168, 60], [170, 72],
                [173, 63], [175, 64], [178, 66], [180, 67], [183, 68]])

height = data[:, 0]
weight = data[:, 1]

plt.xlabel("Chiều cao (cm)")
plt.ylabel("Cân nặng (kg)")
plt.scatter(height, weight, color="red")
