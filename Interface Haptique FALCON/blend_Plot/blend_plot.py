import matplotlib.pyplot as plt

with open('blend.txt', 'r') as file:
    lines = file.readlines()

column1 = []
column2 = []
column3 = []
column4 = []

for line in lines:
    data = line.split()
    if len(data) >= 4:
        column1.append(float(data[0]))
        column2.append(float(data[1]))
        column3.append(float(data[2]))
        column4.append(float(data[3]))

fig, axes = plt.subplots(3, 1, figsize=(8, 12))

axes[0].plot(column1, column2, label='Col 2 vs Col 1', color='b')
axes[0].set_xlabel('Col 1')
axes[0].set_ylabel('Col 2')

axes[1].plot(column1, column3, label='Col 3 vs Col 1', color='g')
axes[1].set_xlabel('Col 1')
axes[1].set_ylabel('Col 3')

axes[2].plot(column1, column4, label='Col 4 vs Col 1', color='r')
axes[2].set_xlabel('Col 1')
axes[2].set_ylabel('Col 4')

for ax in axes:
    ax.legend()

plt.tight_layout()
plt.show()
