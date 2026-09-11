import argparse
import os
import sys

from cv_operations.image_info import display_info
from cv_operations.grayscale import convert_to_grayscale
from cv_operations.edges import detect_edges
from cv_operations.face_detection import detect_faces
from cv_operations.resize import resize_image
from cv_operations.blur import apply_blur

def setup_output_dir(output_dir="output"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def main():
    parser = argparse.ArgumentParser(description="VisionCLI - A Command-line Computer Vision toolkit using OpenCV")
    parser.add_argument("--image", required=True, help="Path to the input image")
    parser.add_argument("--operation", required=True, 
                        choices=["info", "grayscale", "edges", "faces", "resize", "blur"],
                        help="The computer vision operation to perform")
    parser.add_argument("--width", type=int, help="Width for resize operation")
    parser.add_argument("--height", type=int, help="Height for resize operation")
    parser.add_argument("--outdir", default="output", help="Directory to save output files (default: 'output')")
    
    args = parser.parse_args()

    if not os.path.exists(args.image):
        print(f"Error: The image file '{args.image}' does not exist.")
        sys.exit(1)

    output_dir = setup_output_dir(args.outdir)

    print(f"Processing '{args.image}' with operation: {args.operation}...")

    success = False

    if args.operation == "info":
        success = display_info(args.image)
    elif args.operation == "grayscale":
        success = convert_to_grayscale(args.image, output_dir)
    elif args.operation == "edges":
        success = detect_edges(args.image, output_dir)
    elif args.operation == "faces":
        success = detect_faces(args.image, output_dir)
    elif args.operation == "resize":
        success = resize_image(args.image, output_dir, args.width, args.height)
    elif args.operation == "blur":
        success = apply_blur(args.image, output_dir)
        
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
