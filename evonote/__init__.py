import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is None:
    print("You must set environment variable OPENAI_API_KEY before use")
    raise Exception("OPENAI_API_KEY is not set")

"""
:module:
This module is for knowledge base construction 
"""