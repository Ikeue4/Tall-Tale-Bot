from PIL import Image

def get_pixel_coordinates(image_path):
    # Open the image
    image = Image.open(image_path)

    # Display image information
    print(f"Image size: {image.size}")
    print(f"Image mode: {image.mode}")

    # Show the image
    image.show()

    # Get user input for pixel coordinates
    x = int(input("Enter the x-coordinate of the pixel: "))
    y = int(input("Enter the y-coordinate of the pixel: "))

    # Check if the coordinates are within the image bounds
    if x < 0 or x >= image.width or y < 0 or y >= image.height:
        print("Invalid coordinates!")
    else:
        # Get the pixel value at the specified coordinates
        pixel = image.getpixel((x, y))

        # Display the pixel information
        print(f"Pixel coordinates: ({x}, {y})")
        print(f"Pixel value: {pixel}")

    # Close the image
    image.close()

# Example usage
image_path = "C:\GitHub\stuff\map\map.jpeg"
get_pixel_coordinates(image_path)
