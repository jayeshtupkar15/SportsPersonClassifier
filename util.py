import joblib
import json
import os
import numpy as np
import base64
import cv2
from wavelet import w2d


# Global variables for class mappings and model
__class_name_to_number = {}
__class_number_to_name = {}
__model = None

def classify_image(image_base64_data, file_path=None):
    imgs = get_cropped_image_if_2_eyes(file_path, image_base64_data)
    result = []

    for img in imgs:
        # Resize raw image
        scaled_raw_img = cv2.resize(img, (32, 32))
        # Apply wavelet transform
        img_har = w2d(img, 'db1', 5)
        scaled_img_har = cv2.resize(img_har, (32, 32))
        # Combine raw and wavelet images into one vector
        combined_img = np.vstack((
            scaled_raw_img.reshape(32 * 32 * 3, 1),
            scaled_img_har.reshape(32 * 32, 1)
        ))
        len_image_array = 32 * 32 * 3 + 32 * 32
        final = combined_img.reshape(1, len_image_array).astype(float)

        prediction = __model.predict(final)[0]
        prediction_proba = np.around(__model.predict_proba(final) * 100, 2).tolist()[0]

        result.append({
            'class': class_number_to_name(prediction),
            'class_probability': prediction_proba,
            'class_dictionary': __class_name_to_number
        })
    return result

def class_number_to_name(class_num):
    return __class_number_to_name.get(class_num, "Unknown")

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __class_name_to_number
    global __class_number_to_name
    global __model

    # Get absolute path of this util.py file's directory
    dir_path = os.path.dirname(os.path.realpath(__file__))

    class_dict_path = os.path.join(dir_path, "artifacts", "class_dictionary.json")
    model_path = os.path.join(dir_path, "artifacts", "saved_model.pkl")

    with open(class_dict_path, "r") as f:
        __class_name_to_number = json.load(f)
        __class_number_to_name = {v: k for k, v in __class_name_to_number.items()}

    if __model is None:
        with open(model_path, 'rb') as f:
            __model = joblib.load(f)

    print("loading saved artifacts...done")

def get_cv2_image_from_base64_string(b64str):
    '''
    Convert base64 string to OpenCV image.
    '''
    encoded_data = b64str.split(',')[1]  # Remove prefix like 'data:image/jpeg;base64,...'
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def get_cropped_image_if_2_eyes(image_path, image_base64_data):
    face_cascade = cv2.CascadeClassifier('./opencv/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./opencv/haarcascades/haarcascade_eye.xml')

    if image_path:
        img = cv2.imread(image_path)
    else:
        img = get_cv2_image_from_base64_string(image_base64_data)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    cropped_faces = []
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 2:
            cropped_faces.append(roi_color)
    return cropped_faces

def get_b64_test_image_for_virat():
    with open("b64.txt") as f:
        return f.read()

if __name__ == '__main__':
    load_saved_artifacts()
    print(classify_image(get_b64_test_image_for_virat(), None))
    # You can add test image paths to try:
    # print(classify_image(None, "./test_images/federer1.jpg"))
