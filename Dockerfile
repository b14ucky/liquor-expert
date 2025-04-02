FROM ollama/ollama

RUN ollama serve & sleep 5 && ollama run gemma3:1b