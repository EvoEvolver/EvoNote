from hyphen import Hyphenator
from hyphen.textwrap2 import fill

h_en = Hyphenator('en_US')


def hypenate_texts(texts: str, line_width=40):
    """
    Hypenate texts. Add <br> to the end of each line.
    :param texts: The texts to be hypenated
    :param line_width: The width of each line
    :return: The hypenated texts
    """
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
