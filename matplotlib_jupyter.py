import random

fig,ax = plt.subplots(1,1)

random_int = []
timeline = []

for i in range(0, 30) :
    random_int.append(random.randint(0, 100))
    timeline.append(i)
    
ax.plot(random_int, label = 'random')
ax.set_ylim(0, 100)

ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1, borderaxespad=0.)
ax.set_xlabel('timesteps')
ax.set_ylabel('random number')
ax.grid()
ax.set_title('random')

while True:
    for i in range(0, 29) :
        random_int[i] = random_int[i + 1]
        timeline[i] = timeline[i + 1]
        
    random_int[29] = random.randint(0, 100)
    timeline[29] = timeline[28] + 1
    
    ax.set_xlim(timeline[0], timeline[29])
    
    line = ax.lines[0]
    line.set_ydata(random_int)
    line.set_xdata(timeline)
    
    fig.canvas.draw()
    time.sleep(0.01)
