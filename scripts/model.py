from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

def create_model(input_shape=(224, 224, 3), num_classes=2):
    model = Sequential([
        #First conv layer with 32 filters of size 3x3, and ReLU activation
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        #Downsampling the output using a 2x2 max pooling layer
        MaxPooling2D(pool_size=(2, 2)),
        #second conv layer with 64 filters of size 3x3, and ReLU activation
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        #third conv layer with 128 filters of size 3x3, and ReLU activation
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        #Flatten the 2D output of the precious layer into 1d
        Flatten(),
        
        #fully connected layer with 128 neurons and ReLU activation
        Dense(128, activation='relu'),
        #prevent overfitting, disable 50% neurons
        Dropout(0.5)
    ])
    model.add(Dense(num_classes, activation='softmax'))  #output layer
    #compile the model 
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model