from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import os
import requests
from ContentImage.prompt import PROMPT
from ContentImage.utils import img_to_bytes

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")

# Response generation function using LLM
def generate_content(topic, language, tone, content_format, length, style, audience, purpose):
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            temperature=1,
            api_key=GOOGLE_API_KEY
        )
        prompt = PromptTemplate(
            input_variables=["topic", "language", "tone", "content_format", "length", "style", "audience", "purpose"],
            template=PROMPT
        )
        llm_chain = LLMChain(llm=llm, prompt=prompt)
        return llm_chain.run({
            "topic": topic,
            "language": language,
            "tone": tone,
            "content_format": content_format,
            "length": length,
            "style": style,
            "audience": audience,
            "purpose": purpose
        })
    except Exception as e:
        print(f"Error generating content: {e}")
        return "Error generating content."

# Image generation function using Hugging Face API
import time

def generate_image(prompt):
    """
    Generates an image using the Hugging Face API with retry mechanism.

    Args:
        prompt (str): The prompt for image generation.

    Returns:
        PIL.Image.Image or None: Generated image or None if an error occurs.
    """
    retries = 5
    for attempt in range(retries):
        try:
            headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
            data = {"inputs": prompt}

            # Send request to the Hugging Face API
            model_name="strangerzonehf/Flux-Midjourney-Mix2-LoRA"

            response = requests.post(
                f"https://api-inference.huggingface.co/models/{model_name}",
                headers=headers,
                json=data
            )

            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                return img_to_bytes(image)  # Return byte array
            else:
                if response.status_code == 503:
                    print("Service unavailable, retrying...")
                    time.sleep(5)  # Wait for 5 seconds before retrying
                else:
                    print(f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}")
                    return None
        except Exception as e:
            print(f"Exception occurred during image generation: {e}")
            return None
    return None