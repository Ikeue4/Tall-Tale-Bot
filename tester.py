import cv2
import numpy as np
import glob
import threading
import os
import time
import psutil

rotation_angles_deg = 0
ship_center_x = 0
ship_center_y = 0
islandpositionx = []
islandpositiony = []
islandname = []

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def num1():
    global islandpositionx, islandpositiony, islandname
    todo = 0
    done = 0
    # Load the target image
    target = cv2.imread('Sea of Thieves 8_07_2023 11_12_13 AM.png', 0)

    # Define the folder path containing the template images
    templates_folder = 'islands/'

    # Create a SIFT object
    sift = cv2.SIFT_create()

    # Retrieve a list of image files within the folder
    template_files = glob.glob(templates_folder + '*.png')

    # Set the confidence threshold (percentage)
    confidence_threshold = 15
    
    for template_file in template_files:
        todo += 1

    # Iterate over each template file
    for template_file in template_files:
        # Load the template image
        template = cv2.imread(template_file, 0)

        # Detect and compute keypoints and descriptors for the template and target images
        keypoints_template, descriptors_template = sift.detectAndCompute(template, None)
        keypoints_target, descriptors_target = sift.detectAndCompute(target, None)

        # Create a brute-force matcher
        bf = cv2.BFMatcher()

        # Match descriptors between the template and target images
        matches = bf.match(descriptors_template, descriptors_target)

        # Sort the matches by distance (lower distance means better match)
        matches = sorted(matches, key=lambda x: x.distance)

        # Select reliable matches using RANSAC
        src_pts = np.float32([keypoints_template[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints_target[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
        homography, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

        # Calculate the number of inliers
        num_inliers = np.sum(mask)

        # Calculate the percentage of inliers
        confidence = (num_inliers / len(matches)) * 100
        #print('checking confidence')
        #print(confidence, template_file)
        done += 1
        
        

        if confidence >= confidence_threshold:
            print('success')
            # Draw bounding box around the template in the target image
            h, w = template.shape
            corners = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
            corners_transformed = cv2.perspectiveTransform(corners, homography)
            target_with_box = cv2.polylines(target, [np.int32(corners_transformed)], True, (0, 255, 0), 3)
            
            island_center_x = int(np.mean(corners_transformed[:, :, 0]))
            island_center_y = int(np.mean(corners_transformed[:, :, 1]))
            
            islandpositionx.append(island_center_x)
            islandpositiony.append(island_center_y)
            
            islandname.append(template_file)
            # Display the target image with the bounding box
            
    cv2.imshow("Target Image with Bounding Box", target_with_box)
    cv2.waitKey(0)
    print('done')
    
    cv2.destroyAllWindows()
    
def num2():
    global rotation_angles_deg
    global ship_center_x
    global ship_center_y
    # Load the cutout image (template) and the target image
    template = cv2.imread('ship.png', 0)
    target = cv2.imread('Sea of Thieves 8_07_2023 11_12_13 AM.png', 0)
    
    # Create a SIFT object
    sift = cv2.SIFT_create()
    
    # Detect and compute keypoints and descriptors for the template and target images
    keypoints_template, descriptors_template = sift.detectAndCompute(template, None)
    keypoints_target, descriptors_target = sift.detectAndCompute(target, None)
    
    # Create a brute-force matcher
    bf = cv2.BFMatcher()
    
    # Match descriptors between the template and target images
    matches = bf.match(descriptors_template, descriptors_target)
    
    # Sort the matches by distance (lower distance means better match)
    matches = sorted(matches, key=lambda x: x.distance)
    
    # Select reliable matches using RANSAC
    src_pts = np.float32([keypoints_template[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([keypoints_target[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
    homography, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    
    # Calculate rotation angles from the homography matrix
    rotation_angles_rad = np.arctan2(homography[1, 0], homography[0, 0])
    rotation_angles_deg = np.degrees(rotation_angles_rad)
    
    # Adjust the rotation angles to be within the range of 0 to 360 degrees
    rotation_angles_deg = (rotation_angles_deg + 360) % 360
    # Print the estimated rotation angles
    #print("Estimated Rotation Angles (in degrees):", rotation_angles_deg)
    
    # Draw bounding box around the template in the target image
    h, w = template.shape
    corners = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
    corners_transformed = cv2.perspectiveTransform(corners, homography)
    target_with_box = cv2.polylines(target, [np.int32(corners_transformed)], True, (0, 255, 0), 3)
    
    ship_center_x = int(np.mean(corners_transformed[:, :, 0]))
    ship_center_y = int(np.mean(corners_transformed[:, :, 1]))
    
    #print(f"ship_center_x ", ship_center_x, "ship_center_y ", ship_center_y)
    
    cv2.imshow("Target Image with Bounding Box", target_with_box)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def num3():
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_system_load():
        cpu_load = psutil.cpu_percent()
        gpu_load = 0  # Add code here to get GPU load if available
        ram_load = psutil.virtual_memory().percent
        return cpu_load, gpu_load, ram_load

    def display_system_load(cpu_load, gpu_load, ram_load):
        print(f"CPU Load: {cpu_load}%")
        print(f"GPU Load: {gpu_load}%")
        print(f"RAM Load: {ram_load}%")

    def main():
        while True:
            clear_terminal()
            cpu_load, gpu_load, ram_load = get_system_load()
            display_system_load(cpu_load, gpu_load, ram_load)
            time.sleep(0.5)

    if __name__ == '__main__':
        main()
    
    
island_thread = threading.Thread(target=num1)
boat_thread = threading.Thread(target=num2)
#mon_thread = threading.Thread(target=num3)

island_thread.start()
boat_thread.start()
#mon_thread.start()

island_thread.join()
boat_thread.join()


print(f"ship_center_x ", ship_center_x, "ship_center_y ", ship_center_y)
print("Estimated Rotation Angles (in degrees):", rotation_angles_deg)

for i in islandpositionx:
    print(f"island_center_x ", i)
for i in islandpositiony:
    print("island_center_y ", i)


num = 0 
try:
    for i in islandpositionx:
        print(islandname[num])
        print(islandpositionx[num], islandpositiony[num])
        num += 1
    
except:
    print('done')


    


