from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from vector_db import retriever

model = OllamaLLM(model="gemma3:1b", base_url="http://ollama:11434")

template = """
You are a professional liquor taster with extensive knowledge of alcoholic beverages. Your job is to provide expert answers to users' questions, using both your knowledge and any relevant reviews provided.

Here are some relevant reviews (the user has never seen them): {reviews}

Use these reviews as supporting information, but do not rely solely on them. If they are insufficient, answer based on your own expertise.

Here is the user's question for you to answer: {question}
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

    reviews = retriever.invoke(query.question)
    response = chain.invoke({"reviews": reviews, "question": query.question})

    return {"response": response}
