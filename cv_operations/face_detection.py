import cv2
import os

def detect_faces(image_path, output_dir):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: OpenCV could not read the image - {image_path}")
        return False

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Load Haar Cascade
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    if face_cascade.empty():
        print("Error: Could not load Haar cascade face detector.")
        return False

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(output_dir, f"{name}_faces{ext}")
    
    cv2.imwrite(output_path, image)
    print(f"Found {len(faces)} face(s). Result saved to {output_path}")
    return True
