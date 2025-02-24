
import streamlit as st
from ContentImage.helper import *
from ContentImage.utils import *



# Streamlit UI
st.set_page_config(
    page_title="Content & Image Generator",
    page_icon=":art:",
    layout="wide"
)

st.title("📜 Content & Image Generator")
st.write("Create compelling content and images effortlessly.")

# User inputs
topic = st.text_input("Enter the Topic", placeholder="e.g., The role of AI in education")

# Side bar :-
with st.sidebar:
    st.title("⚙️ Parameters")
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
if st.button("🚀 Generate Content & Images"):
    if not topic.strip():
        st.error("Please enter a topic!")
    else:
        with st.spinner("Generating content and images..."):
            # Generate content
            content = generate_content(topic, language, tone, content_format, length, style, audience, purpose)
            st.subheader("📄 Generated Content:")
            st.write(content)


            # Generate images
            st.subheader("🖼️ Generated Images:")
            images = []
            for i in range(num_images):
                unique_prompt = f"{topic}, {style} style, image {i + 1}"
                image = generate_image(unique_prompt)  # Ensure the prompt is unique for each image
                if image:
                    st.image(image, caption=f"Generated Image {i + 1}", use_column_width=True)
                    images.append(image)
                else:
                    st.warning(f"Failed to generate Image {i + 1}")

            # Generate DOCX file
            doc_buffer = convert_to_docx(content, images)
            if doc_buffer:
                st.download_button(
                    label="📥 Download as DOCX",
                    data=doc_buffer,
                    file_name="generated_content_and_images.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
            else:
                st.error("Failed to generate DOCX file.")
