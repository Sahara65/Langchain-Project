# Action Agents
import os

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

from langchain_openai import OpenAI
from langchain.agents import initialize_agent, load_tools
# from langchain_community.agent_toolkits import load_tools

prompt = "Who is currently the governor of New York? What is their birth year times 1?"

llm = OpenAI(temperature=0)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

agent.run(prompt)


# Output
# > Entering new AgentExecutor chain...
#  I should use Wikipedia to find the current governor of New York
# Action: wikipedia
# Action Input: Governor of New York
# Observation: Page: Governor of New York
# Summary: The governor of New York is the head of government of the U.S. state of New York. The governor is the head of the executive branch of New York's state government and the commander-in-chief of the state's military forces. The governor has a duty to enforce state laws and the power to either approve or veto bills passed by the New York Legislature, to convene the legislature and grant pardons, except in cases of impeachment and treason. The governor of New York is the highest paid governor in the country.
# The current governor is Kathy Hochul, a member of the Democratic Party who took office on August 24, 2021, following the resignation of Andrew Cuomo. She was elected to a full term in 2022.
#
# Page: List of governors of New York
# Summary: The governor of New York is the head of government of the U.S. state of New York, the head of the executive branch of New York's state government, and the commander-in-chief of the state's military forces. The officeholder has a duty to enforce state laws, to convene the New York State Legislature, the power to either approve or veto bills passed by the legislature, as well as to grant pardons, except in cases of treason and impeachment.
# Fifty-seven people have served as state governor, four of whom served non-consecutive terms (George Clinton, DeWitt Clinton, Horatio Seymour, and Al Smith); the official numbering lists each governor only once. There has only been one female governor so far: Kathy Hochul. This numbering includes one acting governor: the lieutenant governor who filled the vacancy after the resignation of the governor, under the 1777 Constitution. The list does not include the prior colonial governors nor those who have acted as governor when the governor was out of state, such as Lieutenant Governor Timothy L. Woodruff during Theodore Roosevelt's vice presidential campaign in 1900, or Acting Speaker of the New York State Assembly Moses M. Weinstein, who acted as governor for 10 days in 1968 while the governor, the lieutenant governor and the senate majority leader were out of the state, attending the Republican National Convention in Miami.
# Four men have become president of the United States after serving as governor of New York: Martin Van Buren, Grover Cleveland, Theodore Roosevelt, and Franklin D. Roosevelt, and six were vice president. Van Buren and Theodore Roosevelt held both offices. Numerous Governors have also sought the Presidency, and won their party's respective nomination, but lost the general election, such as Al Smith, Samuel J. Tilden, Horatio Seymour, Thomas E. Dewey, and Charles Evans Hughes. Two governors have been chief justice: John Jay held that position when he was elected governor in 1795, and Charles Evans Hughes became chief justice in 1930, two decades after leaving the governorship.
# The longest-serving governor was the first, George Clinton, who first took office on July 30, 1777, and served seven terms in two different periods, totaling just under 21 years in office. As 18 of those years were consecutive, Clinton also served the longest consecutive period in office for a New York governor. Charles Poletti had the shortest term, serving 29 days following the resignation of the previous governor, Herbert H. Lehman in 1942. Lehman was the state's first Jewish governor; David Paterson was the first African American governor of New York, and the first legally blind governor as well. Paterson is only the fourth African American to hold the office of governor in the United States. The current governor is Democrat Kathy Hochul, the state's first female governor, who assumed the office on August 24, 2021, upon the resignation of Andrew Cuomo. Hochul went on to be elected as governor for a full term, after beating Republican Lee Zeldin in the 2022 election.
#
# Page: Lieutenant Governor of New York
# Summary: The lieutenant governor of New York is a constitutional office in the executive branch of the Government of the State of New
# Thought: Now that I know the current governor of New York is Kathy Hochul, I can use the Calculator to find her birth year and multiply it by 1
# Action: Calculator
# Action Input: Kathy Hochul's birth year * 1
# Observation: Answer: 1958
# Thought: I now know the final answer
# Final Answer: 1958
#
# > Finished chain.