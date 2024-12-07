from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv
import os
from PIL import Image
from io import BytesIO
import requests
from ContentImage.prompt import *

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")


# Response generation function using LLM
def generate_content(topic, language, tone, content_format, length, style, audience, purpose):

    # Initialize the LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro-002",
        temperature=1,
        api_key=GOOGLE_API_KEY
    )

    # Define the prompt template
    template = PROMPT

    # Create the LLM prompt template
    prompt = PromptTemplate(
        input_variables=["topic", "language", "tone", "content_format", "length", "style", "audience", "purpose"],
        template=template
    )
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Generate response
    response = llm_chain.run({
        "topic": topic,
        "language": language,
        "tone": tone,
        "content_format": content_format,
        "length": length,
        "style": style,
        "audience": audience,
        "purpose": purpose
    })
    return response





# Set the Hugging Face API URL and model name
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"}

def generate_image(prompt):
    data = {
        "inputs": prompt,
    }

    # Send the request to the Hugging Face API
    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        print(f"Error: {response.status_code}")
        return None