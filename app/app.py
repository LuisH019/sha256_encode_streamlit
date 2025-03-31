from util.encode import encode
from pathlib import Path
import streamlit as st

st.title("File or Text to SHA256 Encode")
st.write("By Luis019")

uploaded_file = st.file_uploader("Chose a file:")

if uploaded_file:
    temp_file_path = Path("temp_uploaded_file")
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
    
    encoded_content = encode(temp_file_path, 'f')
    st.write(f"Encoded content: {encoded_content}")
    
    temp_file_path.unlink()

st.write("or...")

text = st.text_input("Type a text:")

if text:
    encoded_content = encode(text, 's')
    st.write(f"Encoded content: {encoded_content}")
