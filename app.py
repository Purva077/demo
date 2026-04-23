import streamlit as st
from PIL import Image
import pytesseract
import pdfplumber
import fitz  # PyMuPDF
import io

st.title("DocuScan - PDF/Image to Text")

uploaded_file = st.file_uploader("Upload PDF or image", type=["pdf", "png", "jpg", "jpeg", "webp"])

def extract_text_from_pdf(file_bytes):
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_text_from_image(file_bytes):
    image = Image.open(io.BytesIO(file_bytes))
    return pytesseract.image_to_string(image)

if uploaded_file:
    file_bytes = uploaded_file.read()

    if uploaded_file.type == "application/pdf":
        extracted_text = extract_text_from_pdf(file_bytes)
    else:
        extracted_text = extract_text_from_image(file_bytes)

    st.subheader("Extracted Text")
    st.text_area("Output", extracted_text, height=400)
