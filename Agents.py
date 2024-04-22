from crewai import Agent
import os
from langchain_community.llms import Ollama

Debug=True

ollama_openhermes = Ollama(model="openhermes")
ollama_solar = Ollama(model="solar")
ollama_alfred = Ollama(model="alfred")
ollama_llama_pro = Ollama(model="llama-pro")
ollama_llama2_uncensored = Ollama(model="llama2-uncensored")
ollama_stable_code = Ollama(model="stable-code")
ollama_nomic_embed = Ollama(model="nomic-embed-text")
ollama_codellama = Ollama(model="codellama")

class CustomAgents:
    def __init__(self):

