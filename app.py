from huggingface_hub import hf_hub_download
import os
from pyngrok import ngrok
from llama_cpp import Llama

# Set up environment variables
ngrok_auth_token = os.getenv("NGROK_AUTH_TOKEN", "2qNKOgrXwxp4MaBmmu4AFjpH58E_6V9RPz5WDzu9xdEnaJN96")

# Download the model
repo_id = "huggingdaveTest1/unsolt_Llama"
filename = "unsloth.Q4_K_M.gguf"
model_path = hf_hub_download(repo_id=repo_id, filename=filename)
print(f"Model downloaded to: {model_path}")

# Load the model
llm = Llama(model_path=model_path, n_ctx=2048)

# Test the model with a simple prompt
response = llm("What is diabetes?", max_tokens=100)
print(response["choices"][0]["text"])

# Streamlit App UI
import streamlit as st
st.title("🩺 Medical Chatbot")
st.write("Ask me a medical question and get an AI-powered response.")

# User Input
user_input = st.text_input("Your Question:")

# Generate Response
if user_input:
    with st.spinner("Generating response..."):
        response = llm(user_input, max_tokens=150)
        st.write(f"**Chatbot:** {response['choices'][0]['text']}")

# Configure ngrok
ngrok.set_auth_token(ngrok_auth_token)
public_url = ngrok.connect(8501, "http")
print(f"Streamlit app is running at: {public_url}")
