from __future__ import annotations

from typing import TYPE_CHECKING

import plotly.graph_objects as go
from hyphen import Hyphenator

from evonote.gui.utlis import hypenate_texts

if TYPE_CHECKING:
    from evonote.mindtree import Note, Tree

h_en = Hyphenator('en_US')


def draw_treemap(root: Note):

    ids, labels, parents, texts = prepare_tree_parameters(root)

    fig = go.Figure(go.Treemap(
        labels=labels,
        parents=parents,
        # values=values,
        ids=ids,
        text=texts,
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


def get_json_for_treemap(root: Note):
    ids, labels, parents, texts = prepare_tree_parameters(root)
    node_list = []
    for i in range(len(ids)):
        node_list.append({
            "id": ids[i],
            "label": labels[i],
            "parent": parents[i],
            "text": texts[i]
        })
    return node_list


def prepare_tree_parameters(root):
    mindtree = root.tree
    labels = []
    parents = []
    texts = []
    ids = []
    add_note_to_list(labels, parents, texts, ids, root, mindtree)
    line_width = 40
    for i in range(len(texts)):
        if len(texts[i].strip()) == 0:
            continue
        texts[i] = hypenate_texts(texts[i], line_width)
        labels[i] = hypenate_texts(labels[i], line_width)
    return ids, labels, parents, texts


def add_note_to_list(labels, parents, values, ids, note: Note, mindtree: Tree):
    i = 1
    children = mindtree.get_children_dict(note)
    for key, child in children.items():
        notepath = mindtree.get_note_path(child)
        label = str(i) + ". " + key if len(children) > 1 else key
        labels.append(label)
        parents.append("/".join(notepath[:-1]))
        values.append(child.content)
        ids.append("/".join(notepath))
        add_note_to_list(labels, parents, values, ids, child, mindtree)
        i += 1
