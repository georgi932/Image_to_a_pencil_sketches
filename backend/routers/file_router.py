from services.image_service import transform_to_pencil_sketch, allowed_file
from services.file_service import save_uploaded_file, save_sketch, delete_file
from flask import request, jsonify
from main import app

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and allowed_file(file.filename):
        # Save the uploaded file
        file_path = save_uploaded_file(file)

        # Transform the image to a pencil sketch
        sketch = transform_to_pencil_sketch(file_path)

        # Save the sketch
        sketch_path = save_sketch(sketch)

        return jsonify({'sketch_url': sketch_path})

    return jsonify({'error': 'Invalid file format!'})


@app.route('/delete/<filename>', methods=['DELETE'])
def delete_uploaded_file(filename):
    return jsonify({'message': delete_file(filename)})
