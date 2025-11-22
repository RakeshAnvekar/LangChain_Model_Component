from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
#HuggingFacePipeline is used if you are downlaoding the model in local machine
from dotenv import load_dotenv
import os


# Load API Key from .env
load_dotenv()

os.environ['HF_HOME']='D:/hggingface_cache'

# Create LLM Endpoint
llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
        )
)

# Wrap into Chat model
model = ChatHuggingFace(llm=llm)

# Invoke model
response = model.invoke("What is the capital of India?")

print(response.content)
