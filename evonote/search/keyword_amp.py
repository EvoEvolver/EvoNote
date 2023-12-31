from typing import List

from evonote.file_helper.cache_manage import cached_function
from evonote.model.chat import Chat

system_message = "You should output everything concisely as if you are a computer " \
                 "program. "

@cached_function("keyword_amplify")
def keyword_amplify(keywords: List[str], n_limit=3):
    """Return a list of keywords that are similar to the given keyword."""

    prompt = "You are a program that generates related keywords based on given keywords " \
             "to help the search engine find related logs. "
    prompt += "\nExisting keywords: " + "\n".join(keywords)
    chat = Chat(user_message=prompt, system_message=system_message)
    chat.add_user_message(
        f"Output at most {n_limit} related keywords. Separate each keyword by newline.")
    res = chat.complete_chat()
    res = res.split("\n")
    res = [r.strip() for r in res]
    res = [r for r in res if len(r) > 0]
    return res


if __name__ == "__main__":
    keywords = ["quantum computing", "quantum algorithm"]
    print(keyword_amplify(keywords))
