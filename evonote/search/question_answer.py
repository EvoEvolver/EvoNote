"""
# Question Answering
## First round similarity search
- Keyword Extraction & Amplification
- Imagine the answer
- Get the top k similar notes
## Analyze the results
- Initialize a new notebook
Put the results in a stack. Whenever the stack is non-empty, do the following:
- Judge whether they are useful. If so, add them to the new notebook
- Judge whether their children, siblings, parents are useful. If so, try to add them to the stack
"""
