import os
from backend.services.image_service import transform_to_pencil_sketch, allowed_file
from backend.services.file_service import save_uploaded_file, save_sketch, delete_file, create_folders
from flask import Blueprint, request, jsonify, render_template, redirect, url_for

file_router = Blueprint('file', __name__)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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

    if file and allowed_file(file.filename):
        # Save the uploaded file
        file_path = save_uploaded_file(file)

        # # Transform the image to a pencil sketch
        # sketch = transform_to_pencil_sketch(file_path)
        #
        # # Save the sketch
        # sketch_path = save_sketch(sketch)

        return redirect(request.referrer)

    return redirect(request.referrer)

        # return jsonify({'redirect_url': '/transform' + file_path})

        # return render_template('result.html', original_file=file_path, sketch_file=sketch_path)

    # return jsonify({'error': 'Invalid file format!'})


@file_router.route('/delete/<filename>', methods=['DELETE'])
def delete_uploaded_file(filename):
    return jsonify({'message': delete_file(filename)})


@file_router.route('/sketch', methods=['POST'])
def sketch_file():

    upload_dir = 'uploads'
    uploaded_files = os.listdir(upload_dir)

    # Assuming there's only one file uploaded, you can take the first file from the list
    if uploaded_files:
        file_name = uploaded_files[0]
        file_path = os.path.join(upload_dir, file_name)
    else:
        return jsonify({"error": "No files uploaded"})

    # Transform the image to a pencil sketch
    sketch = transform_to_pencil_sketch(file_path)

    # Save the sketch
    sketch_path = save_sketch(sketch)

    return redirect(url_for('result.html', original_file=file_path, sketch_file=sketch_path))
    # return render_template('result.html', original_file=file_path, sketch_file=sketch_path)

    # return redirect(url_for('file.result_page'))


# @file_router.route('/result', methods=['GET'])
# def result_page():
#     return render_template('result.html')
