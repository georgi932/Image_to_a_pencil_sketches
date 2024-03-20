import os
import cv2
import numpy as np

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


# ---To be connected  to the router and to the buttons---
def apply_filter(image, filter_type):
    if filter_type == "blur":
        return cv2.blur(image, (5, 5))  # Applying a blur filter
    elif filter_type == "sharpen":
        kernel = np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]])
        return cv2.filter2D(image, -1, kernel)  # Applying a sharpen filter
    elif filter_type == "edge":
        return cv2.Canny(image, 100, 200)  # Applying an edge detection filter
    elif filter_type == "emboss":
        kernel = np.array([[-2, -1, 0],
                           [-1, 1, 1],
                           [0, 1, 2]])
        return cv2.filter2D(image, -1, kernel)  # Applying an emboss filter
    elif filter_type == "sepia":
        kernel = np.array([[0.393, 0.769, 0.189],
                           [0.349, 0.686, 0.168],
                           [0.272, 0.534, 0.131]])
        sepia_image = cv2.transform(image, kernel)
        sepia_image = cv2.cvtColor(sepia_image, cv2.COLOR_BGR2RGB)
        return sepia_image  # Applying a sepia tone filter
    elif filter_type == "grayscale":
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Converting to grayscale
    else:
        return image  # Return original image if filter type not recognized

    # Load the image
    image_path = "input_image.jpg"
    input_image = cv2.imread(image_path)

    # Apply the desired filter
    filtered_image = apply_filter(input_image, "emboss")  # Change the filter type as desired

    # Display the original and filtered images
    cv2.imshow("Original Image", input_image)
    cv2.imshow("Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
