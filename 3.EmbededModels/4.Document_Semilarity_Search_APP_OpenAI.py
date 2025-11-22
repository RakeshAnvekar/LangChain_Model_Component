
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-3-large",
                           dimensions=300
                           )

documents = [
    "MS Dhoni is a former Indian cricketer and captain of the national team.",
    "Sachin Tendulkar is a former Indian cricketer known as the 'God of Cricket'.",
    "Rohit Sharma is an Indian cricketer and current captain of the national team.",
    "Jasprit Bumrah is an Indian cricketer known for his fast bowling."
]

query='tell me about Sachin'

doc_Embeddngs=embedding.embed_documents(documents)

query_Embedding=embedding.embed_query(query)

scrores=cosine_similarity([query_Embedding],doc_Embeddngs)[0] ## we need to pass as the 2d

index,score=sorted(list(enumerate(scrores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity Score is:", score)


