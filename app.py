import streamlit as st
import requests

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

st.set_page_config(
    page_title = 'SMN',
    page_icon = ':lower_left_paintbrush:',
    initial_sidebar_state= 'auto'
)

with st.sidebar:
    st.title("'Say my name'")
    st.image('smn.png')

st.markdown("<h1 style='text-align: center; color: Crimson;'>SMN</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: IndianRed;'>Painting's movement classifier</h5>", unsafe_allow_html=True)


painting = st.file_uploader(
    label = ':lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush:\
            :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush: :lower_left_paintbrush:',
    type = ['png', 'jpg'],
    accept_multiple_files = False,
    help = ':middle_finger:',
)


if painting is not None:
    r = requests.post(url = 'http://localhost:8000/predict?', files = {'file':painting})
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



# Section 1
st.title('My Presentation')

# Section 2
st.header('Introduction')
st.write('This is an introduction to my presentation.')
image = plt.imread('presentation/La_Junta_de_Filipinas-romanticism.jpg')
st.image(image)

# Section 3
st.header('Main Content')
st.write('This is the main content of my presentation.')
st.image(plt.imread('presentation/Iwan_Iwanowitsch_Schischkin_001-realism.jpg'))

# Section 4
st.header('Conclusion')
st.write('This is the conclusion.')

# Section 5
st.header('References')
st.write('Here are some references.')

# Section 6
st.write('This is more content to make the page longer.')
st.write('This is more content to make the page longer.')
st.write('This is more content to make the page longer.')
st.write('This is more content to make the page longer.')
st.write('This is more content to make the page longer.')
