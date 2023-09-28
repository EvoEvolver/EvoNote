import re
import html2text
from evonote.data_cleaning.document import Document


def html_to_markdown(html: str):
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    abs = re.findall(r'''<meta name="description" content="(.+?)">''', html, re.DOTALL)
    if abs:
        abs=abs[0].strip()
    else:
        abs=""
    title = re.findall(r"<title>(.+?)</title>", html, re.DOTALL)
    author = re.findall(r'''<meta name="author" content="(.+?)">''', html, re.DOTALL)
    markdown = h.handle(html)
    # markdown = re.sub(r"# (.+?)#", r"## \1", markdown)

    return markdown, {"abstract": abs, "title": title, "author": author}


def process_section_level(section_level, curr_level, doc: Document):
    if section_level == curr_level:
        content, subsections = divide_text_into_section(section_level, doc.content)
        doc.content = content
        for subsection in subsections:
            doc.sections.append(Document(subsection[0], subsection[1].strip(), []))
    else:
        for i, section in enumerate(doc.sections):
            process_section_level(section_level, curr_level + 1, section)



# need refactor
def divide_text_into_section(section_level, text):
    searched = r"((" + ("#" * (section_level+1)) + "))" + r" (.+?)#"
    # find first section
    m = re.search(searched, text)
    if m:
        content = text[:m.start()]
        text = text[m.start():]
    else:
        return text, []

    sections = []
    for m in re.finditer(searched, text):
        # get the section title
        section_title = m.group(3)
        # print(section_title)
        # get the section content
        section_content = text[m.end():]
        # find the end of the section content
        end = re.search(searched, section_content)
        if end:
            section_content = section_content[:end.start()]
        sections.append((section_title, section_content))

    return content, sections


def process_html_sections(html: str, meta: dict):
    doc = Document(meta["title"], html, [])
    for i in range(0, 4):
        process_section_level(i, 0, doc)
    doc.content = ""
    return doc


def process_html_into_standard(html: str):
    mkd, meta = html_to_markdown(html)
    doc = process_html_sections(mkd, meta)
    return doc, meta


if __name__ == "__main__":
    from pprint import pprint
    from evonote.testing.sample_html import sample_html
    # converted_mkd = html_to_markdown(sample_html)
    # with open("test.md", "w") as f:
    #     f.writelines(converted_mkd)
    doc, meta = process_html_into_standard(sample_html)
