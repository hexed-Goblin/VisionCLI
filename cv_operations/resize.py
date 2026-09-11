import cv2
import os

def resize_image(image_path, output_dir, width, height):
    if width is None or height is None:
        print("Error: Both --width and --height must be specified for resize operation.")
        return False

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: OpenCV could not read the image - {image_path}")
        return False

    resized = cv2.resize(image, (width, height))
    
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(output_dir, f"{name}_resize_{width}x{height}{ext}")
    
    cv2.imwrite(output_path, resized)
    print(f"Image resized to {width}x{height} and saved to {output_path}")
    return True
