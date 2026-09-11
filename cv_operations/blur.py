import cv2
import os

def apply_blur(image_path, output_dir):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: OpenCV could not read the image - {image_path}")
        return False
        
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(image, (15, 15), 0)
    
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(output_dir, f"{name}_blurred{ext}")
    
    cv2.imwrite(output_path, blurred)
    print(f"Blurred image saved to {output_path}")
    return True
