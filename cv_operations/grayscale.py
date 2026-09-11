import cv2
import os

def convert_to_grayscale(image_path, output_dir):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: OpenCV could not read the image - {image_path}")
        return False

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(output_dir, f"{name}_grayscale{ext}")
    
    cv2.imwrite(output_path, gray_image)
    print(f"Grayscale image saved to {output_path}")
    return True
