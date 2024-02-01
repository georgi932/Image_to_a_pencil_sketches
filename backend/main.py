from flask import Flask, request, jsonify, render_template
from services.image_service import transform_to_pencil_sketch, allowed_file
from services.file_service import create_upload_folder, save_uploaded_file, save_sketch, delete_file
import uvicorn

app = Flask(__name__)


@app.route('/')
def home():
    return {"Welcome": "Welcome to my Flask web app!"}


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

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
