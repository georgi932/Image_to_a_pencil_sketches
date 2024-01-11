# from flask import Flask, request, jsonify
# import cv2
# import numpy as np
# import os
# from backend.image_processing import transform_to_pencil_sketch
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def home():
#     return render_template('index.html') #"Welcome to my Flask web app!"
#
#
# UPLOAD_FOLDER = 'upload'
# ALLOWED_EXTENSION = {'png', 'jpg', 'jpeg'}
#
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#
#
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION
#
#
# # Function to create directory if not exist
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'})
#
#     file = request.files['file']
#
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'})
#
#     if file and allowed_file(file.filename):
#         # Save the uploaded file
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(file_path)
#
#         # Transform the image to a pencil sketch
#         sketch = transform_to_pencil_sketch(file_path)
#
#         # Save the sketch
#         sketch_path = os.path.join(app.config['UPLOAD_FOLDER'], 'sketch.png')
#         cv2.imwrite(sketch_path, sketch)
#
#         return jsonify({'sketch_url': sketch_path})
#
#     return jsonify({'error': 'Invalid file format!'})
#
#
# # Function to delete file
# @app.route('/delete/<filename>', methods=['DELETE'])
# def delete_file(filename):
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     try:
#         os.remove(file_path)
#         return jsonify({'message': f'File {filename} deleted successfully'})
#     except FileNotFoundError:
#         return jsonify({'error': f'File {filename} not found'})
#
#
# if __name__ == '__main__':
#     os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
#     app.run(debug=True)


from flask import Flask, request, jsonify, render_template
from services.image_service import transform_to_pencil_sketch, allowed_file
from services.file_service import create_upload_folder, save_uploaded_file, save_sketch, delete_file

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html') #"Welcome to my Flask web app!"


create_upload_folder()


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


if __name__ == '__main__':
    app.run(debug=True)