from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
#HuggingFaceEndpoint is used if you are connecting to open sorce model using inference api
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()

# Create LLM Endpoint
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # Model repo
    task="text-generation",                       # Task type
)

# Wrap into Chat model
model = ChatHuggingFace(llm=llm)

# Invoke model
response = model.invoke("What is the capital of India?")

print(response.content)
