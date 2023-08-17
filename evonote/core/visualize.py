import plotly.graph_objects as go
from hyphen.textwrap2 import fill
from hyphen import Hyphenator

from evonote.core.note import Note

h_en = Hyphenator('en_US')


def draw_treemap(note: Note):
    labels = []
    parents = []
    values = []
    names = []
    add_note_to_list(labels, parents, values, names, "", note)

    line_width = 40
    for i in range(len(values)):
        if len(values[i].strip()) == 0:
            continue
        if "\\" in values[i]:
            hyphenator = False
        else:
            hyphenator = h_en
        try:
            values[i] = fill(values[i], width=line_width, use_hyphenator=hyphenator)
            values[i] = values[i].replace("\n", "<br>")
            labels[i] = fill(labels[i], width=line_width, use_hyphenator=hyphenator)
            labels[i] = labels[i].replace("\n", "<br>")
        except:
            values[i] = fill(values[i], width=line_width, use_hyphenator=False)
            values[i] = values[i].replace("\n", "<br>")
            labels[i] = fill(labels[i], width=line_width, use_hyphenator=False)
            labels[i] = labels[i].replace("\n", "<br>")

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


def add_note_to_list(labels, parents, values, names, key, note: Note):
    i = 1
    for key, child in note.children.items():
        label = str(i) + ". " + key if len(note.children) > 1 else key
        labels.append(label)
        parents.append(child.parents[0].note_path)
        values.append(child._content)
        names.append(child.note_path)
        add_note_to_list(labels, parents, values, names, key, child)
        i += 1
