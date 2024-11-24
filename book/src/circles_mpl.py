import matplotlib.pyplot as plt

# Create a simple plot
fig, ax = plt.subplots()
ax.add_patch(plt.Circle((0.125, 0.5), 0.1, color='blue'))
ax.add_patch(plt.Circle((0.275, 0.5), 0.1, color='blue'))

# Set limits and show the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()