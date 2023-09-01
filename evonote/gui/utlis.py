
from hyphen.textwrap2 import fill
from hyphen import Hyphenator
h_en = Hyphenator('en_US')

def hypenate_texts(texts: str, line_width=40):
    if "\\" in texts:
        hyphenator = False
    else:
        hyphenator = h_en
    try:
        texts = fill(texts, width=line_width, use_hyphenator=hyphenator)
    except:
        texts = fill(texts, width=line_width, use_hyphenator=False)
    texts = texts.replace("\n", "<br>")
    return texts