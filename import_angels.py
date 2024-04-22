import csv
import random

# Read data from CSV file
agents = []

def get_randomint(min,max):
    return random.randint(min, max)


def Create_agent_angels():
    with open('CSV\Angels.csv') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            agent_name = row['Name'].replace(' ', '_').lower()

            agent_str = f"""
            def agent_{agent_name}(self):
                return Agent(
                    role="{row['Rank']}",
                    backstory=(f\"{row['Backstory']}\"),
                    goal=(f\"{row['Goal']}\"),
                    # abilities=(f\"{row['Abilities']}\"),
                    # tools=[],
                    allow_delegation=False,
                    verbose=Debug,
                    llm=ollama_llama2_uncensored,
                    function_calling_llm=ollama_solar,
                    max_iter={get_randomint(5,15)},  # Optional
                    max_rpm={get_randomint(5,15)}, # Optional
        )"""
            print(agent_str)
            agents.append(agent_str)


def Create_agent_executives():
    with open('CSV\Executives.csv') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            agent_name = row['Name'].replace(' ', '_').lower()

            agent_str = f"""
            def agent_{agent_name}(self):
                return Agent(
                    role="{row['Rank']}",
                    backstory=(f\"{row['Backstory']}\"),
                    goal=(f\"{row['Goal']}\"),
                    # abilities=(f\"{row['Abilities']}\"),
                    # tools=[],
                    allow_delegation=False,
                    verbose=Debug,
                    llm=ollama_llama2_uncensored,
                    function_calling_llm=ollama_solar,
                    max_iter={get_randomint(5,15)},  # Optional
                    max_rpm={get_randomint(5,15)}, # Optional
        )"""
            print(agent_str)

            agents.append(agent_str)

def Create_agent_Dept_managers():
    with open('CSV\Dept_managers.csv') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            agent_name = row['Name'].replace(' ', '_').lower()

            agent_str = f"""
            def agent_{agent_name}(self):
                return Agent(
                    role="{row['Rank']}",
                    backstory=(f\"{row['Backstory']}\"),
                    goal=(f\"{row['Goal']}\"),
                    # abilities=(f\"{row['Abilities']}\"),
                    # tools=[],
                    allow_delegation=False,
                    verbose=Debug,
                    llm=ollama_llama2_uncensored,
                    function_calling_llm=ollama_solar,
                    max_iter={get_randomint(5,15)},  # Optional
                    max_rpm={get_randomint(5,15)}, # Optional
        )"""
            print(agent_str)

            agents.append(agent_str)


def Create_agent_Employees():
    with open('CSV\Employees.csv') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            agent_name = row['Name'].replace(' ', '_').lower()

            agent_str = f"""
            def agent_{agent_name}(self):
                return Agent(
                    role="{row['Rank']}",
                    backstory=(f\"{row['Backstory']}\"),
                    goal=(f\"{row['Goal']}\"),
                    # abilities=(f\"{row['Abilities']}\"),
                    # tools=[],
                    allow_delegation=False,
                    verbose=Debug,
                    llm=ollama_llama2_uncensored,
                    function_calling_llm=ollama_solar,
                    max_iter={get_randomint(5,15)},  # Optional
                    max_rpm={get_randomint(5,15)}, # Optional
        )"""
            print(agent_str)
            agents.append(agent_str)




csv_files = ['CSV\Angels.csv', 'CSV\Executives.csv', 'CSV\Dept_managers.csv', 'CSV\Employees.csv']

def CREATE_LOAD_AGENTS():
    # Create agent_load.csv file
    agent_load_data = []
    for csv_file in csv_files:
        with open(csv_file) as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                agent_name = row['Name'].replace(' ', '_').lower()
                custom_agent_statement = f"custom_{agent_name} = agents.agent_{agent_name}()"
                print(custom_agent_statement)
                agent_load_data.append({'Custom_Agent_Statement': custom_agent_statement})

csv_file_path = 'CSV\agent_load.csv'

def CREATE_AGENTS_LIST():
    # Create agent_load.csv file
    agent_LIST_data = []
    for csv_file in csv_files:
        with open(csv_file) as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                agent_name = row['Name'].replace(' ', '_').lower()
                AGENT_NAME = f"agent_{agent_name}"
                print(AGENT_NAME)
                agent_LIST_data.append({AGENT_NAME})

csv_file_path = 'CSV\agent_LIST.csv'



if __name__ == "__main__":
    print('test')
    print(get_randomint(0,100))







    # Write data to agents.py file
    with open('crews\Agents.py', 'a') as file:
        file.write('\n\n'.join(agents))









#CODE THAT WILL BE NEEDED LATER ONCE I CREATE THE MORE ADVANCED LOGIC MAYBE WHO KNOWS. MAY CHANGE MY MIND.



    # def create_agent_from_csv(csv_file):
    # with open(csv_file) as file:
    #     reader = csv.DictReader(file, delimiter=';')
    #     for row in reader:
    #         agent_name = row['Name'].replace(' ', '_').lower()

    #         agent_str = f"""
    #         def agent_{agent_name}():
    #             return Agent(
    #                 role="{row['Rank']}",
    #                 backstory=(f\"{row['Backstory']}\"),
    #                 goal=(f\"{row['Goal']}\"),
    #                 allow_delegation=False,
    #                 verbose=Debug,
    #                 llm=ollama_llama2_uncensored,
    #                 function_calling_llm=ollama_solar,
    #                 max_iter={get_randomint(5, 15)},
    #                 max_rpm={get_randomint(5, 15)}
    #             )"""

    #         agents.append(agent_str)

