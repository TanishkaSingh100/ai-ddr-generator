import streamlit as st
from extractor import extract_pdf_data
from ddr_generator import generate_ddr
from PIL import Image
import io

st.markdown("---")
st.title("AI Detailed Diagnostic Report Generator")

report_file_1 = st.file_uploader("Upload Report 1", type=["pdf"])
report_file_2 = st.file_uploader("Upload Report 2", type=["pdf"])

if report_file_1 and report_file_2 and st.button("Generate DDR"):

    text1, images1 = extract_pdf_data(report_file_1)
    text2, images2 = extract_pdf_data(report_file_2)

    with st.spinner("Analyzing reports and generating DDR..."):
        report = generate_ddr(text1, text2)

    st.markdown(report)
    
    st.markdown("---")
    st.subheader("Extracted Images From Report 1")

    cols = st.columns(3)

    for i, img in enumerate(images1):
        try:
            image = Image.open(io.BytesIO(img))
            if image.width > 0 and image.height > 0:
                cols[i % 3].image(image, width=250)
        except:
            pass

    st.subheader("Extracted Images From Report 2")

    cols = st.columns(3)

    for i, img in enumerate(images2):
        try:
            image = Image.open(io.BytesIO(img))
            if image.width > 0 and image.height > 0:
                cols[i % 3].image(image, width=250)
        except:
            pass

st.markdown("---")
st.caption("AI-powered diagnostic report generated from uploaded inspection documents.")