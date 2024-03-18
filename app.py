import streamlit as st
import requests

import numpy as np
from PIL import Image

st.set_page_config(
    page_title = 'SMN',
    page_icon = ':lower_left_paintbrush:',
    initial_sidebar_state= 'auto'
)

with st.sidebar:
    st.title("'Hallo.'")
    st.image('smn.png')

st.markdown("<h1 style='text-align: center; color: Crimson;'>SMN</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: IndianRed;'>Painting's movement classifier</h5>", unsafe_allow_html=True)



painting = st.file_uploader(
    label = ':lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush:\
             Upload a saved painting :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush:',
    type = ['png', 'jpg'],
    accept_multiple_files = False,
    help = ':middle_finger:',
)

if painting is not None:
    r = requests.post(url = 'https://smndocker-rdwmjilicq-ew.a.run.app/predict?', files = {'file':painting})
    response = r.json()
    my_pred = response['mypred'][1].upper()

    st.write(f"Paiting's movement : **{my_pred}**")

    image = Image.open(painting)
    img_array = np.array(image)
    st.balloons()

    if image is not None:
        st.image(
            image,
            caption=f"You amazing image has shape {img_array.shape[0:2]}",
            use_column_width=True,
        )

painting = st.camera_input(
    label = ":lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush:\
             Take a picture of a painting :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush:",
    help = ':middle_finger:'
)

if painting is not None:
    r = requests.post(url = 'https://smndocker-rdwmjilicq-ew.a.run.app/predict?', files = {'file':painting})
    response = r.json()
    my_pred = response['mypred'][1].upper()

    st.write(f"Paiting's movement : **{my_pred}**")

    image = Image.open(painting)
    img_array = np.array(image)
    st.balloons()

    if image is not None:
        st.image(
            image,
            caption=f"You amazing image has shape {img_array.shape[0:2]}",
            use_column_width=True,
        )
