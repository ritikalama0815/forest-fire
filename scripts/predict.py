import numpy as np
from tensorflow.keras.processing import image

def predict_image(model, img_path, image_size=(224, 224)):
    img = image.load_img(img_path, target_size=image_size)
    img_array = image.img_to_array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    predictions = model.predict(img_array)
    return "Fire" if predictions[0][0] > 0.5 else "No Fire"