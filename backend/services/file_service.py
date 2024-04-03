import os
import cv2
import numpy as np
from flask import jsonify

# Upload folders
UPLOAD_FOLDER = 'uploads'
SKETCH_FOLDER = 'sketches'


def create_folders():
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(SKETCH_FOLDER, exist_ok=True)


def save_uploaded_file(file):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return file_path


def save_sketch(sketch):
    sketch_path = os.path.join(SKETCH_FOLDER, 'sketch.png')
    cv2.imwrite(sketch_path, sketch)
    return sketch_path


def delete_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        os.remove(file_path)
        return f'File {filename} deleted successfully'
    except FileNotFoundError:
        return f'File {filename} not found'


def get_file_path():

    upload_dir = upload_dir = 'uploads'
    uploaded_files = os.listdir(upload_dir)

    # Assuming there's only one file uploaded, you can take the first file from the list
    if uploaded_files:
        file_name = uploaded_files[0]
        file_path = os.path.join(upload_dir, file_name)
    else:
        return jsonify({"error": "No files uploaded"}), None

    return file_path