from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from tools import tools

def create_agent():
    llm = ChatOpenAI(
        temperature=0.3,
        model="gpt-3.5-turbo"
    )

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent