from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure()
fig.set_facecolor('lightsteelblue')


#fig.set_edgecolor('green')

##fig.set_edgecolor('green')

# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()

##print(plt.style.available) show styles available

plt.style.use('Solarize_Light2')

x_axes = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
y_axes = [40, 42, 46, 49, 53, 56, 62, 64, 67, 68, 73]

#plt.plot(x_axes, y_axes, 'green')

#plt.plot([30, 40, 50], [20, 25, 30], 'ro')

#plt.axis([0, 50, 0, 10]) [xmin, xmax, ymin, ymax]

plt.title('Plant')

plt.xlabel('time')
plt.ylabel('length')

plt.plot(x_axes, y_axes, color='green', marker='.', linestyle=':',
     linewidth=2, markersize=12)

plt.grid(True)

plt.show()


