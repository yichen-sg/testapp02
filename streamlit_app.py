import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

st.title("🎈 this is my 2nd ")

st.write("Great Hello World.")

input_result = st.text_input("pls input a value") 

st.write(input_result)

local_image_path = "4.jpg"

base64_image = get_base64_image(local_image_path)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    /* 可选：为了让文本更清晰，可以给内容区域添加半透明背景 */
    .stBlockContainer {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 2rem;
        border-radius: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
