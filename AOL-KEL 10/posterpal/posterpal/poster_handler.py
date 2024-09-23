import os
import openai
import urllib.request
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('open_ai_api_key')

def generate_poster(theme, background_text):
    user_prompt = "make a poster with " +theme+ " theme, and " +background_text+ " as a background text"
    response = openai.Image.create(
        prompt=user_prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print("\nposter url :")
    print(image_url)
    print("\nsaving image...")
    file_name = "image" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".png"
    urllib.request.urlretrieve(image_url, file_name)
    print("image saved as image" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".png")
    