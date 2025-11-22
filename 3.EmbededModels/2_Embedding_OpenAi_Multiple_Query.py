from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-3-large",
                 dimensions=32)


documents=[
    "Delhi is the capital of india",
    "Bangalore is capital of Karnataka",
    "Belgam is the second capital of karnataka"
    ]
result=embedding.embed_documents(documents)
print(str(result))
