import os
from backend.services.image_service import transform_to_pencil_sketch, allowed_file
from backend.services.file_service import save_uploaded_file, save_sketch, delete_file, create_folders, get_file_path
from flask import Blueprint, request, jsonify, render_template, redirect, send_from_directory

file_router = Blueprint('file', __name__)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


@file_router.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@file_router.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    folder = create_folders()

    # Save the uploaded file
    if file and allowed_file(file.filename):
        file_path = save_uploaded_file(file)

        return redirect(request.referrer)

    return redirect(request.referrer)


@file_router.route('/delete/<filename>', methods=['DELETE'])
def delete_uploaded_file(filename):
    return jsonify({'message': delete_file(filename)})


@file_router.route('/sketch', methods=['GET', 'POST'])
def sketch_file():
    file_path = get_file_path()

    # Transform the image to a pencil sketch
    sketch = transform_to_pencil_sketch(file_path)

    # Save the sketch
    sketch_path = save_sketch(sketch)

    return render_template('result.html', original_file=file_path, sketch_file=sketch_path)

