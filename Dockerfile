FROM ollama/ollama

RUN ollama serve && sleep 5 && ollama pull gemma3:1b && ollama pull nomic-embed-text