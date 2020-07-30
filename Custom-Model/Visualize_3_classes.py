import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import pickle

cap = cv2.VideoCapture(0)
class_name = ['Paper', 'Rock', 'Scissors']


model = tf.keras.models.load_model('.\model_saved.h5')

while(cap.isOpened()):
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    resized = cv2.resize(frame, (150, 150), interpolation=cv2.INTER_AREA)
    resized = resized/255

    x = image.img_to_array(resized)
    x = np.expand_dims(x, axis=0)

    final_img = np.vstack([x])
    classes = model.predict(final_img, batch_size=10)
    classes = np.reshape(classes, (3,))

    idx = np.argmax(classes)

    cv2.putText(frame, class_name[idx], (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.namedWindow('original', cv2.WINDOW_NORMAL)
    cv2.imshow('original', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
