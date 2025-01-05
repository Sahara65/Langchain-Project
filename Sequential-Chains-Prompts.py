# Sequential Chains
import os

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

llm = OpenAI(temperature=0)
template = "What is a good name for a company that makes {product}?"
first_prompt = PromptTemplate.from_template(template)
first_chain = LLMChain(llm=llm, prompt=first_prompt)

second_template = "Write a 20 words description for the following company: {company_name}"
second_prompt = PromptTemplate.from_template(second_template)
second_chain = LLMChain(llm=llm, prompt=second_prompt)

overall_chain = SimpleSequentialChain(chains=[first_chain, second_chain], verbose=True)
review = overall_chain.invoke("colorful socks")
print(review)

# Output
# 1. "Rainbow Threads" or "Vibrant Socks Co."
#
# 2. "Rainbow Threads offers a colorful selection of high-quality socks, adding a touch of vibrancy to your everyday wardrobe."
#
# Finished chain.
# {'input': 'colorful socks',
# 'output': '\n\n"Rainbow Threads offers a colorful selection of high-quality socks, adding a touch of vibrancy to your everyday wardrobe."'}