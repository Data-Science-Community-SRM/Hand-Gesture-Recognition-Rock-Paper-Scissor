import cv2
import tensorflow as tf
import numpy as np
from keras.preprocessing import image

cap = cv2.VideoCapture(0)
class_name = ['Nothing', 'Paper', 'Rock', 'Scissors']

model=tf.keras.models.load_model('Model_4thclass.h5')

while(cap.isOpened()):
    _, frame = cap.read()
    frame = cv2.flip(frame,1)	#flip
    
    resized = cv2.resize(frame, (150,150), interpolation = cv2.INTER_AREA)	#resize
    resized = resized/255	#normalize

    x = image.img_to_array(resized)
    x = np.expand_dims(x, axis=0)
    
    final_img = np.vstack([x])
    classes = model.predict(final_img, batch_size=10)
    classes = np.reshape(classes, (4,))
    
    idx = np.argmax(classes)
    
    cv2.putText(frame, class_name[idx], (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2, cv2.LINE_AA)
    
    cv2.namedWindow ('original', cv2.WINDOW_NORMAL)
    cv2.namedWindow ('resized', cv2.WINDOW_NORMAL)
    
    cv2.imshow('original', frame)
    cv2.imshow('resized', resized)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
