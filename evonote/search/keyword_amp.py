from typing import List

from evonote import EvolverInstance
from evonote.model.chat import Chat

system_message = "You should output everything concisely as if you are a computer " \
                 "program. "


def keyword_amplify(keywords: List[str], n_limit=3, use_cache=True):
    """Return a list of keywords that are similar to the given keyword."""
    cache_key = str(keywords)
    cache = EvolverInstance.read_cache(cache_key, "keyword_amplify")
    if use_cache and cache.is_valid():
        return cache._value

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
    cache.set_cache(res)
    return res


if __name__ == "__main__":
    keywords = ["quantum computing", "quantum algorithm"]
    print(keyword_amplify(keywords))
