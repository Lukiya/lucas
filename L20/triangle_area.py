import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_triangle():
    # Coordinates of the three vertices
    vertices = [(-1, -1), (3, -1), (2, 3)]
    
    # Create a new figure
    fig, ax = plt.subplots()
    
    # Add a triangle
    triangle = patches.Polygon(vertices, closed=True, edgecolor='r', facecolor='none')
    ax.add_patch(triangle)
    
    # Set the range of the axes
    ax.set_xlim(min(v[0] for v in vertices) - 1, max(v[0] for v in vertices) + 1)
    ax.set_ylim(min(v[1] for v in vertices) - 1, max(v[1] for v in vertices) + 1)
    
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
