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

    sketch_path = sketch_path.replace('\\', '/')

    cv2.imwrite(sketch_path, sketch)
    return sketch_path


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