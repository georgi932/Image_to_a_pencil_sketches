from backend.services.image_service import transform_to_pencil_sketch, allowed_file
from backend.services.file_service import save_uploaded_file, save_sketch, delete_file, create_folders
from flask import Blueprint, request, jsonify, render_template

file_router = Blueprint('file', __name__)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'''}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@file_router.route('/', methods=['GET'])
def home():
    # return {"Welcome": "Welcome to my Flask web app!"}
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

        # Transform the image to a pencil sketch
        sketch = transform_to_pencil_sketch(file_path)

        # Save the sketch
        sketch_path = save_sketch(sketch)

        # return jsonify({'sketch_url': sketch_path})
        return render_template('result.html', original_file=file_path, sketch_file=sketch_path)

    return jsonify({'error': 'Invalid file format!'})


@file_router.route('/delete/<filename>', methods=['DELETE'])
def delete_uploaded_file(filename):
    return jsonify({'message': delete_file(filename)})