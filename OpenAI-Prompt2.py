# Chaining Template Sample
import os

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

from langchain_community.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

template = """
    You are a helpful assistant that translates {input_language} to {output_language}.
    Translate the following text
    {text}
"""

prompt = PromptTemplate.from_template(template)
llm = OpenAI(temperature=0.9)

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run(input_language="English", output_language="French", text="I adore Artificial Intelligence."))

# Output = J'adore l'Intelligence Artificielle.
