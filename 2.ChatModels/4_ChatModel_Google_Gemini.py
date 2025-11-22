from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="",
                             temperature=1,
                             max_output_tokens=100
                             )

response = model.invoke("which is best time to visit Goa")
print(response.content)