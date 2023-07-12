import matplotlib.pyplot as plt
import numpy as np
import math
import time
import threading

start_time = time.time()

# Set the coordinates for the point and line
point_x = 776
point_y = 717
pointsx = [830, 761, 755, 888, 718, 551, 352, 355, 461, 153, 669, 659, 666, 799, 267, 475, 619, 475, 117, 735, 202, 890, 597, 238, 932, 391, 421, 438, 845, 156, 708, 673, 321, 606, 462, 845, 533, 357, 244, 436, 169, 272, 392, 314, 254, 338, 471, 776, 628, 878, 410, 338]
pointsy = [260, 332, 894, 829, 783, 102, 829, 604, 324, 628, 317, 219, 699, 155, 272, 398, 394, 695, 536, 636, 759, 473, 785, 474, 552, 690, 777, 245, 903, 436, 155, 857, 195, 258, 858, 775, 211, 313, 571, 619, 853, 390, 892, 737, 835, 248, 481, 717, 131, 599, 536, 471]
line_length = 70.65
line_angle = 173.99 + 180
targetx = 200
targety = 200

# Set the plot limits
xlim = (0, 959)
ylim = (0, 1088)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the point
ax.plot(point_x, point_y, 'ro', label='islands')
ax.plot(targetx, targety, 'yo', label='target')

# Plot the circles around each red dot
for i in range(len(pointsx)):
    ax.plot(pointsx[i], pointsy[i], 'ro')
    
    circle = plt.Circle((pointsx[i], pointsy[i]), radius=25, color='none', ec='red')
    ax.add_artist(circle)

# Calculate the line coordinates
line_x = point_x + line_length * np.cos(np.radians(line_angle))
line_y = point_y + line_length * np.sin(np.radians(line_angle))

# Plot the line
ax.plot([point_x, line_x], [point_y, line_y], 'b-', label='Line')
ax.plot([line_x, targetx], [line_y, targety], 'y-', label='Line')
ax.plot(line_x, line_y, 'bo', label='boat')

# Calculate the total distance between the starting and ending points
total_distance = ((targetx - line_x) ** 2 + (targety - line_y) ** 2) ** 0.5

# Plot the line
ax.plot([line_x, targetx], [line_y, targety], 'y-', label='Line')

# Add dots every two units
distance_between_dots = 6  # Set the distance between dots here

# Calculate the number of dots to add
num_dots = int(total_distance / distance_between_dots)

# Create empty lists to store the dots and their indices
dots = []
dot_indices = []
last_dotx = []
last_doty = []

# Variable to store the index of the first intersecting point
intersection_index = None

# Variable to store the index of the previous dot
previous_index = None

# Iterate to add dots
for i in range(num_dots + 1):
    # Calculate the position of the dot
    dot_x = line_x + (targetx - line_x) * (i / num_dots)
    dot_y = line_y + (targety - line_y) * (i / num_dots)

    # Calculate the distance between the dot and each point
    distances = [math.sqrt((dot_x - px) ** 2 + (dot_y - py) ** 2) for px, py in zip(pointsx, pointsy)]

    # Check if any of the distances are less than 20 units
    if any(distance < 25 for distance in distances):
        # If a point is closer than 20 units, add it to the lists
        closest_index = distances.index(min(distances))
        dots.append((dot_x, dot_y))
        dot_indices.append(closest_index)

        # Check if it's the first intersecting point
        if intersection_index is None:
            intersection_index = closest_index
        else:
            # If it's not the first intersecting point, remove the dot and break the loop
            dots.pop()
            dot_indices.pop()
            break

        # Update the previous index
        previous_index = closest_index

    # Plot the dot
    last_dotx.append(dot_x)
    last_doty.append(dot_y)
    ax.plot(dot_x, dot_y, 'ro')  # 'ro' represents red dots, you can modify it as needed

# Plot circles around the closest points
for index in dot_indices:
    ax.add_artist(plt.Circle((pointsx[index], pointsy[index]), radius=25, color='none', ec='green'))

if intersection_index is not None:
    intersection_point = (dots[-1][0], dots[-1][1])
    ax.plot([point_x, intersection_point[0]], [point_y, intersection_point[1]], 'y-', label='travel line')

    # Check if there is a previous dot
    if len(dots) >= 2:
        previous_point = (dots[-2][0], dots[-2][1])
        ax.plot([point_x, previous_point[0]], [point_y, previous_point[1]], 'g-', label='previous line')
        
def set_lines(last_dotx, last_doty, angle, targetx, targety, check, check_number):
    start_point = [last_dotx[len(last_dotx) - 2], last_doty[len(last_doty) - 2]]
    angle_degrees = angle


    angle_radians = np.deg2rad(angle_degrees)
    line_length = 500

    end_point = (
        start_point[0] + line_length * np.cos(angle_radians),
        start_point[1] + line_length * np.sin(angle_radians)
    )

    plt.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], 'r-')
    plt.plot(start_point[0], start_point[1], 'bo')
    
    # Calculate the total distance between the starting and ending points
    total_distance = line_length#((end_point[0] - start_point[0]) ** 2 + ((end_point[1] - start_point[1]) ** 2) ** 0.5)

    # Plot the line
    ax.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], 'r-')

    # Add dots every two units
    distance_between_dots = 20  # Set the distance between dots here

    # Calculate the number of dots to add
    num_dots = int(total_distance / distance_between_dots)

    # Create empty lists to store the dots and their indices
    dots = []
    dot_indices = []
    last_dotx = []
    last_doty = []
    global back_line_length_out
    global foundx
    global foundy

    # Variable to store the index of the first intersecting point
    intersection_index = None

    # Variable to store the index of the previous dot
    previous_index = None
    

    # Iterate to add dots
    for i in range(num_dots + 1):
        # Calculate the position of the dot
        dot_x = start_point[0] + (end_point[0] - start_point[0]) * (i / num_dots)
        dot_y = start_point[1] + (end_point[1] - start_point[1]) * (i / num_dots)

        # Calculate the distance between the dot and each point
        distances = [math.sqrt((dot_x - px) ** 2 + (dot_y - py) ** 2) for px, py in zip(pointsx, pointsy)]

        # Check if any of the distances are less than 20 units
        if any(distance < 25 for distance in distances):
            # If a point is closer than 20 units, add it to the lists
            closest_index = distances.index(min(distances))
            dots.append((dot_x, dot_y))
            dot_indices.append(closest_index)

            # Check if it's the first intersecting point
            if intersection_index is None:
                intersection_index = closest_index
            else:
                # If it's not the first intersecting point, remove the dot and break the loop
                dots.pop()
                dot_indices.pop()
                break

            # Update the previous index
            previous_index = closest_index
            
        last_dotx.append(dot_x)
        last_doty.append(dot_y)
        # Plot the dot
        ax.plot(dot_x, dot_y, 'ro')  # 'ro' represents red dots, you can modify it as needed
        
    if len(last_dotx) > 2:
        try:
            back_line_length = math.sqrt((targetx - last_dotx[len(last_dotx) - 2]) ** 2 + ((targety - last_doty[len(last_doty) - 2]) ** 2))
            back_line_length_out.append(back_line_length)
        except:
            print("error")
            
        if check == True:
            time.sleep(2)
            low = 999999999999999999999999999
            for i in back_line_length_out:
                if i < low:
                    low = i
            print(low)
            if low == back_line_length:
                foundx = last_dotx[len(last_dotx) - 2]
                foundy = last_doty[len(last_doty) - 2]
                ax.plot([last_dotx[len(last_dotx) - 2], targetx], [last_doty[len(last_doty) - 2], targety], 'b-')
            
            '''foundx = last_dotx[len(last_dotx) - 2]
            foundy = last_doty[len(last_doty) - 2]
            ax.plot([last_dotx[len(last_dotx) - 2], targetx], [last_doty[len(last_doty) - 2], targety], 'b-')'''
        

angels = [0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108,112,116,120,124,128,132,136,140,144,148,152,156,160,164,168,172,176,180,184,188,192,196,200,204,208,212,216,220,224,228,232,236,240,244,248,252,256,260,264,268,272,276,280,284,288,292,296,300,304,308,312,316,320,324,328,332,336,340,344,348,352,356,360]
back_line_length_out = []
check = True
check_number = 0
foundx = 0
foundy = 0

for i in angels:
    thread = threading.Thread(target=set_lines, args=(last_dotx, last_doty, i, targetx, targety, check, check_number))
    thread.start()

time.sleep(3)

print(foundx)
print(foundy)
print(back_line_length_out)

# Set the plot limits
ax.set_xlim(xlim)
ax.set_ylim(ylim)

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Plot with Point and Line')
print([len(last_dotx) - 2])
print([len(last_doty) - 2])

# Print or use the last dot as needed
print("Last Dotx:", last_dotx[len(last_dotx) - 2])
print("Last Doty:", last_doty[len(last_doty) - 2])

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")

# Show the plot
plt.show()


'''st = 0
while st < 360:
    print(',' + str(st))
    st += 4
'''