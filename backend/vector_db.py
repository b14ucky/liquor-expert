from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import pandas as pd

db_location = "./vector_db"
batch_size = 100

embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url="http://ollama:11434")

vector_db = Chroma(
    collection_name="liquor_reviews",
    persist_directory=db_location,
    embedding_function=embeddings,
)

retriever = vector_db.as_retriever(
    search_kwargs={"k": 5},
)

if __name__ == "__main__":
    column_names = ["brand", "name", "reviews.text", "reviews.rating", "reviews.date"]
    df = pd.read_csv("liquor_reviews.csv")
    df = df[column_names]

    documents = []
    ids = []

    for i, row in df.iterrows():
        print(f"Creating documents: {int(str(i)) + 1}/{len(df)}", end="\r")
        document = Document(
            page_content=f"{row['brand']}, {row['name']}: {row['reviews.text']}",
            metadata={"rating": row["reviews.rating"], "date": row["reviews.date"]},
            id=str(i),
        )
        ids.append(str(i))
        documents.append(document)

    for i in range(0, len(documents), batch_size):
        print(f"Adding documents: {i}/{len(documents)}", end="\r")
        vector_db.add_documents(
            documents=documents[i : i + batch_size], ids=ids[i : i + batch_size]
        )
    print(f"Vector database succesfully created. Database location: {db_location}")
