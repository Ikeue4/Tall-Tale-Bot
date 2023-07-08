import matplotlib.pyplot as plt
import numpy as np

# Set the coordinates for the point and line
point_x = 666
point_y = 389
pointsx = [830,761,755,888,718,551,352,355,461,153,669,659,666,799,267,475,619,475,117,735,202,890,597,238,932,391,421,438,845,156,708,673,321,606,462,845,533,357,244,436,169,272,392,314,254,338,471,776,628,878,410,338]
pointsy = [828, 756, 194, 259, 305, 986, 259, 484, 764, 460, 771, 869, 389, 933, 816, 690, 694, 393, 552, 452, 329, 615, 303, 614, 536, 398, 311, 843, 185, 652, 933, 231, 893, 830, 230, 313, 877, 775, 517, 469, 235, 698, 196, 351, 253, 840, 607, 371, 957, 489, 552, 617]
line_length = 70.65
line_angle = 173.99 + 180

# Set the plot limits
xlim = (0, 959)
ylim = (0, 1088)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the point
ax.plot(point_x, point_y, 'ro', label='Point')
pos = 0
for i in pointsx:
    ax.plot(pointsx[pos], pointsy[pos], 'ro', label='Point')
    print(pointsx[pos], pointsy[pos])
    pos += 1

# Calculate the line coordinates
line_x = point_x + line_length * np.cos(np.radians(line_angle))
line_y = point_y + line_length * np.sin(np.radians(line_angle))

# Plot the line
ax.plot([point_x, line_x], [point_y, line_y], 'b-', label='Line')

# Set the plot limits
ax.set_xlim(xlim)
ax.set_ylim(ylim)

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Plot with Point and Line')
ax.legend()

# Show the plot
plt.show()
