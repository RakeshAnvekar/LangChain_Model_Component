from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4")
result= model.invoke("What is the capital of india")
print(result) # in result its not just only the plan text,we get some additilan data as meta data

print(result.content)