from langchain_groq import ChatGroq
from langchain.agents import create_agent
from tools import calculator
from dotenv import load_dotenv

load_dotenv()


def create_agent_instance():
    llm_model = ChatGroq(
        model = "llama-3.3-70b-versatile",
        temperature=0
    )

    agent = create_agent(
        model=llm_model,
        tools = [calculator]
    )

    return agent