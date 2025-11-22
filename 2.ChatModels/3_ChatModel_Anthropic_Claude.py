from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()


model= ChatAnthropic(
                model_name="claude-3-5-sonnet-20241022",
                temperature=1,
                max_tokens_to_sample=50
                )

result = model.invoke("Tell me something about india")
print(result.content)