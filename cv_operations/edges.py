import cv2
import os

def detect_edges(image_path, output_dir):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Error: OpenCV could not read the image - {image_path}")
        return False

    edges = cv2.Canny(image, 100, 200)
    
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(output_dir, f"{name}_edges{ext}")
    
    cv2.imwrite(output_path, edges)
    print(f"Edge detection completed. Saved to {output_path}")
    return True
