# Import necessary libraries
import plotly.graph_objects as go


def show_document_with_key_gui(keys, documents):
    if len(keys) == 0:
        print("No keys to show")
        return

    html_documents = [document.replace("\n", "<br>") for document in documents]

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


# Run the app
if __name__ == '__main__':
    # Your dictionary
    data = {
        "Key1": "Value1",
        "Key2": "Value2",
        "Key3": "Value3",
        # ... add as many keys and values as you like
    }
    show_document_with_key_gui(list(data.keys()), list(data.values()))
