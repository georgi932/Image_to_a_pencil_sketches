import cv2
from PIL import Image

ALLOWED_EXTENSION = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION


def transform_to_pencil_sketch(image_path):
    image = cv2.imread(image_path)
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    inverted_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, inverted_blur, scale=256.0)
    return sketch


def transform_to_sepia(image_path):
    image = cv2.imread(image_path)


def transform_to_grayscale(image_path):
    # Transformation to grayscale
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return Image.fromarray
