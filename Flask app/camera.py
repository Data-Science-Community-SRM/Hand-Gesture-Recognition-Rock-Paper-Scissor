import cv2

import tensorflow as tf

from keras.preprocessing import image


import tensorflow.keras as k
import cv2
import numpy as np
import time


model = tf.keras.models.load_model('Model_4_classes.h5')

ds_factor = 0.6



class VideoCamera(object):

    def __init__(self):

        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        class_name = ['Nothing', 'Paper', 'Rock', 'Scissors']
        success, frame = self.video.read()
        frame = cv2.flip(frame, 1)

        resized = cv2.resize(frame, (150, 150), interpolation=cv2.INTER_AREA)
        resized = resized/255

        cv2.imwrite('static\\img.png', frame)

        path = "static\\img.png"

        x = image.img_to_array(resized)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])
        classes = model.predict(images, batch_size=10)
        #print(classes)
        classes = np.reshape(classes, (4,))

        idx = np.argmax(classes)

        cv2.putText(frame, class_name[idx], (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return (jpeg.tobytes())
