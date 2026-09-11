# VisionCLI

A Python-based command-line Computer Vision toolkit using OpenCV.

## Features
- **Image Information:** Get dimensions, channels, and file size.
- **Grayscale Conversion:** Convert color images to grayscale.
- **Edge Detection:** Detect edges using the Canny algorithm.
- **Face Detection:** Detect faces using OpenCV Haar Cascades.
- **Image Resizing:** Resize images to specified dimensions.
- **Image Blurring:** Apply Gaussian blur to images.

## Technologies Used
- Python 3
- OpenCV (opencv-python)
- NumPy
- argparse

## Project Structure
```
VisionCLI/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── cv_operations/
│   ├── __init__.py
│   ├── grayscale.py
│   ├── edges.py
│   ├── face_detection.py
│   ├── resize.py
│   ├── blur.py
│   └── image_info.py
├── samples/
│   └── sample.jpg
└── output/
```

## Prerequisites
- Python 3.7+
- pip (Python package installer)

## Installation Steps
1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository_url>
   cd VisionCLI
   ```
2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions

The main interface is through `main.py`. The toolkit provides various computer vision operations out-of-the-box. Ensure that the input image path actually points to a valid image file.

### Help Command
To list all available commands and options, you can use the help function:
```bash
python main.py --help
```

### Commands

**1. Image Information**
```bash
python main.py --image samples/sample.jpg --operation info
```
*Outputs: Filename, width, height, dimensions, channels, file size.*

**2. Grayscale Conversion**
```bash
python main.py --image samples/sample.jpg --operation grayscale
```
*Outputs: A grayscale version of the image saved in the `output/` directory.*

**3. Edge Detection**
```bash
python main.py --image samples/sample.jpg --operation edges
```
*Outputs: A black-and-white image containing the detected edges saved in the `output/` directory.*

**4. Face Detection**
```bash
python main.py --image samples/sample.jpg --operation faces
```
*Outputs: An image with bounding boxes drawn around detected faces, saved in the `output/` directory. The terminal will log the number of detected faces.*

**5. Image Resizing**
```bash
python main.py --image samples/sample.jpg --operation resize --width 800 --height 600
```
*Outputs: A resized copy of the input image according to the specified width and height, saved in the `output/` directory.*

**6. Image Blurring**
```bash
python main.py --image samples/sample.jpg --operation blur
```
*Outputs: A blurred copy of the input image, saved in the `output/` directory.*

## Troubleshooting
- **ModuleNotFoundError: No module named 'cv2'**: Ensure that you have correctly activated the virtual environment and installed the dependencies with `pip install -r requirements.txt`.
- **Error: OpenCV could not read the image**: Check that the `--image` path points to a file, and verify that the file format is supported by OpenCV (e.g., .jpg, .png).
