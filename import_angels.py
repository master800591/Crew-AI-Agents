import csv

# Read data from CSV file
agents = []
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
                abilities=(f\"{row['Abilities']}\"),
                # tools=[],
                allow_delegation=False,
                verbose=True,
                llm=ollama_llama2_uncensored,
                function_calling_llm=ollama_solar,
                max_iter=6,  # Optional
                max_rpm=6, # Optional
    )"""

        agents.append(agent_str)

# Write data to agents.py file
with open('crews\Agents.py', 'a') as file:
    file.write('\n\n'.join(agents))