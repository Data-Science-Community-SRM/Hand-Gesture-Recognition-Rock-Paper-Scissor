import numpy as np
from PIL import Image, ImageOps
import cv2
import streamlit as st
import tensorflow as tf
model = tf.keras.models.load_model('Model_4_classes.h5')
st.write("""# Rock-Paper-Scissor Hand Sign Prediction""")
st.write("This is a simple image classification web app to predict rock-paper-scissor hand sign")
file = st.file_uploader("Please upload an image file", type=["jpg"])

st.set_option('deprecation.showfileUploaderEncoding', False)


def import_and_predict(image_data, model):

    size = (150, 150)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    image = np.asarray(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resize = (cv2.resize(img, dsize=(150, 150),
                             interpolation=cv2.INTER_CUBIC))/255.

    img_reshape = img_resize[np.newaxis, ...]

    prediction = model.predict(img_reshape)

    return prediction


if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    if np.argmax(prediction) == 0:
        st.write("Nothing Detected!")
    elif np.argmax(prediction) == 1:
        st.write("It is a Paper!")
    elif np.argmax(prediction) == 2:
        st.write("It is a Rock!")
    else:
        st.write("It is a scissor!")
    st.text("Probability (0: Nothing, 1: Paper, 2: Rock, 3:Scissor")
    st.write(prediction)
