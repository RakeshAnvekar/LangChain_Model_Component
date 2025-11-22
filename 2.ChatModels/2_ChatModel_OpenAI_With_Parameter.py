from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#tepareture is the parameter that controls the randomness of the language models output
#Lower values(0.0 - 0.3) -> more deterministic
#Higher values(0.7 - 1.5) -> more random,creative and diverse 



model = ChatOpenAI(
                    model="gpt-4",
                    temperature=1.5,
                    max_completion_tokens=10 #max_completion_tokens tells model that the maximum token or words in the response from model
                    )
result= model.invoke("Write 5 line poem on cricket")


print(result.content)