from PIL import Image
import requests

import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.title("My mama")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/mama.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("She is Mariecor Fajardo Lapingcao")
    st.write("She is my mother and I love her. My mama is so kind and she's beautiful")

st.title("My Mommy Nita")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/mommy.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("She is Marianita Llabore.")
    st.write("She is my grandmother. I was raised by my mommy and she's always been on my side")

st.title("My Brother")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/dong dong.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("He's my Brother.")
    st.write("He's a HUMSS student now in DJEMC")


st.title("My Sister")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/inday.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("She's my sister, Kisha Gwyn.")
    st.write("She's a Grade 9 student in DHNHS. We always fight a lot but I still love her")

st.title("My little sister")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/cassity.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("She's my youngest sister")
    st.write("She was born on August 7,2023. I love her so much much much")
    
    
    









    
