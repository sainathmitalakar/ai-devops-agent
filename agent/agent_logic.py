import os
from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from utils import get_logs, analyze_health

class DevOpsAIAgent:
    def __init__(self):
        llm = OpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))
        tools = [
            Tool(name="GetLogs", func=get_logs, description="Fetch system logs"),
            Tool(name="HealthCheck", func=analyze_health, description="Check system health status"),
        ]
        self.agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

    def run(self):
        print("Ask the AI Agent a DevOps-related question (type 'exit' to quit):")
        while True:
            user_input = input("> ")
            if user_input.lower() == "exit":
                break
            response = self.agent.run(user_input)
            print(f"AI Agent: {response}")