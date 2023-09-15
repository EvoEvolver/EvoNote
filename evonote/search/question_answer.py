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
import json
from typing import List

from evonote.model.chat import Chat
from evonote.notebook.notebook import Notebook
from evonote.search.fine_searcher import filter_notebook_in_group
from evonote.utils import robust_json_parse


class Plan:
    def __init__(self, objective, parent=None):
        self.objective = objective
        self.parent = parent
        self.sub_plans: List[Plan] = []
        self.finished = False


def imagine_answer(query: str, n_fragments=4):
    system_prompt = "You are part of a information searching system."
    prompt = f"""Give fragments of phrases that can be part of the answer to the query of search. 
    For example:
    "What is the capital of France?" -> "The capital of France is"
    "Importance of drink water" -> "Drinking water is important because"
    "How to make a cake" -> "To make a cake, you need"
    
    Give no more than {n_fragments} fragments in a JSON string with the key `fragments`.
    """
    chat = Chat(user_message=prompt, system_message=system_prompt)
    chat.add_user_message("Question:\n" + query)
    res = chat.complete_chat()
    res = robust_json_parse(res)
    return res


def search(query: str, notebook: Notebook):
    imagined_answer = imagine_answer(query)["fragments"]
    sub_notebook = notebook.get_sub_notebook_by_similarity(imagined_answer, top_k=10)
    sub_notebook = filter_notebook_in_group(sub_notebook,
                                            "The note answers the search query:" + query)
    return sub_notebook


def answer(question: str, notebook: Notebook):
    sub_notebook = search(question, notebook)
    prompt = f"""Here is some items obtained from a knowledge base. The context of the items are implied by their path.
    {sub_notebook.get_path_content_str_for_prompt()}"""
    chat = Chat(user_message=prompt)
    chat.add_user_message(f"""Please analyze and give an answer to the question: 
{question}

If the question can be answer by the items, give a JSON string with the key `analysis` and `answer`.
If not, give a JSON string with the key `analysis` and `reason`.
""")
    res = chat.complete_chat()
    res = robust_json_parse(res)
    return res


def analyze_question(question: str, context=""):
    system_prompt = "You are world-class analyzer for planning a question answering problem."
    prompt = f"""
Think step-by-step and analyze how to gather information for answering the following question."""
    if len(context) > 0:
        prompt += f"""\n{context}"""
    prompt += f"""    
- Each of your step must start with `Ask:` followed by a question.
- You only need to consider the next 3 steps.
Give your analysis by a JSON string with the following keys in order: `analysis`, `first step`, `second step`, `third step`. 
If you think the question can be answered by a memory listed above, give a JSON string with the key `analysis` and `answer`.
"""
    chat = Chat(user_message=prompt, system_message=system_prompt)
    chat.add_user_message("Question:\n" + question)
    res = chat.complete_chat()
    res = robust_json_parse(res)
    return res


def single_notebook_qa_agent(question: str, knowledge_base: Notebook):
    """
    :param question: The question
    :param notebook: The notebook to search
    :return: The answer
    """
    working_memory = Notebook("Working Notebook")
    old_plan = None
    exit_flag = False
    while not exit_flag:
        context = ""
        if old_plan is not None:
            context += "Here is your previous analysis plan. You have finished the first step of it.\n"
            context += json.dumps(old_plan, indent=1)
            context += "\n"

        if len(working_memory.children) > 1:
            context += "Here is your memory. Use them when plan and answer the question.\n"
            context += working_memory.get_path_content_str_for_prompt()
            context += "\n"

        with debug.display_chats():
            plan = analyze_question(question, context)

        if "first step" not in plan:
            return plan["answer"]
        first_step = plan["first step"]
        if first_step.startswith("Ask: "):
            old_plan = plan
            sub_question = first_step[4:]
            with debug.display_chats():
                ans = answer(sub_question, knowledge_base)
            if "answer" in ans:
                working_memory.root.s(sub_question).be(ans["answer"])
            else:
                working_memory.root.s(sub_question).be(
                    "You failed to find the answer of the question.")
        else:
            continue

    return None


if __name__ == "__main__":
    import evonote.debug as debug

    knowledge_base = Notebook("An introduction to the republic of Ganzi")
    knowledge_base.get_new_note_by_path(["Ganzi"]).be(
        "The republic of Ganzi is a country in the world.")
    knowledge_base.get_new_note_by_path(["Ganzi", "Capital"]).be(
        "Litang is the capital of the republic of Ganzi.")
    knowledge_base.get_new_note_by_path(["Ganzi", "Leaders"]).be(
        "There are many leaders in of the republic of Ganzi.")
    knowledge_base.get_new_note_by_path(["Ganzi", "Leaders", "President"]).be(
        "Dingzhen is the president of the republic of Ganzi.")
    knowledge_base.get_new_note_by_path(["Ganzi", "Leaders", "Vice President"]).be(
        "Ruike is the vice president of the republic of Ganzi.")
    knowledge_base.get_new_note_by_path(["Dingzhen", "Pet"]).be(
        "Zhenzhu the horse is the pet of the president of the republic of Ganzi.")
    knowledge_base.get_new_note_by_path(["Dingzhen", "Motto"]).be(
        "It's the mother who give me life.")

    # knowledge_base.show_notebook_gui()

    question = "Who is the pet of the president of the republic of Ganzi?"

    single_notebook_qa_agent(question, knowledge_base)
