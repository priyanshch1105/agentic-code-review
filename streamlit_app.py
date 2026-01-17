import streamlit as st
import requests
import json

API_URL = "http://localhost:8000/review"

st.set_page_config(
    page_title="Agentic Code Review",
    layout="centered"
)

st.title("🤖 Agentic AI Code Review")
st.write("Paste a GitHub repository URL to analyze code quality and security.")

repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/psf/requests"
)

if st.button("Review Repository"):
    if not repo_url:
        st.warning("Please enter a repository URL")
    else:
        with st.spinner("Running agentic review..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"repo_url": repo_url},
                    timeout=600
                )
                response.raise_for_status()
                result = response.json()

                st.success("Review completed")
                st.json(result)

            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {e}")
