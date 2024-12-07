# Content & Image Generator

A Streamlit-based web application that generates content and images based on user inputs. The application uses language models for content generation and Stable Diffusion via Hugging Face API for image generation. Additionally, the generated content and images can be saved in a DOCX file format.

## Features

- **Content Generation**: Generate text content based on user-selected parameters like topic, tone, style, audience, and purpose.
- **Image Generation**: Generate images based on the content topic and style using the Hugging Face Stable Diffusion model.
- **Downloadable DOCX**: Combine the generated content and images into a downloadable DOCX file.

## Installation

To run this project, make sure you have Python 3.10+ installed. Then follow these steps:

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/PriyanshuDey23/ContentImageGenPro.git
```

### Step 2: Install Dependencies

Navigate to the project directory and install the required dependencies:

```bash
cd <project-directory>
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables

Create a `.env` file in the root of the project and add the following environment variables with your own values:

```bash
GOOGLE_API_KEY=<your-google-api-key>
HUGGING_FACE_API_KEY=<your-hugging-face-api-key>
```

Make sure to replace `<your-google-api-key>` and `<your-hugging-face-api-key>` with the respective API keys.

### Step 4: Run the Streamlit App

To start the Streamlit application, run the following command:

```bash
streamlit run app.py
```

This will open the app in your default web browser, where you can interact with the interface and generate content and images.

## Usage

1. **Enter the Topic**: Type a topic for which you want to generate content.
2. **Select Parameters**: Use the sidebar to select various parameters:
   - **Language**: Choose the language for content generation.
   - **Tone**: Select the tone for the content (e.g., formal, conversational).
   - **Content Format**: Choose between article, blog post, social media post, or specify your format.
   - **Word Count**: Specify the desired word count for the generated content.
   - **Style**: Select the style (e.g., professional, creative).
   - **Audience**: Specify the intended audience.
   - **Purpose**: Define the purpose of the content (e.g., inform, educate).
   - **Number of Images**: Select how many images to generate for the content.

3. **Generate**: Click the "Generate" button to see the generated content and images.
4. **Download**: After the content and images are generated, you can download the result as a DOCX file by clicking the "Download as DOCX" button.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Hugging Face](https://huggingface.co/)
- [Pillow](https://pillow.readthedocs.io/)
- [langchain](https://langchain.com/)
