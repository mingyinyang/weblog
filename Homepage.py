from asyncio import _enter_task
from tkinter import CENTER
from PIL import Image
import requests

import streamlit as st
#from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.set_page_config(
    page_title="Multipage App",
    page_icon="wave"
)


st.title("Tiffany's Blog")                                   
  
    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form_any =Image.open("images/tiffany.jpg") 



# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form_any)


with st.container():
    st.subheader("Hi, I am Tiffany Lapingcao Llabore :butterfly:")
    st.subheader("I'm a Computer Engineering student at Surigao del Norte State University")
    
    st.subheader("This is my socials feel free to visit them.")
    st.write(" ▶ Facebook: https://www.facebook.com/tiffany.llabore.7")
    st.write(" ▶ Instagram: frenny_frays")
    st.write(" ▶Email: tiffllabore831@gmail.com")
    st.write(" ▶Contact Number: 09703583417")
