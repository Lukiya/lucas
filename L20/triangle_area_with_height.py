import matplotlib.pyplot as plt
import numpy as np

def draw_triangle_and_height():
    # Coordinates of the three vertices
    A = np.array([-1, -1])
    B = np.array([3, -1])
    C = np.array([2, 3])
    
    # Calculate the equation of line AB in the form ax + by + c = 0
    a = B[1] - A[1]
    b = A[0] - B[0]
    c = - (a * A[0] + b * A[1])
    
    # Calculate the perpendicular distance from C to line AB, and find the coordinates of the foot D
    D = np.array([
        (b * (b * C[0] - a * C[1]) - a * c) / (a ** 2 + b ** 2),
        (a * (-b * C[0] + a * C[1]) - b * c) / (a ** 2 + b ** 2)
    ])
    
    # Create a new plot
    fig, ax = plt.subplots()
    
    # Add the triangle
    triangle = plt.Polygon([A, B, C], closed=True, edgecolor='r', facecolor='none')
    ax.add_patch(triangle)
    
    # Add the perpendicular line
    height_line = plt.Line2D([C[0], D[0]], [C[1], D[1]], color='b', linestyle='--')
    ax.add_line(height_line)
    
    # Mark the point D
    ax.plot(D[0], D[1], 'bo')
    
    # Set the limits of the axes
    ax.set_xlim(min(A[0], B[0], C[0]) - 1, max(A[0], B[0], C[0]) + 1)
    ax.set_ylim(min(A[1], B[1], C[1]) - 1, max(A[1], B[1], C[1]) + 1)
    
    # Set the labels of the axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    # Show the grid
    ax.grid(True, which='both')
    
    # Show the axes
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    draw_triangle_and_height()
