import os

UPLOAD_FOLDER = 'upload'


def create_upload_folder():
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_uploaded_file(file):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return file_path


def save_sketch(sketch):
    sketch_path = os.path.join(UPLOAD_FOLDER, 'sketch.png')
    cv2.imwrite(sketch_path, sketch)
    return sketch_path


def delete_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        os.remove(file_path)
        return f'File {filename} deleted successfully'
    except FileNotFoundError:
        return f'File {filename} not found'