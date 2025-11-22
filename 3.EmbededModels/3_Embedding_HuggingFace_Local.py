from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv

load_dotenv()

embedding=HuggingFaceEmbeddings(model="sentence-transformall-miniLM-L6-v2")

text="Delhi is the capital of india"

vector=embedding.aembed_query(text)
print(str(vector))