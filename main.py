import gradio as gr
import google.generativeai as genai
import myAPI # here my API key stored, its okay to delete this line


# SET GOOGLE API KEY
GOOGLE_API_KEY = myAPI.API_KEY # change with your own Gemini API key
if GOOGLE_API_KEY is None:
    raise ValueError("Please set the GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def generate_content_with_image(prompt, img):
    try:
      response = model.generate_content(prompt)
      return response.text
    except Exception as e:
        return str(e)

# Gradio UI components
prompt_input = gr.Textbox(lines=3, placeholder="Enter your prompt here...")
output_text = gr.Textbox(lines=4, placeholder="Answer will appear here...")

# Gradio interface
gr.Interface(
    fn=generate_content_with_image,
    inputs=[prompt_input],
    outputs=output_text,
    title="Generative AI Content Generator",
    description="Enter a prompt and optionally upload an image to generate content using the Generative AI model.",
# ).launch(share=True) # uncomment this line to share your Gradio app
).launch()