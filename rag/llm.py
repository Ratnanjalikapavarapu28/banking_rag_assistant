from langchain_community.llms import Ollama

llm = Ollama(model="llama3")
def ask_llm(question, context):

    prompt = f"""
    you are a Banking Assistant.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = llm.invoke(prompt)

    return response 