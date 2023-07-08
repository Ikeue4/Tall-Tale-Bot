import matplotlib.pyplot as plt
import glob

templates_folder = 'islands/'
template_files = glob.glob(templates_folder + '*.png')
temp = []

for template_file in template_files:
    print (template_file)
    temp.append(template_file)

print(temp[52])
upto1 = len(temp) - 1
upto = 0

def on_click(event):
    global upto
    global temp
    if event.button == 1:  # Left mouse button
        x = int(event.xdata)
        y = int(event.ydata)
        template_file = temp[upto]
        print(f"{template_file} = {x}, {y}")
        upto += 1
        print(f"up next {temp[upto]}")
        
        

def choose_pixel(image_path):
    # Load the image
    image = plt.imread(image_path)

    # Create a figure and display the image
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.set_title("Click on a pixel")

    # Connect the mouse click event to the on_click function
    fig.canvas.mpl_connect('button_press_event', on_click)

    # Show the plot
    plt.show()

# Example usage
image_path = "map\map.jpg"
choose_pixel(image_path)
