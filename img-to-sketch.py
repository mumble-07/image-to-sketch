# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:03:49 2024

@author: mumble

CONVERT AN IMAGE TO SKETCH
"""

import cv2
import os
from datetime import datetime

def convert_to_sketch(input_image_path, output_folder='generated_sketch'):
    # read/get the image
    image = cv2.imread(input_image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)
    
    # Blur the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (111, 111), 0)
    
    # Invert the blurred image
    inverted_blurred_image = cv2.bitwise_not(blurred_image)
    
    # Create the sketch by blending the original and inverted blurred images
    sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    
    # Display the original and sketch images
    cv2.imshow('Original Image', image)
    cv2.imshow('Sketch', sketch)
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Generate a timestamped name for the output image with hyphens
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    output_image_name = f'{timestamp}_sketch.png'
    
    # Save the sketch in the "generated_sketch" folder with a timestamped name
    output_image_path = os.path.join(output_folder, output_image_name)
    cv2.imwrite(output_image_path, sketch)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Replace 'path/to/your/input_image.jpg' with the actual path for your input image
input_image_path = 'steven.jpg'
convert_to_sketch(input_image_path)

