from __future__ import annotations
import plotly.graph_objects as go
from hyphen.textwrap2 import fill
from hyphen import Hyphenator
from typing import TYPE_CHECKING

from evonote.gui.utlis import hypenate_texts

if TYPE_CHECKING:
    from evonote.core.note import Note
    from evonote.core.notebook import Notebook

h_en = Hyphenator('en_US')


def draw_treemap(root: Note, notebook: Notebook = None):
    if notebook is None:
        notebook = root.default_notebook
    labels = []
    parents = []
    values = []
    names = []
    add_note_to_list(labels, parents, values, names, root, notebook)

    line_width = 40
    for i in range(len(values)):
        if len(values[i].strip()) == 0:
            continue
        values[i] = hypenate_texts(values[i], line_width)
        labels[i] = hypenate_texts(labels[i], line_width)

    fig = go.Figure(go.Treemap(
        labels=labels,
        parents=parents,
        # values=values,
        ids=names,
        text=values,
        # text=values,
        root_color="lightgrey",
        # hoverinfo="label+text",
        # hovertemplate="<b>%{label}</b><br>%{hovertext}",
        texttemplate="<b>%{label}</b><br>%{text}",
        hovertemplate="<b>%{label}</b><br>%{text}<extra></extra>",
        hoverinfo="text",
        # marker=dict(cornerradius=5)
    ))

    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    # fig.update_traces(marker=dict(cornerradius=5))
    fig.show()


def add_note_to_list(labels, parents, values, names, note: Note, notebook: Notebook):
    i = 1
    children = note.get_children(notebook=notebook)
    for key, child in children.items():
        notepath = child.get_note_path(notebook=notebook)
        label = str(i) + ". " + key if len(children) > 1 else key
        labels.append(label)
        parents.append("/".join(notepath[:-1]))
        values.append(child.content)
        names.append("/".join(notepath))
        add_note_to_list(labels, parents, values, names, child, notebook)
        i += 1
