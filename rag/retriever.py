from langchain_huggingface import (HuggingFaceEmbeddings)

from langchain_chroma import Chroma

CHROMA_PATH = "database/chroma_db"

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma(persist_directory = CHROMA_PATH, embedding_function=embedding)

retriever = db.as_retriever()

search_kwargs = {"k": 5}

def get_context(query):
    
    docs = retriever.invoke(query)

    context = "/n".join(
        [doc.page_content for doc in docs]
    )
    return context