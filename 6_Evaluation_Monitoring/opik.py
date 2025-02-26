import sys
import os

# Remove local script from path to avoid conflicts
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
if script_dir in sys.path:
    sys.path.remove(script_dir)

import opik
from opik import track
from langchain_ollama import ChatOllama

opik.configure()

@track
def call_ollama(prompt):
    llm = ChatOllama(model="deepseek-r1:1.5b", temperature=0.8)
    return llm.invoke(prompt)

result = call_ollama("Hi!!")
print(result.content)
