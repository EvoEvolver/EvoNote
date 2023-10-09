Workflow:

0. Initialize the objective stack

1. Get objective from top -> Plan -> Search

Satisfied?

2. No -> Ask for help -> Gain knowledge -> Go to 1
3. Yes -> Execute with the result -> Update objectives -> Go to 1

Atomic operations:

1. Search in notetree
2. Execute action in the retrieved note
3. Ask (and update in-prompt memory and notetree) (I doubt this can be removed from atomic)
4. Memo (update in-prompt memory)
5. Planing: Make a complex objective into atomic operations

Operation arguments:

1. Search in notetree: notetree, indexing, query, query_type: similarity | question
2. Execute action in the retrieved note: note, action
3. Ask: question
4. Memo: content
5. Planning: delete, add, update

Important question: adding memo is easy, but how to delete memo that's not useful?

Output format:

1. Ask the llm to answer with natural language with an expensive model and then parse the output with a cheap model.
2. Ask the llm to choose from atomic operations and start the answer with "I want to xxx. In detail, xxx"

Planning:

1. Prompt to ask the agent break down the objective into atomic operations when possible. When not possible, break down
   the objective into sub-objectives.
2. Prompt to ask the agent give an analysis first. Then retrieve notes and ask whether the analysis is still correct. If
   so, pass. Else, ask the agent to update the analysis. Repeat until the analysis is consistent with the retrieved
   notes. Or the agent start to ask for help.
3. After getting the self-consistent analysis, ask the agent to update the objective stack. Then ask for doing a new
   atomic operation.

Search:

1. The search should be done with a special searching agent. The input is the searching objective. A special notetree
   for how to search might be used.
2. The searching agent will break down the objective into further sub-objectives. The sub-objectives are finer and more
   specific than the original objective.
3. The sub-objectives might include what index to use?, is new index needed?.
4. Some special tools might be provided: like keyword amplification, filtering by llm.

Execute:

1. Because the note is already retrieved, the execution is easy. The agent just need to fill the parameters.
2. In the future, the agent might be able to memo by creating variables. In this case, we might need to provide a list
   of available variables.

Roadmap from making a simple demo.