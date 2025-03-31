from util.encode import encode
from pathlib import Path
import streamlit as slt

slt.title("File or Text to SHA256 Encode")
slt.write("By Luis019")

uploaded_file = slt.file_uploader("Chose a file:")

if uploaded_file:
    temp_file_path = Path("temp_uploaded_file")
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
    
    encoded_content = encode(temp_file_path, 'f')
    slt.write(f"Encoded content: {encoded_content}")
    
    temp_file_path.unlink()

slt.write("or...")

text = slt.text_input("Type a text:")

if text:
    encoded_content = encode(text, 's')
    slt.write(f"Encoded content: {encoded_content}")
