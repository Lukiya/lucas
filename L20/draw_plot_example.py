import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure and axis
fig, ax = plt.subplots()

# Create a polygon and add it to the axis
triangle_points = [(1, 1), (2, 4), (4, 2)]
triangle = patches.Polygon(triangle_points, closed=True, edgecolor='b')   # blue edge line, default inner color
ax.add_patch(triangle)

# Use Polygon to draw a rectangle
rectangle_points = [(1, 1), (1, 4), (3, 4), (3, 1)]
rectangle = patches.Polygon(rectangle_points, closed=True, edgecolor='r', facecolor='none')   # red edge line, no inner color
ax.add_patch(rectangle)

# Set axis limits
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)

# Show the plot
plt.show()
