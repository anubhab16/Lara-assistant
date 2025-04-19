import gradio as gr
import google.generativeai as genai
import webbrowser
import os
from dotenv import load_dotenv
import subprocess

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("Error: GEMINI_API_KEY is missing! Check your .env file.")
genai.configure(api_key=API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")

def process_command(command):
    command = command.lower().strip()

    # Web commands
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google..."

    elif "open anime" in command:
        webbrowser.open("https://hianime.to/home")
        return "Opening Anime..."

    elif "open chatgpt" in command:
        webbrowser.open("https://chatgpt.com")
        return "Opening ChatGPT..."

    elif "open spotify" in command:
        try:
            subprocess.Popen(["explorer", "shell:AppsFolder\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0!Spotify"])
            return "Opening Spotify..."
        except Exception as e:
            return f"Error opening Spotify: {e}"

    # Default: Gemini handles all
    else:
        try:
            response = model.generate_content(command)
            return response.text if hasattr(response, "text") else "I couldn't generate a response."
        except Exception as e:
            return f"Gemini Error: {e}"

# Gradio interface
demo = gr.Interface(
    fn=process_command,
    inputs=gr.Textbox(lines=2, placeholder="Ask Lara anything..."),
    outputs="text",
    title="Lara (Gemini-Powered)",
    description="Lara, your assistant powered by Gemini Pro. Ask anything!"
)

demo.launch()
