# Testing HuggingFaceHub LLMs
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "HUGGINGFACEHUB_API_TOKEN"

from langchain_community.llms import HuggingFaceHub

llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":0, "max_length":64})

prompt = "What is the capital of France?"

print(llm(prompt))

# Output = paris