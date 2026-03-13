import fitz

def extract_pdf_data(file):

    # Read uploaded file as bytes
    file_bytes = file.read()

    # Open PDF from memory
    doc = fitz.open(stream=file_bytes, filetype="pdf")

    text_content = ""
    images = []

    for page in doc:
        text_content += page.get_text()

        image_list = page.get_images()

        for img in image_list:
            xref = img[0]
            base_image = doc.extract_image(xref)
            images.append(base_image["image"])

    return text_content, images