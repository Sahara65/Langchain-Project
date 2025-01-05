# Plan and Execute Agents
import os
from tabnanny import verbose

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"
os.environ["SERPAPI_API_KEY"] = "SERPAPI_API_KEY"


from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain_experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from langchain_community.utilities import SerpAPIWrapper
from langchain.chains import LLMMathChain
from langchain.tools import Tool

search = SerpAPIWrapper()
llm = OpenAI(temperature=0)
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math"
    )]

model = ChatOpenAI(temperature=0)
planner = load_chat_planner(model)
executor = load_agent_executor(model, tools, verbose=True)
agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

agent.run("What is the weather in NYC? What is that number times 1?")

# Output
# > Finished chain.
# *****
#
# Step: Provide the user with the weather in NYC and the result of the multiplication.
#
# Response: The current weather in New York City is 32°F with 0% precipitation, 38% humidity, and 9 mph wind speed. It is partly cloudy. The result of multiplying the temperature in NYC by 1 is 32°F.
#
# > Entering new AgentExecutor chain...
# Thought: The original question from the user is missing, but based on the previous steps, it seems like they were asking for the current weather in New York City and the result of multiplying the temperature by 1.
#
# Action:
# ```
# {
#   "action": "Final Answer",
#   "action_input": "The current weather in New York City is 32°F with 0% precipitation, 38% humidity, and 9 mph wind speed. It is partly cloudy. The result of multiplying the temperature in NYC by 1 is 32°F."
# }
# ```
#
# > Finished chain.
# *****
#
# Step: Given the above steps taken, please respond to the user's original question.
#
#
# Response: The current weather in New York City is 32°F with 0% precipitation, 38% humidity, and 9 mph wind speed. It is partly cloudy. The result of multiplying the temperature in NYC by 1 is 32°F.
# > Finished chain.