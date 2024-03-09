import streamlit as st
import requests

import numpy as np
from PIL import Image


st.markdown("<h1 style='text-align: center; color: Crimson;'>Say My Name</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: grey;'>Classify yo Painting</h5>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: left; color: IndianRed;'>Upload yo Painting</h4>", unsafe_allow_html=True)


painting = st.file_uploader(
    label = ':lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush:',
    type = ['png', 'jpg'],
    accept_multiple_files = False,
    help = ':middle_finger:',
)

if painting is not None:
    r = requests.post(url = 'http://localhost:8000/predict?', files = {'file':painting})
    st.write(r)
    response = r.json()
    st.write('This is my response:')
    st.markdown(response)


    st.write('----------This is testing from now on------------')
    image = Image.open(painting)
    img_array = np.array(image)

    if image is not None:
        st.image(
            image,
            caption=f"You amazing image has shape {img_array.shape[0:2]}",
            use_column_width=True,
        )
