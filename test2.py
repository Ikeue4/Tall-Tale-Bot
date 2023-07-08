import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

# Coordinates of the points
x = [2143, 1193]
y = [662, 762]

# Plotting the points
plt.scatter(x, y)

# Adding labels to the points
for i in range(len(x)):
    plt.text(x[i], y[i], f'({x[i]}, {y[i]})', ha='right')

# Connecting the points with a line
plt.plot(x, y)

# Draw a circle around the first point
circle_radius = 100
circle = patches.Circle((x[1], y[1]), circle_radius, edgecolor='red', facecolor='none')
plt.gca().add_patch(circle)

# Calculate the angle of the line
dx = x[1] - x[0]
dy = y[1] - y[0]
angle_rad = math.atan2(dy, dx)
angle_deg = math.degrees(angle_rad)
angle_deg = (angle_deg + 360) % 360

# Display the angle
plt.text(x[1] + 20, y[1] + 20, f'Angle: {angle_deg:.2f} degrees')

# Setting up the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plotting Two Points')

plt.xlim(0, 3440)  # Set the x-axis limits
plt.ylim(0, 1440)  # Set the y-axis limits

# Displaying the plot
plt.show()
