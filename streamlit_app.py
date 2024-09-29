import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key = 'AIzaSyB3M56MfiQwFP3MbBMStmVW5j3-DQUIrvs')

model= genai.GenerativeModel('gemini-1.5-flash')

def get_gemeini_response(input_t,img_data, prompt):
    response=model.generate_content([input_t,img_data[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue() #Making a byte array
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("Gandu file upload hi nahi kiya")
    
st.set_page_config(page_title="WIE's gemini chatbot")
st.sidebar.header("Question Answering Machine")
st.sidebar.write("Made by Team Cobraz")
st.sidebar.header("Powered by google gemini ai")
st.header("The All Knowing One")
st.subheader("Made by Team Cobraz")
st.subheader("Give a prompt, give a picture and enjoy!")
input = st.text_input("What do you want me to do",key='input')
uploaded_file=st.file_uploader("CHoose an image",type=['jpg','jpeg','png'])
image = ""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

submit=st.button("Let's Go!")

input_prompt="""
You are an expert in calculus. Solve this question step by step and explain everything nicely
"""

if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemeini_response(input_prompt, image_data, input)
    st.subheader("Here's what you need to know: ")
    st.write(response)

#thanks for visiting!
