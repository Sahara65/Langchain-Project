#Invoking OpenAI through prompts - Sample
import os

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

from langchain_community.llms import OpenAI

llm = OpenAI(temperature=0)
prompt = "What would a good company name be for a company that makes AI solutions?"

result = llm.generate([prompt] * 1)
for company_name in result.generations:
    print(company_name[0].text)

# Output = "IntelliTech Solutions" or "AI Innovations Co."