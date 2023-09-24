# Import necessary libraries
import plotly.graph_objects as go

from evonote.gui.utlis import hypenate_texts


def show_document_with_key_gui(keys, documents):
    if len(keys) == 0:
        print("No keys to show")
        return

    html_documents = []
    for document in documents:
        html_document = []
        for lines in document.split("\n"):
            html_document.append(hypenate_texts(lines, 100).replace("<br>", " \\<br>"))
        html_documents.append("<br>".join(html_document))

    values = [keys,
              html_documents]

    fig = go.Figure(data=[go.Table(
        columnorder=[1, 2],
        columnwidth=[80, 400],
        header=dict(
            values=[['Keys'],
                    ['Logs']],
            line_color='darkslategray',
            fill_color='royalblue',
            align=['left', 'center'],
            font=dict(color='white', size=12),
            height=40
        ),
        cells=dict(
            values=values,
            line_color='darkslategray',
            fill=dict(color=['paleturquoise', 'white']),
            align=['left', 'center'],
            font_size=12,
            height=30)
    )
    ])
    fig.show()


def example():
    # Your dictionary
    data = {
        "Key1": "Value1",
        "Key2": "Value2",
        "Key3": "Value3",
        # ... add as many keys and values as you like
    }
    show_document_with_key_gui(list(data.keys()), list(data.values()))


if __name__ == '__main__':
    example()
