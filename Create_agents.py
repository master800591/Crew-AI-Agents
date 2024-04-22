import csv
import random


# create global Vars
csv_files = ['CSV\Angels.csv', 'CSV\Executives.csv', 'CSV\Dept_managers.csv', 'CSV\Employees.csv']
agent_load_data = []
agent_LIST_data = []
agents = []





# creates random int within the min max range given.
def get_randomint(min,max):
    return random.randint(min, max)



# creates the agents and adds them. have 3 functions so they can have different presets for now.
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




# creates the load agents. used in the main.py to load agents 
def CREATE_LOAD_AGENTS():
    # Create agent_load.csv file
    for csv_file in csv_files:
        with open(csv_file) as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                agent_name = row['Name'].replace(' ', '_').lower()
                custom_agent_statement = f"custom_{agent_name} = agents.agent_{agent_name}()"
                print(custom_agent_statement)
                agent_load_data.append(custom_agent_statement)

csv_file_path = 'CSV\Agent_load.csv'





# creates list of agents names. just wanted it may need it later so why not. more data more better!!!!
def CREATE_AGENTS_LIST():
    # Create agent_load.csv file
    for csv_file in csv_files:
        with open(csv_file) as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                agent_name = row['Name'].replace(' ', '_').lower()
                AGENT_NAME = f"agent_{agent_name}"
                print(AGENT_NAME)
                agent_LIST_data.append(AGENT_NAME)



# runs the program have some test stuff and other goodies.
if __name__ == "__main__":
    print('test')
    print(get_randomint(0,100))
    Create_agent_angels()
    Create_agent_Employees()
    Create_agent_Dept_managers()
    Create_agent_executives()
    CREATE_LOAD_AGENTS()
    CREATE_AGENTS_LIST()
    # Write data to agents.py file
    with open('Agents.py', 'a') as file:
        file.write('\n\n'.join(agents))
    with open('CSV\Agent_load.csv', 'a') as file:
        file.write('\n'.join(agent_load_data))
    with open('CSV\Agent_LIST.csv', 'a') as file:
        file.write('\n'.join(agent_LIST_data))









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

