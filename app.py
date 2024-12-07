import os
import streamlit as st
from ContentImage.helper import *
from ContentImage.utils import *



# Streamlit UI
st.set_page_config(
    page_title="Content & Image Generator",
    page_icon=":notebook_with_decorative_cover:",
    layout="centered"
)

st.header("Content & Image Generator")

# User inputs
topic = st.text_input("Enter the Topic", placeholder="e.g., The role of AI in education")

# Side bar :-
with st.sidebar:
    st.title("Parameters")
    # Language Input with "Other" option
    language = st.selectbox("Language", ["English", "Other (please specify)"])
    if language == "Other (please specify)":
        other_language = st.text_input("Other Language", placeholder="Specify the language")
    else:
        other_language = ""

    # Tone Input with additional options
    tone = st.selectbox("Select Tone", ["Formal", "Conversational", "Persuasive", "Neutral", "Other (please specify)"])
    if tone == "Other (please specify)":
        other_tone = st.text_input("Other Tone", placeholder="Specify the tone")
    else:
        other_tone = ""

    # Content Format Input with additional options
    content_format = st.selectbox("Select Format", ["Article", "Blog Post", "Social Media Post", "Other (please specify)"])
    if content_format == "Other (please specify)":
        other_format = st.text_input("Other Format", placeholder="Specify the format")
    else:
        other_format = ""

    # Word Count Input (Length)
    length = st.text_input("Enter Word Count", placeholder="e.g., 300")
    if not length.isdigit() and length != "":
        st.error("Please enter a valid number for word count.")
    else:
        word_count = length

    # Style Input with additional options
    style = st.selectbox("Select Style", ["Professional", "Creative", "Technical", "Other (please specify)"])
    if style == "Other (please specify)":
        other_style = st.text_input("Other Style", placeholder="Specify the style")
    else:
        other_style = ""

    # Audience Input with "Other" option
    audience = st.selectbox("Audience", ["General Public", "Industry Professionals", "Students", "Other (please specify)"])
    if audience == "Other (please specify)":
        other_audience = st.text_input("Other Audience", placeholder="Specify the audience")
    else:
        other_audience = ""

    # Purpose Input with "Other" option
    purpose = st.selectbox("Purpose", ["Inform", "Educate", "Entertain", "Persuade", "Other (please specify)"])
    if purpose == "Other (please specify)":
        other_purpose = st.text_input("Other Purpose", placeholder="Specify the purpose")
    else:
        other_purpose = ""
    
    # Number of Images Slider
    num_images = st.slider("Number of Images", min_value=1, max_value=5, value=1)


# Function to generate images and display them
if st.button("Generate"):
    if not topic.strip():
        st.error("Please enter a topic!")
    else:
        with st.spinner("Generating content and images..."):
            # Generate content
            content = generate_content(topic, language, tone, content_format, length, style, audience, purpose)
            st.subheader("Generated Content:")
            st.write(content)

            # Generate images
            st.subheader("Generated Images:")
            image_prompt = f"{topic}, {style} style"
            images = [generate_image(image_prompt)] * num_images  # Repeat image generation for the desired number of images

            if images:
                for i, image in enumerate(images):
                    st.image(image, caption=f"Generated Image {i + 1}", use_column_width=True)
            else:
                st.error("Failed to generate images.")
                st.stop()  # Stop the app if no images are generated

            # Combine content and images for download (DOCX)
            doc_buffer = convert_to_docx(content, images)

            # Provide download button for DOCX
            st.download_button(
                label="Download as DOCX",
                data=doc_buffer,
                file_name="generated_content_and_images.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )