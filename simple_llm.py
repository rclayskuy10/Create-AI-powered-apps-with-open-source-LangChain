import os
from langchain_openai import ChatOpenAI
import gradio as gr

# Memasukkan API key
os.environ["OPENAI_API_KEY"] = "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"

gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo")

def chatbot(prompt):
    # Pass the prompt to gpt3.invoke()
    response = gpt3.invoke(prompt).content
    return response

demo = gr.Interface(fn=chatbot, inputs="textbox", outputs="textbox")

demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
