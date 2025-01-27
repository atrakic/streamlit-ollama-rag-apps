"""
Addapted from: https://blog.streamlit.io/langchain-tutorial-1-build-an-llm-powered-app-in-18-lines-of-code/
"""

import streamlit as st
import os
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

load_dotenv()

OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2")


@st.cache_resource
def get_llm():
    return OllamaLLM(
        model=OLLAMA_MODEL,
        temperature=0,
    )


@st.cache_data
def generate_response(text):
    llm = get_llm()
    return llm.invoke(text)


def main():
    st.title("🦜🔗 Langchain app demo")
    st.write(
        """This demo shows how to use
    [`langchain`](https://github.com/langchain-ai/langchain/tree/master) with Ollama API."""
    )

    with st.form("my_form"):
        text = st.text_area(
            "Enter text:",
            "The meaning of life is",
        )

        submitted = st.form_submit_button("Submit")

        if submitted:
            response = generate_response(text)
            st.write(response)


if __name__ == "__main__":
    main()
