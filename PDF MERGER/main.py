import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import os

st.set_page_config(page_title="PDF Tool", layout="centered")
st.title("Simple PDF Toolkit")

task = st.selectbox("Choose Task", ["Merge PDFs", "Compress PDF", "Extract Images"])


os.makedirs("output", exist_ok=True)


if task == "Merge PDFs":
    st.subheader("Upload PDFs to Merge")
    uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

    if uploaded_files and st.button("Merge Now"):
        merger = PdfWriter()
        for uploaded_file in uploaded_files:
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                merger.add_page(page)
        
        merged_path = "output/merged-pdf.pdf"
        with open(merged_path, "wb") as f:
            merger.write(f)

        with open(merged_path, "rb") as f:
            st.success("Merged PDF Created!")
            st.download_button("Download Merged PDF", f, file_name="merged-pdf.pdf")


elif task == "Compress PDF":
    st.subheader("Upload PDF to Compress")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file and st.button("Compress Now"):
        reader = PdfReader(uploaded_file)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)
        writer.add_metadata(reader.metadata)

        compressed_path = "output/compressed.pdf"
        with open(compressed_path, "wb") as f:
            writer.write(f)

        with open(compressed_path, "rb") as f:
            st.success("Compressed PDF Ready!")
            st.download_button("Download Compressed PDF", f, file_name="compressed.pdf")


elif task == "Extract Images":
    st.subheader("Upload PDF to Extract Images")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file and st.button("Extract Images"):
        reader = PdfReader(uploaded_file)
        count = 0
        image_files = []

        for page in reader.pages:
            for image in page.images:
                filename = f"output/image_{count}_{image.name}"
                with open(filename, "wb") as f:
                    f.write(image.data)
                image_files.append(filename)
                count += 1

        if image_files:
            st.success(f"Extracted {count} image(s)!")
            for file in image_files:
                with open(file, "rb") as f:
                    st.download_button(f"Download {os.path.basename(file)}", f, file_name=os.path.basename(file))
        else:
            st.warning("No images found in the uploaded PDF.")