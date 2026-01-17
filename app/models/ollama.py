from langchain_community.chat_models import ChatOllama
import os

def get_llm():
    return ChatOllama(
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        model=os.getenv("OLLAMA_MODEL", "qwen2.5:7b"),
        temperature=0.2,
    )
