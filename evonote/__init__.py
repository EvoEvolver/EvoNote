import os
from evonote.core import EvoCore

import openai
EvolverInstance = EvoCore()
from evonote.core.evolver import show, evolve, inline
openai.api_key = os.getenv("OPENAI_API_KEY")