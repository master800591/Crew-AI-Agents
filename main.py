import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from decouple import config
import random

from textwrap import dedent
from Agents import CustomAgents
from Tasks import CustomTasks





# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search




from langchain.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()


os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")



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
        custom_asmodeus = agents.agent_asmodeus()
        custom_bael = agents.agent_bael()
        custom_ipos = agents.agent_ipos()
        custom_agiel = agents.agent_agiel()
        custom_vassago = agents.agent_vassago()
        custom_gamigin = agents.agent_gamigin()
        custom_marbas = agents.agent_marbas()
        custom_valefor = agents.agent_valefor()
        custom_amon = agents.agent_amon()
        custom_barbatos = agents.agent_barbatos()
        custom_paimon = agents.agent_paimon()
        custom_buer = agents.agent_buer()
        custom_gusion = agents.agent_gusion()
        custom_sitri = agents.agent_sitri()
        custom_beleth = agents.agent_beleth()
        custom_leraje = agents.agent_leraje()
        custom_eligos = agents.agent_eligos()
        custom_zepar = agents.agent_zepar()
        custom_botis = agents.agent_botis()
        custom_bathin = agents.agent_bathin()
        custom_sallos = agents.agent_sallos()
        custom_purson = agents.agent_purson()
        custom_marax = agents.agent_marax()
        custom_ipos = agents.agent_ipos()
        custom_aim = agents.agent_aim()
        custom_naberius = agents.agent_naberius()
        custom_glasya_labolas = agents.agent_glasya_labolas()
        custom_bune = agents.agent_bune()
        custom_ronove = agents.agent_ronove()
        custom_berith = agents.agent_berith()
        custom_astaroth = agents.agent_astaroth()
        custom_forneus = agents.agent_forneus()
        custom_foras = agents.agent_foras()
        custom_asmoday = agents.agent_asmoday()
        custom_gaap = agents.agent_gaap()
        custom_furfur = agents.agent_furfur()
        custom_marchosias = agents.agent_marchosias()
        custom_stolas = agents.agent_stolas()
        custom_phenex = agents.agent_phenex()
        custom_halphas = agents.agent_halphas()
        custom_malphas = agents.agent_malphas()
        custom_raum = agents.agent_raum()
        custom_focalor = agents.agent_focalor()
        custom_vepar = agents.agent_vepar()
        custom_sabnock = agents.agent_sabnock()
        custom_shax = agents.agent_shax()
        custom_vine = agents.agent_vine()
        custom_bifrons = agents.agent_bifrons()
        custom_vual = agents.agent_vual()
        custom_haagenti = agents.agent_haagenti()
        custom_crocell = agents.agent_crocell()
        custom_furcas = agents.agent_furcas()
        custom_balam = agents.agent_balam()
        custom_alloces = agents.agent_alloces()
        custom_caim = agents.agent_caim()
        custom_murmur = agents.agent_murmur()
        custom_orobas = agents.agent_orobas()
        custom_gremory = agents.agent_gremory()
        custom_ose = agents.agent_ose()
        custom_amy = agents.agent_amy()
        custom_orias = agents.agent_orias()
        custom_vapula = agents.agent_vapula()
        custom_zagan = agents.agent_zagan()
        custom_volac = agents.agent_volac()
        custom_andras = agents.agent_andras()
        custom_forneus = agents.agent_forneus()
        custom_asmodeus = agents.agent_asmodeus()
        custom_ayperos = agents.agent_ayperos()
        custom_naberius = agents.agent_naberius()
        custom_castiel = agents.agent_castiel()
        custom_azazel = agents.agent_azazel()
        custom_raphael = agents.agent_raphael()
        custom_gabriel = agents.agent_gabriel()
        custom_michael = agents.agent_michael()
        custom_uriel = agents.agent_uriel()
        custom_sariel = agents.agent_sariel()
        custom_lucifer = agents.agent_lucifer()
        custom_zeus = agents.agent_zeus()
        custom_athena = agents.agent_athena()
        custom_thor = agents.agent_thor()
        custom_freya = agents.agent_freya()
        custom_cernunnos = agents.agent_cernunnos()
        custom_isis = agents.agent_isis()
        custom_diana = agents.agent_diana()
        custom_brigid = agents.agent_brigid()
        custom_odin = agents.agent_odin()
        custom_hecate = agents.agent_hecate()
        custom_lugh = agents.agent_lugh()
        custom_persephone = agents.agent_persephone()
        custom_anubis = agents.agent_anubis()
        custom_morrigan = agents.agent_morrigan()
        custom_freyr = agents.agent_freyr()
        custom_bastet = agents.agent_bastet()
        custom_demeter = agents.agent_demeter()
        custom_dagda = agents.agent_dagda()
        custom_pan = agents.agent_pan()
        custom_hera = agents.agent_hera()
        custom_brigantia = agents.agent_brigantia()
        custom_aphrodite = agents.agent_aphrodite()
        custom_loki = agents.agent_loki()
        custom_artemis = agents.agent_artemis()
        custom_cernach = agents.agent_cernach()
        custom_sif = agents.agent_sif()
        custom_maeve = agents.agent_maeve()
        custom_jupiter = agents.agent_jupiter()
        custom_juno = agents.agent_juno()
        custom_neptune = agents.agent_neptune()
        custom_minerva = agents.agent_minerva()
        custom_mars = agents.agent_mars()
        custom_venus = agents.agent_venus()
        custom_mercury = agents.agent_mercury()
        custom_pluto = agents.agent_pluto()
        custom_ceres = agents.agent_ceres()
        custom_vesta = agents.agent_vesta()
        custom_bacchus = agents.agent_bacchus()
        custom_apollo = agents.agent_apollo()
        custom_diana = agents.agent_diana()
        custom_vulcan = agents.agent_vulcan()
        custom_janus = agents.agent_janus()

        # Custom tasks include agent name and variables as input



        #reading tasks 
        custom_task_1 = tasks.task_1_name(
            custom_agent_1,
            self.var1,
            self.var2,
        )

        custom_task_2 = tasks.task_2_name(
            custom_agent_2,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[custom_agent_1, custom_agent_2],
            tasks=[custom_task_1, custom_task_2],
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