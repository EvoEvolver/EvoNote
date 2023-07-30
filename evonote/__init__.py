import os
from evonote.file_helper import EvoCore
import openai

EvolverInstance = EvoCore()
openai.api_key = os.getenv("OPENAI_API_KEY")
