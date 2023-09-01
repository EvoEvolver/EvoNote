from evonote.core.note import Note, make_notebook_root
from evonote.core.notebook import Notebook
from evonote.writer.writer_build_from import digest_content, set_notes_by_digest
import concurrent.futures
from evonote.file_helper.evolver import save_cache


def notebook_from_doc(doc, meta) -> Notebook:
    root, notebook = make_notebook_root(meta["title"])
    build_from_sections(doc, root)
    root.related_info["annotation"] = "This is a notebook of the paper \"" + meta[
        "title"] + "\"."
    return notebook


def build_from_sections(doc, root: Note):
    root.be(doc["content"])
    for section in doc["sections"]:
        build_from_sections(section, root.s(section["title"]))


def digest_all_descendants(notebook: Notebook):
    all_notes = notebook.get_all_notes()
    all_notes = [note for note in all_notes if len(note.content) > 0]
    # digests = []
    digest_content_with_cache = lambda x: digest_content(x, use_cache=True)
    finished = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for note, digest in zip(all_notes, executor.map(digest_content_with_cache,
                                                        [note.content for note in
                                                         all_notes])):
            # digests.append(digest)
            set_notes_by_digest(note, digest)
            note.related_info["original text"] = note.content
            note.content = ""
            finished += 1
        if finished % 5 == 4:
            print("digest received ", finished, "/", len(all_notes))
            save_cache()
    save_cache()
