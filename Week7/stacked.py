# Data
groups = ['G1', 'G2', 'G3', 'G4', 'G5']
values1 = [12, 19, 14, 27, 16]
values2 = [21, 30, 15, 17, 20]

# Stacked bar chart
ax = (groups, values1)
ax = (groups, values2, bottom = values1)

# plt.show()