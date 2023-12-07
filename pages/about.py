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

st.title("About Me ૮ ˶ᵔ ᵕ ᵔ˶ ა")                                   
  
    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form_any =Image.open("images/tiffany.jpg") 



# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form_any)


with st.container():
    st.write("I am 18 years old and I was born on August 31, 2005")
    st.write("I really don't like being in big gatherings because I don't socialize that much. When in a group, I don’t talk too much, but I look around, pay attention, and listen… I'm very observant. I like to learn by watching others on their activities. But when I am with my close friends I become a different person and talk all day as long as I'm with them. I usually zone out in the midst of a gathering. That’s because I need to “rest” from social interaction. Being with lots of people drains my energy. Sometimes I need to be by myself. Being around a lot of people all day is exhausting, so when I come home from a stressful day of school I need some time to re-energize and clear my mind. I enjoy being alone and listening to good music, watching my favorite TV show, or a good walk. ")