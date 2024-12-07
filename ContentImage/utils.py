# Utility Functions for File Conversion

import io
from PIL import Image
from docx import Document
from io import BytesIO

# Function to convert image to bytes (for saving to DOCX)
def img_to_bytes(img, img_format="JPEG"):
    try:
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=img_format)
        img_byte_arr.seek(0)
        return img_byte_arr.read()
    except Exception as e:
        print(f"Error in converting image to bytes: {e}")
        return None

# Function to create DOCX file with text and images embedded
def convert_to_docx(content, images):
    try:
        doc = Document()
        doc.add_heading("Generated Content and Images", 0)

        # Add content to the DOCX file
        doc.add_heading("Generated Content", level=1)
        doc.add_paragraph(content)

        # Add images to the DOCX file if images exist
        if images:
            for idx, img in enumerate(images):
                doc.add_heading(f"Generated Image {idx + 1}", level=1)
                img_bytes = img_to_bytes(img)
                if img_bytes:
                    doc.add_picture(io.BytesIO(img_bytes))
                else:
                    doc.add_paragraph(f"Error with Image {idx + 1}")
        else:
            doc.add_paragraph("No images were generated.")

        # Save doc to a BytesIO buffer
        doc_buffer = BytesIO()
        doc.save(doc_buffer)
        doc_buffer.seek(0)

        return doc_buffer

    except Exception as e:
        print(f"Error in generating DOCX: {e}")
        return None
