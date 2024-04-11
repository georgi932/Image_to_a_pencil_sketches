import cv2
import numpy as np

# Allowed file extensions
ALLOWED_EXTENSION = {'png', 'jpg', 'jpeg', 'gif'}


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


def apply_filter(image, filter_type):
    if filter_type == "blur":
        return cv2.blur(image, (5, 5))

    elif filter_type == "sharpen":
        kernel = np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]])
        return cv2.filter2D(image, -1, kernel)

    elif filter_type == "edge":
        return cv2.Canny(image, 100, 200)

    elif filter_type == "emboss":
        kernel = np.array([[-2, -1, 0],
                           [-1, 1, 1],
                           [0, 1, 2]])
        return cv2.filter2D(image, -1, kernel)

    elif filter_type == "sepia":
        kernel = np.array([[0.393, 0.769, 0.189],
                           [0.349, 0.686, 0.168],
                           [0.272, 0.534, 0.131]])
        sepia_image = cv2.transform(image, kernel)
        sepia_image = cv2.cvtColor(sepia_image, cv2.COLOR_BGR2RGB)
        return sepia_image

    elif filter_type == "grayscale":
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        return image  # Return original image if filter type not recognized

    # Load the image
    image_path = "input_image.jpg"
    input_image = cv2.imread(image_path)

    # Apply the desired filter
    filtered_image = apply_filter(input_image, "emboss")

    # Display the original and filtered images
    cv2.imshow("Original Image", input_image)
    cv2.imshow("Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
