from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import (
   HuggingFaceEmbeddings
)
from langchain_chroma import Chroma
import os
Chroma_PATH = "database/chroma_db"
def ingest_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=Chroma_PATH
    )
    
    return "✅ PDF ingested and indexed successfully"