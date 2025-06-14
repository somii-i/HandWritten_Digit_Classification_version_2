from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout, BatchNormalization # type: ignore
from tensorflow.keras.regularizers import l2 # type: ignore
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config

def build_cnn_model():
    model = Sequential()

    #1
    model.add(Conv2D(filters=32, kernel_size=(5,5), padding='Same', 
                     activation='relu', kernel_regularizer=l2(0.001), input_shape=(Config.IMAGE_SIZE, Config.IMAGE_SIZE, 1)))
    model.add(BatchNormalization())
    model.add(Conv2D(filters=32, kernel_size=(5,5), padding='Same', 
                     activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    #2
    model.add(Conv2D(filters=64, kernel_size=(3,3), padding='Same', 
                     activation='relu', kernel_regularizer=l2(0.001))),
    model.add(BatchNormalization())
    model.add(Conv2D(filters=64, kernel_size=(3,3), padding='Same', 
                     activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
    model.add(Dropout(0.25))
    #additional
    model.add(Conv2D(filters=128, kernel_size=(3,3), padding='Same'))
    model.add(BatchNormalization())
    model.add(Dropout(0.25))

    #classifier
    model.add(Flatten())
    model.add(Dense(256, activation="relu", kernel_regularizer=l2(0.001)))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
    model.add(Dense(Config.NUM_CLASSES, activation="softmax"))
    
    return model

if __name__ == '__main__':
    model = build_cnn_model()
    model.summary()
    print("Model built successfully")