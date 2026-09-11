import cv2
import os

def display_info(image_path):
    print(f"Image Information for: {image_path}")
    if not os.path.exists(image_path):
        print(f"Error: File not found - {image_path}")
        return False
    
    file_size = os.path.getsize(image_path)
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: OpenCV could not read the image - {image_path}")
        return False
    
    height, width = image.shape[:2]
    channels = image.shape[2] if len(image.shape) == 3 else 1
    
    print(f"Filename: {os.path.basename(image_path)}")
    print(f"Width: {width} pixels")
    print(f"Height: {height} pixels")
    print(f"Channels: {channels}")
    print(f"Dimensions: {width}x{height}")
    print(f"File size: {file_size / 1024:.2f} KB")
    
    return True
