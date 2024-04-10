import os
import cv2
import numpy as np
from flask import jsonify

# Upload folders
UPLOAD_FOLDER = 'uploads'
SKETCH_FOLDER = 'sketches'


# This is new method for creates directories in "static" directory
def create_folders():
    static_folder = 'static'
    UPLOAD_FOLDER = os.path.join(static_folder, 'uploads')
    SKETCH_FOLDER = os.path.join(static_folder, 'sketches')

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(SKETCH_FOLDER, exist_ok=True)


def save_uploaded_file(file):
    static_folder = 'static'
    UPLOAD_FOLDER = os.path.join(static_folder, 'uploads')

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return file_path


def save_sketch(sketch):
    static_folder = 'static'
    SKETCH_FOLDER = os.path.join(static_folder, 'sketches')

    sketch_path = os.path.join(SKETCH_FOLDER, 'sketch.png')

    # Check if the image_data is bytes or numpy array
    if isinstance(sketch, bytes):

        # If image_data is bytes, decode it to numpy array
        image_array = np.frombuffer(sketch, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    elif isinstance(sketch, np.ndarray):

        # If image_data is numpy array, directly assign it
        image = sketch
    else:
        raise ValueError("Unsupported image data format")

    # Save the image
    cv2.imwrite(sketch_path, image)
    sketch_path = sketch_path.replace('\\', '/')
    return sketch_path

    # sketch_path = sketch_path.replace('\\', '/')
    #
    # # Decode the image bytes to a NumPy array
    # sketch_array = np.frombuffer(sketch, dtype=np.uint8)
    #
    # # Reshape the array to match the image dimensions
    # sketch_image = cv2.imdecode(sketch_array, cv2.IMREAD_COLOR)
    #
    # cv2.imwrite(sketch_path, sketch_image)
    # return sketch_path


# --- To be implemented ---
def delete_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        os.remove(file_path)
        return f'File {filename} deleted successfully'
    except FileNotFoundError:
        return f'File {filename} not found'


def get_file_path():

    upload_dir = upload_dir = 'static/uploads'
    uploaded_files = os.listdir(upload_dir)

    # Assuming there's only one file uploaded, you can take the first file from the list
    if uploaded_files:
        file_name = uploaded_files[0]
        file_path = os.path.join(upload_dir, file_name)
    else:
        return jsonify({"error": "No files uploaded"}), None

    # Replace double backslashes with single forward slashes
    file_path = file_path.replace('\\', '/')

    return file_path