import os
from crewai import Agent, Task, Crew
# Optional OpenAI import (commented out for Ollama setup)
# from langchain_openai import ChatOpenAI
from decouple import config
import random

from textwrap import dedent
from Agents import CustomAgents
from Tasks import CustomTasks





# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search




# Optional: Search tool (commented out for now)
# from langchain_community.tools import DuckDuckGoSearchRun  
# search_tool = DuckDuckGoSearchRun()


# Optional: Configuration for environment variables
try:
    from decouple import config
    # Only set if environment variables are provided
    if config("OPENAI_API_KEY", default=""):
        os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
    if config("OPENAI_ORGANIZATION_ID", default=""):
        os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")
except ImportError:
    print("Note: python-decouple not available, skipping environment variable setup")
except Exception as e:
    print(f"Note: Could not load environment variables: {e}")



Angels_list =[]

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        # Using just a few agents for the example
        custom_asmodeus = agents.agent_asmodeus()
        custom_bael = agents.agent_bael()
        custom_ipos = agents.agent_ipos()

        # Create tasks for these agents
        custom_task_1 = tasks.task_1_name(
            custom_asmodeus,
            self.var1,
            self.var2,
        )

        custom_task_2 = tasks.task_2_name(
            custom_bael,
        )

        custom_task_3 = tasks.general_assistance_task(
            custom_ipos,
            f"Provide insights and analysis for {self.var1} {self.var2}"
        )

        # Define your custom crew here
        crew = Crew(
            agents=[custom_asmodeus, custom_bael, custom_ipos],
            tasks=[custom_task_1, custom_task_2, custom_task_3],
            verbose=True,
        )

        result = crew.kickoff()
        return result










# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    First_name = input("""Enter first name: """)
    Last_name = input("""Enter last name: """)
    User_angels= random.choice(Angels_list)

    custom_crew = CustomCrew(First_name,Last_name)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)