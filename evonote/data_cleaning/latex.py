import re

from evonote.data_cleaning.document import Document


def latex_to_markdown(latex: str):
    # replace \textit{xxx} with *xxx*
    res = re.sub(r"\\textit{(.+?)}", r"*\1*", latex)
    # replace \textbf{xxx} with **xxx**
    res = re.sub(r"\\textbf{(.+?)}", r"**\1**", res)
    # remove \cite{xxx}
    res = re.sub(r"\\cite{.+?}", "[citations]", res)
    # replace \footnote{xxx} with (xxx)
    res = re.sub(r"\\footnote{(.+?)}", r"(\1)", res)
    # replace \item with -
    res = re.sub(r"\\item", "-", res)
    # remove \begin{enumerate} and \end{enumerate}
    res = re.sub(r"\\(begin|end){(enumerate|iterate)}", "\n", res)
    # remove \label{xxx}
    res = re.sub(r"\\label{.+?}", "", res)
    # remove lines starting with %
    res = re.sub(r"\n%.*", "", res)
    # replace more than two \n to two \n
    res = re.sub(r"\n{3,}", "\n\n", res)
    return res


def divide_text_into_section(section_level, tex):
    searched = r"((\\" + ("sub" * section_level) + "section)|paragraph)" + r"\*?{(.+?)}"
    # find first section
    m = re.search(searched, tex)
    if m:
        content = tex[:m.start()]
        tex = tex[m.start():]
    else:
        return tex, []
    sections = []
    for m in re.finditer(searched, tex):
        # get the section title
        section_title = m.group(3)
        # get the section content
        section_content = tex[m.end():]
        # find the end of the section content
        end = re.search(searched, section_content)
        if end:
            section_content = section_content[:end.start()]
        sections.append((section_title, section_content))

    return content, sections


def process_section_level(section_level, curr_level, doc: Document):
    if section_level == curr_level:
        content, subsections = divide_text_into_section(section_level, doc.content)
        doc.content = content
        for subsection in subsections:
            doc.sections.append(Document(subsection[0], subsection[1].strip(), []))
    else:
        for i, section in enumerate(doc.sections):
            process_section_level(section_level, curr_level + 1, section)


def process_latex_sections(tex: str):
    abs = re.findall(r"\\begin{abstract}(.+?)\\end{abstract}", tex, re.DOTALL)[0].strip()
    title = re.findall(r"\\title{(.+?)}", tex, re.DOTALL)
    if len(title) > 0:
        title = title[0].strip()
    else:
        title = ""
    doc = Document(title, tex, [])
    for i in range(0, 4):
        process_section_level(i, 0, doc)
    # delete the content before first section in the root
    # because it's usually irrelevant
    doc.content = ""
    return doc, {"abstract": abs, "title": title}


def process_latex(latex: str):
    """
    Convert latex to markdown
    :param latex:
    :return:
    """

    # find \begin{abstract} and \end{abstract} and extract the text between
    abs = re.findall(r"\\begin{abstract}(.+?)\\end{abstract}", latex, re.DOTALL)

    # remove \begin{xxx}
    res = re.sub(r"\\begin{.+?}", "", latex)
    res = re.sub(r"\\end{.+?}", "", res)

    return res


def to_paragraphs(text):
    # separate by \n\n
    paragraphs = text.split("\n\n")
    # remove empty paragraphs
    paragraphs = [p.strip() for p in paragraphs]
    paragraphs = [p for p in paragraphs if len(p) > 0]
    return paragraphs


def process_latex_into_standard(tex: str):
    tex = latex_to_markdown(tex)
    doc, meta = process_latex_sections(tex)
    return doc, meta


if __name__ == "__main__":
    from pprint import pprint
    from evonote.testing.sample_paper import sample_paper

    tex = sample_paper
    doc, meta = process_latex_into_standard(tex)
    pprint(doc)
