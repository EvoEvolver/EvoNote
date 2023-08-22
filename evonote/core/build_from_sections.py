from evonote import EvolverInstance
from evonote.core.note import Note, make_notebook_root
from evonote.core.writer_build_from import digest_content, set_notes_by_digest
import concurrent.futures
from evonote.file_helper.evolver import save_cache


def notebook_from_doc(doc, meta):
    root = make_notebook_root(meta["title"])
    build_from_sections(doc, root)
    return root


def build_from_sections(doc, root: Note):
    root.be(doc["content"])
    for section in doc["sections"]:
        build_from_sections(section, root.s(section["title"]))


def digest_all_descendants(root: Note, caller_path=None):
    if caller_path is None:
        caller_path = EvolverInstance.get_caller_path()
    all_notes = root.get_descendants()
    all_notes = [note for note in all_notes if len(note.content) > 0]
    digests = []
    digest_content_with_cache = lambda x: digest_content(x, use_cache=True,
                                                         caller_path=caller_path)
    finished = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for note, digest in zip(all_notes, executor.map(digest_content_with_cache,
                                                        [note.content for note in
                                                         all_notes])):
            digests.append(digest)
            set_notes_by_digest(note, digest)
            note.content = ""
            set_notes_by_digest(note, digest)
            finished += 1
            print("received ", finished, "/", len(all_notes))
        if finished % 5 == 4:
            save_cache()
    save_cache()
