# Human as a tool sample
import os

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

from langchain_openai import ChatOpenAI, OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools

llm = ChatOpenAI(temperature=0)
math_llm = OpenAI(temperature=0)
tools = load_tools(["human", "llm-math"], llm=math_llm)

agent_chain = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent_chain.run("What is my friend's first name? And what is 2 raised to the .123234 power?")

# Output
# > Entering new AgentExecutor chain...
# I can't determine your friend's first name, but I can calculate 2 raised to the power of .123234.
# Action: Calculator
# Action Input: 2, .123234
# Observation: Answer: 2.123234
# Thought:I have the answer for 2 raised to the power of .123234, but I still can't determine your friend's first name.
# Action: human
# Action Input: What is your friend's first name?
#
# What is your friend's first name?
# Sarah
#
# Observation: Sarah
# Thought:I now know the final answer
# Final Answer: 2.123234, Sarah
#
# > Finished chain.