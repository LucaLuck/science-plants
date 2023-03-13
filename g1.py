from matplotlib import pyplot as plt
import numpy as np

fig, ax1 = plt.subplots()
#layout
left = 0.125  # the left side of the subplots of the figure
right = 0.9   # the right side of the subplots of the figure
bottom = 0.11  # the bottom of the subplots of the figure
top = 0.85     # the top of the subplots of the figure
fig.subplots_adjust(left, bottom, right, top)


# setting the x and y axes
time_x = [17.2, 18.2, 19.2, 20.2, 21.2, 22.2, 23.2, 24.2, 25.2, 26.2, 27.2]
temperature_x = [30, 35, 35, 35, 35, 31, 50, 45, 43, 43, 40]
length_y = [13, 12.5, 14, 17, 21, 24, 26, 27.5, 28, 29, 30,]

#face colour
background = '#658864'
ingraph = '#EDF1D6'
titleColor = '#698269'

ax1.set_facecolor(ingraph)
fig.set_facecolor(background)

#title + ax label
font1 = {'family':'sans-serif','color': ingraph,'size':15}
font2 = {'family':'sans-serif','color': ingraph,'size':10}
ax1.set_title('High temperature plants', font1)
ax1.set_xlabel('time(date)', font2, fontweight = 'bold')
ax1.set_ylabel('height of plant(cm)', font2, fontweight = 'bold')

#setting ticks
ax1.set_xticks(time_x)
ax1.set_yticks(np.arange(min(length_y)-0.5, max(length_y)+1, 2.0))

#add grid + grid style 
ax1.grid(linestyle=':', linewidth=1)
ax1.plot(time_x, length_y, color = '#AA5656', marker = '.')

ax2 = ax1.twiny()
ax2.set_xlim(ax1.get_xlim())
ax2.set_xticks(time_x)
ax2.set_xticklabels(temperature_x)
ax2.xaxis.set_label_position('top')
ax2.set_xlabel('temperature(°C)', font2, fontweight = 'bold')

plt.show()

print(plt.style.available)