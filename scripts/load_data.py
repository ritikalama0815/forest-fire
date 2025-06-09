import tensorflow as tf

def load_dataset(data, image_size=(224, 224), batch_size=32, label_mode='categorical', shuffle=True):
    return tf.keras.preprocessing.image_dataset_from_directory(
        data,
        image_size=image_size,
        batch_size=batch_size,
        label_mode=label_mode,
        shuffle=shuffle
    )