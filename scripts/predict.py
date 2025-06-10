import numpy as np
from keras.preprocessing import image

def predict_image(model, img_path, image_size=(224, 224)):
    img = image.load_img(img_path, target_size=image_size) #load image and resize
    img_array = image.img_to_array(img)/255.0 #convert image into numpy array and normalize from [0, 255] to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  #add dimension
    predictions = model.predict(img_array)
    return "Fire" if predictions[0][0] > 0.5 else "No Fire"