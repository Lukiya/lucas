import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_triangle():
    # Coordinates of the three vertices
    vertices = [(-1, -1), (3, -1), (2, 3)]
    
    # Create a new figure
    fig, ax = plt.subplots()
    
    # Add a triangle
    triangle = patches.Polygon(vertices, closed=True, edgecolor='r', facecolor='none')
    ax.add_patch(triangle)
    
    # Set integer ticks for the x-axis and y-axis
    x_ticks = np.arange(-2, 5, 1)  # Integer ticks from -2 to 5, each grid is 1
    y_ticks = np.arange(-2, 5, 1)  # Integer ticks from -2 to 5, each grid is 1
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    
    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    # Display the grid
    ax.grid(True, which='both')
    
    # Display the axes
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    draw_triangle()
