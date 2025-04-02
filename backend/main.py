from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="gemma3:1b", base_url="http://ollama:11434")

template = """
You are a professional liquor taster and your job is to answer questions about alcoholic beverages

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GenerateQuery(BaseModel):
    question: str


@app.post("/generate")
def generate(query: GenerateQuery):

    response = chain.invoke({"reviews": [], "question": query.question})

    return {"response": response}
