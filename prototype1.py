import google.generativeai as genai
import PIL.Image
import gradio as gr
import myAPI # here my API key stored

# Retrieve the Google API key from environment variables
GOOGLE_API_KEY = myAPI.API_KEY # change with your own Gemini API key
if GOOGLE_API_KEY is None:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable.")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def generate_content(prompt): # write your prompt here
    response = model.generate_content(prompt)
    return response.text

def generate_content_with_image(prompt, img_path): # write your prompt here
    image = PIL.Image.open(img_path)
    response = model.generate_content([prompt, img_path])
    return response.text

# Example usage
prompt = "How many penguins are in Africa?"
print(generate_content(prompt))

# Example usage with an image
# img_path = "path_to_your_image.jpg"  # Provide the path to your image file
# print(generate_content_with_image(prompt, img_path))
